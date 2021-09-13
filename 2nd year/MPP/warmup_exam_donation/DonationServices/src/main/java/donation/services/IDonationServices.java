package donation.services;


import donation.model.CharityCase;
import donation.model.Donation;
import donation.model.Donor;
import donation.model.Volunteer;

import java.sql.SQLException;
import java.util.List;

public interface IDonationServices {
    Volunteer FindVolunteerByCredentials(Volunteer vol, IDonationObserver client) throws DonationException;
    void Logout(Volunteer vol, IDonationObserver client) throws DonationException;
    List<Donor> FindDonorsByName(String name) throws DonationException;
    List<CharityCase> GetAllCharityCases() throws DonationException;
    Donation AddDonation(Donation d) throws SQLException, DonationException;
    Donor AddDonor(Donor d) throws SQLException, DonationException;
    Long GetRaisedSum(Long charityId);


}
