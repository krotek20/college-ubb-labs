package donation.persistence.repository;


import donation.model.Entity;

import java.sql.SQLException;
import java.util.List;

public interface ICrudRepository<ID, E extends Entity<ID>> {
    /**
     * Adds to the list
     * @param entity the entity to be added
     * @return null on success, otherwise returns back the entity
     */
    E Add(E entity);
    E Delete(ID id);
    E Update(E entity);
    E FindById(ID id);
    List<E> FindAll();
    ID GetMaxId() throws SQLException;
}
