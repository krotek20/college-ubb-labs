using System.Text.RegularExpressions;
using model;

namespace persistence.validators
{
    public class RefereeValidator : IValidator<Referee>
    {
        public void Validate(Referee referee)
        {
            if (referee == null)
            {
                throw new ValidationException("Entity not instance of referee");
            }

            var nameMatch = Regex.Match(referee.Name, "^[A-Z][a-z]+([ -][A-Z][a-z]+)*$");
            if (referee.Name == null || !nameMatch.Success)
            {
                throw new ValidationException("Name is invalid (null or malformed)");
            }

            var passwordMatchCapitals = Regex.Match(referee.Password, "^.*[A-Z]+.*$");
            var passwordMatchNumeric = Regex.Match(referee.Password, "^.*[0-9]+.*$");
            if (referee.Password == null || referee.Password.Length < 8 || !passwordMatchCapitals.Success ||
                !passwordMatchNumeric.Success)
            {
                throw new ValidationException("Referee password is invalid (null or malformed)");
            }

            if (referee.Username == null || referee.Username.Length < 2 || referee.Username.Length > 100)
            {
                throw new ValidationException("Referee username is invalid (null or malformed)");
            }
        }
    }
}
