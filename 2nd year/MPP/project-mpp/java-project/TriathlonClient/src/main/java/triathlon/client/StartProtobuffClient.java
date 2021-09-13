package triathlon.client;

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
import triathlon.client.controller.AuthController;
import triathlon.client.controller.MainController;
import triathlon.services.ITriathlonServices;

import java.net.URL;
import java.util.EnumMap;

public class StartProtobuffClient extends Application {
    public static EnumMap<AppPane, Pair<FXMLLoader, Parent>> appLoaderMap;
    private static Scene appScene;

    private static Pair<FXMLLoader, Parent> loader(String location) throws Exception {
        FXMLLoader fxmlLoader = new FXMLLoader(StartRMIClient.class.getResource(location));
        return new Pair<>(fxmlLoader, fxmlLoader.load());
    }

    public static void activatePane(AppPane appPane) {
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
        appLoaderMap = new EnumMap<>(AppPane.class);
    }

    @Override
    public void start(Stage primaryStage) throws Exception {
        ApplicationContext factory = new ClassPathXmlApplicationContext("classpath:spring-client.xml");
        ITriathlonServices server = (ITriathlonServices) factory.getBean("triathlonService");
        System.out.println("Obtained a reference to remote chat server");

        appLoaderMap.put(AppPane.AUTH, loader("/fxml/auth_pane.fxml"));
        appLoaderMap.put(AppPane.MAIN, loader("/fxml/main_pane.fxml"));

        AuthController authController = appLoaderMap.get(AppPane.AUTH).getKey().getController();
        authController.setService(server);

        MainController mainController = appLoaderMap.get(AppPane.MAIN).getKey().getController();
        mainController.setService(server);

        activatePane(AppPane.AUTH);

        primaryStage.setTitle("Triathlon Manager Pro");
        primaryStage.setScene(appScene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        Application.launch(args);
    }
}
