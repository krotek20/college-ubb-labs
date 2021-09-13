package donation.persistence.repository;

import donation.model.Donation;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

public class DonationDatabaseRepository implements IDonationRepository{
    Connection connection;
    public DonationDatabaseRepository(Properties props) {
        connection = dbUtils.getInstance().getConnection(props);
    }

    @Override
    public Donation Add(Donation entity) {
        try {
            Statement st = connection.createStatement();
            int res = st.executeUpdate(String.format("insert into donations (id, caseid, donorid, sum) values (%d, %d, %d, %d)",
                    entity.getId(),entity.getCaseId(),entity.getDonorId(),entity.getSum()));
            return null;
        } catch (SQLException throwables) {
            return entity;
        }    }

    @Override
    public Donation Delete(Long id) {
        try {
            Statement st = connection.createStatement();
            st.executeQuery(String.format("delete from donations where id=%d returning *",id));
            ResultSet rs = st.getResultSet();
            if(rs.next())
                return new Donation(id, rs.getLong("caseid"), rs.getLong("donorid"), rs.getLong("sum"));
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public Donation Update(Donation entity) {
        try {
            Statement st = connection.createStatement();
            st.execute(String.format("update donations set caseid=%d, donorid=%d, sum=%d where id=%d returning *",
                    entity.getCaseId(),entity.getDonorId(),entity.getSum(),entity.getId()));
            ResultSet rs = st.getResultSet();
            if(rs.next())
                return entity;
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public Donation FindById(Long id) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery(String.format("select * from donations where id=%d",id));
            if(rs.next())
                return new Donation(id, rs.getLong("caseid"), rs.getLong("donorid"), rs.getLong("sum"));
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public List<Donation> FindAll() {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery("select * from donations");
            ArrayList<Donation> list = new ArrayList<>();
            while(rs.next())
                list.add(new Donation(rs.getLong("id"), rs.getLong("caseid"), rs.getLong("donorid"), rs.getLong("sum")));
            return list;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public List<Donation> FilterByCaseId(Long id) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery("select * from donations where caseid ="+id);
            ArrayList<Donation> list = new ArrayList<>();
            while(rs.next())
                list.add(new Donation(rs.getLong("id"), rs.getLong("caseid"), rs.getLong("donorid"), rs.getLong("sum")));
            return list;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public Donation FilterByDonorId(Long id) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery("select * from donations where donorid ="+id);
            if(rs.next())
                return new Donation(rs.getLong("id"), rs.getLong("caseid"), rs.getLong("donorid"), rs.getLong("sum"));
            return null;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public List<Donation> FilterBySum(Long minimum) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery("select * from donations where sum > "+minimum);
            ArrayList<Donation> list = new ArrayList<>();
            while(rs.next())
                list.add(new Donation(rs.getLong("id"), rs.getLong("caseid"), rs.getLong("donorid"), rs.getLong("sum")));
            return list;
        } catch (SQLException throwables) {
            return null;
        }
    }

    @Override
    public Long getRaisedSum(Long charityId) {
        try {
            Statement st = connection.createStatement();
            ResultSet rs = st.executeQuery(String.format("select sum(sum) from donations where caseid=%d",charityId));
            rs.next();
            return rs.getLong(1);
        } catch (SQLException throwables) {
            return 0L;
        }
    }
    @Override
    public Long GetMaxId() throws SQLException {
        Statement st = connection.createStatement();
        ResultSet rs = st.executeQuery(String.format("select max(id) from donations"));
        rs.next();
        return rs.getLong(1);
    }
}
