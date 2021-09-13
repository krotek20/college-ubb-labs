package triathlon.services;

public class TriathlonException extends Exception {
    public TriathlonException() {
    }

    public TriathlonException(String message) {
        super(message);
    }

    public TriathlonException(String message, Throwable cause) {
        super(message, cause);
    }

}
