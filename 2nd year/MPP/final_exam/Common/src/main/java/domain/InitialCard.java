package domain;

import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;
import java.io.Serializable;

@javax.persistence.Entity
@Table(name = "InitialCards")
public class InitialCard extends Entity<Long> implements Serializable {
    private Player player;
    private Game game;
    private String card1;
    private String card2;
    private String card3;

    public InitialCard() { }

    public InitialCard(Player player, Game game, String card1, String card2, String card3) {
        this.player = player;
        this.game = game;
        this.card1 = card1;
        this.card2 = card2;
        this.card3 = card3;
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

    public String getCard1() {
        return card1;
    }

    public void setCard1(String card1) {
        this.card1 = card1;
    }

    public String getCard2() {
        return card2;
    }

    public void setCard2(String card2) {
        this.card2 = card2;
    }

    public String getCard3() {
        return card3;
    }

    public void setCard3(String card3) {
        this.card3 = card3;
    }

    @Override
    public String toString() {
        return "Move{" +
                "player=" + player +
                ", game=" + game +
                '}';
    }
}