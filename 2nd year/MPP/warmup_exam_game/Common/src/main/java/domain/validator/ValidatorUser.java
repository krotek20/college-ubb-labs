package domain.validator;

import domain.User;

public class ValidatorUser implements Validator<User> {

    @Override
    public void validate(User entity) throws ValidationException {
        String errors = "";
        if (entity.getUsername() == null || entity.getUsername().equals("")) {
            errors += "Username must not be null!\n";
        }
        if (entity.getPassword() == null || entity.getPassword().equals("")) {
            errors += "Password must not be null!\n";
        }
        if (errors.length() > 0) {
            throw new ValidationException(errors);
        }
    }
}
