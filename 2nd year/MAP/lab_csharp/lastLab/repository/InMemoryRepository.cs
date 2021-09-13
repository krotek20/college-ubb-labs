using System;
using System.Collections.Generic;
using System.Linq;
using lastLab.domain;

namespace lastLab.repository
{
    public class InMemoryRepository<ID, E> : IRepository<ID, E> where E : Entity<ID>
    {
        protected IDictionary<ID, E> Entities = new Dictionary<ID, E>();

        public IEnumerable<E> FindAll()
        {
            return Entities.Values.ToList();
        }

        public virtual E Save(E entity)
        {
            if (entity == null)
            {
                throw new ArgumentException("entity must be not null");
            }

            if (Entities.ContainsKey(entity.Id))
            {
                return entity;
            }

            Entities[entity.Id] = entity;
            return default(E);
        }

        public E FindOne(ID id)
        {
            if (!Entities.ContainsKey(id))
            {
                return null;
            }
            return Entities[id];
        }
    }
}