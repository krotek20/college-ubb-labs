package repository;

import domain.Player;
import org.hibernate.Session;
import org.hibernate.Transaction;
import org.springframework.stereotype.Component;

@Component
public class PlayerRepository extends GenericOrmRepository<Player> implements IPlayerRepository {
    public PlayerRepository() {
        super(Player.class);
    }

    @Override
    public Player loginPlayer(Player player) {
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = null;
            try {
                tx = session.beginTransaction();
                Player p = session.createQuery("from Player where username = :username and password = :password",
                        Player.class)
                        .setParameter("username", player.getUsername())
                        .setParameter("password", player.getPassword())
                        .getSingleResult();
                tx.commit();
                return p;
            } catch (RuntimeException ex) {
                if (tx != null) {
                    tx.rollback();
                }
            }
        }
        return null;
    }
}
