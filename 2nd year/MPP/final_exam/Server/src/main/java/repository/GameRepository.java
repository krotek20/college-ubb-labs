package repository;

import domain.Game;
import org.springframework.stereotype.Component;

@Component
public class GameRepository extends GenericOrmRepository<Game> implements IGameRepository {
    public GameRepository() {
        super(Game.class);
    }
}
