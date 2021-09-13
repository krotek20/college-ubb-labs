package repository;

import domain.User;

public interface IUserRepository extends ICrudRepository<Long, User> {
    User loginUser(User user);
}
