package service;

import domain.Participant;
import domain.User;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface IServiceObserver extends Remote {
//    void excursieUpdated() throws service.IServiceException, RemoteException;

    void updateParticipanti(List<Participant> allParticipanti) throws IServiceException, RemoteException;
}
