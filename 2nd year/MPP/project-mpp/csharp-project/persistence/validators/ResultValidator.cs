using model;

namespace persistence.validators
{
    public class ResultValidator : IValidator<Result>
    {
        public void Validate(Result result)
        {
            if (result == null)
            {
                throw new ValidationException("Entity not instance of result");
            }

            if (result.Value < 0)
            {
                throw new ValidationException("Result value can't be negative");
            }
        }
    }
}
