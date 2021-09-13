package triathlon.persistence.validators;

public interface Validator<T> {
    void validate(T entity) throws ValidationException;
}