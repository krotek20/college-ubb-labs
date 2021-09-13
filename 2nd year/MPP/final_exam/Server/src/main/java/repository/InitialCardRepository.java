package repository;

import domain.InitialCard;
import org.springframework.stereotype.Component;

@Component
public class InitialCardRepository extends GenericOrmRepository<InitialCard> implements IInitialCardRepository {
    public InitialCardRepository() {
        super(InitialCard.class);
    }
}

