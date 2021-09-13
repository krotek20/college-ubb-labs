package controller;

import domain.User;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TextField;
import service.IServiceException;
import ui.gui.StagePuppeteer;
import ui.gui.StageStatus;

import java.io.IOException;

public class LogInFormController extends IController {
    @FXML
    TextField usernameField;
    @FXML
    javafx.scene.control.PasswordField passwordField;

    public void logInButtonPressed(ActionEvent actionEvent) {
        try {
            controller.loginUser(new User(usernameField.getText(), passwordField.getText()));
        } catch (IServiceException ex) {
            new Alert(Alert.AlertType.ERROR, ex.getMessage()).show();
            return;
        }
        try {
            StagePuppeteer.changeStage(StageStatus.MAIN);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
