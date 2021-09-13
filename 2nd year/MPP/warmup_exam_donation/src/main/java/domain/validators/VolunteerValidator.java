package domain.validators;

import domain.Volunteer;

public class VolunteerValidator {
    public static void Validate(Volunteer v) throws ValidationException
    {
        if (v.getName() == "") throw new ValidationException("name is empty");
        if (v.getUsername() == "") throw new ValidationException("username is empty");
        if (v.getPassword() == "") throw new ValidationException("password is empty");
    }
}
