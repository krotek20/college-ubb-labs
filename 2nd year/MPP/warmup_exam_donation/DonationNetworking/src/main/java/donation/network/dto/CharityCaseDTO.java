package donation.network.dto;

import java.io.Serializable;

public class CharityCaseDTO implements Serializable {
    Long id;
    String name;
    Long sumRaised;

    public CharityCaseDTO(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    public CharityCaseDTO(Long id, String name, Long sumRaised) {
        this.id = id;
        this.name = name;
        this.sumRaised = sumRaised;
    }

    public Long getSumRaised() {
        return sumRaised;
    }

    public void setSumRaised(Long sumRaised) {
        this.sumRaised = sumRaised;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
