package start;

import org.hibernate.SessionFactory;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import triathlon.persistence.ormRepository.ORMAthleteRepository;
import triathlon.persistence.ormRepository.ORMGameRepository;
import triathlon.persistence.ormRepository.ORMRefereeRepository;
import triathlon.persistence.ormRepository.ORMResultRepository;

@ComponentScan("triathlon")
@SpringBootApplication
public class StartRestServices {
    public static void main(String[] args) {
        final StandardServiceRegistry registry = new StandardServiceRegistryBuilder().configure().build();
        SessionFactory sessionFactory = null;
        try {
            sessionFactory = new MetadataSources(registry).buildMetadata().buildSessionFactory();
        } catch (Exception e) {
            System.err.println("Exception " + e);
            e.printStackTrace();
            StandardServiceRegistryBuilder.destroy(registry);
        }
        ORMAthleteRepository.setSessionFactory(sessionFactory);
        ORMRefereeRepository.setSessionFactory(sessionFactory);
        ORMGameRepository.setSessionFactory(sessionFactory);
        ORMResultRepository.setSessionFactory(sessionFactory);

        SpringApplication.run(StartRestServices.class, args);
    }
}