namespace model
{
    public class AthleteGameResult
    {
        public double Points { get; set; }
        public string AthleteName { get; set; }
        
        public override string ToString()
        {
            return AthleteName + " " + Points;
        }
    }
}
