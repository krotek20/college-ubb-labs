using System;

namespace networking.dto
{
    [Serializable]
    public class GameDto
    {
        public long Id { get; set; }
        public string Name { get; set; }
    }
}
