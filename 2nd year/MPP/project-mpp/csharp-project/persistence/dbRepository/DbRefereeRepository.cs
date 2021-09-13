using System;
using System.Collections.Generic;
using log4net;
using Microsoft.Data.Sqlite;
using model;
using persistence.validators;

namespace persistence.dbRepository
{
    public class DbRefereeRepository : IRefereeRepository
    {
        private static readonly ILog Log = LogManager.GetLogger(typeof(DbRefereeRepository));
        private readonly SqliteConnection _connection = JdbcManager.GetConnection();
        private readonly IValidator<Referee> _validator;

        public DbRefereeRepository(IValidator<Referee> validator)
        {
            this._validator = validator;
        }

        public Referee FindOne(long id)
        {
            Log.Info($"Entered with id = {id}");
            try
            {
                const string commandText = "select * from Referee where id = @id";
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", id);

                using var reader = command.ExecuteReader();
                if (reader.Read())
                {
                    return new Referee
                    {
                        Id = reader.GetInt64(0),
                        Game = new Game
                        {
                            Id = reader.GetInt64(1)
                        },
                        Name = reader.GetString(2),
                        Username = reader.GetString(3),
                        Password = reader.GetString(4)
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

        public IEnumerable<Referee> FindAll()
        {
            Log.Info("");
            const string commandText = "select * from Referee";
            IList<Referee> referees = new List<Referee>();

            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                using var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    referees.Add(new Referee
                    {
                        Id = reader.GetInt64(0),
                        Game = new Game
                        {
                            Id = reader.GetInt64(1)
                        },
                        Name = reader.GetString(2),
                        Username = reader.GetString(3),
                        Password = reader.GetString(4)
                    });
                }
            }
            catch (Exception ex)
            {
                Log.Error(ex.Message);
                Console.Write(ex.Message);
            }

            Log.Info(referees);
            return referees;
        }

        public void Save(Referee referee)
        {
            Log.Info($"Entered with entity = {referee}");
            const string commandText =
                "insert into Referee (id, gameId, name, username, password) values (@id, @gameId, @name, @username, @password)";
            _validator.Validate(referee);
            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", referee.Id);
                command.Parameters.AddWithValue("gameId", referee.Game.Id);
                command.Parameters.AddWithValue("name", referee.Name);
                command.Parameters.AddWithValue("username", referee.Username);
                command.Parameters.AddWithValue("password", referee.Password);

                command.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                Log.Error(ex.Message);
                Console.Write(ex.Message);
            }
        }

        public void Update(Referee referee)
        {
            Log.Info($"Entered with entity = {referee}");
            const string commandText =
                "update Referee set gameId = @gameId, name = @name, username = @username, password = @password where id = @id";
            _validator.Validate(referee);
            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", referee.Id);
                command.Parameters.AddWithValue("gameId", referee.Game.Id);
                command.Parameters.AddWithValue("name", referee.Name);
                command.Parameters.AddWithValue("username", referee.Username);
                command.Parameters.AddWithValue("password", referee.Password);

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
            const string commandText = "delete from Referee where id = @id";
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