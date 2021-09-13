package com.radu.salesman.controllers;

import com.itextpdf.text.DocumentException;
import com.radu.salesman.domain.Contact;
import com.radu.salesman.domain.Order;
import com.radu.salesman.domain.Payment;
import javafx.collections.FXCollections;
import javafx.collections.ObservableMap;
import javafx.fxml.FXML;
import com.radu.salesman.ui.gui.AppLayout;
import com.radu.salesman.ui.gui.MainGUI;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.control.ComboBox;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class DeliveryDetailsController extends Controller {
    private final ObservableMap<String, Set<String>> countiesCities = FXCollections.observableHashMap();

    @FXML
    private AnchorPane pane;
    @FXML
    private TextField cardNumber;
    @FXML
    private TextField expirationMonth;
    @FXML
    private TextField expirationYear;
    @FXML
    private TextField fullName;
    @FXML
    private TextField cvv;
    @FXML
    private TextField firstName;
    @FXML
    private TextField lastName;
    @FXML
    private TextField phoneNumber;
    @FXML
    private TextField address;
    @FXML
    private ComboBox<String> countyComboBox;
    @FXML
    private ComboBox<String> cityComboBox;

    private void populateCountiesAndCities() {
        File file = new File("orase_judete.txt");
        Scanner reader = null;
        try {
            reader = new Scanner(file);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        while (true) {
            assert reader != null;
            if (!reader.hasNextLine()) break;
            String[] data = reader.nextLine().split(",");
            countiesCities.putIfAbsent(data[1].trim(), new HashSet<>());
            countiesCities.get(data[1].trim()).add(data[0].trim());
        }
    }

    private void populateCitiesComboBox(String selectedCounty) {
        cityComboBox.setItems(FXCollections.observableArrayList(countiesCities.get(selectedCounty)).sorted());
    }

    private void populateComboBoxes() {
        countyComboBox.setItems(FXCollections.observableArrayList(countiesCities.keySet()).sorted());
        countyComboBox.getSelectionModel().selectFirst();
        populateCitiesComboBox(countyComboBox.getSelectionModel().getSelectedItem());
    }

    private void initializeData() {
        firstName.setText(currentUser.getContact().getFirstname());
        lastName.setText(currentUser.getContact().getLastname());
        phoneNumber.setText(currentUser.getContact().getPhoneNumber());
        address.setText(currentUser.getContact().getAddress());
        cardNumber.setText(currentUser.getPayment().getCardNumber());
        expirationMonth.setText(String.valueOf(currentUser.getPayment().getExpirationMonth()));
        expirationYear.setText(String.valueOf(currentUser.getPayment().getExpirationYear()));
        fullName.setText(currentUser.getPayment().getFullName());
        cvv.setText(currentUser.getPayment().getCvv());
        countyComboBox.getSelectionModel().select(currentUser.getContact().getCounty());
        cityComboBox.getSelectionModel().select(currentUser.getContact().getCity());
    }

    private void persistUserDetails() {
        Contact contact = new Contact(firstName.getText(), lastName.getText(), phoneNumber.getText(),
                countyComboBox.getSelectionModel().getSelectedItem(), cityComboBox.getSelectionModel().getSelectedItem(),
                address.getText());
        Payment payment = new Payment(cardNumber.getText(), Integer.parseInt(expirationMonth.getText()),
                Integer.parseInt(expirationYear.getText()), fullName.getText(), cvv.getText());
        currentUser.setContact(contact);
        currentUser.setPayment(payment);
    }

    @FXML
    private void initialize() {
        pane.sceneProperty().addListener((observable, oldValue, newValue) -> {
            if (newValue != null && newValue.getRoot() == pane) {
                Scene scene = pane.sceneProperty().get();
                if (scene != null && scene.getRoot() != pane) {
                    return;
                }
                if (countiesCities.size() == 0) {
                    populateCountiesAndCities();
                    populateComboBoxes();
                }
                initializeData();
            }
        });
    }

    @FXML
    public void handlePopulateCities() {
        populateCitiesComboBox(countyComboBox.getSelectionModel().getSelectedItem());
    }

    @FXML
    public void handleCancel() {
        MainGUI.activatePane(AppLayout.CART);
    }

    @FXML
    public void handleSubmit() {
        persistUserDetails();
        Order order = service.generateOrder(currentUser, totalPrice);
        if (order != null) {
            MainGUI.showAlert(Alert.AlertType.INFORMATION,
                    String.format("Order %d has been placed!", order.getId()), ButtonType.CLOSE);
            return;
        }
        MainGUI.showAlert(Alert.AlertType.ERROR, "Error placing order!", ButtonType.CLOSE);
    }
}
