package triathlon.model;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.Entity;
import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name = "Athlete")
public class Athlete extends triathlon.model.Entity<Long> implements Serializable {
    private String name;

    public Athlete() {}

    public Athlete(Long id, String name) {
        setId(id);
        this.name = name;
    }

    public Athlete(Long id) {
        setId(id);
    }

    @Override
    public void setId(Long id) {
        super.setId(id);
    }

    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    @GenericGenerator(name="identity", strategy = "identity")
    @Override
    public Long getId() {
        return super.getId();
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}