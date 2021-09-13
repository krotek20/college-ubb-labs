package domain.validators;

import domain.CharityCase;

public class CharityCaseValidator{
    public static void Validate(CharityCase v) throws ValidationException
    {
        if (v.getName() == "") throw new ValidationException("name is empty");
    }
}
