package client.controller;

import client.AppPane;
import client.StartRMIClient;
import domain.Player;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import services.IService;
import services.IServiceException;

public class AuthController {
    private static Player player = null;
    private IService server;

    @FXML
    private AnchorPane pane;
    @FXML
    private TextField usernameField;
    @FXML
    private PasswordField passwordField;

    public void setService(IService server) {
        this.server = server;
    }

    private void authenticateJucator() throws IServiceException {
        player = server.login(new Player(usernameField.getText(), passwordField.getText()),
                StartRMIClient.appLoaderMap.get(AppPane.MAIN).getKey().getController());
        if (player != null) {
            StartRMIClient.activatePane(AppPane.MAIN);
        } else {
            StartRMIClient.showAlert(
                    Alert.AlertType.ERROR,
                    "USERNAME & PASSWORD combination wrong!",
                    ButtonType.CLOSE
            );
        }
    }

    void invalidatePlayer() {
        player = null;
    }

    Player getPlayer() {
        return player;
    }

    @FXML
    private void initialize() {
        pane.sceneProperty().addListener((observable, oldValue, newValue) -> {
            if (oldValue != null && oldValue.getRoot() == pane) {
                passwordField.setText("");
            }
        });
    }

    @FXML
    private void handleLoginButtonAction() throws IServiceException {
        authenticateJucator();
    }

    @FXML
    private void handlePasswordFieldAction() throws IServiceException {
        authenticateJucator();
    }
}
