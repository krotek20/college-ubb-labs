using System;
using System.Collections.Generic;
using log4net;
using Microsoft.Data.Sqlite;
using model;
using persistence.validators;

namespace persistence.dbRepository
{
    public class DbAthleteRepository : IAthleteRepository
    {
        private static readonly ILog Log = LogManager.GetLogger(typeof(DbAthleteRepository));
        private readonly SqliteConnection _connection = JdbcManager.GetConnection();
        private readonly IValidator<Athlete> _validator;

        public DbAthleteRepository(IValidator<Athlete> validator)
        {
            this._validator = validator;
        }

        public Athlete FindOne(long id)
        {
            Log.Info($"Entered with id = {id}");
            try
            {
                const string commandText = "select * from Athlete where id = @id";
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", id);

                using var reader = command.ExecuteReader();
                if (reader.Read())
                {
                    return new Athlete
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

        public IEnumerable<Athlete> FindAll()
        {
            Log.Info("");
            const string commandText = "select * from Athlete";
            IList<Athlete> athletes = new List<Athlete>();

            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                using var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    athletes.Add(new Athlete
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

            Log.Info(athletes);
            return athletes;
        }

        public void Save(Athlete athlete)
        {
            Log.Info($"Entered with entity = {athlete}");
            const string commandText =
                "insert into Athlete (id, name) values (@id, @name)";
            _validator.Validate(athlete);
            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", athlete.Id);
                command.Parameters.AddWithValue("name", athlete.Name);

                command.ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                Log.Error(ex.Message);
                Console.Write(ex.Message);
            }
        }

        public void Update(Athlete athlete)
        {
            Log.Info($"Entered with entity = {athlete}");
            const string commandText =
                "update Athlete set name = @name where id = @id";
            _validator.Validate(athlete);
            try
            {
                using var command = new SqliteCommand(commandText, _connection);
                Log.Debug(commandText);

                command.Parameters.AddWithValue("id", athlete.Id);
                command.Parameters.AddWithValue("name", athlete.Name);

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
            const string commandText = "delete from Athlete where id = @id";
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
