using System.Collections.Generic;
using System.IO;

namespace lastLab.repository
{
    public class DataReader
    {
        public static List<T> ReadData<T>(string fileName, CreateEntity<T> createEntity)
        {
            List<T> list = new List<T>();
            using (StreamReader sr = new StreamReader(fileName))
            {
                string s;
                while ((s = sr.ReadLine()) != null)
                {
                    T entity = createEntity(s);
                    list.Add(entity);
                }
            }

            return list;
        }

        public static List<string> ReadGeneratedData(string fileName)
        {
            List<string> list = new List<string>();
            using (StreamReader sr = new StreamReader(fileName))
            {
                string s;
                while ((s = sr.ReadLine()) != null)
                {
                    list.Add(s);
                }
            }

            return list;
        }
    }
}