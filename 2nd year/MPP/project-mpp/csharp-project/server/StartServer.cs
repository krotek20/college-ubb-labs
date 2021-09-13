using System;
using System.Net.Sockets;
using System.Threading;
using networking;
using persistence;
using persistence.dbRepository;
using persistence.validators;
using services;

namespace server
{
    public class StartServer
    {
        static void Main(string[] args)
        {
            IGameRepository gameRepository = new DbGameRepository(new GameValidator());
            IResultRepository resultRepository = new DbResultRepository(new ResultValidator());
            IAthleteRepository athleteRepository = new DbAthleteRepository(new AthleteValidator());
            IRefereeRepository refereeRepository = new DbRefereeRepository(new RefereeValidator());

            ITriathlonServices triathlonService = new SuperService(
                gameRepository, resultRepository, athleteRepository, refereeRepository);

            var server = new ProtoV3TriathlonServer("127.0.0.1", 55557, triathlonService);
            server.Start();
            Console.WriteLine("Server started ...");
            Console.ReadLine();
        }

        public class ProtoV3TriathlonServer : ConcurrentServer
        {
            private readonly ITriathlonServices _server;
            private TriathlonV3ClientWorker _worker;
            public ProtoV3TriathlonServer(string host, int port, ITriathlonServices server)
                : base(host, port)
            {
                this._server = server;
                Console.WriteLine("ProtoTriathlonServer...");
            }
            protected override Thread CreateWorker(TcpClient client)
            {
                _worker = new TriathlonV3ClientWorker(_server, client);
                return new Thread(_worker.Run);
            }
        }
    }
}
