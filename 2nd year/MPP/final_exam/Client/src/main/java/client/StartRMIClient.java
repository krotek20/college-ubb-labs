package client;

import client.controller.AuthController;
import client.controller.MainController;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;
import javafx.util.Pair;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import services.IService;

import java.util.EnumMap;

public class StartRMIClient extends Application {
    public static EnumMap<client.AppPane, Pair<FXMLLoader, Parent>> appLoaderMap;
    private static Scene appScene;

    private static Pair<FXMLLoader, Parent> loader(String location) throws Exception {
        FXMLLoader fxmlLoader = new FXMLLoader(StartRMIClient.class.getResource(location));
        return new Pair<>(fxmlLoader, fxmlLoader.load());
    }

    public static void activatePane(client.AppPane appPane) {
        StartRMIClient.appScene.setRoot(appLoaderMap.get(appPane).getValue());
    }

    public static void showAlert(Alert.AlertType type, String content, ButtonType... buttons) {
        Alert alert = new Alert(type, content, buttons);
        alert.setResizable(true);
        alert.show();
    }

    @Override
    public void init() {
        appScene = new Scene(new Pane());
        appLoaderMap = new EnumMap<>(client.AppPane.class);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        ApplicationContext factory = new ClassPathXmlApplicationContext("classpath:props.xml");
        IService server = (IService) factory.getBean("service");

        appLoaderMap.put(client.AppPane.AUTH, loader("/fxml/auth_pane.fxml"));
        appLoaderMap.put(client.AppPane.MAIN, loader("/fxml/main_pane.fxml"));

        AuthController authController = appLoaderMap.get(client.AppPane.AUTH).getKey().getController();
        authController.setService(server);

        MainController mainController = appLoaderMap.get(client.AppPane.MAIN).getKey().getController();
        mainController.setService(server);

        activatePane(client.AppPane.AUTH);

        primaryStage.setTitle("Game App");
        primaryStage.setScene(appScene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        Application.launch(args);
    }
}