package triathlon.network.rpcprotocol;

import triathlon.model.*;
import triathlon.network.dto.*;
import triathlon.services.ITriathlonObserver;
import triathlon.services.ITriathlonServices;
import triathlon.model.exceptions.TriathlonException;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.Collection;
import java.util.Map;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class ITriathlonServicesRpcProxy implements ITriathlonServices {
    private final int port;
    private final String host;
    private Socket connection;
    private ITriathlonObserver client;
    private ObjectInputStream input;
    private ObjectOutputStream output;
    private final BlockingQueue<Response> responses;
    private volatile boolean finished;

    public ITriathlonServicesRpcProxy(String host, int port) {
        this.host = host;
        this.port = port;
        responses = new LinkedBlockingQueue<>();
    }

    private void closeConnection() {
        finished = true;
        try {
            input.close();
            output.close();
            connection.close();
            client = null;
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void sendRequest(Request request) throws TriathlonException {
        try {
            output.writeObject(request);
            output.flush();
        } catch (IOException e) {
            throw new TriathlonException("Error sending object " + e);
        }
    }

    private Response readResponse() throws TriathlonException {
        Response response = null;
        try {
            response = responses.take();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return response;
    }

    private void initializeConnection() throws TriathlonException {
        try {
            connection = new Socket(host, port);
            output = new ObjectOutputStream(connection.getOutputStream());
            output.flush();
            input = new ObjectInputStream(connection.getInputStream());
            finished = false;
            startReader();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void startReader() {
        Thread tw = new Thread(new ReaderThread());
        tw.start();
    }

    @Override
    public Collection<Athlete> getAthletes() {
        Request req = new Request.Builder().type(RequestType.GET_ALL_ATHLETES).data(null).build();
        sendRequest(req);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            String err = response.data().toString();
            throw new TriathlonException(err);
        }
        return DTOUtils.getFromDTO(() -> ((Collection<AthleteDTO>) response.data()));
    }

    @Override
    public Map<String, Float> getAthletesTotalPoints() {
        Request req = new Request.Builder().type(RequestType.GET_ATHLETES_TOTAL_POINTS).data(null).build();
        sendRequest(req);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            String err = response.data().toString();
            throw new TriathlonException(err);
        }
        return (Map<String, Float>) response.data();
    }

    @Override
    public Game getGameById(Long id) {
        Request req = new Request.Builder().type(RequestType.GET_GAME_ID).data(id).build();
        sendRequest(req);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            String err = response.data().toString();
            throw new TriathlonException(err);
        }
        return DTOUtils.getFromDTO((GameDTO) response.data());
    }

    @Override
    public Referee authenticate(Referee referee, ITriathlonObserver client) {
        initializeConnection();
        RefereeDTO refereeDTO = new RefereeDTO(0L, referee.getName(),
                referee.getUsername(), referee.getPassword());
        Request req = new Request.Builder().type(RequestType.AUTHENTICATION).data(refereeDTO).build();
        sendRequest(req);
        Response response = readResponse();
        if (response.type() == ResponseType.OK) {
            this.client = client;
        }
        if (response.type() == ResponseType.ERROR) {
            String err = response.data().toString();
            closeConnection();
            throw new TriathlonException(err);
        }
        return DTOUtils.getFromDTO((RefereeDTO) response.data());
    }

    @Override
    public void logout(Referee referee, ITriathlonObserver client) {
        RefereeDTO refereeDTO = DTOUtils.getDTO(referee);
        Request req = new Request.Builder().type(RequestType.LOGOUT).data(refereeDTO).build();
        sendRequest(req);
        Response response = readResponse();
        closeConnection();
        if (response.type() == ResponseType.ERROR) {
            String err = response.data().toString();
            throw new TriathlonException(err);
        }
    }

    @Override
    public Collection<Result> getResultsForGame(Long gameId) {
        Request req = new Request.Builder().type(RequestType.GET_RESULTS_GAME).data(gameId).build();
        sendRequest(req);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            String err = response.data().toString();
            throw new TriathlonException(err);
        }
        return DTOUtils.getFromDTO((Collection<ResultDTO>) response.data());
    }

    @Override
    public void setResult(Athlete athlete, Game game, Float value) {
        ResultDTO resultDTO = new ResultDTO(game.getID(), athlete.getID(), value);
        Request req = new Request.Builder().type(RequestType.SET_POINTS).data(resultDTO).build();
        sendRequest(req);
        Response response = readResponse();
        if (response.type() == ResponseType.ERROR) {
            String err = response.data().toString();
            throw new TriathlonException(err);
        }
    }

    private void handleUpdate(Response response) {
        if (response.type() == ResponseType.UPDATE_POINTS) {
            Result result = DTOUtils.getFromDTO((ResultDTO) response.data());
            try {
                client.pointsChanged(result);
            } catch (TriathlonException e) {
                e.printStackTrace();
            }
        }
    }

    private boolean isUpdate(Response response) {
        return response.type() == ResponseType.UPDATE_POINTS;
    }

    private class ReaderThread implements Runnable {
        public void run() {
            while (!finished) {
                try {
                    Object response = input.readObject();
                    System.out.println("response received " + response);
                    if (isUpdate((Response) response)) {
                        handleUpdate((Response) response);
                    } else {
                        try {
                            responses.put((Response) response);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                } catch (IOException | ClassNotFoundException e) {
                    System.out.println("Reading error " + e);
                }
            }
        }
    }
}