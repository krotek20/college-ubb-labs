import controller.GeneralController;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import service.IService;
import ui.IUI;
import ui.gui.GUI;
import ui.gui.StagePuppeteer;

import java.rmi.RemoteException;

public class Main {
    public static void main(String[] args) {
        try {
            GeneralController controller = new GeneralController();
            ApplicationContext factory = new ClassPathXmlApplicationContext("classpath:props.xml");
            //Properties props = (Properties) factory.getBean("props");
            //ClientNetworking client = new ClientNetworking(props.getProperty("hostname"), Integer.parseInt(props.getProperty("port")));
            //IService service = new ServiceProxy(client);
            IService service = (IService) factory.getBean("service");
            StagePuppeteer.setController(controller);
            controller.setService(service);
            IUI gui = new GUI();
            gui.startUI();
            controller.logout();
        } catch (RemoteException e) {
            e.printStackTrace();
        }
    }
}
