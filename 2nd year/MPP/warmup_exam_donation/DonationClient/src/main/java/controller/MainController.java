package controller;

import donation.model.CharityCase;
import donation.model.Donation;
import donation.model.Donor;
import donation.model.Volunteer;
import donation.services.DonationException;
import donation.services.IDonationObserver;
import donation.services.IDonationServices;
import javafx.application.Platform;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.ListCell;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyEvent;
import javafx.stage.Stage;
import javafx.util.Callback;
import java.io.IOException;
import java.io.Serializable;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

public class MainController extends UnicastRemoteObject implements IDonationObserver, Serializable {
    @FXML
    Label lblWelcome;
    @FXML
    Label lblError;
    @FXML
    TextField tboxDonorSearch;
    @FXML
    TextField tboxName;
    @FXML
    TextField tboxAddress;
    @FXML
    TextField tboxPhoneNumber;
    @FXML
    TextField tboxSum;
    @FXML
    ListView listDonors;
    @FXML
    ListView listCharityCases;




    ObservableList<Donor> modelDonors = FXCollections.observableArrayList();
    ObservableList<CharityCase> modelCharityCases = FXCollections.observableArrayList();


    IDonationServices service;

    public MainController() throws RemoteException {
    }

    public void setService(IDonationServices service){
        this.service = service;
    }


    Volunteer connectedUser;
    public void setConnectedUser(Volunteer vol){
        connectedUser = vol;
        lblWelcome.setText("Welcome, "+vol.getName()+"!");
    }

    public void initModel() {
        if(service == null) return;
        try {
            updateDonors(service.FindDonorsByName(tboxDonorSearch.getText()));
            modelCharityCases.setAll(service.GetAllCharityCases());
        } catch (DonationException e) {
            e.printStackTrace();
        }
    }

    private void updateDonors(List<Donor> donors){
        modelDonors.setAll(donors);
        modelDonors.add(0,new Donor(-1L,"ADD NEW DONOR","",""));
    }

    @FXML
    public void initialize() throws IOException {
        listDonors.setCellFactory(new Callback<ListView<Donor>, ListCell<Donor>>() {
            @Override
            public ListCell call(ListView<Donor> param) {
                return new ListCell<Donor>(){
                    @Override
                    protected void updateItem(Donor item, boolean empty) {
                        super.updateItem(item, empty);
                        if (empty || item == null || item == null) {
                            setText(null);
                        } else {
                            setText(item.toString());
                        }
                    }};
            }
        });
        listCharityCases.setCellFactory(new Callback<ListView<CharityCase>, ListCell<CharityCase>>() {
            @Override
            public ListCell call(ListView<CharityCase> param) {
                return new ListCell<CharityCase>(){
                    @Override
                    protected void updateItem(CharityCase item, boolean empty) {
                        super.updateItem(item, empty);
                        if (empty || item == null || item == null)
                            setText(null);
                        else if(item.getId() < 0) setText(item.toString());
                        else setText(String.format("%s -> %d LEI",item.toString(),item.getRaisedSum()));
                    }};
            }
        });
        listDonors.getSelectionModel().selectedItemProperty().addListener(new ChangeListener() {
            @Override
            public void changed(ObservableValue observable, Object oldValue, Object newValue) {
                Donor v = (Donor) newValue;
                if(v == null){
                    tboxName.setDisable(true);
                    tboxAddress.setDisable(true);
                    tboxPhoneNumber.setDisable(true);
                    tboxName.clear();
                    tboxAddress.clear();
                    tboxPhoneNumber.clear();
                }
                else if(v.getId() < 0){
                    tboxName.setDisable(false);
                    tboxAddress.setDisable(false);
                    tboxPhoneNumber.setDisable(false);
                    tboxName.clear();
                    tboxAddress.clear();
                    tboxPhoneNumber.clear();
                }
                else{
                    tboxName.setDisable(true);
                    tboxAddress.setDisable(true);
                    tboxPhoneNumber.setDisable(true);
                    tboxName.setText(v.getName());
                    tboxAddress.setText(v.getAddress());
                    tboxPhoneNumber.setText(v.getPhoneNumber());
                }
            }
        });
        listDonors.setItems(modelDonors);
        listCharityCases.setItems(modelCharityCases);
    }
        public void lblLogout_Click(ActionEvent actionEvent) throws IOException, DonationException {
            logout();
            Stage stage = (Stage) lblWelcome.getScene().getWindow();
            FXMLLoader loader = new FXMLLoader(getClass().getClassLoader().getResource("Login.fxml"));
            Parent root = loader.load();
            LoginController loginController = loader.getController();
            loginController.setService(service);

            FXMLLoader cloader = new FXMLLoader(
                    getClass().getClassLoader().getResource("Main.fxml"));
            Parent croot=cloader.load();
            MainController mainCtrl = cloader.getController();
            mainCtrl.setService(service);

            loginController.setMainCtrl(mainCtrl);
            loginController.setParent(croot);

            stage.setTitle("Login");
            stage.setScene(new Scene(root, 800, 600));
            stage.show();


            //Stage stage = (Stage) lblWelcome.getScene().getWindow();
            //stage.close();
        }

