package domain;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;
import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;

@javax.persistence.Entity
@Table(name = "Games")
public class Game extends Entity<Long> implements Serializable {
    private Set<Move> moves = new HashSet<>();
    private Set<InitialCard> initialCards = new HashSet<>();

    public Game() { }

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

    @OneToMany(mappedBy = "game", cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    public Set<Move> getMoves() {
        return moves;
    }

    public void setMoves(Set<Move> moves) {
        this.moves = moves;
    }

    public void addMove(Move move) {
        this.moves.add(move);
    }

    @OneToMany(mappedBy = "game", cascade = CascadeType.ALL, fetch = FetchType.EAGER)
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
        return super.getId().toString();
    }
}