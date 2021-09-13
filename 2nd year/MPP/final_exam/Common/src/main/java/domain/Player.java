package domain;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;
import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;

@javax.persistence.Entity
@Table(name = "Players")
public class Player extends Entity<Long> implements Serializable {
    private String username;
    private String password;
    private Set<Move> moves = new HashSet<>();
    private Set<InitialCard> initialCards = new HashSet<>();

    public Player() { }

    public Player(String username, String password) {
        this.username = username;
        this.password = password;
    }

    @Override
    public void setId(Long id) {
        super.setId(id);
    }

    @Id
    @GeneratedValue(generator = "identity")
    @GenericGenerator(name = "identity", strategy = "identity")
    @Override
    public Long getId() {
        return super.getId();
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    @OneToMany(mappedBy = "player", cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    public Set<Move> getMoves() {
        return moves;
    }

    public void setMoves(Set<Move> moves) {
        this.moves = moves;
    }

    public void addMove(Move move) {
        this.moves.add(move);
    }

    @OneToMany(mappedBy = "player", cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    public Set<InitialCard> getInitialCards() {
        return initialCards;
    }

    public void setInitialCards(Set<InitialCard> initialCards) {
        this.initialCards = initialCards;
    }

    public void addInitialCard(InitialCard initialCard) {
        this.initialCards.add(initialCard);
    }

    @Override
    public String toString() {
        return username;
    }
}