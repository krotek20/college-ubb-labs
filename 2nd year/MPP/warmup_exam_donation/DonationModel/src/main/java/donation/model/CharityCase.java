package donation.model;

import java.io.Serializable;

public class CharityCase extends Entity<Long> implements Serializable {

    public long raisedSum;

    public long getRaisedSum() {
        return raisedSum;
    }

    public void setRaisedSum(long raisedSum) {
        this.raisedSum = raisedSum;
    }

    public CharityCase(Long id, String name, Long raisedSum) {
        this.id = id;
        this.raisedSum = raisedSum;
        this.name = name;
    }

    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public CharityCase(String name) {
        this.name = name;
    }

    public CharityCase(Long id,String name) {
        this.id = id;
        this.name = name;
    }

    @Override
    public String toString() {
        return name;
    }
}
