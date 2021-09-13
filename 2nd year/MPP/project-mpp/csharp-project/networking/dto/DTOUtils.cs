using System.Collections.Generic;
using System.Linq;
using model;

namespace networking.dto
{
    public static class DtoUtils
    {
        public static Athlete GetFromDto(AthleteDto athleteDto)
        {
            long id = athleteDto.Id;
            string name = athleteDto.Name;
            return new Athlete
            {
                Id = id,
                Name = name
            };
        }

        public static AthleteDto GetDto(Athlete athlete)
        {
            long id = athlete.Id;
            string name = athlete.Name;
            return new AthleteDto
            {
                Id = id,
                Name = name
            };
        }

        public static Game GetFromDto(GameDto gameDto)
        {
            long id = gameDto.Id;
            string name = gameDto.Name;
            return new Game
            {
                Id = id,
                Name = name
            };
        }

        public static GameDto GetDto(Game game)
        {
            long id = game.Id;
            string name = game.Name;
            return new GameDto
            {
                Id = id,
                Name = name
            };
        }

        public static Result GetFromDto(ResultDto resultDto)
        {
            string athleteName = resultDto.AthleteName;
            long gameId = resultDto.GameId;
            double points = resultDto.Points;
            return new Result
            {
                Game = new Game
                {
                    Id = gameId
                },
                Athlete = new Athlete
                {
                    Name = athleteName
                },
                Value = points
            };
        }

        public static ResultDto GetDto(Result result)
        {
            string athleteName = result.Athlete.Name;
            long gameId = result.Game.Id;
            double points = result.Value;
            return new ResultDto
            {
                GameId = gameId,
                AthleteName = athleteName,
                Points = points
            };
        }

        public static Referee GetFromDto(RefereeDto refereeDto)
        {
            long gameId = refereeDto.GameId;
            string name = refereeDto.Name;
            string username = refereeDto.Username;
            string password = refereeDto.Password;
            return new Referee
            {
                Game = new Game
                {
                    Id = gameId
                },
                Name = name,
                Username = username,
                Password = password
            };
        }

        public static RefereeDto GetDto(Referee referee)
        {
            long gameId = referee.Game.Id;
            string name = referee.Name;
            string username = referee.Username;
            string password = referee.Password;
            return new RefereeDto
            {
                GameId = gameId,
                Name = name,
                Username = username,
                Password = password
            };
        }

        public static ResultUpdateHandler GetFromDto(ResultHandlerDto resultHandlerDto)
        {
            return new ResultUpdateHandler
            {
                Result = GetFromDto(resultHandlerDto.ResultDto),
                TotalPoints = resultHandlerDto.TotalPoints
            };
        }

        public static ResultHandlerDto GetDto(ResultUpdateHandler resultUpdateHandler)
        {
            return new ResultHandlerDto
            {
                ResultDto = GetDto(resultUpdateHandler.Result),
                TotalPoints = resultUpdateHandler.TotalPoints
            };
        }

        public static List<Athlete> GetFromDto(IEnumerable<AthleteDto> athletesDto)
        {
            return athletesDto.Select(athleteDto => new Athlete
            {
                Id = athleteDto.Id,
                Name = athleteDto.Name
            }).ToList();
        }

        public static List<AthleteDto> GetDto(List<Athlete> athletes)
        {
            return athletes.Select(athlete => new AthleteDto
            {
                Id = athlete.Id,
                Name = athlete.Name
            }).ToList();
        }

        public static List<Result> GetFromDto(IEnumerable<ResultDto> resultsDto)
        {
            return resultsDto.Select(resultDto => new Result
            {
                Game = new Game
                {
                    Id = resultDto.GameId
                },
                Athlete = new Athlete
                {
                    Name = resultDto.AthleteName
                },
                Value = resultDto.Points
            }).ToList();
        }

        public static List<ResultDto> GetDto(IEnumerable<Result> results)
        {
            return results.Select(result => new ResultDto
            {
                GameId = result.Game.Id,
                AthleteName = result.Athlete.Name,
                Points = result.Value
            }).ToList();
        }
    }
}
