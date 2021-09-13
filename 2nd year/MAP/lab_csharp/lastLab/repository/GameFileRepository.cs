using System.Xml;
using lastLab.domain;
using lastLab.utils;

namespace lastLab.repository
{
    public class GameFileRepository : InFileRepository<long, Game>
    {
        public GameFileRepository(string fileName, CreateEntity<Game> createEntity) : base(fileName, createEntity)
        {
        }

        public static Game CreateGame(string line)
        {
            string[] elems = line.Split(";");
            
            Team firstTeam = new Team(null);
            Team secondTeam = new Team(null);
            firstTeam.Id = Parser.SafeLongParse(elems[1]);
            secondTeam.Id = Parser.SafeLongParse(elems[2]);

            Game game = new Game(firstTeam, secondTeam, Parser.SafeDateTimeParse(elems[3]));
            game.Id = Parser.SafeLongParse(elems[0]);

            return game;
        }
    }
}