import org.hibernate.SessionFactory;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import triathlon.persistence.ormRepository.ORMAthleteRepository;
import triathlon.persistence.ormRepository.ORMRefereeRepository;

public class StartRMIServer {
    public static void main(String[] args) {
         final StandardServiceRegistry registry = new StandardServiceRegistryBuilder().configure().build();
//        Configuration cfg = new Configuration().configure();
        SessionFactory sessionFactory = null;
        try {
            sessionFactory = new MetadataSources(registry).buildMetadata().buildSessionFactory();
//        SessionFactory sessionFactory = cfg.buildSessionFactory();
        } catch (Exception e) {
            System.err.println("Exception " + e);
            e.printStackTrace();
            StandardServiceRegistryBuilder.destroy(registry);
        }
        System.out.println("HELOO");
        System.out.println(sessionFactory);
        System.out.println("BYE");
        ORMAthleteRepository.setSessionFactory(sessionFactory);
        ORMRefereeRepository.setSessionFactory(sessionFactory);
        ApplicationContext factory = new ClassPathXmlApplicationContext("classpath:spring-server.xml");
    }
}