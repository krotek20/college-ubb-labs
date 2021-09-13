using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using model;
using persistence;
using services;

namespace server
{
    public class SuperService : ITriathlonServices
    {
        private readonly IGameRepository _gameRepository;
        private readonly IResultRepository _resultRepository;
        private readonly IAthleteRepository _athleteRepository;
        private readonly IRefereeRepository _refereeRepository;
        private readonly IDictionary<string, ITriathlonObserver> _loggedClients;

        public SuperService(IGameRepository gameRepository, IResultRepository resultRepository,
            IAthleteRepository athleteRepository, IRefereeRepository refereeRepository)
        {
            _gameRepository = gameRepository;
            _resultRepository = resultRepository;
            _athleteRepository = athleteRepository;
            _refereeRepository = refereeRepository;
            _loggedClients = new Dictionary<string, ITriathlonObserver>();
        }

        public Referee Authenticate(Referee inputReferee, ITriathlonObserver client)
        {
            foreach (var referee in _refereeRepository.FindAll())
            {
                if (referee.Username.Equals(inputReferee.Username) && referee.Password.Equals(inputReferee.Password))
                {
                    if (_loggedClients.ContainsKey(referee.Username))
                    {
                        throw new TriathlonException("User already logged in.");
                    }

                    _loggedClients[referee.Username] = client;
                    return referee;
                }
            }

            return null;
        }

        public IList<Athlete> GetAthletes()
        {
            return _athleteRepository.FindAll().ToList();
        }

        public Dictionary<string, double> GetAthletesTotalPoints()
        {
            Dictionary<string, double> athleteResultMap = new Dictionary<string, double>();
            foreach (var result in _resultRepository.FindAll())
            {
                var athlete = _athleteRepository.FindOne(result.Athlete.Id);
                if (athleteResultMap.ContainsKey(athlete.Name))
                {
                    athleteResultMap[athlete.Name] += result.Value;
                }
                else
                {
                    athleteResultMap.Add(athlete.Name, result.Value);
                }
            }

            return athleteResultMap;
        }

        public Game GetGameById(long id)
        {
            return _gameRepository.FindOne(id);
        }

        public IList<Result> GetResultsForGame(long gameId)
        {
            return _resultRepository.FindAll()
                .Where(result => result.Game.Id == gameId)
                .Select(result => new Result
                {
                    Athlete = _athleteRepository.FindOne(result.Athlete.Id),
                    Game = result.Game,
                    Id = result.Id,
                    Value = result.Value
                }).ToList();
        }

        public void Logout(Referee referee, ITriathlonObserver client)
        {
            var localClient = _loggedClients[referee.Username];
            if (localClient == null)
            {
                throw new TriathlonException("Referee " + referee.Username + " is not logged in.");
            }

            _loggedClients.Remove(referee.Username);
        }

        public void SetResult(Athlete athlete, Game game, double value)
        {
            var result = (from r in _resultRepository.FindAll()
                where r.Athlete.Id == athlete.Id && r.Game.Id == game.Id
                select new Result
                {
                    Athlete = athlete,
                    Game = game,
                    Value = value,
                    Id = r.Id
                }).FirstOrDefault();
            if (result != null)
            {
                result.Value = value;
                _resultRepository.Update(result);
            }
            else
            {
                result = new Result()
                {
                    Game = game,
                    Athlete = athlete,
                    Value = value
                };
                _resultRepository.Save(result);
            }

            NotifyUpdateResult();
        }

        private void NotifyUpdateResult()
        {
            foreach (var client in _loggedClients)
            {
                Task.Run(() => client.Value.PointsChanged());
            }
        }
    }
}
