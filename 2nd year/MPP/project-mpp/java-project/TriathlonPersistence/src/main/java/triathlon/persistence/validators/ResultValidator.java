package triathlon.persistence.validators;

import triathlon.model.Result;

public class ResultValidator implements Validator<Result> {
    @Override
    public void validate(Result result) throws ValidationException {
        if (result == null) {
            throw new ValidationException("triathlon.model.entities.Entity not instance of result");
        }
        if (result.getValue() == null
                || result.getValue() < 0) {
            throw new ValidationException("Result value can't be negative");
        }
    }
}
