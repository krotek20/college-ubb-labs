using System.Collections.Generic;
using model;

namespace persistence
{
    public interface IRepository<in TId, TEntity> where TEntity : Entity<TId>
    {
        TEntity FindOne(TId id);
        IEnumerable<TEntity> FindAll();
        void Save(TEntity entity);
        void Update(TEntity entity);
        void Delete(TId id);
    }
}
