using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using lastLab.domain;
using lastLab.repository;

namespace lastLab.service
{
    public class Service
    { 
        private IRepository<long, Game> _gameRepository;
        private IRepository<long, Player> _playerRepository;
        private IRepository<Tuple<long, long>, ActivePlayer> _activePlayerRepository;

        public Service(IRepository<long, Game> gameRepository,
            IRepository<long, Player> playerRepository,
            IRepository<Tuple<long, long>, ActivePlayer> activePlayerRepository)
        {
            _gameRepository = gameRepository;
            _playerRepository = playerRepository;
            _activePlayerRepository = activePlayerRepository;
        }

        public IList GetTeamedPlayers(long teamId)
        {
            return _playerRepository.FindAll()
                .Where(x => x.Team.Id.Equals(teamId))
                .ToList();
        }

        public IList GetActivePlayersByGame(long teamId, long gameId)
        {
            return _activePlayerRepository.FindAll()
                .Where(x => x.Id.Item2 == gameId)
                .Where(x => _playerRepository
                    .FindOne(x.Id.Item1).Team.Id.Equals(teamId))
                .ToList();
        }

        public IList GetGamesByDateTime(DateTime from, DateTime to)
        {
            return _gameRepository.FindAll()
                .Where(x => x.Date > from && x.Date < to)
                .ToList();
        }

        public Tuple<long, long> GamePoints(long gameId)
        {
            List<long> gameScore = _activePlayerRepository.FindAll()
                .Where(x => x.Id.Item2 == gameId)
                .Select(x => new
                {
                    TeamId = _playerRepository.FindOne(x.Id.Item1).Team.Id,
                    Score = x.ScoredPoints
                })
                .GroupBy(x => x.TeamId)
                .Select(x => x.Sum(y => y.Score))
                .ToList();

            if (gameScore.Count != 2)
            {
                return null;
            }

            return new Tuple<long, long>(gameScore[0], gameScore[1]);
        }
    }
}