using System;
using lastLab.domain;
using lastLab.utils;

namespace lastLab.repository
{
    public class StudentFileRepository : InFileRepository<long, Student>
    {
        public StudentFileRepository(string fileName, CreateEntity<Student> createEntity) : base(fileName, createEntity)
        {
        }
        
        public static Student CreateStudent(string line)
        {
            string[] elems = line.Split(";");
            Student student = new Student(elems[1], elems[2]);
            student.Id = Parser.SafeLongParse(elems[0]);

            return student;
        }
    }
}