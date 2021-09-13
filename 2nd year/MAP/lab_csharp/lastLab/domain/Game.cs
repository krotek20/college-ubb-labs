using System;

namespace lastLab.domain
{
    public class Game : Entity<long>
    {
        public Team FirstTeam { get; set; } 
        public Team SecondTeam { get; set; }
        public DateTime Date { get; set; }

        public Game(Team firstTeam, Team secondTeam, DateTime date)
        {
            FirstTeam = firstTeam;
            SecondTeam = secondTeam;
            Date = date;
        }
        
        public override string ToString()
        {
            return Id + ";" + FirstTeam.Id + ";" + SecondTeam.Id + ";" + Date;
        }
    }
}