using System;

namespace networking.dto
{
    [Serializable]
    public class ResultHandlerDto
    {
        public ResultDto ResultDto  { get; set; }
        public double TotalPoints { get; set; }
    }
}