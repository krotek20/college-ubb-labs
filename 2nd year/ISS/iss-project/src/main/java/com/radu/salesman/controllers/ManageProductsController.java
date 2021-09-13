package com.radu.salesman.controllers;

import com.radu.salesman.domain.Product;
import com.radu.salesman.utils.Parse;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import com.radu.salesman.ui.gui.AppLayout;
import com.radu.salesman.ui.gui.MainGUI;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.AnchorPane;

import java.util.Collection;

public class ManageProductsController extends Controller {
    private final ObservableList<Product> products = FXCollections.observableArrayList();

    @FXML
    private AnchorPane pane;
    @FXML
    private TextField idTextField;
    @FXML
    private TextField nameTextField;
    @FXML
    private TextField quantityTextField;
    @FXML
    private TextField priceTextField;
    @FXML
    private TableView<Product> productsTable;
    @FXML
    private TableColumn<Product, String> nameColumn;
    @FXML
    private TableColumn<Product, Integer> quantityColumn;
    @FXML
    private TableColumn<Product, Float> priceColumn;

    private void invalidateData() {
        products.clear();
    }

    private Collection<Product> handleViewProducts() {
        return service.getProducts();
    }

    private void initializeData() {
        Scene scene = pane.sceneProperty().get();
        if (scene != null && scene.getRoot() != pane) {
            return;
        }
        products.setAll(handleViewProducts());
    }

    @FXML
    private void initialize() {
        pane.sceneProperty().addListener((observable, oldValue, newValue) -> {
            if (newValue != null && newValue.getRoot() == pane) {
                initializeData();
            }
        });

        productsTable.getSelectionModel().selectedItemProperty().addListener((obs, oldSelection, newSelection) -> {
            if (newSelection != null) {
                idTextField.setText(newSelection.getId().toString());
                nameTextField.setText(newSelection.getName());
                quantityTextField.setText(String.valueOf(newSelection.getQuantity()));
                priceTextField.setText(String.valueOf(newSelection.getPrice()));
            }
        });

        nameColumn.setCellValueFactory(new PropertyValueFactory<>("name"));
        quantityColumn.setCellValueFactory(new PropertyValueFactory<>("quantity"));
        priceColumn.setCellValueFactory(new PropertyValueFactory<>("price"));
        productsTable.setItems(products);
    }

    @FXML
    public void handleAddButton() {
        if (service.addProduct(new Product(nameTextField.getText(),
                Parse.safeParseInteger(quantityTextField.getText()),
                Parse.safeParseFloat(priceTextField.getText()))) == null) {
            MainGUI.showAlert(Alert.AlertType.ERROR, "Add error!", ButtonType.CLOSE);
        } else {
            initializeData();
        }
    }

    @FXML
    public void handleModifyButton() {
        service.modifyProduct(new Product(
                Parse.safeParseLong(idTextField.getText()),
                nameTextField.getText(),
                Parse.safeParseInteger(quantityTextField.getText()),
                Parse.safeParseFloat(priceTextField.getText())));
        initializeData();
    }

    @FXML
    public void handleDeleteButton() {
        service.deleteProduct(Parse.safeParseLong(idTextField.getText()));
        initializeData();
    }

    @FXML
    public void handleExit() {
        MainGUI.activatePane(AppLayout.MAIN);
        invalidateData();
    }
}
