namespace lastLab.domain
{
    public class Student : Entity<long>
    {
        public string Name { get; set; }
        public string School { get; set; }

        public Student(string name, string school)
        {
            Name = name;
            School = school;
        }

        public override string ToString()
        {
            return Id + ";" + Name + ";" + School;
        }
    }
}