    public void logout(){
        try {
            service.Logout(connectedUser, this);
        } catch (DonationException e) {
            System.out.println("Logout error " + e);
        }
    }

    public void tboxDonorSearch_Changed(KeyEvent keyEvent) {
        try {
            updateDonors(service.FindDonorsByName(tboxDonorSearch.getText()));
        } catch (DonationException e) {
            e.printStackTrace();
        }
    }

    public void btnConfirm_CLick(ActionEvent actionEvent) {
        CharityCase charity = (CharityCase)listCharityCases.getSelectionModel().getSelectedItem();
        if(charity==null){
            lblError.setText("Select the charity!");
            return;
        }
        Donor donor = (Donor)listDonors.getSelectionModel().getSelectedItem();
        if(donor==null){
            lblError.setText("Select a donor from the list!");
            return;
        }
        else if(donor.getId() < 0) {
            if(tboxName.getText().equals("")) lblError.setText("Enter a name!");
            else if(tboxAddress.getText().equals("")) lblError.setText("Enter the address!");
            else if(tboxPhoneNumber.getText().equals("")) lblError.setText("Enter the phone number!");
            else if(tboxSum.getText().equals("")) lblError.setText("Enter the sum!");
            else try {
                Donor newDonor = new Donor(tboxName.getText(),tboxAddress.getText(),tboxPhoneNumber.getText());
                service.AddDonor(newDonor);
                Donation d = new Donation(charity.getId(),newDonor.getId(),Long.parseLong(tboxSum.getText()));
                service.AddDonation(d);
            } catch (SQLException | DonationException throwables) {
                lblError.setText("An error occured! - " + throwables.getMessage());
            }
        }
        else {
            if(tboxSum.getText().equals("")) {
                lblError.setText("Enter the sum!");
                return;
            }
            try {
                Donation d = new Donation(charity.getId(),donor.getId(),Long.parseLong(tboxSum.getText()));
                service.AddDonation(d);
            } catch (SQLException | DonationException throwables) {
                lblError.setText("An error occured! - " + throwables.getMessage());
            }
        }
    }

    @Override
    public void donorAdded(Donor newDonor) {
        Platform.runLater(()-> {
            System.out.println("DONOR ADDED!!!!!! - " + newDonor.getName());
            modelDonors.add(1, newDonor);
            listDonors.refresh();
        });
    }

    @Override
    public void donationAdded(Donation d) {
        for(CharityCase c : modelCharityCases)
            if(c.getId().equals(d.getCaseId())) {
                c.setRaisedSum(c.getRaisedSum()+d.getSum());
                break;
            }
        Platform.runLater(()->{
                    listCharityCases.refresh();
        });
    }
}
