package donation.persistence.repository;

import donation.model.Volunteer;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class VolunteerDatabaseRepository implements IVolunteerRepository {
    Connection connection;
    public VolunteerDatabaseRepository(Properties props) {
        connection = dbUtils.getInstance().getConnection(props);
    }

    @Override
    public Volunteer Add(Volunteer entity) {
        try {
            Statement st = connection.createStatement();
            int res = st.executeUpdate(String.format("insert into volunteers (id, name, username, password) values (%d, '%s', '%s', '%s')",
                        entity.getId(),entity.getName(),entity.getUsername(),entity.getPassword()));
            return null;
        } catch (SQLException throwables) {
            return entity;
        }
    }

    @Override
    public Volunteer Delete(Long id) {
        try {
            Statement st = connection.createStatement();
            st.executeQuery(String.format("delete from volunteers where id=%d returning *",id));
            ResultSet rs = st.getResultSet();
            if(rs.next())
                 return new Volunteer(id, rs.getString("name"),rs.getString("username"),rs.getString("password"));
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public Volunteer Update(Volunteer entity) {
        try {
            Statement st = connection.createStatement();
            st.execute(String.format("update volunteers set name='%s', username='%s', password='%s' where id=%d returning *",
                    entity.getName(),entity.getUsername(),entity.getPassword(),entity.getId()));
            ResultSet rs = st.getResultSet();
            if(rs.next())
                return entity;
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public Volunteer FindById(Long id) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery(String.format("select * from volunteers where id=%d",id));
            if(rs.next())
                return new Volunteer(id, rs.getString("name"),rs.getString("username"),rs.getString("password"));
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public List<Volunteer> FindAll() {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery("select * from volunteers");
            ArrayList<Volunteer> list = new ArrayList<>();
            while(rs.next())
                list.add(new Volunteer(rs.getLong("id"), rs.getString("name"),rs.getString("username"),rs.getString("password")));
            return list;
        } catch (SQLException throwables) {
            return null;
        }
    }


    @Override
    public List<Volunteer> FilterByName(String name) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery("select * from volunteers where name like '%"+name+"%'");
            ArrayList<Volunteer> list = new ArrayList<>();
            while(rs.next())
                list.add(new Volunteer(rs.getLong("id"), rs.getString("name"),rs.getString("username"),rs.getString("password")));
            return list;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public Volunteer FindByCredentials(String username, String password) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery(String.format("select * from volunteers where username='%s' and password='%s'",username,password));
            ArrayList<Volunteer> list = new ArrayList<>();
            if(rs.next())
                return new Volunteer(rs.getLong("id"), rs.getString("name"),rs.getString("username"),rs.getString("password"));
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }
    @Override
    public Long GetMaxId() throws SQLException {
        Statement st = connection.createStatement();
        ResultSet rs = st.executeQuery(String.format("select max(id) from volunteers"));
        rs.next();
        return rs.getLong(1);
    }
}
