package triathlon.client.controller;

import triathlon.client.AppPane;
import triathlon.client.StartRMIClient;
import triathlon.model.Referee;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import triathlon.services.ITriathlonServices;
import triathlon.services.TriathlonException;

public class AuthController {
    private static Referee referee = null;
    private ITriathlonServices server;

    @FXML
    private AnchorPane pane;
    @FXML
    private TextField usernameField;
    @FXML
    private PasswordField passwordField;

    public void setService(ITriathlonServices server) {
        this.server = server;
    }

    private void authenticateReferee() throws TriathlonException {
        referee = server.authenticate(new Referee(null, "", usernameField.getText(), passwordField.getText()),
                StartRMIClient.appLoaderMap.get(AppPane.MAIN).getKey().getController());
        if (referee != null) {
            StartRMIClient.activatePane(AppPane.MAIN);
        } else {
            StartRMIClient.showAlert(
                    Alert.AlertType.ERROR,
                    "USERNAME & PASSWORD combination wrong!",
                    ButtonType.CLOSE
            );
        }
    }

    void invalidateReferee() {
        referee = null;
    }

    Referee getReferee() {
        return referee;
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
    private void handleLoginButtonAction() throws TriathlonException {
        authenticateReferee();
    }

    @FXML
    private void handlePasswordFieldAction() throws TriathlonException {
        authenticateReferee();
    }
}
