package repository;

import domain.Entity;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public interface ICrudRepository<ID, E extends Entity<ID>> {
    Logger logger = LogManager.getLogger();

    E findOne(ID id);

    Iterable<E> findAll();

    E save(E entity);

    E delete(ID id);

    E update(E entity);
}
