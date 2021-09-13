namespace model
{
    public class Game : Entity<long>
    {
        public string Name { get; set; }

       /* public Game(long id) : this(id, "")
        {

        }

        public Game(long id, string name)
        {
            Id = id;
            Name = name;
        } */

        public override string ToString()
        {
            return "{\"id\": " + Id +
                ", \"name\": \"" + Name + "\"" + "}";
        }
    }
}
