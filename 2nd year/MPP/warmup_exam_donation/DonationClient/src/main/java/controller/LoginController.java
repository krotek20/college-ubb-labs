package controller;
import donation.model.Volunteer;
import donation.services.IDonationObserver;
import donation.services.IDonationServices;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;

public class LoginController {
    private IDonationServices server;

    public void setMainCtrl(MainController mainCtrl) {
        this.mainCtrl = mainCtrl;
    }

    Parent mainDonationParent;
    public void setParent(Parent p){
        mainDonationParent =p;
    }

    private MainController mainCtrl;

    @FXML
    TextField tboxUsername;
    @FXML
    TextField tboxPassword;
    @FXML
            Label lblError;

    IDonationServices service;
    public void setService(IDonationServices service){
        this.service = service;
    }

    public void initialize() {
        //String javaVersion = System.getProperty("java.version");
        //String javafxVersion = System.getProperty("javafx.version");
    }

    public void btnLogin_Click(ActionEvent actionEvent) throws Exception {

        Volunteer vol = service.FindVolunteerByCredentials(new Volunteer("",tboxUsername.getText(), tboxPassword.getText()), mainCtrl);
        if (vol == null)
        {
            lblError.setText("Invalid credentials!");
        }
        else
        {
            Stage stage = new Stage();
            stage.setTitle("Main");
            stage.setScene(new Scene(mainDonationParent));

            stage.setOnCloseRequest(new EventHandler<WindowEvent>() {
                @Override
                public void handle(WindowEvent event) {
                    //mainCtrl.logout();
                    //System.exit(0);
                }
            });

            stage.show();
            mainCtrl.setConnectedUser(vol);
            mainCtrl.initModel();
            ((Node)(actionEvent.getSource())).getScene().getWindow().hide();
        }

    }
}