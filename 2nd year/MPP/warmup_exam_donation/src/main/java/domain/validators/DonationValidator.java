package domain.validators;

import domain.Donation;

public class DonationValidator {
    public static void Validate(Donation v)throws ValidationException
    {
        if (v.getCaseId() < 0) throw new ValidationException("invalid Case Id");
        if (v.getDonorId() < 0) throw new ValidationException("invalid Donor Id");
        if (v.getSum() < 0) throw new ValidationException("Negative Sum");
    }
}
