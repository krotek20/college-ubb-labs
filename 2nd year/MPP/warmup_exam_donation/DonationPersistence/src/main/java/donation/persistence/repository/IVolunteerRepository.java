package donation.persistence.repository;


import donation.model.Volunteer;

import java.util.List;

public interface IVolunteerRepository extends ICrudRepository<Long,Volunteer>{
    List<Volunteer> FilterByName(String name);
    Volunteer FindByCredentials(String username, String password);
}
