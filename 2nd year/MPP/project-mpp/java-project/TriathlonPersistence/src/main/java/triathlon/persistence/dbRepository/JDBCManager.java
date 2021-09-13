package triathlon.persistence.dbRepository;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class JDBCManager {
    private final Properties jdbcProps;
    private Connection connection = null;

    public JDBCManager(Properties props) {
        jdbcProps = props;
    }

    private Connection getNewConnection() {

        String url = jdbcProps.getProperty("jdbc.url");
        String user = jdbcProps.getProperty("jdbc.user");
        String pass = jdbcProps.getProperty("jdbc.pass");
        Connection con = null;
        try {
            if (user != null && pass != null)
                con = DriverManager.getConnection(url, user, pass);
            else
                con = DriverManager.getConnection(url);
        } catch (SQLException e) {
            System.out.println("Error getting connection " + e);
        }
        return con;
    }

    public Connection getConnection() {
        try {
            if (connection == null || connection.isClosed())
                connection = getNewConnection();

        } catch (SQLException e) {
            System.out.println("Error DB " + e);
        }
        return connection;
    }
}
