using System;
using System.Data;
using System.Data.SqlClient;
using System.Threading;

namespace lab4_sgbd
{
    class Program
    {
        static SqlConnection conn = null;
        private static SqlConnection GetConnection()
        {
            if (conn == null)
            {
                conn = new SqlConnection("Server=DESKTOP-LLHQVU9;Database=L1;Integrated Security=true;");
            }
            if (conn.State == ConnectionState.Closed)
            {
                conn.Open();
            }
            return conn;
        }

        static void HandleThread()
        {
            int reruns = 3;
            while (reruns > 0)
            {
                try
                {
                    string cmdString = "exec uspGenerateDeadlock2 @currentCityName, @updatedCityName, @currentProductName, @updatedProductName";
                    using (SqlCommand cmd = new SqlCommand(cmdString, GetConnection()))
                    {
                        cmd.Parameters.AddWithValue("@currentCityName", "Atlantic");
                        cmd.Parameters.AddWithValue("@updatedCityName", "AtlanticModified2");
                        cmd.Parameters.AddWithValue("@currentProductName", "Cabtopor");
                        cmd.Parameters.AddWithValue("@updatedProductName", "CabtoporModified2");
                        cmd.ExecuteNonQuery();

                        break;
                    }
                }
                catch (SqlException ex) when (ex.Number == 1205)
                {
                    Console.WriteLine("Retry second thread");
                    reruns--;
                }
            }
            if (reruns <= 0)
            {
                Console.WriteLine("Abort!");
            }
            Console.WriteLine("Finish2");
        }

        static void Main(string[] args)
        {
            GetConnection();
            Thread thread = new Thread(HandleThread);
            thread.Start();
            int reruns = 3;
            while (reruns > 0)
            {
                try
                {
                    string cmdString = "exec uspGenerateDeadlock1 @currentCityName, @updatedCityName, @currentProductName, @updatedProductName";
                    using (SqlCommand cmd = new SqlCommand(cmdString, GetConnection()))
                    {
                        cmd.Parameters.AddWithValue("@currentCityName", "Atlantic");
                        cmd.Parameters.AddWithValue("@updatedCityName", "AtlanticModified1");
                        cmd.Parameters.AddWithValue("@currentProductName", "Cabtopor");
                        cmd.Parameters.AddWithValue("@updatedProductName", "CabtoporModified1");
                        cmd.ExecuteNonQuery();
                        break;
                    }
                }
                catch (SqlException ex) when (ex.Number == 1205)
                {
                    Console.WriteLine("Retry first thread");
                    reruns--;
                }
            }
            if (reruns <= 0)
            {
                Console.WriteLine("Abort!");
            }
            Console.WriteLine("Finish1");
            thread.Join();
            Console.WriteLine("Done!");
            Console.ReadKey();
        }
    }
}
