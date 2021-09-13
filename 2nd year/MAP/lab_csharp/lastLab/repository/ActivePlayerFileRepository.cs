using System;
using lastLab.domain;
using lastLab.utils;

namespace lastLab.repository
{
    public class ActivePlayerFileRepository : InFileRepository<Tuple<long, long>, ActivePlayer>
    {
        public ActivePlayerFileRepository(string fileName, CreateEntity<ActivePlayer> createEntity) : base(fileName, createEntity)
        {
        }

        public static ActivePlayer CreateActivePlayer(string line)
        {
            string[] elems = line.Split(";");

            long playerId = Parser.SafeLongParse(elems[0]);
            long gameId = Parser.SafeLongParse(elems[1]);
            long scoredPoints = Parser.SafeLongParse(elems[2]);

            PlayerType playerType;
            Enum.TryParse(elems[3], out playerType);

            ActivePlayer activePlayer = new ActivePlayer(playerId, gameId, scoredPoints, playerType);

            return activePlayer;
        }
    }
}