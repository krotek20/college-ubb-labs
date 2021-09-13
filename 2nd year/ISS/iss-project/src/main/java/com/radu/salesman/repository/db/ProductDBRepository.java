package com.radu.salesman.repository.db;

import com.radu.salesman.domain.Product;
import com.radu.salesman.repository.ProductRepository;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class ProductDBRepository implements ProductRepository {
    private final Connection connection;

    public ProductDBRepository(JDBCUtils jdbcUtils) throws SQLException {
        this.connection = jdbcUtils.getConnection();
    }
    @Override
    public Product findOne(Long aLong) {
        return null;
    }

    @Override
    public Iterable<Product> findAll() {
        final String sql_query = "select * from Products";

        try (PreparedStatement statement = connection.prepareStatement(sql_query)) {
            List<Product> products = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                products.add(new Product(
                        resultSet.getString("name"),
                        resultSet.getInt("quantity"),
                        resultSet.getFloat("price")
                ));
            }
            return products;
        } catch (SQLException e) {
            System.err.println("Error DB: " + e);
        }

        return null;
    }

    @Override
    public Product save(Product entity) {
        return null;
    }

    @Override
    public void update(Product entity) {

    }

    @Override
    public void delete(Long aLong) {

    }
}
