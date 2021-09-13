import donation.model.Donation;
import donation.persistence.repository.CharityCaseDatabaseRepository;
import donation.persistence.repository.DonationDatabaseRepository;
import donation.persistence.repository.DonorDatabaseRepository;
import donation.persistence.repository.VolunteerDatabaseRepository;
import donation.server.DonationServicesImpl;
import donation.services.IDonationServices;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.io.IOException;
import java.util.Properties;

public class StartRpcServer {
    private static int defaultPort=55555;
    public static void main(String[] args) {
        /*
        // UserRepository userRepo=new UserRepositoryMock();
        Properties serverProps=new Properties();
        try {
            serverProps.load(StartRpcServer.class.getResourceAsStream("/donationserver.properties"));
            System.out.println("Server properties set. ");
            serverProps.list(System.out);
        } catch (IOException e) {
            System.err.println("Cannot find chatserver.properties "+e);
            return;
        }
        VolunteerDatabaseRepository volRepo = new VolunteerDatabaseRepository(serverProps);
        DonationDatabaseRepository donaRepo = new DonationDatabaseRepository(serverProps);
        DonorDatabaseRepository donRepo = new DonorDatabaseRepository(serverProps);
        CharityCaseDatabaseRepository charRepo = new CharityCaseDatabaseRepository(serverProps);
        IDonationServices donationServerImpl = new DonationServicesImpl(volRepo, donaRepo, donRepo, charRepo);
        int chatServerPort=defaultPort;
        try {
            chatServerPort = Integer.parseInt(serverProps.getProperty("chat.server.port"));
        }catch (NumberFormatException nef){
            System.err.println("Wrong  Port Number"+nef.getMessage());
            System.err.println("Using default port "+defaultPort);
        }
        System.out.println("Starting server on port: "+chatServerPort);
        AbstractServer server = new DonationRpcConcurrentServer(chatServerPort, donationServerImpl);
        try {
            server.start();
        } catch (ServerException e) {
            System.err.println("Error starting the server" + e.getMessage());
        }finally {
            try {
                server.stop();
            }catch(ServerException e){
                System.err.println("Error stopping server "+e.getMessage());
            }
        }
         */
        ApplicationContext factory = new ClassPathXmlApplicationContext("classpath:spring-server.xml");
    }
}
