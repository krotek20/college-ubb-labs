using System.Text.RegularExpressions;
using model;

namespace persistence.validators
{
    public class GameValidator : IValidator<Game>
    {
        public void Validate(Game game)
        {
            if (game == null)
            {
                throw new ValidationException("Entity not instance of game");
            }

            var nameMatch = Regex.Match(game.Name, "^[A-Z]");
            if (game.Name == null || !nameMatch.Success)
            {
                throw new ValidationException("Game name is invalid (null or malformed)");
            }
        }
    }
}