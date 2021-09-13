/*
 * This code has been generated by the Rebel: a code generator for modern Java.
 *
 * Drop us a line or two at feedback@archetypesoftware.com: we would love to hear from you!
 */
package com.radu.salesman.controllers;

import com.radu.salesman.domain.Role;
import com.radu.salesman.domain.User;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import com.radu.salesman.service.ServiceException;
import com.radu.salesman.ui.gui.AppLayout;
import com.radu.salesman.ui.gui.MainGUI;

// ----------- << imports@AAAAAAF4xnsn09ihobo= >>
// ----------- >>

// ----------- << class.annotations@AAAAAAF4xnsn09ihobo= >>
// ----------- >>
public class LoginController extends Controller {
    @FXML
    private AnchorPane pane;
    @FXML
    private TextField usernameField;
    @FXML
    private PasswordField passwordField;

    // ----------- << method.annotations@AAAAAAF5DwzlSy4gMb4= >>
    // ----------- >>
    private void handleLoginUser() {
        // ----------- << method.body@AAAAAAF5DwzlSy4gMb4= >>
        // ----------- >>
        try {
            User user = service.loginUser(new User(insertUsername(), insertPassword()));
            Controller.setCurrentUser(user);
            MainGUI.activatePane(AppLayout.MAIN);
        } catch (ServiceException e) {
            MainGUI.showAlert(
                    Alert.AlertType.ERROR,
                    "USERNAME & PASSWORD combination wrong!",
                    ButtonType.CLOSE);
        }
    }

    // ----------- << method.annotations@AAAAAAF4xnuh8NpxqeM= >>
    // ----------- >>
    private String insertUsername() {
        // ----------- << method.body@AAAAAAF4xnuh8NpxqeM= >>
        // ----------- >>
        return usernameField.getText();
    }

    // ----------- << method.annotations@AAAAAAF4xnx9VdwxbFI= >>
    // ----------- >>
    private String insertPassword() {
        // ----------- << method.body@AAAAAAF4xnx9VdwxbFI= >>
        // ----------- >>
        return passwordField.getText();
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
    private void handleLoginButtonAction() throws ServiceException {
        handleLoginUser();
    }

    @FXML
    private void handlePasswordFieldAction() throws ServiceException {
        handleLoginUser();
    }
    // ----------- << class.extras@AAAAAAF4xnsn09ihobo= >>
    // ----------- >>
}
