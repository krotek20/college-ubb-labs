using lastLab.domain;
using lastLab.utils;

namespace lastLab.repository
{
    public class PlayerFileRepository : InFileRepository<long, Player>
    {
        public PlayerFileRepository(string fileName, CreateEntity<Player> createEntity) : base(fileName, createEntity)
        {
        }

        public static Player CreatePlayer(string line)
        {
            string[] elems = line.Split(";");

            Team team = new Team(null);
            team.Id = Parser.SafeLongParse(elems[3]);
            
            Player player = new Player(elems[1], elems[2], team);
            player.Id = Parser.SafeLongParse(elems[0]);

            return player;
        }
    }
}