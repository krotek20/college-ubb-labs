package service;
/*
import domain.CharityCase;
import domain.Donation;
import domain.Donor;
import domain.Volunteer;
import repository.*;

import java.sql.SQLException;
import java.util.List;

public class Service {
    IVolunteerRepository volunteerRepository;
    IDonationRepository donationRepository;
    IDonorRepository donorRepository;
    ICharityCaseRepository charityCaseRepository;

    public Service(IVolunteerRepository volR, IDonationRepository donaR,IDonorRepository donR, ICharityCaseRepository charR)
    {
        this.volunteerRepository = volR;
        this.donationRepository = donaR;
        this.donorRepository = donR;
        this.charityCaseRepository = charR;
    }

    public Volunteer FindVolunteerByCredentials(String username, String password)
    {
        return volunteerRepository.FindByCredentials(username, password);
    }

    public List<Donor> FindDonorsByName(String name, boolean caseSensitive){
        return donorRepository.FilterByName(name, caseSensitive);
    }

    public List<CharityCase> GetAllCharityCases(){
        return charityCaseRepository.FindAll();
    }

    public Donation AddDonation(Long charityId, Long donorId, Long sum) throws SQLException {
        Donation d = new Donation(donationRepository.GetMaxId()+1,charityId, donorId, sum);
        return donationRepository.Add(d) == null ? d : null;
    }
    public Donor addDonor(String name, String address, String phoneNumber) throws SQLException {
        Donor d = new Donor(donorRepository.GetMaxId()+1,name,address,phoneNumber);
        return donorRepository.Add(d) == null ? d : null;
    }

    public Long GetRaisedSum(Long charityId){
        return donationRepository.getRaisedSum(charityId);
    }
}

 */