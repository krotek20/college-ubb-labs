package com.radu.salesman.repository.orm;

import com.radu.salesman.domain.OrderElement;
import com.radu.salesman.repository.OrderElementRepository;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

public class OrderElementORMRepository implements OrderElementRepository {
    private static SessionFactory sessionFactory;

    public static void setSessionFactory(SessionFactory sessionFactory) {
        OrderElementORMRepository.sessionFactory = sessionFactory;
    }

    @Override
    public OrderElement findOne(Long aLong) {
        return null;
    }

    @Override
    public Iterable<OrderElement> findAll() {
        return null;
    }

    @Override
    public OrderElement save(OrderElement orderElement) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                session.save(orderElement);
                tx.commit();
                return orderElement;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public void update(OrderElement entity) {

    }

    @Override
    public void delete(Long aLong) {

    }
}
