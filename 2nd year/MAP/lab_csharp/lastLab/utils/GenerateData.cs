using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using lastLab.domain;
using lastLab.repository;

namespace lastLab.utils
{
    public class GenerateData
    {
        private IList<string> FirstNames;
        private IList<string> LastNames;
        private IList<string> Students;
        private IList<string> Schools;

        private Random random = new Random();

        public GenerateData()
        {
            FirstNames = ReadFirstNames();
            LastNames = ReadLastNames();
            Students = ReadStudents();
            Schools = ReadSchools();
        }

        private IList<string> ReadFirstNames()
        {
            return DataReader.ReadGeneratedData("..\\..\\..\\data\\generateData\\firstNames.txt");
        }

        private IList<string> ReadLastNames()
        {
            return DataReader.ReadGeneratedData("..\\..\\..\\data\\generateData\\lastNames.txt");
        }

        private IList<string> ReadStudents()
        {
            return DataReader.ReadGeneratedData("..\\..\\..\\data\\students.txt");
        }

        private IList<string> ReadSchools()
        {
            return DataReader.ReadGeneratedData("..\\..\\..\\data\\generateData\\schools.txt");
        }

        public void GenerateStudents(IRepository<long, Student> studentRepository)
        {
            // clearing data
            File.WriteAllText("..\\..\\..\\data\\students.txt", String.Empty);

            long id = 0;
            foreach (string school in Schools)
            {
                for (int i = 0; i < 15; i++)
                {
                    id++;
                    string firstName = FirstNames[random.Next(FirstNames.Count)];
                    string lastName = LastNames[random.Next(LastNames.Count)];
                    Student student = new Student(firstName + " " + lastName, school);
                    student.Id = id;

                    studentRepository.Save(student);
                }
            }
        }

        public void GeneratePlayers(IRepository<long, Player> playerRepository, IRepository<long, Team> teamRepository)
        {
            // clearing data
            File.WriteAllText("..\\..\\..\\data\\players.txt", String.Empty);

            int teamId = -1;
            IList<Team> teams = teamRepository.FindAll().ToList();
            foreach (string student in Students)
            {
                string[] elems = student.Split(";");
                if ((Parser.SafeLongParse(elems[0]) - 1) % 15 == 0)
                {
                    teamId++;
                }

                Player player = new Player(elems[1], elems[2], teams[teamId]);
                player.Id = Parser.SafeLongParse(elems[0]);

                playerRepository.Save(player);
            }
        }

        public void GenerateGames(IRepository<long, Game> gameRepository, IRepository<long, Team> teamRepository)
        {
            // clearing data
            File.WriteAllText("..\\..\\..\\data\\games.txt", String.Empty);

            IList<Team> teams = teamRepository.FindAll().ToList();

            for (int i = 1; i <= 20; i++)
            {
                Team firstTeam = teams[random.Next(teams.Count)];
                Team secondTeam;
                do
                {
                    secondTeam = teams[random.Next(teams.Count)];
                } while (firstTeam.Id.Equals(secondTeam.Id));

                DateTime date = new DateTime(2010, 1, 1);
                int range = (DateTime.Today - date).Days;
                date = date
                    .AddDays(random.Next(range))
                    .AddHours(random.Next(24))
                    .AddMinutes(random.Next(60));

                Game game = new Game(firstTeam, secondTeam, date);
                game.Id = i;

                gameRepository.Save(game);
            }
        }

        private void GenerateFirstTeam(Game game, IRepository<Tuple<long, long>, ActivePlayer> activePlayerRepository)
        {
            Team firstTeam = game.FirstTeam;
            IList<Player> firstTeamPlayers = DataReader.ReadGeneratedData("..\\..\\..\\data\\players.txt")
                .ConvertAll(x => PlayerFileRepository.CreatePlayer(x))
                .Where(x => x.Team.Id.Equals(firstTeam.Id)).ToList();

            // choose 10 players to play
            for (int i = 0; i < 10; i++)
            {
                PlayerType playerType = (i < 6 ? PlayerType.Active : PlayerType.Reserve);
                long scoredPoints = (playerType == PlayerType.Reserve ? 0 : random.Next(20));

                ActivePlayer activePlayer =
                    new ActivePlayer(firstTeamPlayers[i].Id, game.Id, scoredPoints, playerType);

                activePlayerRepository.Save(activePlayer);
            }
        }

        private void GenerateSecondTeam(Game game, IRepository<Tuple<long, long>, ActivePlayer> activePlayerRepository)
        {
            Team secondTeam = game.SecondTeam;
            IList<Player> secondTeamPlayers = DataReader.ReadGeneratedData("..\\..\\..\\data\\players.txt")
                .ConvertAll(x => PlayerFileRepository.CreatePlayer(x))
                .Where(x => x.Team.Id.Equals(secondTeam.Id)).ToList();

            // choose 10 players to play
            for (int i = 0; i < 10; i++)
            {
                PlayerType playerType = (i < 6 ? PlayerType.Active : PlayerType.Reserve);
                long scoredPoints = (playerType == PlayerType.Reserve ? 0 : random.Next(20));

                ActivePlayer activePlayer =
                    new ActivePlayer(secondTeamPlayers[i].Id, game.Id, scoredPoints, playerType);

                activePlayerRepository.Save(activePlayer);
            }
        }

        public void GenerateActivePlayers(IRepository<Tuple<long, long>, ActivePlayer> activePlayerRepository)
        {
            // clearing data
            File.WriteAllText("..\\..\\..\\data\\activePlayers.txt", String.Empty);

            IList<Game> games = DataReader.ReadGeneratedData("..\\..\\..\\data\\games.txt")
                .ConvertAll(x => GameFileRepository.CreateGame(x));

            foreach (Game game in games)
            {
                GenerateFirstTeam(game, activePlayerRepository);
                GenerateSecondTeam(game, activePlayerRepository);
            }
        }
    }
}