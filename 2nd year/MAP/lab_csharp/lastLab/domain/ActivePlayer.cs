using System;

namespace lastLab.domain
{
    public class ActivePlayer : Entity<Tuple<long, long>>
    {
        public long ScoredPoints { get; set; }
        public PlayerType Type { get; set; }

        public ActivePlayer(long playerId, long gameId, long scoredPoints, PlayerType type)
        {
            Id = new Tuple<long, long>(playerId, gameId);
            ScoredPoints = scoredPoints;
            Type = type;
        }
        
        public override string ToString()
        {
            return Id.Item1 + ";" + Id.Item2 + ";" + ScoredPoints + ";" + Type;
        }
    }
}