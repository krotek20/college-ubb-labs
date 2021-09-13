package triathlon.persistence.dbRepository;

import triathlon.model.Game;
import triathlon.model.Referee;
import triathlon.persistence.RefereeRepository;
import triathlon.persistence.RepositoryException;
import triathlon.persistence.validators.ValidationException;
import triathlon.persistence.validators.Validator;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class DBRefereeRepository implements RefereeRepository {
    private final Validator<Referee> validator;
    private final Connection connection;

    public DBRefereeRepository(Properties props, Validator<Referee> validator) {
        this.connection = new JDBCManager(props).getConnection();
        this.validator = validator;
    }

    @Override
    public Referee findOne(Long id) {
        final String sql_query = "select r.id as id, g.id as gid, r.name as name, g.name as gname, username, password " +
                "from Referee r, Game g where id = ? and r.gameId=g.id";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, id);

            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                Referee referee = new Referee(
                        resultSet.getLong("id"),
                        new Game(resultSet.getLong("gid"), resultSet.getString("gname")),
                        resultSet.getString("name"),
                        resultSet.getString("username"),
                        resultSet.getString("password")
                );
                return referee;
            }
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }

        return null;
    }

    @Override
    public Iterable<Referee> findAll() {
        final String sql_query = "select r.id as id, g.id as gid, r.name as name, g.name as gname, username, password" +
                " from Referee r, Game g where r.gameId=g.id";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            List<Referee> referees = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                referees.add(new Referee(
                        resultSet.getLong("id"),
                        new Game(resultSet.getLong("gid"), resultSet.getString("gname")),
                        resultSet.getString("name"),
                        resultSet.getString("username"),
                        resultSet.getString("password")
                ));
            }
            return referees;
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }

        return null;
    }

    @Override
    public void save(Referee referee) {
        final String sql_query =
                "insert into Referee (gameId, name, username, password) values (?,?,?,?)";
        try {
            validator.validate(referee);
        } catch (ValidationException ex) {
            throw new RepositoryException(ex.getMessage());
        }

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, referee.getGame().getId());
            statement.setString(2, referee.getName());
            statement.setString(3, referee.getUsername());
            statement.setString(4, referee.getPassword());

            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }

    @Override
    public void update(Referee referee) {
        final String sql_query = "update Referee set gameId = ?, name = ?, username = ?, password = ? where id = ?";
        try {
            validator.validate(referee);
        } catch (ValidationException ex) {
            throw new RepositoryException(ex.getMessage());
        }

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, referee.getGame().getId());
            statement.setString(2, referee.getName());
            statement.setString(3, referee.getUsername());
            statement.setString(4, referee.getPassword());
            statement.setLong(5, referee.getId());

            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }

    @Override
    public void delete(Long id) {
        final String sql_query = "delete from Referee where id = ?";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            statement.setLong(1, id);

            int updates = statement.executeUpdate();
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }
    }
}