package triathlon.persistence.validators;

import triathlon.model.Referee;

public class RefereeValidator implements Validator<Referee> {
    @Override
    public void validate(Referee referee) throws ValidationException {
        if (referee == null) {
            throw new ValidationException("triathlon.model.entities.Entity not instance of referee");
        }
        if (referee.getName() == null
                || referee.getName().matches("^[A-Z][a-z]+([ -][A-Z][a-z]+)*$")) {
            throw new ValidationException("Name is invalid (null or malformed)");
        }
        if (referee.getPassword() == null
                || referee.getPassword().length() < 8
                || !referee.getPassword().matches("^.*[A-Z]+.*$")
                || !referee.getPassword().matches("^.*[0-9]+.*$")) {
            throw new ValidationException("Referee password is invalid (null or malformed)");
        }
        if (referee.getUsername() == null
                || referee.getUsername().length() < 2
                || referee.getUsername().length() > 100) {
            throw new ValidationException("Referee username is invalid (null or malformed)");
        }
    }
}
