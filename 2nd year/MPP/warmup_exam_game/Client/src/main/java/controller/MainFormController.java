package controller;

import domain.Participant;
import domain.ParticipantStatus;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;
import service.IServiceException;
import ui.gui.StagePuppeteer;
import ui.gui.StageStatus;

import java.io.IOException;

public class MainFormController extends IController {
    public TableView<Participant> participantTable;
    public TableColumn<Participant, String> numeTableColumn;
    public TableColumn<Participant, ParticipantStatus> statusTableColumn;
    public TextField notaTextField;
    public TableColumn<Participant, Double> notaTableColumn;

    @FXML
    public void initialize() {
        numeTableColumn.setCellValueFactory(new PropertyValueFactory<>("nume"));
        statusTableColumn.setCellValueFactory(new PropertyValueFactory<>("status"));
        notaTableColumn.setCellValueFactory(new PropertyValueFactory<>("total"));
        participantTable.setItems(controller.getModelParticipant());
    }

    public void logoutButtonClicked(ActionEvent actionEvent) {
        controller.logout();
        try {
            StagePuppeteer.changeStage(StageStatus.LOGIN);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void daNotaButtonPressed(ActionEvent actionEvent) {
        Double nota;
        try {
            nota = Double.parseDouble(notaTextField.getText());
        } catch (NumberFormatException ex) {
            new Alert(Alert.AlertType.ERROR, "Trebuie dat un numar valid!").show();
            return;
        }
        Participant participant = participantTable.getSelectionModel().getSelectedItem();
        if (null == participant) {
            new Alert(Alert.AlertType.ERROR, "Trebuie selectat un participant!").show();
            return;
        }
        try {
            controller.daNota(participant, nota);
        } catch (IServiceException ex) {
            new Alert(Alert.AlertType.ERROR, ex.getMessage()).show();
        }
    }
}
