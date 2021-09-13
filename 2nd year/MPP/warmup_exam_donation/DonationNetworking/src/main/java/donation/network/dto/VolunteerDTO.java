package donation.network.dto;

import donation.model.Volunteer;

import java.io.Serializable;

public class VolunteerDTO implements Serializable {
    private Long id;
    private String username;
    private String password;
    private String name;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public VolunteerDTO(Long id,String name, String username, String password) {
        this.id = id;
        this.username = username;
        this.password = password;
        this.name = name;
    }

    public VolunteerDTO(String username, String password) {
        this.username = username;
        this.password = password;
    }
}
