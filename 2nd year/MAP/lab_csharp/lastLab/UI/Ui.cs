using System;
using System.Collections.Generic;
using lastLab.service;
using lastLab.utils;

namespace lastLab.UI
{
    public class Ui
    {
        private Service _service;

        private IDictionary<string, Action> _functionsDictionary;

        public Ui(Service service)
        {
            _service = service;
        }

        private void TeamedPlayers()
        {
            Console.WriteLine("\nTeam id: ");
            long id = Parser.SafeLongParse(Console.ReadLine());
            foreach (var teamedPlayer in _service.GetTeamedPlayers(id))
            {
                Console.WriteLine(teamedPlayer);
            }
        }

        private void ActivePlayersByGame()
        {
            Console.WriteLine("\nTeam id:");
            long teamId = Parser.SafeLongParse(Console.ReadLine());
            Console.WriteLine("\nGame id:");
            long gameId = Parser.SafeLongParse(Console.ReadLine());
            foreach (var activePlayers in _service.GetActivePlayersByGame(teamId, gameId))
            {
                Console.WriteLine(activePlayers);   
            }
        }

        private void GamesByDateTime()
        {
            Console.WriteLine("\nFrom date:");
            DateTime from = Parser.SafeDateTimeParse(Console.ReadLine());
            Console.WriteLine("\nTo date:");
            DateTime to = Parser.SafeDateTimeParse(Console.ReadLine());
            foreach (var game in _service.GetGamesByDateTime(@from, to))
            {
                Console.WriteLine(game);
            }
        }

        private void GamePoints()
        {
            Console.WriteLine("\nGame id:");
            long id = Parser.SafeLongParse(Console.ReadLine());
            Tuple<long, long> scores = _service.GamePoints(id);
            Console.WriteLine(scores.Item1 + " - " + scores.Item2);
        }

        private void ExitApplcation()
        {
            Environment.Exit(0);
        }

        private void PopulateDictionary()
        {
            _functionsDictionary = new Dictionary<string, Action>();
            _functionsDictionary["1"] = TeamedPlayers;
            _functionsDictionary["2"] = ActivePlayersByGame;
            _functionsDictionary["3"] = GamesByDateTime;
            _functionsDictionary["4"] = GamePoints;
            _functionsDictionary["5"] = ExitApplcation;
        }

        private void PrintMenu()
        {
            Console.WriteLine(
                "Main Menu: \n" +
                "\t1. All players in a team\n" +
                "\t2. A team's active players by game\n" +
                "\t3. All games in a time period\n" +
                "\t4. Game score\n" +
                "\t5. Exit\n"
            );
        }

        public void Run()
        {
            PopulateDictionary();
            while (true)
            {
                PrintMenu();
                string option = Console.ReadLine();
                try
                {
                    _functionsDictionary[option ?? string.Empty].Invoke();
                }
                catch (KeyNotFoundException)
                {
                    Console.WriteLine("\nInvalid option\n");
                }
                catch (ArgumentException ae)
                {
                    Console.WriteLine(ae.Message);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            }
        }
    }
}