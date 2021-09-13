using System.Collections.Generic;
using System.IO;
using lastLab.domain;

namespace lastLab.repository
{
    public delegate E CreateEntity<E>(string line);

    public class InFileRepository<ID, E> : InMemoryRepository<ID, E> where E : Entity<ID>
    {
        private string fileName;
        private CreateEntity<E> _createEntity;

        public InFileRepository(string fileName, CreateEntity<E> createEntity)
        {
            this.fileName = fileName;
            _createEntity = createEntity;
            if (createEntity != null)
            {
                LoadFromFile();
            }
        }

        protected void LoadFromFile()
        {
            List<E> list = DataReader.ReadData(fileName, _createEntity);
            list.ForEach(x => Entities[x.Id] = x);
        }

        public void WriteToFile(E entity)
        {
            using (StreamWriter file = File.AppendText(fileName))
            {
                file.WriteLine(entity.ToString());
            }
        }

        public override E Save(E entity)
        {
            E returnedValue = base.Save(entity);
            WriteToFile(entity);
            return returnedValue;
        }
    }
}