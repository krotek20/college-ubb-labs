using System.Text.RegularExpressions;
using model;

namespace persistence.validators
{
    public class AthleteValidator : IValidator<Athlete>
    {
        public void Validate(Athlete athlete)
        {
            if (athlete == null)
            {
                throw new ValidationException("Entity not instance of athlete");
            }

            var nameMatch = Regex.Match(athlete.Name, "^[A-Z]");
            if (athlete.Name == null || !nameMatch.Success)
            {
                throw new ValidationException("Athlete name is invalid (null or malformed)");
            }
        }
    }
}
