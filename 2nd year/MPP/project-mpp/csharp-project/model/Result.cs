namespace model
{
    public class Result : Entity<long>
    {
        public Game Game { get; set; }
        public Athlete Athlete { get; set; }
        public double Value { get; set; }

       /* public Result(Game game, Athlete athlete, double value) : this(0L, game, athlete, value)
        {

        }

        public Result(long id, Game game, Athlete athlete, double value)
        {
            Id = id;
            Game = game;
            Athlete = athlete;
            Value = value;
        }
       */
        public override string ToString()
        {
            return Athlete.Name + " " + Value;
        }
    }
}
