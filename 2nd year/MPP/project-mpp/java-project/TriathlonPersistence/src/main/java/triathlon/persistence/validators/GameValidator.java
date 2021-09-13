package triathlon.persistence.validators;

import triathlon.model.Game;

public class GameValidator implements Validator<Game> {
    @Override
    public void validate(Game game) throws ValidationException {
        if (game == null) {
            throw new ValidationException("triathlon.model.entities.Entity not instance of game");
        }
        if (game.getName() == null
                || game.getName().matches("^[A-Z]")) {
            throw new ValidationException("Game name is invalid (null or malformed)");
        }
    }
}
