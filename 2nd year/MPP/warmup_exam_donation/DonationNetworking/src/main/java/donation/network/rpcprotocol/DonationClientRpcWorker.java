package donation.network.rpcprotocol;

import donation.model.CharityCase;
import donation.model.Donation;
import donation.model.Donor;
import donation.model.Volunteer;
import donation.network.dto.*;
import donation.services.DonationException;
import donation.services.IDonationObserver;
import donation.services.IDonationServices;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class DonationClientRpcWorker implements Runnable, IDonationObserver {
    private IDonationServices server;
    private Socket connection;

    private ObjectInputStream input;
    private ObjectOutputStream output;
    private volatile boolean connected;

    public DonationClientRpcWorker(IDonationServices server, Socket connection) {
        this.server = server;
        this.connection = connection;
        try{
            output=new ObjectOutputStream(connection.getOutputStream());
            output.flush();
            input=new ObjectInputStream(connection.getInputStream());
            connected=true;
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void donorAdded(Donor newDonor) {
        Response updateResponse=new Response.Builder().type(ResponseType.NEW_DONOR).data(DTOUtils.getDTO(newDonor)).build();
        try {
            sendResponse(updateResponse);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void donationAdded(Donation d) {
        Response updateResponse=new Response.Builder().type(ResponseType.NEW_DONATION).data(DTOUtils.getDTO(d)).build();
        try {
            sendResponse(updateResponse);
        } catch (IOException e) {
            e.printStackTrace();
        }


    }

    @Override
    public void run() {
        while(connected){
            try {
                System.out.println("Available : " + input.available() + ", reading");
                Object request=input.readObject();
                Response response=handleRequest((Request)request);
                if (response!=null){
                    sendResponse(response);
                }
            } catch (IOException e) {
                e.printStackTrace();
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        try {
            input.close();
            output.close();
            connection.close();
        } catch (IOException e) {
            System.out.println("Error "+e);
        }
    }

    private static Response okResponse=new Response.Builder().type(ResponseType.OK).build();
    //  private static Response errorResponse=new Response.Builder().type(ResponseType.ERROR).build();
    private Response handleRequest(Request request){
        Volunteer vol;
        Response response=null;
        switch(request.type()){
            case LOGIN:
                vol=DTOUtils.getFromDTO((VolunteerDTO)request.data());
                System.out.println("Login request - " + vol.getUsername());
                try {
                    Volunteer v = server.FindVolunteerByCredentials(vol, this);
                    return new Response.Builder().type(ResponseType.OK).data(DTOUtils.getDTO(v)).build();
                } catch (DonationException e) {
                    connected=false;
                    return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
                }

            case LOGOUT:
                vol =DTOUtils.getFromDTO((VolunteerDTO)request.data());
                System.out.println("Logout request - " + vol.getUsername());
            try{
                    server.Logout(vol,this);
                   connected = false;

                return okResponse;
            } catch (DonationException e) {
                    return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
                }
            case SEARCH_DONOR:
                String name = (String)request.data();
                System.out.println("Search donor request - " + name);
                try {
                    List<Donor> list = server.FindDonorsByName(name);
                    DonorDTO[] arr = new DonorDTO[list.size()];
                    for(int i = 0; i < list.size(); i++)
                        arr[i] = DTOUtils.getDTO(list.get(i));
                    return new Response.Builder().type(ResponseType.OK).data(arr).build();
                } catch (DonationException e) {
                    return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
                }
            case GET_CHARITIES:
                System.out.println("Get Charities request");
                try {
                    List<CharityCase> list = server.GetAllCharityCases();
                    CharityCaseDTO[] arr = new CharityCaseDTO[list.size()];
                    for(int i = 0; i < list.size(); i++) {
                        arr[i] = DTOUtils.getDTO(list.get(i), server.GetRaisedSum(list.get(i).getId()));
                    }
                    return new Response.Builder().type(ResponseType.OK).data(arr).build();
                } catch (DonationException e) {
                    return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
                }

            case ADD_DONOR:
                System.out.println("Add donor request");
                DonorDTO donDto = (DonorDTO)request.data();
                Donor donor = DTOUtils.getFromDTO(donDto);
                try {
                    donor = server.AddDonor(donor);
                    return new Response.Builder().type(ResponseType.OK).build();
                } catch (DonationException | SQLException e) {
                    return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
                }
                case ADD_DONATION:
                System.out.println("Add donation request");
                DonationDTO d = (DonationDTO)request.data();
                Donation don = DTOUtils.getFromDTO(d);
                try {
                    server.AddDonation(don);
                    return new Response.Builder().type(ResponseType.OK).build();
                } catch (DonationException | SQLException e) {
                    return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
                }
        }

        return response;
    }


    private void sendResponse(Response response) throws IOException{
        System.out.println("sending response "+response);
        output.writeObject(response);
        output.flush();
    }
}
