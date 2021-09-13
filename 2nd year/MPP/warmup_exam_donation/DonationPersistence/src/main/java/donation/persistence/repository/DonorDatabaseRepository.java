package donation.persistence.repository;

import donation.model.Donor;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class DonorDatabaseRepository implements IDonorRepository{

    Connection connection;
    public DonorDatabaseRepository(Properties props) {
        connection = dbUtils.getInstance().getConnection(props);
    }

    @Override
    public Donor Add(Donor entity) {
        try {
            Statement st = connection.createStatement();
            int res = st.executeUpdate(String.format("insert into donors (id, name, address, phonenumber) values (%d, '%s', '%s', '%s')",
                    entity.getId(),entity.getName(),entity.getAddress(),entity.getPhoneNumber()));
            return null;
        } catch (SQLException throwables) {
            return entity;
        }
    }

    @Override
    public Donor Delete(Long id) {
        try {
            Statement st = connection.createStatement();
            st.executeQuery(String.format("delete from donors where id=%d returning *",id));
            ResultSet rs = st.getResultSet();
            if(rs.next())
                return new Donor(id, rs.getString("name"),rs.getString("address"),rs.getString("phonenumber"));
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public Donor Update(Donor entity) {
        try {
            Statement st = connection.createStatement();
            st.execute(String.format("update donors set name='%s', address='%s', phonenumber='%s' where id=%d returning *",
                    entity.getName(),entity.getAddress(),entity.getPhoneNumber(),entity.getId()));
            ResultSet rs = st.getResultSet();
            if(rs.next())
                return entity;
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public Donor FindById(Long id) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery(String.format("select * from donors where id=%d",id));
            if(rs.next())
                return new Donor(id, rs.getString("name"),rs.getString("address"),rs.getString("phonenumber"));
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public List<Donor> FindAll() {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery("select * from donors");
            ArrayList<Donor> list = new ArrayList<>();
            while(rs.next())
                list.add(new Donor(rs.getLong("id"), rs.getString("name"),rs.getString("address"),rs.getString("phonenumber")));
            return list;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public Long GetMaxId() throws SQLException {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery(String.format("select max(id) from donors"));
        rs.next();
        return rs.getLong(1);
    }

    @Override
    public List<Donor> FilterByName(String name, boolean caseSensitive) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = caseSensitive ? st.executeQuery("select * from donors where name like '%"+name+"%'")
                    : st.executeQuery("select * from donors where lower(name) like '%"+name.toLowerCase()+"%'");
            ArrayList<Donor> list = new ArrayList<>();
            while(rs.next())
                list.add(new Donor(rs.getLong("id"), rs.getString("name"),rs.getString("address"),rs.getString("phonenumber")));
            return list;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public List<Donor> FilterByPhoneNumber(String phone) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery("select * from donors where phonenumber like '%"+phone+"%'");
            ArrayList<Donor> list = new ArrayList<>();
            while(rs.next())
                list.add(new Donor(rs.getLong("id"), rs.getString("name"),rs.getString("address"),rs.getString("phonenumber")));
            return list;
        } catch (SQLException throwables) {
            return null;
        }
    }
}
