package com.radu.salesman.repository.orm;

import com.radu.salesman.domain.Order;
import com.radu.salesman.repository.OrderRepository;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

public class OrderORMRepository implements OrderRepository {
    private static SessionFactory sessionFactory;

    public static void setSessionFactory(SessionFactory sessionFactory) {
        OrderORMRepository.sessionFactory = sessionFactory;
    }

    @Override
    public Order findOne(Long aLong) {
        return null;
    }

    @Override
    public Iterable<Order> findAll() {
        return null;
    }

    @Override
    public Order save(Order order) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                session.save(order);
                tx.commit();
                return order;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public void update(Order entity) {

    }

    @Override
    public void delete(Long aLong) {

    }
}
