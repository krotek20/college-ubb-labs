package repository;

import domain.Move;
import org.springframework.stereotype.Component;

@Component
public class MoveRepository extends GenericOrmRepository<Move> implements IMoveRepository {
    public MoveRepository() {
        super(Move.class);
    }
}