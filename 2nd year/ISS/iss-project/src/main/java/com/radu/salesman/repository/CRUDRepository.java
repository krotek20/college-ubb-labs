package com.radu.salesman.repository;

import com.radu.salesman.domain.Entity;

public interface CRUDRepository<ID, E extends Entity<ID>> {
    E findOne(ID id);

    Iterable<E> findAll();

    E save(E entity);

    void update(E entity);

    void delete(ID id);
}