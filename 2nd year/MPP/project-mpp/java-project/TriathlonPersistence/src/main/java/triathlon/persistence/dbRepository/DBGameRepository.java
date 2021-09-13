package triathlon.persistence.dbRepository;

import triathlon.persistence.validators.ValidationException;
import triathlon.persistence.RepositoryException;
import triathlon.persistence.GameRepository;
import triathlon.model.Game;
import triathlon.persistence.validators.Validator;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class DBGameRepository implements GameRepository {
    private final Validator<Game> validator;
    private final Connection connection;

    public DBGameRepository(Properties props, Validator<Game> validator) {
        this.connection = new JDBCManager(props).getConnection();
        this.validator = validator;
    }

    @Override
    public Game findOne(Long id) {
        final String sql_query = "select * from Game where id = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, id);

            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Game(
                        resultSet.getLong("id"),
                        resultSet.getString("name")
                );
            }
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }

        return null;
    }

    @Override
    public Iterable<Game> findAll() {
        final String sql_query = "select * from Game";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            List<Game> games = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                games.add(new Game(
                        resultSet.getLong("id"),
                        resultSet.getString("name")
                ));
            }
            return games;
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }

        return null;
    }

    @Override
    public void save(Game game) {
        final String sql_query = "insert into Game (name) values (?)";
        try {
            validator.validate(game);
        } catch (ValidationException ex) {
            throw new RepositoryException(ex.getMessage());
        }

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setString(1, game.getName());
            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }

    @Override
    public void update(Game game) {
        final String sql_query = "update Game set name = ? where id = ?";
        try {
            validator.validate(game);
        } catch (ValidationException ex) {
            throw new RepositoryException(ex.getMessage());
        }

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setString(1, game.getName());
            statement.setLong(2, game.getId());
            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }

    @Override
    public void delete(Long id) {
        final String sql_query = "delete from Game where id = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, id);

            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }
}