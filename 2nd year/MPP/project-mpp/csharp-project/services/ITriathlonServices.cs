using System.Collections.Generic;
using model;

namespace services
{
    public interface ITriathlonServices
    {
        IList<Athlete> GetAthletes();

        Dictionary<string, double> GetAthletesTotalPoints();

        Game GetGameById(long id);

        Referee Authenticate(Referee referee, ITriathlonObserver client);

        void Logout(Referee referee, ITriathlonObserver client);

        IList<Result> GetResultsForGame(long gameId);

        void SetResult(Athlete athlete, Game game, double value);
    }
}
