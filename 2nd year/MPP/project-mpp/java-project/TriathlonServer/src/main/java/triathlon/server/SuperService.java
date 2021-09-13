package triathlon.server;

import triathlon.model.Athlete;
import triathlon.model.Game;
import triathlon.model.Referee;
import triathlon.model.Result;
import triathlon.persistence.AthleteRepository;
import triathlon.persistence.GameRepository;
import triathlon.persistence.RefereeRepository;
import triathlon.persistence.ResultRepository;
import triathlon.services.ITriathlonObserver;
import triathlon.services.ITriathlonServices;
import triathlon.services.TriathlonException;

import java.rmi.RemoteException;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

public class SuperService implements ITriathlonServices {
    private final GameRepository gameRepository;
    private final ResultRepository resultRepository;
    private final RefereeRepository refereeRepository;
    private final AthleteRepository athleteRepository;
    private final Map<String, ITriathlonObserver> loggedClients;

    public SuperService(GameRepository gameRepository, ResultRepository resultRepository,
                        RefereeRepository refereeRepository, AthleteRepository athleteRepository) {
        this.gameRepository = gameRepository;
        this.resultRepository = resultRepository;
        this.refereeRepository = refereeRepository;
        this.athleteRepository = athleteRepository;
        loggedClients = new ConcurrentHashMap<>();
    }

    @Override
    public synchronized Collection<Athlete> getAthletes() {
        return StreamSupport
                .stream(athleteRepository.findAll().spliterator(), false)
                .collect(Collectors.toList());
    }

    @Override
    public synchronized Map<String, Float> getAthletesTotalPoints() {
        Map<String, Float> athleteResultMap = new HashMap<>();
        for (Result result : resultRepository.findAll()) {
            Athlete athlete = athleteRepository.findOne(result.getAthlete().getId());
            athleteResultMap.compute(athlete.getName(), (k, v) -> (v == null ? 0 : v) + result.getValue());
        }
        return athleteResultMap;
    }

    @Override
    public synchronized Game getGameById(Long id) {
        return gameRepository.findOne(id);
    }

    @Override
    public synchronized Referee authenticate(Referee referee, ITriathlonObserver client) throws TriathlonException {
        for (Referee ref : refereeRepository.findAll()) {
            if (ref.getUsername().equals(referee.getUsername()) &&
                    ref.getPassword().equals(referee.getPassword())) {
                if (loggedClients.containsKey(ref.getUsername()))
                    throw new TriathlonException("User already logged in!");
                loggedClients.put(ref.getUsername(), client);
                return ref;
            }
        }
        return null;
    }

    @Override
    public synchronized void logout(Referee referee, ITriathlonObserver client) throws TriathlonException {
        System.out.println("Logout: " + referee.getUsername());
        ITriathlonObserver localClient = loggedClients.remove(referee.getUsername());
        if (localClient == null) {
            throw new TriathlonException("Referee " + referee.getId() + " is not logged in.");
        }
    }

    @Override
    public synchronized Collection<Result> getResultsForGame(Long gameId) {
        return StreamSupport
                .stream(resultRepository.findAll().spliterator(), false)
                .filter(result -> result.getGame().getId().equals(gameId))
                .collect(Collectors.toList());
    }

    @Override
    public synchronized void setResult(Athlete athlete, Game game, Float value) {
        Result result = StreamSupport.stream(resultRepository.findAll().spliterator(), false)
                .filter(r -> r.getAthlete().getId().equals(athlete.getId()) && r.getGame().getId().equals(game.getId()))
                .findFirst()
                .orElse(null);

        if (result != null) {
            result.setValue(value);
            resultRepository.update(result);
        } else {
            resultRepository.save(new Result(game, athlete, value));
        }
        notifyUpdateResult(result);
    }

    private void notifyUpdateResult(Result result) {
        ExecutorService executor = Executors.newFixedThreadPool(5);
        for (String username : loggedClients.keySet()) {
            ITriathlonObserver client = loggedClients.get(username);
            if (client != null) {
                executor.execute(() -> {
                    try {
                        System.out.println("Notifying [" + username + "] to update its info.");
                        client.pointsChanged(result);
                    } catch (TriathlonException | RemoteException e) {
                        System.err.println("Error notifying operator " + e);
                    }
                });
            }
        }
        executor.shutdown();
    }
}
