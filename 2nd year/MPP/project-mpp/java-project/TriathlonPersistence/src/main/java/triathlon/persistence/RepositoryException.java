package triathlon.persistence;

public class RepositoryException extends RuntimeException {
    public RepositoryException() {
    }

    public RepositoryException(String message) {
        super(message);
    }
}