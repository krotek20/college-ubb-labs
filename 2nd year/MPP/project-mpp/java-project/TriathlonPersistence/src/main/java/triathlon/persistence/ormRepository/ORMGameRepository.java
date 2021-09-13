package triathlon.persistence.ormRepository;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import triathlon.model.Game;
import triathlon.persistence.GameRepository;

import java.util.ArrayList;
import java.util.List;

public class ORMGameRepository implements GameRepository {
    private static SessionFactory sessionFactory;

    public static void setSessionFactory(SessionFactory sessionFactory) {
        ORMGameRepository.sessionFactory = sessionFactory;
    }

    @Override
    public Game findOne(Long id) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Game game = session.createQuery("from Game where id = :id", Game.class)
                        .setParameter("id", id).getSingleResult();
                tx.commit();
                return game;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public Iterable<Game> findAll() {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                List<Game> games = session.createQuery("from Game ", Game.class).list();
                tx.commit();
                return games;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return new ArrayList<>();
    }

    @Override
    public void save(Game game) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                session.save(game);
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }

    @Override
    public void update(Game game) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Game updatedGame = session.load(Game.class, game.getId());
                updatedGame.setName(game.getName());
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
                Game game = session.createQuery("from Game where id = :id", Game.class)
                        .setParameter("id", id).getSingleResult();
                session.delete(game);
                tx.commit();
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
    }
}
