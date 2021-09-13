package triathlon.services;

import triathlon.model.Athlete;
import triathlon.model.Game;
import triathlon.model.Referee;
import triathlon.model.Result;

import java.util.Collection;
import java.util.Map;

public interface ITriathlonServices {
    Collection<Athlete> getAthletes() throws TriathlonException;

    Map<String, Float> getAthletesTotalPoints() throws TriathlonException;

    Game getGameById(Long id) throws TriathlonException;

    Referee authenticate(Referee referee, ITriathlonObserver client) throws TriathlonException;

    void logout(Referee referee, ITriathlonObserver client) throws TriathlonException;

    Collection<Result> getResultsForGame(Long gameId) throws TriathlonException;

    void setResult(Athlete athlete, Game game, Float value) throws TriathlonException;
}
