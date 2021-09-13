using System;

namespace networking.dto
{
    [Serializable]
    public class ResultDto
    {
        public long GameId { get; set; }
        public string AthleteName { get; set; }
        public double Points { get; set; }
    }
}
