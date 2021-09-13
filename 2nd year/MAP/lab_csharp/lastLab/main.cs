using System;
using lastLab.domain;
using lastLab.repository;
using lastLab.service;
using lastLab.UI;
using lastLab.utils;

namespace lastLab
{
    class main
    {
        static void Main(string[] args)
        {
            // Repositories
            IRepository<long, Team> teamRepository =
                new TeamFileRepository("..\\..\\..\\data\\teams.txt", TeamFileRepository.CreateTeam);
            IRepository<long, Game> gameRepository =
                new GameFileRepository("..\\..\\..\\data\\games.txt", GameFileRepository.CreateGame);
            IRepository<long, Player> playerRepository =
                new PlayerFileRepository("..\\..\\..\\data\\players.txt", PlayerFileRepository.CreatePlayer);
            IRepository<long, Student> studentRepository = 
                new StudentFileRepository("..\\..\\..\\data\\students.txt", StudentFileRepository.CreateStudent);
            IRepository<Tuple<long, long>, ActivePlayer> activePlayerRepository =
                new ActivePlayerFileRepository("..\\..\\..\\data\\activePlayers.txt",
                    ActivePlayerFileRepository.CreateActivePlayer);

            // Service
            Service service = new Service(gameRepository, playerRepository, activePlayerRepository);
            
            // generate data
            // GenerateData generateData = new GenerateData();
            // generateData.GenerateStudents(studentRepository);
            // generateData.GeneratePlayers(playerRepository, teamRepository);
            // generateData.GenerateGames(gameRepository, teamRepository);
            // generateData.GenerateActivePlayers(activePlayerRepository);
            
            // Ui
            Ui ui = new Ui(service);
            
            // Run application
            ui.Run();
        }
    }
}