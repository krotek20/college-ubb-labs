namespace persistence.validators
{
    public interface IValidator<T>
    {
        void Validate(T entity);
    }
}
