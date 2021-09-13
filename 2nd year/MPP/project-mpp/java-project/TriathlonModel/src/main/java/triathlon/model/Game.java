package triathlon.model;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;
import javax.persistence.Entity;

import java.io.Serializable;

@Entity
@Table(name = "Game")
public class Game extends triathlon.model.Entity<Long> implements Serializable {
    private String name;

    public Game(Long id, String name) {
        setId(id);
        this.name = name;
    }

    public Game(Long id) {
        setId(id);
    }

    public Game() {}

    @Override
    public void setId(Long id) {
        super.setId(id);
    }

    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    @GenericGenerator(name="identity", strategy = "identity")
    @Override
    public Long getId() {
        return super.getId();
    }

    public void setName(String name) {
        this.name = name;
    }

    @Column(name = "name")
    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Game{" +
                "id=" + getId() +
                ", name='" + name + '\'' +
                '}';
    }
}