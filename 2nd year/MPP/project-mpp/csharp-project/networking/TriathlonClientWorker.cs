using System;
using System.Collections.Generic;
using System.Net.Sockets;
using services;
using Google.Protobuf;
using Proto;
using Athlete = model.Athlete;
using Game = model.Game;
using Referee = model.Referee;
using Result = model.Result;

namespace networking
{
	public sealed class TriathlonV3ClientWorker : ITriathlonObserver
	{
		private readonly ITriathlonServices _server;
		private readonly TcpClient _connection;

		private readonly NetworkStream _stream;
		private volatile bool _connected;

		public TriathlonV3ClientWorker(ITriathlonServices server, TcpClient connection)
		{
			_server = server;
			_connection = connection;
			try
			{
				_stream = connection.GetStream();
				_connected = true;
			}
			catch (Exception e)
			{
				Console.WriteLine(e.StackTrace);
			}
		}

		public void Run()
		{
			while (_connected)
			{
				try
				{
					var request = TriathlonRequest.Parser.ParseDelimitedFrom(_stream);
					var response = HandleRequest(request);
					if (response != null)
					{
						SendResponse(response);
					}
				}
				catch (Exception e)
				{
					Console.WriteLine(e.StackTrace);
				}
			}

			try
			{
				_stream.Close();
				_connection.Close();
			}
			catch (Exception e)
			{
				Console.WriteLine("Error " + e);
			}
		}

		public void PointsChanged()
		{
			Console.WriteLine("Result updated");
			try
			{
				SendResponse(ProtoUtils.CreateUpdatePointsResponse());
			}
			catch (Exception e)
			{
				throw new TriathlonException("Sending error: " + e);
			}
		}

		private TriathlonResponse HandleRequest(TriathlonRequest request)
		{
			switch (request.Type)
			{
				case TriathlonRequest.Types.Type.Authentication:
				{
					Console.WriteLine("Authentication request ...");
					var referee = ProtoUtils.GetReferee(request);
					try
					{
						Referee returnedReferee;
						lock (_server)
						{
							returnedReferee = _server.Authenticate(referee, this);
						}

						return ProtoUtils.CreateLoginResponse(returnedReferee);
					}
					catch (TriathlonException e)
					{
						_connected = false;
						return ProtoUtils.CreateErrorResponse(e.Message);
					}
				}
				case TriathlonRequest.Types.Type.Logout:
				{
					Console.WriteLine("Logout request");
					Referee referee = ProtoUtils.GetReferee(request);
					try
					{
						lock (_server)
						{
							_server.Logout(referee, this);
						}

						_connected = false;
						return ProtoUtils.CreateOkResponse();
					}
					catch (TriathlonException e)
					{
						return ProtoUtils.CreateErrorResponse(e.Message);
					}
				}
				case TriathlonRequest.Types.Type.GetAllAthletes:
					Console.WriteLine("Get athletes Request ...");
					try
					{
						List<Athlete> athletes;
						lock (_server)
						{
							athletes = (List<Athlete>) _server.GetAthletes();
						}

						return ProtoUtils.CreateSendAthletesResponse(athletes.ToArray());
					}
					catch (TriathlonException e)
					{
						return ProtoUtils.CreateErrorResponse(e.Message);
					}

				case TriathlonRequest.Types.Type.GetAthletesTotalPoints:
					Console.WriteLine("Get athletes total points Request ...");
					try
					{
						Dictionary<string, double> athletesPoints;
						lock (_server)
						{
							athletesPoints = _server.GetAthletesTotalPoints();
						}

						return ProtoUtils.CreateAthletesTotalPointsResponse(athletesPoints);
					}
					catch (TriathlonException e)
					{
						return ProtoUtils.CreateErrorResponse(e.Message);
					}

				case TriathlonRequest.Types.Type.GetGameId:
				{
					Console.WriteLine("Get game Request ...");
					var gameId = request.GameId;
					try
					{
						Game game;
						lock (_server)
						{
							game = _server.GetGameById(gameId);
						}

						return ProtoUtils.CreateGetGameByIdResponse(game);
					}
					catch (TriathlonException e)
					{
						return ProtoUtils.CreateErrorResponse(e.Message);
					}
				}
				case TriathlonRequest.Types.Type.GetResultsGame:
				{
					Console.WriteLine("Get results for game Request ...");
					var gameId = request.GameId;
					try
					{
						List<Result> results;
						lock (_server)
						{
							results = (List<Result>) _server.GetResultsForGame(gameId);
						}

						return ProtoUtils.CreateResultsForGameResponse(results.ToArray());
					}
					catch (TriathlonException e)
					{
						return ProtoUtils.CreateErrorResponse(e.Message);
					}
				}
				case TriathlonRequest.Types.Type.SetPoints:
				{
					Console.WriteLine("Set result Request ...");
					var updatePointsParams = request.Params;
					var athlete = new Athlete
					{
						Id = updatePointsParams.Athlete.Id,
						Name = updatePointsParams.Athlete.Name
					};
					var game = new Game
					{
						Id = updatePointsParams.Game.Id,
						Name = updatePointsParams.Game.Name
					};
					try
					{
						lock (_server)
						{
							_server.SetResult(athlete, game, updatePointsParams.Value);
						}

						return ProtoUtils.CreateOkResponse();
					}
					catch (TriathlonException e)
					{
						return ProtoUtils.CreateErrorResponse(e.Message);
					}
				}
				default:
					return null;
			}
		}

		private void SendResponse(TriathlonResponse response)
		{
			Console.WriteLine("sending response " + response);
			lock (_stream)
			{
				response.WriteDelimitedTo(_stream);
				_stream.Flush();
			}
		}
	}
}
