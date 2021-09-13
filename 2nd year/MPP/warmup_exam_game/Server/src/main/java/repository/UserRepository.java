package repository;

import domain.User;
import org.hibernate.Session;
import org.hibernate.Transaction;
import org.springframework.stereotype.Component;

@Component
public class UserRepository extends GenericOrmRepository<User> implements IUserRepository {
    public UserRepository() {
        super(User.class);
    }

    @Override
    public User loginUser(User user) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                User u = session.createQuery("from User where username = :username and password = :password",
                        User.class)
                        .setParameter("username", user.getUsername())
                        .setParameter("password", user.getPassword())
                        .getSingleResult();
                tx.commit();
                return u;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }
}
