package triathlon.services;

import triathlon.model.Result;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ITriathlonObserver extends Remote {
    void pointsChanged(Result result) throws TriathlonException, RemoteException;
}
