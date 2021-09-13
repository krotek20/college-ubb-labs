package services;

import domain.Game;
import domain.InitialCard;
import domain.Move;
import domain.Player;
import repository.GameRepository;
import repository.InitialCardRepository;
import repository.MoveRepository;
import repository.PlayerRepository;

import java.rmi.RemoteException;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Service implements IService {
    private final PlayerRepository playerRepository;
    private final GameRepository gameRepository;
    private final InitialCardRepository initialCardRepository;
    private final MoveRepository moveRepository;

    private final Map<String, IServiceObserver> loggedClients = new ConcurrentHashMap<>();

    // username -> Player + list of player's cards
    private final Map<String, Map.Entry<Player, List<String>>> playersInGame = new ConcurrentHashMap<>();

    private final Map<String, String> playedCards = new HashMap<>();
    private final String[] cards = {"red.8", "red.9", "red.10", "black.8", "black.5", "black.2", "black.7", "red.7", "red.2"};
    private final Random random = new Random();
    private static int roundCounter = 0;
    private static Game currentGame;

    public Service(PlayerRepository playerRepository, GameRepository gameRepository,
                   InitialCardRepository initialCardRepository, MoveRepository moveRepository) {
        this.playerRepository = playerRepository;
        this.gameRepository = gameRepository;
        this.initialCardRepository = initialCardRepository;
        this.moveRepository = moveRepository;
    }

    @Override
    public Player login(Player player, IServiceObserver client) {
        Player loggedPlayer = playerRepository.loginPlayer(player);
        if (null == loggedPlayer) {
            return null;
        }
        loggedPlayer.setPassword("");
        loggedClients.put(loggedPlayer.getUsername(), client);
        return loggedPlayer;
    }

    @Override
    public synchronized void startGame(Player player) {
        if (playersInGame.containsKey(player.getUsername())) {
            return;
        }
        playersInGame.put(player.getUsername(), new AbstractMap.SimpleEntry<>(player, new ArrayList<>()));
        if (playersInGame.size() == 3) {
            // incepe joc
            currentGame = gameRepository.save(new Game());
            List<String> allCards = new ArrayList<>();
            for (Map.Entry<Player, List<String>> playerListEntry : playersInGame.values()) {
                List<String> currentHand = new ArrayList<>();
                for (int i = 0; i < 3; i++) {
                    String card = cards[random.nextInt(cards.length)];
                    while (allCards.contains(card)) {
                        card = cards[random.nextInt(cards.length)];
                    }
                    currentHand.add(card);
                    allCards.add(card);
                }
                playersInGame.get(playerListEntry.getKey().getUsername()).getValue().addAll(currentHand);
                initialCardRepository.save(new InitialCard(playerListEntry.getKey(), currentGame,
                        currentHand.get(0), currentHand.get(1), currentHand.get(2)));
            }
            updatePlayersInGame();
            updateOwnCards();
            roundCounter = 0;
        }
    }

    @Override
    public synchronized void playGame(Player player, String card) {
        if (!playersInGame.containsKey(player.getUsername())) {
            return;
        }
        playedCards.put(player.getUsername(), card);
        if (playedCards.size() == 3) {
            // incepe runda
            String bestCard = null;
            String bestPlayer = null;
            for (Map.Entry<String, String> entry : playedCards.entrySet()) {
                if (bestCard == null) {
                    bestCard = entry.getValue();
                    bestPlayer = entry.getKey();
                } else {
                    String currentCard = entry.getValue();
                    String[] bestCardSplit = bestCard.split("\\.");
                    String[] currentCardSplit = currentCard.split("\\.");
                    if (bestCardSplit[0].compareTo(currentCardSplit[0]) < 0) {
                        bestCard = currentCard;
                        bestPlayer = entry.getKey();
                    } else if (bestCardSplit[0].compareTo(currentCardSplit[0]) == 0) {
                        if (bestCardSplit[0].equals("black") &&
                                bestCardSplit[1].compareTo(currentCardSplit[1]) > 0) {
                            bestCard = currentCard;
                            bestPlayer = entry.getKey();
                        } else if (bestCardSplit[0].equals("red") &&
                                bestCardSplit[1].compareTo(currentCardSplit[1]) < 0) {
                            bestCard = currentCard;
                            bestPlayer = entry.getKey();
                        }
                    }
                }
            }
            roundCounter++;
            sendRoundWinner(bestPlayer);
            for (Map.Entry<Player, List<String>> entry : playersInGame.values()) {
                if (entry.getKey().getUsername().equals(bestPlayer)) {
                    moveRepository.save(new Move(entry.getKey(), currentGame, bestCard, 3));
                } else {
                    moveRepository.save(new Move(entry.getKey(), currentGame,
                            playedCards.get(entry.getKey().getUsername()), 0));
                }
            }
            removePlayedCards();
            playedCards.clear();
            if(roundCounter == 3) {
                stopGame();
            }
        }
    }

    private void stopGame() {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        Map<Player, Integer> scores = new HashMap<>();
        for (Map.Entry<Player, List<String>> playerListEntry : playersInGame.values()) {
            Player player = playerRepository.findOne(playerListEntry.getKey().getId());
            int score = 0;
            for (Move move : player.getMoves()) {
                if(move.getGame().getId().equals(currentGame.getId())) {
                    score += move.getNumberOfReceivedCards();
                }
            }
            scores.put(player, score);
        }
        List<Map.Entry<Player, Integer>> leaderboard = scores.entrySet()
                .stream()
                .map(x -> new AbstractMap.SimpleEntry<>(x.getKey(), x.getValue()))
                .sorted(Comparator.comparingInt(Map.Entry::getValue))
                .collect(Collectors.toList());
        for (Map.Entry<Player, List<String>> playerListEntry : playersInGame.values()) {
            IServiceObserver client = loggedClients.get(playerListEntry.getKey().getUsername());
            executor.execute(() -> {
                try {
                    client.updateLeaderBoard(leaderboard);
                } catch (IServiceException | RemoteException e) {
                    System.err.println("Error notifying operator " + e);
                }
            });
        }
        executor.shutdown();
    }

    private void removePlayedCards() {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (Map.Entry<Player, List<String>> playerListEntry : playersInGame.values()) {
            IServiceObserver client = loggedClients.get(playerListEntry.getKey().getUsername());
            playerListEntry.getValue().remove(playedCards.get(playerListEntry.getKey().getUsername()));
            executor.execute(() -> {
                try {

                    client.updateOwnCards(playerListEntry.getValue());
                } catch (IServiceException | RemoteException e) {
                    System.err.println("Error notifying operator " + e);
                }
            });
        }
        executor.shutdown();
    }

    private void sendRoundWinner(String playerName) {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (Map.Entry<Player, List<String>> playerListEntry : playersInGame.values()) {
            IServiceObserver client = loggedClients.get(playerListEntry.getKey().getUsername());
            executor.execute(() -> {
                try {
                    client.updateRoundWinner(roundCounter, playerName);
                } catch (IServiceException | RemoteException e) {
                    System.err.println("Error notifying operator " + e);
                }
            });
        }
        executor.shutdown();
    }

    private void updatePlayersInGame() {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (Map.Entry<Player, List<String>> playerListEntry : playersInGame.values()) {
            IServiceObserver client = loggedClients.get(playerListEntry.getKey().getUsername());
            executor.execute(() -> {
                try {
                    client.updatePlayersList(playersInGame.values().stream()
                            .map(x -> x.getKey().getUsername()).collect(Collectors.toList()));
                } catch (IServiceException | RemoteException e) {
                    System.err.println("Error notifying operator " + e);
                }
            });
        }
        executor.shutdown();
    }

    private void updateOwnCards() {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (Map.Entry<Player, List<String>> playerListEntry : playersInGame.values()) {
            IServiceObserver client = loggedClients.get(playerListEntry.getKey().getUsername());
            executor.execute(() -> {
                try {
                    client.updateOwnCards(playerListEntry.getValue());
                } catch (IServiceException | RemoteException e) {
                    System.err.println("Error notifying operator " + e);
                }
            });
        }
        executor.shutdown();
    }


    @Override
    public void logout(Player player) {
        player.setPassword("");
        loggedClients.remove(player.getUsername());
    }
}
