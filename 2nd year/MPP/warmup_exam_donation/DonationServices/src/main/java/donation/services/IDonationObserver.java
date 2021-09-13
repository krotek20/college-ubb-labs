package donation.services;

import donation.model.Donation;
import donation.model.Donor;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface IDonationObserver extends Remote {
    void donorAdded(Donor newDonor) throws DonationException, RemoteException;
    void donationAdded(Donation d) throws DonationException, RemoteException;
}
