namespace model
{
    public class Referee : Entity<long>
    {
        public Game Game { get; set; }
        public string Name { get; set; }
        public string Username { get; set; }
        public string Password { get; set; }

       /* public Referee(Game game, string name, string username, string password) : this(0L, game, name, username, password)
        {

        }

        public Referee(long id, Game game, string name, string username, string password)
        {
            Id = id;
            Game = game;
            Name = name;
            Username = username;
            Password = password;
        } */

        public override string ToString()
        {
            return "{\"id\": " + Id +
                ", \"game\": " + Game.ToString() +
                ", \"name\": \"" + Name + "\"" +
                ", \"username\": \"" + Username + "\"" +
                ", \"password\": \"" + Password + "\"" + "}";
        }
    }
}
