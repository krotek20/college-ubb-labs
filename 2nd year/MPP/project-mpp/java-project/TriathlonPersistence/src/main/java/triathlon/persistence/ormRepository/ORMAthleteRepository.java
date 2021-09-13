package triathlon.persistence.ormRepository;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import triathlon.model.Athlete;
import triathlon.persistence.AthleteRepository;

import java.util.ArrayList;
import java.util.List;

public class ORMAthleteRepository implements AthleteRepository {
    private static SessionFactory sessionFactory;

    public static void setSessionFactory(SessionFactory sessionFactory) {
        ORMAthleteRepository.sessionFactory = sessionFactory;
    }

    @Override
    public Athlete findOne(Long id) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Athlete athlete = session.createQuery("from Athlete where id = :id", Athlete.class)
                        .setParameter("id", id).getSingleResult();
                tx.commit();
                return athlete;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public Iterable<Athlete> findAll() {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                List<Athlete> athletes = session.createQuery("from Athlete ", Athlete.class).list();
                tx.commit();
                return athletes;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return new ArrayList<>();
    }

    @Override
    public void save(Athlete athlete) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                session.save(athlete);
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }

    @Override
    public void update(Athlete athlete) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Athlete updatedAthlete = session.load(Athlete.class, athlete.getId());
                updatedAthlete.setName(athlete.getName());
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
                Athlete athlete = session.createQuery("from Athlete where id = :id", Athlete.class)
                        .setParameter("id", id).getSingleResult();
                session.delete(athlete);
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }
}
