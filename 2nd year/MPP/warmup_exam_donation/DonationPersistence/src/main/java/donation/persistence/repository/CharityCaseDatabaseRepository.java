package donation.persistence.repository;


import donation.model.CharityCase;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class CharityCaseDatabaseRepository implements ICharityCaseRepository {
    Connection connection;
    public CharityCaseDatabaseRepository(Properties props) {
        connection = dbUtils.getInstance().getConnection(props);
    }

    @Override
    public List<CharityCase> FilterByName(String name) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery("select * from charitycases where name like '%"+name+"%'");
            ArrayList<CharityCase> list = new ArrayList<>();
            while(rs.next())
                list.add(new CharityCase(rs.getLong("id"), rs.getString("name")));
            return list;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public CharityCase Add(CharityCase entity) {
        try {
            Statement st = connection.createStatement();
            int res = st.executeUpdate(String.format("insert into charitycases (id, name) values (%d, '%s')",
                    entity.getId(),entity.getName()));
            return null;
        } catch (SQLException throwables) {
            return entity;
        }
    }

    @Override
    public CharityCase Delete(Long id) {
        try {
            Statement st = connection.createStatement();
            st.executeQuery(String.format("delete from charitycases where id=%d returning *",id));
            ResultSet rs = st.getResultSet();
            if(rs.next())
                return new CharityCase(id, rs.getString("name"));
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public CharityCase Update(CharityCase entity) {
        try {
            Statement st = connection.createStatement();
            st.execute(String.format("update charitycases set name='%s' where id=%d returning *", entity.getName()));
            ResultSet rs = st.getResultSet();
            if(rs.next())
                return entity;
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public CharityCase FindById(Long id) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery(String.format("select * from charitycases where id=%d",id));
            if(rs.next())
                return new CharityCase(id, rs.getString("name"));
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public List<CharityCase> FindAll() {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery("select * from charitycases");
            ArrayList<CharityCase> list = new ArrayList<>();
            while(rs.next())
                list.add(new CharityCase(rs.getLong("id"), rs.getString("name")));
            return list;
        } catch (SQLException throwables) {
            return null;
        }
    }
    @Override
    public Long GetMaxId() throws SQLException {
        Statement st = connection.createStatement();
        ResultSet rs = st.executeQuery(String.format("select max(id) from charitycases"));
        rs.next();
        return rs.getLong(1);
    }
}
