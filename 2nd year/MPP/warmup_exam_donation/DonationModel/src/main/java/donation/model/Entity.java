package donation.model;

import java.io.Serializable;

public class Entity<T> implements Serializable {
    public T getId() {
        return id;
    }

    public void setId(T id) {
        this.id = id;
    }

    protected T id;

}
