package repository;

import domain.Entity;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;

public class GenericOrmRepository<T extends Entity<Long>> implements ICrudRepository<Long, T> {
    protected static SessionFactory sessionFactory;

    private final Class<T> type;

    public GenericOrmRepository(Class<T> type) {
        this.type = type;
    }

    public static void setSessionFactory(SessionFactory sessionFactory) {
        GenericOrmRepository.sessionFactory = sessionFactory;
    }

    @Override
    public T findOne(Long aLong) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                T t = session.createQuery(String.format("from %s where id = :id", type.getName()), type).setParameter("id", aLong).getSingleResult();
                tx.commit();
                return t;
            } catch (RuntimeException ex) {
                ex.printStackTrace();
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public Iterable<T> findAll() {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                List<T> tList = session.createQuery(String.format("from %s", type.getName()), type).list();
                tx.commit();
                return tList;
            } catch (RuntimeException ex) {
                ex.printStackTrace();
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return new ArrayList<>();
    }

    @Override
    public T save(T entity) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                session.save(entity);
                tx.commit();
                return entity;
            } catch (RuntimeException ex) {
                ex.printStackTrace();
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public T delete(Long aLong) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                T t = session.createQuery(String.format("from %s where id = :id", type.getName()), type).setParameter("id", aLong).getSingleResult();
                session.delete(t);
                tx.commit();
                return t;
            } catch (RuntimeException ex) {
                ex.printStackTrace();
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }

    @Override
    public T update(T entity) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                T t = session.load(type, entity.getId());
                //T t = this.findOne(entity.getId());
                for (Method method : type.getMethods()) {
                    if (method.getName().startsWith("set")) {
                        //setters.add(method);
                        Method getter = type.getMethod(method.getName().replace("set", "get"));
                        method.invoke(t, getter.invoke(entity));
                    }
                }
                session.saveOrUpdate(t);
                tx.commit();
                return entity;
            } catch (RuntimeException ex) {
                ex.printStackTrace();
                if (tx != null) {
                    tx.rollback();
                }
            } catch (NoSuchMethodException | InvocationTargetException | IllegalAccessException e) {
                e.printStackTrace();
            }
        }
        return null;
    }
}
