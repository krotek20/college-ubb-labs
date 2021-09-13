package controller;

import domain.Participant;
import domain.User;
import javafx.application.Platform;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import service.IService;
import service.IServiceException;
import service.IServiceObserver;

import java.io.Serializable;
import java.rmi.RemoteException;
import java.rmi.server.RMIClientSocketFactory;
import java.rmi.server.RMIServerSocketFactory;
import java.rmi.server.UnicastRemoteObject;
import java.time.LocalTime;
import java.util.List;

public class GeneralController extends UnicastRemoteObject implements IServiceObserver, Serializable {
    private IService service;
    private ObservableList<Participant> modelParticipanti = FXCollections.observableArrayList();
    private User currentLoggedUser;

    public GeneralController() throws RemoteException {
    }

    protected GeneralController(int port) throws RemoteException {
        super(port);
    }

    protected GeneralController(int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf) throws RemoteException {
        super(port, csf, ssf);
    }

    public void setService(IService service) {
        this.service = service;
    }

    public void loginUser(User currentLoggedUser) {
        try {
            this.currentLoggedUser = service.login(currentLoggedUser, this);
            //this.currentLoggedUser = currentLoggedUser;
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
            throw ex;
        }
    }

    public void logout() {
        service.logout(currentLoggedUser);
    }

    public ObservableList<Participant> getModelParticipant() {
        return modelParticipanti;
    }

    @Override
    public void updateParticipanti(List<Participant> allParticipanti) throws IServiceException, RemoteException {
        Platform.runLater(() -> {
            modelParticipanti.clear();
            modelParticipanti.addAll(allParticipanti);
        });
    }

    public void daNota(Participant participant, Double nota) {
        service.adaugaRezultat(currentLoggedUser, participant, nota);
    }
}
