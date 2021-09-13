package triathlon.model;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;
import javax.persistence.Entity;
import java.io.Serializable;

@Entity
@Table(name = "Result")
public class Result extends triathlon.model.Entity<Long> implements Serializable {
    private Game game;
    private Athlete athlete;
    private Float value;

    public Result(Long id, Game game, Athlete athlete, Float value) {
        setId(id);
        this.game = game;
        this.athlete = athlete;
        this.value = value;
    }

    public Result(Game game, Athlete athlete, Float value) {
        this.game = game;
        this.athlete = athlete;
        this.value = value;
    }

    public Result() {}

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

    @ManyToOne
    @JoinColumn(name = "gameId", referencedColumnName = "id")
    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }

    @ManyToOne
    @JoinColumn(name = "athleteId", referencedColumnName = "id")
    public Athlete getAthlete() {
        return athlete;
    }

    public void setAthlete(Athlete athlete) {
        this.athlete = athlete;
    }

    @Column(name = "value")
    public Float getValue() {
        return value;
    }

    public void setValue(Float value) {
        this.value = value;
    }
}