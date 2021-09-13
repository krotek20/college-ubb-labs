package triathlon.persistence.dbRepository;

import triathlon.model.Athlete;
import triathlon.model.Game;
import triathlon.persistence.validators.ValidationException;
import triathlon.persistence.RepositoryException;
import triathlon.persistence.ResultRepository;
import triathlon.model.Result;
import triathlon.persistence.validators.Validator;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class DBResultRepository implements ResultRepository {
    private final Validator<Result> validator;
    private final Connection connection;

    public DBResultRepository(Properties props, Validator<Result> validator) {
        this.connection = new JDBCManager(props).getConnection();
        this.validator = validator;
    }

    @Override
    public Result findOne(Long id) {
        final String sql_query = "select r.id as id, g.id as gid, a.id as aid, g.name as gname, a.name as aname, value " +
                "from Result r, Game g, Athlete a where id = ? and r.gameId=g.id and r.athleteId=a.id";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, id);

            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Result(
                        resultSet.getLong("id"),
                        new Game(resultSet.getLong("gid"), resultSet.getString("gname")),
                        new Athlete(resultSet.getLong("aid"), resultSet.getString("aname")),
                        resultSet.getFloat("value")
                );
            }
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }

        return null;
    }

    @Override
    public Iterable<Result> findAll() {
        final String sql_query = "select r.id as id, g.id as gid, a.id as aid, g.name as gname, a.name as aname, value " +
                "from Result r, Game g, Athlete a where r.gameId=g.id and r.athleteId=a.id";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            List<Result> results = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                results.add(new Result(
                        resultSet.getLong("id"),
                        new Game(resultSet.getLong("gid"), resultSet.getString("gname")),
                        new Athlete(resultSet.getLong("aid"), resultSet.getString("aname")),
                        resultSet.getFloat("value")
                ));
            }
            return results;
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }

        return null;
    }

    @Override
    public void save(Result result) {
        final String sql_query = "insert into Result (gameId, athleteId, value) values (?,?,?)";
        try {
            validator.validate(result);
        } catch (ValidationException ex) {
            throw new RepositoryException(ex.getMessage());
        }

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, result.getGame().getId());
            statement.setLong(2, result.getAthlete().getId());
            statement.setFloat(3, result.getValue());

            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }

    @Override
    public void update(Result result) {
        final String sql_query = "update Result set gameId = ?, athleteId = ?, value = ? where id = ?";
        try {
            validator.validate(result);
        } catch (ValidationException ex) {
            throw new RepositoryException(ex.getMessage());
        }

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, result.getGame().getId());
            statement.setLong(2, result.getAthlete().getId());
            statement.setFloat(3, result.getValue());
            statement.setLong(4, result.getId());

            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }

    @Override
    public void delete(Long id) {
        final String sql_query = "delete from Result where id = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, id);

            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }
}