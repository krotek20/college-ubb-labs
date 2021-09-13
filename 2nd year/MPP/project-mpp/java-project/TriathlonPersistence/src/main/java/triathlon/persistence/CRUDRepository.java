package triathlon.persistence;

import triathlon.model.Entity;

public interface CRUDRepository<ID, E extends Entity<ID>> {
    E findOne(ID id);

    Iterable<E> findAll();

    void save(E entity);

    void update(E entity);

    void delete(ID id);
}