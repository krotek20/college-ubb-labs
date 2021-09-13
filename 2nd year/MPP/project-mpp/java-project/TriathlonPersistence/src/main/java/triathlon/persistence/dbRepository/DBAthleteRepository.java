package triathlon.persistence.dbRepository;

import triathlon.model.Athlete;
import triathlon.persistence.validators.ValidationException;
import triathlon.persistence.RepositoryException;
import triathlon.persistence.AthleteRepository;
import triathlon.persistence.validators.Validator;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class DBAthleteRepository implements AthleteRepository {
    private final Validator<Athlete> validator;
    private final Connection connection;

    public DBAthleteRepository(Properties props, Validator<Athlete> validator) {
        this.connection = new JDBCManager(props).getConnection();
        this.validator = validator;
    }

    @Override
    public Athlete findOne(Long id) {
        final String sql_query = "select * from Athlete where id = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Athlete(
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
    public Iterable<Athlete> findAll() {
        final String sql_query = "select * from Athlete";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            List<Athlete> athletes = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                athletes.add(new Athlete(
                        resultSet.getLong("id"),
                        resultSet.getString("name")
                ));
            }
            return athletes;
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }

        return null;
    }

    @Override
    public void save(Athlete athlete) {
        final String sql_query = "insert into Athlete (name) values (?)";
        try {
            validator.validate(athlete);
        } catch (ValidationException ex) {
            throw new RepositoryException(ex.getMessage());
        }

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setString(1, athlete.getName());
            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }

    @Override
    public void update(Athlete athlete) {
        final String sql_query = "update Athlete set name = ? where id = ?";
        try {
            validator.validate(athlete);
        } catch (ValidationException ex) {
            throw new RepositoryException(ex.getMessage());
        }

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setString(1, athlete.getName());
            statement.setLong(2, athlete.getId());
            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }

    @Override
    public void delete(Long id) {
        final String sql_query = "delete from Athlete where id = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, id);

            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }
}