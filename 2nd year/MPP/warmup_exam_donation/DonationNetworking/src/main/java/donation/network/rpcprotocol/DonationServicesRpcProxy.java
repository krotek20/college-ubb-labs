package donation.network.rpcprotocol;

import donation.model.CharityCase;
import donation.model.Donation;
import donation.model.Donor;
import donation.model.Volunteer;
import donation.network.dto.*;
import donation.services.DonationException;
import donation.services.IDonationObserver;
import donation.services.IDonationServices;

import javax.swing.*;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.sql.Array;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.stream.Collectors;

public class DonationServicesRpcProxy implements IDonationServices{
    private String host;
    private int port;

    private IDonationObserver client;

    private ObjectInputStream input;
    private ObjectOutputStream output;
    private Socket connection;

    private BlockingQueue<Response> qresponses;
    private volatile boolean finished;
    public DonationServicesRpcProxy(String host, int port) {
        this.host = host;
        this.port = port;
        qresponses=new LinkedBlockingQueue<Response>();
    }

    private void closeConnection() {
        finished=true;
        try {
            input.close();
            output.close();
            connection.close();
            client=null;
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private void sendRequest(Request request)throws DonationException {
        try {
            output.writeObject(request);
            output.flush();
        } catch (IOException e) {
            throw new DonationException("Error sending object "+e);
        }

    }

    private Response readResponse() throws DonationException {
        Response response=null;
        try{

            response=qresponses.take();

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return response;
    }
    private void initializeConnection() throws DonationException {
        try {
            connection=new Socket(host,port);
            output=new ObjectOutputStream(connection.getOutputStream());
            output.flush();
            input=new ObjectInputStream(connection.getInputStream());
            finished=false;
            startReader();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void startReader(){
        Thread tw=new Thread(new ReaderThread());
        tw.start();
    }

    private void handleUpdate(Response response){
        switch (response.type()){
            case NEW_DONATION:
                client.donationAdded(DTOUtils.getFromDTO((DonationDTO) response.data()));
                break;
            case NEW_DONOR:
                client.donorAdded(DTOUtils.getFromDTO((DonorDTO) response.data()));
                break;

        }

    }

    private boolean isUpdate(Response response){
        return response.type()== ResponseType.NEW_DONATION || response.type()== ResponseType.NEW_DONOR || response.type()== ResponseType.UPDATE;
    }

    @Override
    public Volunteer FindVolunteerByCredentials(Volunteer vol, IDonationObserver client) throws DonationException {
        initializeConnection();
        VolunteerDTO vdto = DTOUtils.getDTO(vol);
        Request req=new Request.Builder().type(RequestType.LOGIN).data(vdto).build();
        sendRequest(req);
        Response response=readResponse();
        if (response.type()== ResponseType.OK){
            this.client=client;
            return DTOUtils.getFromDTO((VolunteerDTO)response.data());
        }
        if (response.type()== ResponseType.ERROR){
            String err=response.data().toString();
            closeConnection();
            throw new DonationException(err);
        }
        return null;

    }

    @Override
    public void Logout(Volunteer vol, IDonationObserver client) throws DonationException {
        VolunteerDTO vdto = DTOUtils.getDTO(vol);
        Request req=new Request.Builder().type(RequestType.LOGOUT).data(vdto).build();
        sendRequest(req);
        Response response=readResponse();
        closeConnection();
        if (response.type()== ResponseType.ERROR){
            String err=response.data().toString();
            throw new DonationException(err);
        }

    }

    @Override
    public List<Donor> FindDonorsByName(String name) throws DonationException {
        Request req=new Request.Builder().type(RequestType.SEARCH_DONOR).data(name).build();
        sendRequest(req);
        Response response=readResponse();
        if (response.type()== ResponseType.OK){
            return Arrays.asList(DTOUtils.getFromDTO((DonorDTO[]) response.data()));
        }
        if (response.type()== ResponseType.ERROR){
            String err=response.data().toString();
            closeConnection();
            throw new DonationException(err);
        }
        return null;

    }

    @Override
    public List<CharityCase> GetAllCharityCases() throws DonationException {
        Request req=new Request.Builder().type(RequestType.GET_CHARITIES).build();
        sendRequest(req);
        Response response=readResponse();
        if (response.type()== ResponseType.OK){
            return Arrays.asList(DTOUtils.getFromDTO((CharityCaseDTO[]) response.data()));

        }
        if (response.type()== ResponseType.ERROR){
            String err=response.data().toString();
            closeConnection();
            throw new DonationException(err);
        }
        return null;
    }

    @Override
    public Donation AddDonation(Donation d) throws SQLException, DonationException {
        Request req=new Request.Builder().type(RequestType.ADD_DONATION).data(DTOUtils.getDTO(d)).build();
        sendRequest(req);
        Response response=readResponse();
        if (response.type()== ResponseType.ERROR){
            String err=response.data().toString();
            throw new DonationException(err);
        }
        return null;
    }

    @Override
    public Donor AddDonor(Donor d) throws SQLException, DonationException {
        Request req=new Request.Builder().type(RequestType.ADD_DONOR).data(DTOUtils.getDTO(d)).build();
        sendRequest(req);
        Response response=readResponse();
        if (response.type()== ResponseType.ERROR){
            String err=response.data().toString();
            throw new DonationException(err);
        }
        return null;
    }

    @Override
    public Long GetRaisedSum(Long charityId) {
        return null;
    }

    private class ReaderThread implements Runnable{
        public void run() {
            while(!finished){
                try {
                    Object response=input.readObject();
                    System.out.println("response received "+response);
                    if (isUpdate((Response)response)){
                        handleUpdate((Response)response);
                    }else{

                        try {
                            qresponses.put((Response)response);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                } catch (IOException e) {
                    System.out.println("Reading error "+e);
                } catch (ClassNotFoundException e) {
                    System.out.println("Reading error "+e);
                }
            }
        }
    }
}
