package donation.persistence.repository;


import donation.model.Donation;

import java.util.List;

public interface IDonationRepository extends ICrudRepository<Long, Donation>{
    List<Donation> FilterByCaseId(Long id);
    Donation FilterByDonorId(Long id);
    List<Donation> FilterBySum(Long minimum);
    Long getRaisedSum(Long charityId);
}
