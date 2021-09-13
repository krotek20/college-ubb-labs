package donation.persistence.repository;


import donation.model.Donor;

import java.util.List;

public interface IDonorRepository extends ICrudRepository<Long, Donor>{
    List<Donor> FilterByName(String name, boolean caseSensitive);
    List<Donor> FilterByPhoneNumber(String phone);

}
