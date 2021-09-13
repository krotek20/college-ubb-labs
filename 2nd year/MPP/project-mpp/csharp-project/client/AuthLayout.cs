using System;
using System.Windows.Forms;

namespace client
{
    public partial class AuthLayout : Form
    {
        private readonly TriathlonClientController _controller;
        public AuthLayout(TriathlonClientController controller)
        {
            InitializeComponent();
            _controller = controller;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var username = username_tb.Text;
            var password = password_tb.Text;
            try
            {
                _controller.Authenticate(username, password);
                var mainLayout = new MainLayout(_controller)
                {
                    Text = @"Main window for " + username
                };
                mainLayout.Show();
                Hide();
            }
            catch (Exception ex)
            {
                MessageBox.Show(this, @"Authentication Error " + ex.Message,
                    @"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
