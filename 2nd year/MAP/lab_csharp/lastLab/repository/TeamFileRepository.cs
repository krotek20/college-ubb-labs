using lastLab.domain;
using lastLab.utils;

namespace lastLab.repository
{
    public class TeamFileRepository : InFileRepository<long, Team>
    {
        public TeamFileRepository(string fileName, CreateEntity<Team> createEntity) : base(fileName, createEntity)
        {
        }

        public static Team CreateTeam(string line)
        {
            string[] elems = line.Split(";");
            Team team = new Team(elems[1]);
            team.Id = Parser.SafeLongParse(elems[0]);

            return team;
        }
    }
}