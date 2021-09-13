package client.controller;

import client.AppPane;
import client.StartRMIClient;
import domain.Player;
import javafx.application.Platform;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.layout.AnchorPane;
import services.IService;
import services.IServiceException;
import services.IServiceObserver;

import java.io.Serializable;
import java.rmi.RemoteException;
import java.rmi.server.RMIClientSocketFactory;
import java.rmi.server.RMIServerSocketFactory;
import java.rmi.server.UnicastRemoteObject;
import java.util.List;
import java.util.Map;

public class MainController extends UnicastRemoteObject implements IServiceObserver, Serializable {
    private final AuthController authController = new AuthController();
    public Label winnerLabel;
    private IService server;

    private final ObservableList<String> inGamePlayersModel = FXCollections.observableArrayList();
    private final ObservableList<String> ownCardsModel = FXCollections.observableArrayList();
    private final ObservableList<Map.Entry<Player, Integer>> leaderboardModel = FXCollections.observableArrayList();

    @FXML
    private AnchorPane pane;
    @FXML
    private Button pickCardButton;
    @FXML
    private Button startGameButton;
    @FXML
    private ListView<String> playersList;
    @FXML
    private ListView<String> ownCardsList;
    @FXML
    private ListView<Map.Entry<Player, Integer>> leaderBoardList;

    public MainController() throws RemoteException {
    }

    protected MainController(int port) throws RemoteException {
        super(port);
    }

    protected MainController(int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf) throws RemoteException {
        super(port, csf, ssf);
    }

    public void setService(IService server) {
        this.server = server;
    }

    private void invalidateData() {
        inGamePlayersModel.clear();
        leaderboardModel.clear();
        ownCardsModel.clear();
    }

    private void initializeData() throws IServiceException {
        //modelJucatoriInJoc.setAll(server.getJucatoriInJoc());
    }

    private void disableGameButton() {
        this.startGameButton.setDisable(true);
    }

    private void enableGameButton() {
        this.startGameButton.setDisable(false);
    }

    private void disablePickButton() {
        this.pickCardButton.setDisable(true);
    }

    private void enablePickButton() {
        this.pickCardButton.setDisable(false);
    }

    @FXML
    public void initialize() {
        pane.sceneProperty().addListener((observable, oldValue, newValue) -> {
            if (oldValue != null && oldValue.getRoot() == pane) {
            }
            if (newValue != null && newValue.getRoot() == pane) {
                disablePickButton();
                enableGameButton();
            }
        });

        playersList.setItems(inGamePlayersModel);
        ownCardsList.setItems(ownCardsModel);
        leaderBoardList.setItems(leaderboardModel);
    }

    @FXML
    private void handlePickCardButtonAction() {
        String card = ownCardsList.getSelectionModel().getSelectedItem();
        if (card == null) {
            StartRMIClient.showAlert(Alert.AlertType.ERROR, "No card selected!", ButtonType.CANCEL);
            return;
        }
        server.playGame(authController.getPlayer(), card);
    }

    @FXML
    private void handleStartGameButtonAction() {
        server.startGame(authController.getPlayer());
        this.disableGameButton();
    }

    @FXML
    private void handleExitButtonAction() throws IServiceException {
        server.logout(authController.getPlayer());
        StartRMIClient.activatePane(AppPane.AUTH);
        authController.invalidatePlayer();
        invalidateData();
    }

    @Override
    public void updatePlayersList(List<String> players) throws IServiceException, RemoteException {
        Platform.runLater(() -> {
            this.inGamePlayersModel.clear();
            this.inGamePlayersModel.addAll(players);
            this.enablePickButton();
            this.disableGameButton();
        });
    }

    @Override
    public void updateOwnCards(List<String> ownCards) throws IServiceException, RemoteException {
        Platform.runLater(() -> {
            this.ownCardsModel.clear();
            this.ownCardsModel.addAll(ownCards);
        });
    }

    @Override
    public void updateRoundWinner(int round, String name) throws IServiceException, RemoteException {
        Platform.runLater(() -> {
            this.winnerLabel.setText(String.format("Winner of round %d is %s", round, name));
        });
    }

    @Override
    public void updateLeaderBoard(List<Map.Entry<Player, Integer>> leaderboard) throws IServiceException, RemoteException {
        Platform.runLater(() -> {
            this.leaderboardModel.clear();
            this.leaderboardModel.addAll(leaderboard);
        });
    }
}
