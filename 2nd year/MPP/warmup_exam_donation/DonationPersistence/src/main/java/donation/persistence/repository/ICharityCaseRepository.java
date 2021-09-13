package donation.persistence.repository;


import donation.model.CharityCase;

import java.util.List;

public interface ICharityCaseRepository extends ICrudRepository<Long, CharityCase> {
    List<CharityCase> FilterByName(String name);

}
