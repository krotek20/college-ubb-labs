package triathlon.client.controller;

import javafx.application.Platform;
import triathlon.client.AppPane;
import triathlon.client.StartRMIClient;
import triathlon.model.Athlete;
import triathlon.model.Game;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.collections.transformation.SortedList;
import javafx.fxml.FXML;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.AnchorPane;
import javafx.util.StringConverter;
import triathlon.model.AthleteGameResult;
import triathlon.model.Result;
import triathlon.services.ITriathlonObserver;
import triathlon.services.ITriathlonServices;
import triathlon.services.TriathlonException;

import java.io.Serializable;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.Comparator;
import java.util.Map;
import java.util.stream.Collectors;

public class MainController extends UnicastRemoteObject implements ITriathlonObserver, Serializable {
    private final AuthController authController = new AuthController();
    private ITriathlonServices server;
    private Game game = null;

    private final ObservableList<Athlete> athletes = FXCollections.observableArrayList();
    private final ObservableList<AthleteGameResult> gameResults = FXCollections.observableArrayList();
    private final ObservableList<Map.Entry<String, Float>> athletesResults = FXCollections.observableArrayList();

    @FXML
    private AnchorPane pane;
    @FXML
    private TextField refereeField;
    @FXML
    private TextField gameField;
    @FXML
    private ChoiceBox<Athlete> athletePicker;
    @FXML
    private TextField pointsField;
    @FXML
    private ListView<Map.Entry<String, Float>> athletesResultsList;
    @FXML
    private TableView<AthleteGameResult> gameResultsTable;
    @FXML
    private TableColumn<AthleteGameResult, String> gameResultsAthleteColumn;
    @FXML
    private TableColumn<AthleteGameResult, String> gameResultsPointsColumn;

    public MainController() throws RemoteException {
    }

    public void setService(ITriathlonServices server) {
        this.server = server;
    }

    private void invalidateData() {
        athletesResults.clear();
        gameResults.clear();
        athletes.clear();
        game = null;
    }

    private synchronized void initializeData() throws TriathlonException {
        Scene scene = pane.sceneProperty().get();
        if (scene != null && scene.getRoot() != pane) {
            return;
        }

        game = server.getGameById(authController.getReferee().getGame().getId());
        athletes.setAll(server.getAthletes());
        newInitialize();
    }

    private synchronized void newInitialize() throws TriathlonException {
        gameResults.setAll(server.getResultsForGame(game.getId()).stream()
                .map(result -> {
                    Athlete athlete = athletes.stream()
                            .filter(a -> a.getId().equals(result.getAthlete().getId()))
                            .findFirst()
                            .orElse(null);
                    return new AthleteGameResult(result, athlete);
                }).collect(Collectors.toList()));
        athletesResults.setAll(server.getAthletesTotalPoints().entrySet());
    }

    @FXML
    private void initialize() {
        pane.sceneProperty().addListener((observable, oldValue, newValue) -> {
            if (oldValue != null && oldValue.getRoot() == pane) {
                pointsField.setText("");
            }
            if (newValue != null && newValue.getRoot() == pane) {
                try {
                    initializeData();
                } catch (TriathlonException e) {
                    e.printStackTrace();
                }
                gameField.setText(game.getName());
                refereeField.setText(authController.getReferee().getName());
            }
        });

        athletePicker.setItems(athletes.sorted(Comparator.comparing(Athlete::getName)));
        athletePicker.setConverter(new StringConverter<Athlete>() {
            @Override
            public String toString(Athlete athlete) {
                return athlete.getName();
            }

            @Override
            public Athlete fromString(String string) {
                return null;
            }
        });

        athletesResultsList.setItems(athletesResults.sorted(Map.Entry.comparingByKey()));

        SortedList<AthleteGameResult> gameResultSortedList = gameResults.sorted();
        gameResultSortedList.comparatorProperty().bind(gameResultsTable.comparatorProperty());
        gameResultsAthleteColumn.setCellValueFactory(new PropertyValueFactory<>("athleteName"));
        gameResultsPointsColumn.setCellValueFactory(new PropertyValueFactory<>("resultPoints"));
        gameResultsTable.getSortOrder().add(gameResultsPointsColumn);
        gameResultsTable.setItems(gameResultSortedList);
    }

    @FXML
    private void handleExitButtonAction() throws TriathlonException {
        server.logout(authController.getReferee(), this);
        StartRMIClient.activatePane(AppPane.AUTH);
        authController.invalidateReferee();
        invalidateData();
    }

    @FXML
    private void handleSubmitButtonAction() throws TriathlonException {
        Athlete athlete = athletePicker.getSelectionModel().getSelectedItem();
        if (athlete == null) {
            StartRMIClient.showAlert(Alert.AlertType.ERROR, "No athlete selected!", ButtonType.CLOSE);
            return;
        }

        float points;
        try {
            points = Float.parseFloat(pointsField.getText());
            if (points < 0 || points > 10) {
                throw new NumberFormatException("Outside range 0 - 10");
            }
        } catch (NumberFormatException e) {
            StartRMIClient.showAlert(Alert.AlertType.ERROR, e.getMessage(), ButtonType.CLOSE);
            return;
        }

        server.setResult(athlete, game, points);
    }

    @Override
    public void pointsChanged(Result result) {
        Platform.runLater(() -> {
            try {
                newInitialize();
            } catch (TriathlonException e) {
                e.printStackTrace();
            }
            gameResultsTable.refresh();
            athletesResultsList.refresh();
        });
    }
}
