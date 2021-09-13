using System;

namespace lastLab.utils
{
    public class Parser
    {
        public static long SafeLongParse(string stringId)
        {
            long id;
            try
            {
                id = long.Parse(stringId);
            }
            catch (FormatException)
            {
                throw new Exception("Id must be numeric");
            }

            return id;
        }

        public static DateTime SafeDateTimeParse(string stringDateTime)
        {
            DateTime dateTime;
            try
            {
                dateTime = DateTime.Parse(stringDateTime);
            }
            catch (FormatException)
            {
                throw new Exception("Invalid date format");
            }

            return dateTime;
        }
    }
}