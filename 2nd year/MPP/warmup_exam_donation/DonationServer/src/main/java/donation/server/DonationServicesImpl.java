package donation.server;

import donation.model.CharityCase;
import donation.model.Donation;
import donation.model.Donor;
import donation.model.Volunteer;
import donation.persistence.repository.ICharityCaseRepository;
import donation.persistence.repository.IDonationRepository;
import donation.persistence.repository.IDonorRepository;
import donation.persistence.repository.IVolunteerRepository;
import donation.services.DonationException;
import donation.services.IDonationObserver;
import donation.services.IDonationServices;

import java.rmi.RemoteException;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class DonationServicesImpl implements IDonationServices {

    IVolunteerRepository volunteerRepository;
    IDonationRepository donationRepository;
    IDonorRepository donorRepository;
    ICharityCaseRepository charityCaseRepository;
    private Map<Long, IDonationObserver> loggedClients;

    public DonationServicesImpl(IVolunteerRepository volunteerRepository, IDonationRepository donationRepository, IDonorRepository donorRepository, ICharityCaseRepository charityCaseRepository) {
        this.volunteerRepository = volunteerRepository;
        this.donationRepository = donationRepository;
        this.donorRepository = donorRepository;
        this.charityCaseRepository = charityCaseRepository;
        loggedClients = new ConcurrentHashMap<>();
    }

    @Override
    public Volunteer FindVolunteerByCredentials(Volunteer vol, IDonationObserver client) throws DonationException {
        Volunteer requestedVol=volunteerRepository.FindByCredentials(vol.getUsername(),vol.getPassword());
        if (requestedVol!=null){
            if(loggedClients.get(requestedVol.getId())!=null)
                throw new DonationException("Volunteer already logged in.");
            loggedClients.put(requestedVol.getId(), client);
            return requestedVol;
        }else
            throw new DonationException("Authentication failed.");
    }

    @Override
    public void Logout(Volunteer vol, IDonationObserver client) throws DonationException {
        if(loggedClients.get(vol.getId())==null)
            throw new DonationException("Volunteer not logged in.");
        loggedClients.remove(vol.getId());
    }

    @Override
    public List<Donor> FindDonorsByName(String name) {
        return donorRepository.FilterByName(name, false);
    }

    @Override
    public List<CharityCase> GetAllCharityCases() {
        List<CharityCase> ret = charityCaseRepository.FindAll();
        for(CharityCase cc : ret) {
            cc.setRaisedSum(0L);
            for (Donation d : donationRepository.FilterByCaseId(cc.getId()))
                cc.setRaisedSum(cc.getRaisedSum() + d.getSum());
        }
        return ret;
    }

    @Override
    public Donation AddDonation(Donation d) throws SQLException, DonationException {
        d.setId(donationRepository.GetMaxId()+1);
        if(donationRepository.Add(d) != null)
            throw new DonationException("Couldn't add donation.");
        for(Map.Entry<Long, IDonationObserver> pair :  loggedClients.entrySet()){
            try {
                pair.getValue().donationAdded(d);
            } catch (RemoteException e) {
                throw new DonationException(e.getMessage());
            }
        }
        return d;
    }

    @Override
    public Donor AddDonor(Donor d) throws SQLException, DonationException {
        d.setId(donorRepository.GetMaxId() + 1);
        if (donorRepository.Add(d) != null)
            throw new DonationException("Couldn't add donation.");
        for (Map.Entry<Long, IDonationObserver> pair : loggedClients.entrySet()) {
            try{
            pair.getValue().donorAdded(d);
            } catch (RemoteException e) {
                throw new DonationException(e.getMessage());
            }
        }
        return d;

    }

    @Override
    public Long GetRaisedSum(Long charityId) {
        return donationRepository.getRaisedSum(charityId);
    }

    private void notifyDonation(){

    }
}
