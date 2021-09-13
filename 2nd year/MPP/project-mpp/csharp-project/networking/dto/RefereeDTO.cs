using System;

namespace networking.dto
{
    [Serializable]
    public class RefereeDto
    {
        public long GameId { get; set; }
        public string Name { get; set; }
        public string Username { get; set; }
        public string Password { get; set; }
    }
}
