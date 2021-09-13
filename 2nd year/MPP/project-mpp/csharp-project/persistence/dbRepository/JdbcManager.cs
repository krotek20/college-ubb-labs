using System;
using System.Data;
using Microsoft.Data.Sqlite;

namespace persistence.dbRepository
{
    public static class JdbcManager
    {
        private static SqliteConnection _connection;

        public static SqliteConnection GetConnection()
        {
            //var url = ConfigurationManager.AppSettings.Get("jdbc.url");
            const string url =
                @"Data Source=C:\Users\RaduVF\Desktop\mpp-proiect-repository-krotek20\project-csharp\radu_mpp_csharp";
            try
            {
                _connection ??= new SqliteConnection(url);

                if (_connection.State == ConnectionState.Closed)
                {
                    _connection.Open();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }

            return _connection;
        }
    }
}
