using System;
using System.Collections.Generic;
using log4net;
using Microsoft.Data.Sqlite;
using model;
using persistence.validators;

namespace persistence.dbRepository
{
    public class DbResultRepository : IResultRepository
    {
        private static readonly ILog Log = LogManager.GetLogger(typeof(DbRefereeRepository));
        private readonly SqliteConnection _connection = JdbcManager.GetConnection();
        private readonly IValidator<Result> _validator;

        public DbResultRepository(IValidator<Result> validator)
        {
            this._validator = validator;
        }

        public Result FindOne(long id)
        {
            Log.Info($"Entered with id = {id}");
            try
            {
                const string commandText = "select * from Result where id = @id";
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", id);

                using var reader = command.ExecuteReader();
                if (reader.Read())
                {
                    return new Result
                    {
                        Id = reader.GetInt64(0),
                        Game = new Game
                        {
                            Id = reader.GetInt64(1)
                        },
                        Athlete = new Athlete
                        {
                            Id = reader.GetInt64(2)
                        },
                        Value = reader.GetDouble(3)
                    };
                }
            }
            catch (Exception ex)
            {
                Log.Error(ex.Message);
                Console.Write(ex.Message);
            }

            return null;
        }

        public IEnumerable<Result> FindAll()
        {
            Log.Info("");
            const string commandText = "select * from Result";
            IList<Result> results = new List<Result>();

            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                using var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    results.Add(new Result
                    {
                        Id = reader.GetInt64(0),
                        Game = new Game
                        {
                            Id = reader.GetInt64(1)
                        },
                        Athlete = new Athlete
                        {
                            Id = reader.GetInt64(2)
                        },
                        Value = reader.GetDouble(3)
                    });
                }
            }
            catch (Exception ex)
            {
                Log.Error(ex.Message);
                Console.Write(ex.Message);
            }

            Log.Info(results);
            return results;
        }

        public void Save(Result result)
        {
            Log.Info($"Entered with entity = {result}");
            const string commandText =
                "insert into Result (id, gameId, athleteId, value) values (@id, @gameId, @athleteId, @value)";
            _validator.Validate(result);
            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", result.Id);
                command.Parameters.AddWithValue("gameId", result.Game.Id);
                command.Parameters.AddWithValue("athleteId", result.Athlete.Id);
                command.Parameters.AddWithValue("value", result.Value);

                command.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                Log.Error(ex.Message);
                Console.Write(ex.Message);
            }
        }

        public void Update(Result result)
        {
            Log.Info($"Entered with entity = {result}");
            const string commandText =
                "update Result set gameId = @gameId, athleteId = @athleteId, value = @value where id = @id";
            _validator.Validate(result);
            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", result.Id);
                command.Parameters.AddWithValue("gameId", result.Game.Id);
                command.Parameters.AddWithValue("athleteId", result.Athlete.Id);
                command.Parameters.AddWithValue("value", result.Value);

                command.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                Log.Error(ex.Message);
                Console.Write(ex.Message);
            }
        }

        public void Delete(long id)
        {
            Log.Info($"Entered with id = {id}");
            const string commandText = "delete from Result where id = @id";
            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", id);

                command.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                Log.Error(ex.Message);
                Console.Write(ex.Message);
            }
        }
    }
}
