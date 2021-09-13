package com.radu.salesman.repository;

import com.radu.salesman.domain.User;

public interface UserRepository extends CRUDRepository<Long, User> {
    User findUser(String username, String password);
}
