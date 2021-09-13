package com.radu.salesman.repository.db;

import com.radu.salesman.domain.User;
import com.radu.salesman.repository.UserRepository;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class UserDBRepository implements UserRepository {
    private final Connection connection;

    public UserDBRepository(JDBCUtils jdbcUtils) throws SQLException {
        this.connection = jdbcUtils.getConnection();
    }

    @Override
    public User findOne(Long aLong) {
        return null;
    }

    @Override
    public Iterable<User> findAll() {
        return null;
    }

    @Override
    public User save(User entity) {
        return null;
    }

    @Override
    public void update(User entity) {

    }

    @Override
    public void delete(Long aLong) {

    }

    @Override
    public User findUser(String username, String password) {
        final String sql_query = "select * from Users where username = ? and password = ?";
        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setString(1, username);
            statement.setString(2, password);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new User();
            }
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
        return null;
    }
}
