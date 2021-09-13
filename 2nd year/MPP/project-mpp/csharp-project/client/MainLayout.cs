using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using model;

namespace client
{
    public partial class MainLayout : Form
    {
        private readonly TriathlonClientController _controller;
        private readonly List<AthleteGameResult> _gameResults;
        private readonly List<AthleteGameResult> _totalResults;
        private readonly long _gameId;

        public MainLayout(TriathlonClientController controller)
        {
            InitializeComponent();
            _controller = controller;

            // Initialize general information labels
            var game = _controller.GetGameById();
            _gameId = game.Id;
            game_tb.Text = game.Name;
            referee_tb.Text = _controller.GetCurrentReferee().Name;

            // Populate Athletes ComboBox
            var athletes = _controller.GetAthletes().ToList();
            foreach (var athlete in athletes)
            {
                athlete_cb.Items.Add(athlete.Name);
            }

            // Populate list-boxes
            _gameResults = _controller.GetGameResults().ToList();
            gameResults_lb.DataSource = _gameResults;
            _totalResults = _controller.GetTotalResults().ToList();
            totalPoints_lb.DataSource = _totalResults;
            
            _controller.UpdateEvent += RefereeUpdate;
        }

        private void exit_btn_Click(object sender, EventArgs e)
        {
            _controller.Logout();
            _controller.UpdateEvent -= RefereeUpdate;
            var authLayout = new AuthLayout(_controller)
            {
                Text = @"Authentication"
            };
            authLayout.Show();
            Hide();
        }

        private void RefereeUpdate(object sender, TriathlonRefereeEventArgs e)
        {
            if (e.RefereeEventType != TriathlonRefereeEvent.PointsChanged) return;
            var result = (ResultUpdateHandler) e.Data;
            var gameResult = result.Result.Value;
            if (_gameId != result.Result.Game.Id)
            {
                gameResult = 0.0;
            }
            for (var i = 0; i < _gameResults.Count; i++)
            {
                if (!_gameResults[i].AthleteName.Equals(result.Result.Athlete.Name)) continue;
                _gameResults[i] = new AthleteGameResult
                {
                    AthleteName = result.Result.Athlete.Name,
                    Points = gameResult == 0.0 ? _gameResults[i].Points : gameResult
                };
                break;
            }
                
            for (var i = 0; i < _totalResults.Count; i++)
            {
                if (!_totalResults[i].AthleteName.Equals(result.Result.Athlete.Name)) continue;
                _totalResults[i] = new AthleteGameResult
                {
                    AthleteName = result.Result.Athlete.Name,
                    Points = result.TotalPoints
                };
                break;
            }
            Console.WriteLine(@"[Triathlon] Points updated " + result.Result.Game.Id);
            gameResults_lb.BeginInvoke(new UpdateListBoxCallback(UpdateListBox),
                gameResults_lb, _gameResults);
            totalPoints_lb.BeginInvoke(new UpdateListBoxCallback(UpdateListBox),
                totalPoints_lb, _totalResults);
        }

        private void UpdateListBox(ListBox listBox, IList<AthleteGameResult> newData)
        {
            listBox.DataSource = null;
            listBox.DataSource = newData;
        }

        private delegate void UpdateListBoxCallback(ListBox list, IList<AthleteGameResult> data);

        private void submit_btn_Click(object sender, EventArgs e)
        {
            _controller.UpdatePoints(athlete_cb.Text, Convert.ToDouble(points_tb.Text));
            points_tb.Clear();
        }
    }
}