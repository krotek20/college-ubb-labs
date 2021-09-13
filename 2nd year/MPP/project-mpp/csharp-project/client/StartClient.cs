using System;
using System.Windows.Forms;
using networking;
using services;

namespace client
{
    static class StartClient
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            ITriathlonServices server = new TriathlonServerProxy("127.0.0.1", 55555);
            var ctrl = new TriathlonClientController(server);
            var win = new AuthLayout(ctrl);
            Application.Run(win);
        }
    }
}
