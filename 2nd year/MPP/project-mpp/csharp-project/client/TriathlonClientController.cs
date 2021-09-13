using System;
using System.Collections.Generic;
using System.Linq;
using model;
using services;

namespace client
{
    public sealed class TriathlonClientController : ITriathlonObserver
    {
        public event EventHandler<TriathlonRefereeEventArgs> UpdateEvent;
        private readonly ITriathlonServices _server;
        private Referee _currentReferee;

        public TriathlonClientController(ITriathlonServices server)
        {
            _server = server;
            _currentReferee = null;
        }

        public Referee GetCurrentReferee()
        {
            return _currentReferee;
        }

        public void Authenticate(string username, string password)
        {
            var referee = new Referee
            {
                Username = username,
                Password = password
            };
            var returnedReferee = _server.Authenticate(referee, this);
            if (returnedReferee == null) return;
            Console.WriteLine(@"Login succeeded ....");
            _currentReferee = returnedReferee;
            Console.WriteLine(@"Current user {0}", _currentReferee.Username);
        }

        public void Logout()
        {
            Console.WriteLine(@"Controller logout");
            _server.Logout(_currentReferee, this);
            _currentReferee = null;
        }

        public Game GetGameById()
        {
            return _server.GetGameById(_currentReferee.Game.Id);
        }

        public IEnumerable<Athlete> GetAthletes()
        {
            return _server.GetAthletes();
        }

        public IEnumerable<AthleteGameResult> GetGameResults()
        {
            var results = _server.GetResultsForGame(_currentReferee.Game.Id)
                .OrderByDescending(result => result.Value).ToList();
            return results.Select(r => new AthleteGameResult {AthleteName = r.Athlete.Name, Points = r.Value}).ToList();
        }

        public IEnumerable<AthleteGameResult> GetTotalResults()
        {
            return _server.GetAthletesTotalPoints()
                .OrderBy(entry => entry.Key)
                .Select(entry =>
                    new AthleteGameResult {AthleteName = entry.Key, Points = entry.Value})
                .ToList();
        }

        public void UpdatePoints(string athleteName, double points)
        {
            var athlete = _server.GetAthletes().FirstOrDefault(a => a.Name == athleteName);
            if (athlete == null)
            {
                throw new TriathlonException(@"No athlete selected!");
            }

            _server.SetResult(athlete, _currentReferee.Game, points);
        }

        public void PointsChanged(ResultUpdateHandler result)
        {
            var userArgs = new TriathlonRefereeEventArgs
            {
                RefereeEventType = TriathlonRefereeEvent.PointsChanged,
                Data = result
            };
            Console.WriteLine(@"Points updated");
            OnRefereeEvent(userArgs);
        }

        private void OnRefereeEvent(TriathlonRefereeEventArgs e)
        {
            if (UpdateEvent == null) return;
            UpdateEvent(this, e);
            Console.WriteLine(@"Update Event called");
        }
    }
}
