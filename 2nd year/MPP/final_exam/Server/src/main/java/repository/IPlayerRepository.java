package repository;

import domain.Player;

public interface IPlayerRepository extends ICrudRepository<Long, Player> {
    Player loginPlayer(Player player);
}
