import controller.LoginController;
import controller.MainController;
import donation.services.IDonationServices;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainFX extends Application {

    //private Stage primaryStage;
    int port = 1313;
    String host = "localhost";

    @Override
    public void start(Stage primaryStage) throws Exception {

        ApplicationContext factory = new ClassPathXmlApplicationContext("classpath:spring-client.xml");
        IDonationServices proxy=(IDonationServices)factory.getBean("donationService");
        System.out.println("Obtained a reference to remote chat server");


        FXMLLoader loader = new FXMLLoader(getClass().getResource("Login.fxml"));
        Parent root = loader.load();

        LoginController loginController = loader.getController();
        loginController.setService(proxy);

        FXMLLoader cloader = new FXMLLoader(
                getClass().getClassLoader().getResource("Main.fxml"));
        Parent croot=cloader.load();
        MainController mainCtrl = cloader.getController();
        mainCtrl.setService(proxy);

        loginController.setMainCtrl(mainCtrl);
        loginController.setParent(croot);

        primaryStage.setTitle("Login");
        primaryStage.setScene(new Scene(root, 800, 600));
        primaryStage.show();

    }

    public static void main(String[] args) {
        Application.launch(args);
    }

}