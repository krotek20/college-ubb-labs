package service;

public class IServiceException extends RuntimeException {
    public IServiceException() {
    }

    public IServiceException(String message) {
        super(message);
    }

    public IServiceException(String message, Throwable cause) {
        super(message, cause);
    }

    public IServiceException(Throwable cause) {
        super(cause);
    }

    public IServiceException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}
