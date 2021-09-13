package services;

import domain.Player;

public interface IService {
    Player login(Player player, IServiceObserver client);

    void startGame(Player player);

    void playGame(Player player, String card);

    void logout(Player player);
}