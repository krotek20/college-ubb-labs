package donation.persistence.repository;

import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class dbUtils {
    private static dbUtils instance = null;

    private Connection connection;
    public Connection getConnection(Properties properties) {
        try {
            return DriverManager.getConnection(properties.getProperty("donation.jdbc.url"),
                    properties.getProperty("donation.jdbc.user"),
                    properties.getProperty("donation.jdbc.password"));
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    public static dbUtils getInstance()
    {
        if(instance == null) instance = new dbUtils();
        return instance;
    }
}
