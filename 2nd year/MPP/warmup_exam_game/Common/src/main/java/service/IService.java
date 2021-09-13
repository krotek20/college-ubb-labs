package service;


import domain.Participant;
import domain.User;

public interface IService {
    User login(User user, IServiceObserver client);

    void logout(User user);

    void adaugaRezultat(User user, Participant participant, double nota);

    void getAllParticipanti();
}