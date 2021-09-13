package repository;

import domain.Participant;
import org.springframework.stereotype.Component;

@Component
public class ParticipantRepository extends GenericOrmRepository<Participant> implements IParticipantRepository {
    public ParticipantRepository() {
        super(Participant.class);
    }
}
