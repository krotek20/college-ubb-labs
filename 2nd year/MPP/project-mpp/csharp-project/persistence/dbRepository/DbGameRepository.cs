using System;
using System.Collections.Generic;
using log4net;
using Microsoft.Data.Sqlite;
using model;
using persistence.validators;

namespace persistence.dbRepository
{
    public class DbGameRepository : IGameRepository
    {
        private static readonly ILog Log = LogManager.GetLogger(typeof(DbGameRepository));
        private readonly SqliteConnection _connection = JdbcManager.GetConnection();
        private readonly IValidator<Game> _validator;

        public DbGameRepository(IValidator<Game> validator)
        {
            this._validator = validator;
        }

        public Game FindOne(long id)
        {
            Log.Info($"Entered with id = {id}");
            try
            {
                const string commandText = "select * from Game where id = @id";
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", id);

                using var reader = command.ExecuteReader();
                if (reader.Read())
                {
                    return new Game
                    {
                        Id = reader.GetInt64(0),
                        Name = reader.GetString(1)
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

        public IEnumerable<Game> FindAll()
        {
            Log.Info("");
            const string commandText = "select * from Game";
            IList<Game> games = new List<Game>();

            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                using var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    games.Add(new Game
                    {
                        Id = reader.GetInt64(0),
                        Name = reader.GetString(1)
                    });
                }
            }
            catch (Exception ex)
            {
                Log.Error(ex.Message);
                Console.Write(ex.Message);
            }

            Log.Info(games);
            return games;
        }

        public void Save(Game game)
        {
            Log.Info($"Entered with entity = {game}");
            const string commandText = "insert into Game (id, name) values (@id, @name)";
            _validator.Validate(game);
            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", game.Id);
                command.Parameters.AddWithValue("name", game.Name);

                command.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                Log.Error(ex.Message);
                Console.Write(ex.Message);
            }
        }

        public void Update(Game game)
        {
            Log.Info($"Entered with entity = {game}");
            const string commandText = "update Game set name = @name where id = @id";
            _validator.Validate(game);
            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", game.Id);
                command.Parameters.AddWithValue("name", game.Name);

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
            const string commandText = "delete from Game where id = @id";
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
