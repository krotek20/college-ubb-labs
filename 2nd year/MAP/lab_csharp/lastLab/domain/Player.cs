namespace lastLab.domain
{
    public class Player : Student
    {
        public Team Team { get; set; }
        
        public Player(string name, string school, Team team) : base(name, school)
        {
            Team = team;
        }
        
        public override string ToString()
        {
            return Id + ";" + Name + ";" + School + ";" + Team.Id;
        }
    }
}