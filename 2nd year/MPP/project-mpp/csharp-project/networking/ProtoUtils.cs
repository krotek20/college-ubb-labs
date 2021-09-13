using System.Collections.Generic;
using System.Linq;
using Proto;
using Referee = model.Referee;
using Game = model.Game;
using Athlete = model.Athlete;
using Result = model.Result;

namespace networking
{
    static class ProtoUtils
    {
        public static TriathlonResponse CreateOkResponse()
        {
            return new TriathlonResponse
            {
                Type = TriathlonResponse.Types.Type.Ok
            };
        }

        public static TriathlonResponse CreateErrorResponse(string text)
        {
            return new TriathlonResponse
            {
                Type = TriathlonResponse.Types.Type.Error,
                Error = text
            };
        }

        public static TriathlonResponse CreateLoginResponse(Referee referee)
        {
            var gameDto = new Proto.Game
            {
                Id = referee.Game.Id,
            };
            var refereeDto = new Proto.Referee
            {
                Game = gameDto,
                Id = referee.Id,
                Name = referee.Name,
                Password = referee.Password,
                Username = referee.Username
            };
            return new TriathlonResponse
            {
                Type = TriathlonResponse.Types.Type.Ok,
                Referee = refereeDto
            };
        }

        public static TriathlonResponse CreateUpdatePointsResponse()
        {
            return new TriathlonResponse
            {
                Type = TriathlonResponse.Types.Type.UpdatePoints
            };
        }

        public static TriathlonResponse CreateSendAthletesResponse(Athlete[] athletes)
        {
            var response = new TriathlonResponse
            {
                Type = TriathlonResponse.Types.Type.SendAllAthletes
            };
            foreach (var athlete in athletes)
            {
                var athleteDto = new Proto.Athlete
                {
                    Id = athlete.Id,
                    Name = athlete.Name
                };
                response.Athletes.Add(athleteDto);
            }

            return response;
        }

        public static TriathlonResponse CreateResultsForGameResponse(Result[] results)
        {
            var response = new TriathlonResponse
            {
                Type = TriathlonResponse.Types.Type.SendResultsGame
            };
            foreach (var result in results)
            {
                var gameDto = new Proto.Game
                {
                    Id = result.Game.Id,
                };
                var athleteDto = new Proto.Athlete
                {
                    Id = result.Athlete.Id,
                    Name = result.Athlete.Name
                };
                var resultDto = new Proto.Result
                {
                    Athlete = athleteDto,
                    Game = gameDto,
                    Id = result.Id,
                    Value = (float) result.Value
                };
                response.ResultsForGame.Add(resultDto);
            }

            return response;
        }

        public static TriathlonResponse CreateGetGameByIdResponse(Game game)
        {
            var gameDto = new Proto.Game
            {
                Id = game.Id,
                Name = game.Name
            };
            return new TriathlonResponse
            {
                Type = TriathlonResponse.Types.Type.SendGameId,
                Game = gameDto
            };
        }

        public static TriathlonResponse CreateAthletesTotalPointsResponse(Dictionary<string, double> athletesPoints)
        {
            var response = new TriathlonResponse
            {
                Type = TriathlonResponse.Types.Type.SendAthletesTotalPoints
            };
            foreach (KeyValuePair<string, double> entry in athletesPoints)
            {
                response.AthletesTotalPoints.Add(entry.Key, (float) entry.Value);
            }

            return response;
        }

        public static string GetError(TriathlonResponse response)
        {
            return response.Error;
        }

        public static IList<Athlete> GetAthletes(TriathlonResponse response)
        {
            return response.Athletes.Select(athleteDto => new Athlete
            {
                Id = athleteDto.Id,
                Name = athleteDto.Name
            }).ToList();
        }

        public static Dictionary<string, double> GetAthletesTotalPoints(TriathlonResponse response)
        {
            return response.AthletesTotalPoints.ToDictionary(
                athletePoints => athletePoints.Key,
                athletePoints => (double) athletePoints.Value);
        }

        public static Game GetGame(TriathlonResponse response)
        {
            var gameDto = response.Game;
            return new Game
            {
                Id = gameDto.Id,
                Name = gameDto.Name
            };
        }

        public static Referee GetReferee(TriathlonRequest request)
        {
            var refereeDto = request.Referee;
            return new Referee
            {
                Password = refereeDto.Password,
                Username = refereeDto.Username
            };
        }

        public static IList<Result> GetResultsForGame(TriathlonResponse response)
        {
            return (from resultDto in response.ResultsForGame
                    let game = new Game {Id = resultDto.Game.Id, Name = resultDto.Game.Name}
                    let athlete = new Athlete {Id = resultDto.Athlete.Id, Name = resultDto.Athlete.Name}
                    select new Result {Id = resultDto.Id, Game = game, Athlete = athlete, Value = resultDto.Value})
                .ToList();
        }
    }
}