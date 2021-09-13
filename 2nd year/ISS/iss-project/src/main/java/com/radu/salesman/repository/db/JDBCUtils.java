package com.radu.salesman.repository.db;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class JDBCUtils {
    private final Properties properties = new Properties();
    private Connection connection = null;

    public JDBCUtils() {
        String propertiesFile = "jdbc.properties";
        InputStream inputStream = JDBCUtils.class.getClassLoader().getResourceAsStream(propertiesFile);
        try {
            properties.load(inputStream);
        } catch (IOException e) {
            System.err.println(e.toString());
        } finally {
            if (inputStream != null) {
                try {
                    inputStream.close();
                } catch (IOException e) {
                    System.err.println(e.toString());
                }
            }
        }
    }

    public Connection getConnection() throws SQLException {
        if (connection == null) {
            connection = DriverManager.getConnection(properties.getProperty("url"));
        }
        return connection;
    }
}
