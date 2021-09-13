package triathlon.persistence.ormRepository;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import triathlon.model.Result;
import triathlon.persistence.ResultRepository;

import java.util.ArrayList;
import java.util.List;

public class ORMResultRepository implements ResultRepository {
    private static SessionFactory sessionFactory;

    public static void setSessionFactory(SessionFactory sessionFactory) {
        ORMResultRepository.sessionFactory = sessionFactory;
    }

    @Override
    public Result findOne(Long id) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Result result = session.createQuery("from Result where id = :id", Result.class)
                        .setParameter("id", id).getSingleResult();
                tx.commit();
                return result;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public Iterable<Result> findAll() {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                List<Result> results = session.createQuery("from Result ", Result.class).list();
                tx.commit();
                return results;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return new ArrayList<>();
    }

    @Override
    public void save(Result result) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                session.save(result);
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }

    @Override
    public void update(Result result) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Result updatedResult = session.load(Result.class, result.getId());
                updatedResult.setGame(result.getGame());
                updatedResult.setAthlete(result.getAthlete());
                updatedResult.setValue(result.getValue());
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
                Result result = session.createQuery("from Result where id = :id", Result.class)
                        .setParameter("id", id).getSingleResult();
                session.delete(result);
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }
}
