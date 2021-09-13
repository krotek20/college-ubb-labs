/*
 * This code has been generated by the Rebel: a code generator for modern Java.
 *
 * Drop us a line or two at feedback@archetypesoftware.com: we would love to hear from you!
 */
package com.radu.salesman.repository.orm;

import com.radu.salesman.domain.Product;
import com.radu.salesman.repository.ProductRepository;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import java.util.ArrayList;
import java.util.List;

// ----------- << imports@AAAAAAF4xpezfFAozJ4= >>
// ----------- >>

// ----------- << class.annotations@AAAAAAF4xpezfFAozJ4= >>
// ----------- >>

public class ProductORMRepository implements ProductRepository {
    private static SessionFactory sessionFactory;

    public static void setSessionFactory(SessionFactory sessionFactory) {
        ProductORMRepository.sessionFactory = sessionFactory;
    }

    @Override
    public Product findOne(Long id) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Product product = session.createQuery("from Product where id = :id", Product.class)
                        .setParameter("id", id).getSingleResult();
                tx.commit();
                return product;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    // ----------- << method.annotations@AAAAAAF4xprPfG2NevM= >>
    // ----------- >>
    @Override
    public Iterable<Product> findAll() {
        // ----------- << method.body@AAAAAAF4xprPfG2NevM= >>
        // ----------- >>
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                List<Product> products = session.createQuery("from Product", Product.class).list();
                tx.commit();
                return products;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return new ArrayList<>();
    }

    @Override
    public Product save(Product product) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                session.save(product);
                tx.commit();
                return product;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public void update(Product product) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Product updatedProduct = session.load(Product.class, product.getId());
                updatedProduct.setQuantity(product.getQuantity());
                updatedProduct.setPrice(product.getPrice());
                updatedProduct.setName(product.getName());
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }

    @Override
    public void delete(Long id) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Product product = session.createQuery("from Product where id = :id", Product.class)
                        .setParameter("id", id).getSingleResult();
                session.delete(product);
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }
    // ----------- << class.extras@AAAAAAF4xpezfFAozJ4= >>
    // ----------- >>
}
