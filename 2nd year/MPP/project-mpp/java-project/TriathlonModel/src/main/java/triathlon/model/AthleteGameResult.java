package triathlon.model;

import java.io.Serializable;

public class AthleteGameResult implements Serializable {
    private final Result result;
    private final Athlete athlete;

    public AthleteGameResult(Result result, Athlete athlete) {
        this.result = result;
        this.athlete = athlete;
    }

    @SuppressWarnings("unused")
    public String getAthleteName() {
        return athlete.getName();
    }

    @SuppressWarnings("unused")
    public Float getResultPoints() {
        return result.getValue();
    }
}
