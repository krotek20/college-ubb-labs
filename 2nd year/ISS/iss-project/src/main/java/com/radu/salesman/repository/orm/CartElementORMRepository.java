package com.radu.salesman.repository.orm;

import com.radu.salesman.domain.CartElement;
import com.radu.salesman.repository.CartElementRepository;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

public class CartElementORMRepository implements CartElementRepository {
    private static SessionFactory sessionFactory;

    public static void setSessionFactory(SessionFactory sessionFactory) {
        CartElementORMRepository.sessionFactory = sessionFactory;
    }

    @Override
    public CartElement findOne(Long aLong) {
        return null;
    }

    @Override
    public Iterable<CartElement> findAll() {
        return null;
    }

    @Override
    public CartElement save(CartElement cartElement) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                session.save(cartElement);
                tx.commit();
                return cartElement;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public void update(CartElement entity) {

    }

    @Override
    public void delete(Long id) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                CartElement cartElement = session.createQuery("from CartElement where id = :id", CartElement.class)
                        .setParameter("id", id).getSingleResult();
                session.delete(cartElement);
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }
}
