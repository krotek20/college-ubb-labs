package com.radu.salesman;

import com.radu.salesman.repository.*;
import com.radu.salesman.repository.orm.*;
import org.hibernate.SessionFactory;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import com.radu.salesman.service.Service;
import com.radu.salesman.service.ServiceImpl;
import com.radu.salesman.ui.gui.MainGUI;

public class Main {
    private static SessionFactory sessionFactory;

    static void initialize() {
        final StandardServiceRegistry registry = new StandardServiceRegistryBuilder()
                .configure()
                .build();
        try {
            sessionFactory = new MetadataSources(registry).buildMetadata().buildSessionFactory();
        } catch (Exception e) {
            System.err.println("Exceptie " + e);
            StandardServiceRegistryBuilder.destroy(registry);
        }
    }

    static void close() {
        if (sessionFactory != null) {
            sessionFactory.close();
        }
    }

    public static void main(String[] args) {
        initialize();
        UserRepository userRepository = new UserORMRepository();
        ProductRepository productRepository = new ProductORMRepository();
        OrderRepository orderRepository = new OrderORMRepository();
        CartElementRepository cartElementRepository = new CartElementORMRepository();
        OrderElementRepository orderElementRepository = new OrderElementORMRepository();
        Service service = new ServiceImpl(userRepository, productRepository, orderRepository,
                cartElementRepository, orderElementRepository);

        UserORMRepository.setSessionFactory(sessionFactory);
        ProductORMRepository.setSessionFactory(sessionFactory);
        OrderORMRepository.setSessionFactory(sessionFactory);
        CartElementORMRepository.setSessionFactory(sessionFactory);
        OrderElementORMRepository.setSessionFactory(sessionFactory);

        MainGUI mainGUI = new MainGUI();
        mainGUI.setService(service);
        mainGUI.run();

        close();
    }
}
