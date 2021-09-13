package ui.gui;

import controller.GeneralController;
import controller.IController;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

import java.io.IOException;

public class StagePuppeteer extends Application {
    private static Stage stage;
    private static GeneralController controller;

    private static IController changeStageResource(String resource) throws IOException {
        FXMLLoader loader = new FXMLLoader();
        loader.setLocation(StagePuppeteer.class.getResource(resource));
        AnchorPane root = loader.load();
        stage.setScene(new Scene(root));
        IController controller = loader.getController();
        controller.setGeneralController(StagePuppeteer.controller);
        return controller;
    }

    public static void changeStage(StageStatus stageStatus) throws IOException {
        switch (stageStatus) {
            case LOGIN -> changeStageResource("/view/logInForm.fxml");
            case MAIN -> changeStageResource("/view/mainForm.fxml");
        }
    }

    public static void setController(GeneralController controller) {
        StagePuppeteer.controller = controller;
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        stage = primaryStage;
        changeStage(StageStatus.LOGIN);
        stage.setResizable(false);
        stage.show();
    }

    public static void startApp() {
        launch();
    }
}