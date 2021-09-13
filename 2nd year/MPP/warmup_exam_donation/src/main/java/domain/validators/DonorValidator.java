package domain.validators;

import domain.Donor;

public class DonorValidator {
    public static void Validate(Donor v)throws ValidationException
    {
        if (v.getName() == "") throw new ValidationException("name is empty");
        if (v.getAddress() == "") throw new ValidationException("address is empty");
        if (v.getPhoneNumber() == "") throw new ValidationException("phone number is empty");
    }
}
