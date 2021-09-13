package services;

import domain.Player;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;
import java.util.Map;

public interface IServiceObserver extends Remote {
    void updatePlayersList(List<String> players) throws IServiceException, RemoteException;
    void updateOwnCards(List<String> ownCards) throws IServiceException, RemoteException;
    void updateRoundWinner(int round, String name) throws IServiceException, RemoteException;
    void updateLeaderBoard(List<Map.Entry<Player, Integer>> leaderboard) throws IServiceException, RemoteException;
}
