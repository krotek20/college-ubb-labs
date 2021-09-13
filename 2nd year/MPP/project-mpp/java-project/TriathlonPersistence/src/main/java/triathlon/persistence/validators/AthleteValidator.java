package triathlon.persistence.validators;

import triathlon.model.Athlete;

public class AthleteValidator implements Validator<Athlete> {
    @Override
    public void validate(Athlete athlete) throws ValidationException {
        if (athlete == null) {
            throw new ValidationException("triathlon.model.entities.Entity not instance of athlete");
        }
        if (athlete.getName() == null
                || athlete.getName().matches("^[A-Z]")) {
            throw new ValidationException("Athlete name is invalid (null or malformed)");
        }
    }
}
