package triathlon.model;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;
import javax.persistence.Entity;
import java.io.Serializable;

@Entity
@Table(name = "Referee")
public class Referee extends triathlon.model.Entity<Long> implements Serializable {
    private Game game;
    private String name;
    private String username;
    private String password;

    public Referee(Long id, Game game, String name, String username, String password) {
        setId(id);
        this.game = game;
        this.name = name;
        this.username = username;
        this.password = password;
    }

    public Referee(Game game, String name, String username, String password) {
        this.game = game;
        this.name = name;
        this.username = username;
        this.password = password;
    }

    public Referee() {}

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

    @Column(name = "name")
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Column(name = "username")
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    @Column(name = "password")
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    @Override
    public String toString() {
        return "Referee{" +
                "id=" + getId() +
                ", game=" + game +
                ", name='" + name + '\'' +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}