using System.Collections.Generic;
using lastLab.domain;

namespace lastLab.repository
{
    public interface IRepository<ID, E> where E : Entity<ID>
    {
        IEnumerable<E> FindAll();

        E Save(E entity);

        E FindOne(ID id);
    }
}