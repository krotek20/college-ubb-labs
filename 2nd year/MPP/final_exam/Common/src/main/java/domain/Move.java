package domain;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;
import java.io.Serializable;

@javax.persistence.Entity
@Table(name = "Moves")
public class Move extends Entity<Long> implements Serializable {
    private Player player;
    private Game game;
    private String sentCard;
    private int numberOfReceivedCards;

    public Move() { }

    public Move(Player player, Game game, String sentCard, int numberOfReceivedCards) {
        this.player = player;
        this.game = game;
        this.sentCard = sentCard;
        this.numberOfReceivedCards = numberOfReceivedCards;
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

    @ManyToOne
    @JoinColumn(name = "playerId")
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

    @ManyToOne
    @JoinColumn(name = "gameId")
    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }

    public String getSentCard() {
        return sentCard;
    }

    public void setSentCard(String sentCard) {
        this.sentCard = sentCard;
    }

    public int getNumberOfReceivedCards() {
        return numberOfReceivedCards;
    }

    public void setNumberOfReceivedCards(int numberOfReceivedCards) {
        this.numberOfReceivedCards = numberOfReceivedCards;
    }

    @Override
    public String toString() {
        return "Move{" +
                "player=" + player +
                ", game=" + game +
                '}';
    }
}