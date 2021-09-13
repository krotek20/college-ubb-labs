package triathlon.persistence.ormRepository;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.springframework.stereotype.Component;
import triathlon.model.Referee;
import triathlon.persistence.RefereeRepository;

import java.util.ArrayList;
import java.util.List;

@Component
public class ORMRefereeRepository implements RefereeRepository {
    private static SessionFactory sessionFactory;

    public static void setSessionFactory(SessionFactory sessionFactory) {
        ORMRefereeRepository.sessionFactory = sessionFactory;
    }

    @Override
    public Referee findOne(Long id) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Referee referee = session.createQuery("from Referee where id = :id", Referee.class)
                        .setParameter("id", id).getSingleResult();
                tx.commit();
                return referee;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public Iterable<Referee> findAll() {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                List<Referee> referees = session.createQuery("from Referee ", Referee.class).list();
                tx.commit();
                return referees;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return new ArrayList<>();
    }

    @Override
    public void save(Referee referee) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                session.save(referee);
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }

    @Override
    public void update(Referee referee) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Referee updatedReferee = session.load(Referee.class, referee.getId());
                updatedReferee.setGame(referee.getGame());
                updatedReferee.setName(referee.getName());
                updatedReferee.setUsername(referee.getUsername());
                updatedReferee.setPassword(referee.getPassword());
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
                Referee referee = session.createQuery("from Referee where id = :id", Referee.class)
                        .setParameter("id", id).getSingleResult();
                session.delete(referee);
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }
}
