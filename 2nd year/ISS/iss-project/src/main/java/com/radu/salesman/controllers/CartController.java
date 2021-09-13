package com.radu.salesman.controllers;

import com.radu.salesman.domain.CartElement;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import com.radu.salesman.ui.gui.AppLayout;
import com.radu.salesman.ui.gui.MainGUI;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.AnchorPane;

import java.util.List;

public class CartController extends Controller {
    private final ObservableList<CartElement> cartElements = FXCollections.observableArrayList();

    @FXML
    private AnchorPane pane;
    @FXML
    private TextField totalPrice;
    @FXML
    private TableView<CartElement> cartElementsTable;
    @FXML
    private TableColumn<CartElement, String> elementColumn;
    @FXML
    private TableColumn<CartElement, Integer> quantityColumn;
    @FXML
    private TableColumn<CartElement, Float> priceColumn;

    private List<CartElement> handleViewElements() {
        return currentUser.getCart().getCartElements();
    }

    private void initializeData() {
        List<CartElement> elements = handleViewElements();
        cartElements.setAll(handleViewElements());
        Controller.setTotalPrice(elements.stream().map(CartElement::getPrice).reduce(0.0f, Float::sum));
        totalPrice.setText(String.format("Total price: %.2f", Controller.totalPrice));
    }

    @FXML
    private void initialize() {
        pane.sceneProperty().addListener((observable, oldValue, newValue) -> {
            if (newValue != null && newValue.getRoot() == pane) {
                Scene scene = pane.sceneProperty().get();
                if (scene != null && scene.getRoot() != pane) {
                    return;
                }
                initializeData();
            }
        });

        elementColumn.setCellValueFactory(new PropertyValueFactory<>("product"));
        quantityColumn.setCellValueFactory(new PropertyValueFactory<>("quantity"));
        priceColumn.setCellValueFactory(new PropertyValueFactory<>("price"));
        cartElementsTable.setItems(cartElements);
    }

    @FXML
    public void handleRemoveFromCart() {
        CartElement cartElement = cartElementsTable.getSelectionModel().getSelectedItem();
        if (cartElement == null) {
            MainGUI.showAlert(Alert.AlertType.ERROR, "No product selected!", ButtonType.CLOSE);
            return;
        }
        service.removeCartElement(cartElement.getId());
        currentUser.getCart().removeCartElement(cartElement);
        initializeData();
    }

    @FXML
    public void handleExit() {
        MainGUI.activatePane(AppLayout.MAIN);
    }

    @FXML
    public void handleWithdraw() {
        if (currentUser.getCart().getCartElements().size() > 0) {
            MainGUI.activatePane(AppLayout.INS_DATA);
        } else {
            MainGUI.showAlert(Alert.AlertType.ERROR, "No elements in cart!", ButtonType.CLOSE);
        }
    }
}
