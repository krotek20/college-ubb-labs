package service;

import domain.Participant;
import domain.User;
import javafx.util.Pair;
import repository.ParticipantRepository;
import repository.UserRepository;

import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class Service implements IService {

    private final UserRepository userRepository;
    private final ParticipantRepository participantRepository;
    private Map<String, Pair<User, IServiceObserver>> clients = new ConcurrentHashMap<>();
    //private Map<String, User> loggedUsers = new ConcurrentHashMap<>();

    public Service(UserRepository userRepository, ParticipantRepository participantRepository) {
        this.userRepository = userRepository;
        this.participantRepository = participantRepository;
    }


    @Override
    public User login(User user, IServiceObserver client) {
        User loggedUser = userRepository.loginUser(user);
        if (null == loggedUser) {
            throw new IServiceException("Username/password are invalid!");
        }
        loggedUser.setPassword("");
        if (clients.containsKey(loggedUser.getUsername())) {
            throw new IServiceException("User already logged in!");
        }
        if (clients.size() >= 3) {
            throw new IServiceException("There can only be 3 judges!");
        }
        clients.put(loggedUser.getUsername(), new Pair<>(loggedUser, client));
        getAllParticipanti();
        return loggedUser;
    }

    @Override
    public void logout(User user) {
        user.setPassword("");
        clients.remove(user.getUsername());
    }

    @Override
    public void adaugaRezultat(User user, Participant participant, double nota) {
        Long id = user.getId();
        participant = participantRepository.findOne(participant.getId());
        if (id == 1L) {
                if (participant.getNota1() == null) {
                    participant.setNota1(nota);
                    participant.entityUpdated();
                    participantRepository.update(participant);
                }
                else {
                    throw new IServiceException("Participantul deja are nota!");
                }
        } else if (id == 2L) {
            if (participant.getNota2() == null) {
                participant.setNota2(nota);
                participant.entityUpdated();
                participantRepository.update(participant);
            }
            else {
                throw new IServiceException("Participantul deja are nota!");
            }
        } else if (id == 3L) {
            if (participant.getNota3() == null) {
                participant.setNota3(nota);
                participant.entityUpdated();
                participantRepository.update(participant);
            }
            else {
                throw new IServiceException("Participantul deja are nota!");
            }
        }
        getAllParticipanti();
    }

    @Override
    public void getAllParticipanti() {
        List<Participant> allParticipanti = new ArrayList<>();
        participantRepository.findAll().forEach(allParticipanti::add);
        for (Pair<User, IServiceObserver> client : clients.values()) {
            try {
                client.getValue().updateParticipanti(allParticipanti);
            } catch (RemoteException e) {
                e.printStackTrace();
            }
        }
    }
}
