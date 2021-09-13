package donation.network.utils;

import donation.network.rpcprotocol.DonationClientRpcWorker;
import donation.services.IDonationServices;

import java.net.Socket;

public class DonationRpcConcurrentServer extends AbsConcurrentServer {
    private IDonationServices donationServer;
    public DonationRpcConcurrentServer(int port, IDonationServices donationServer) {
        super(port);
        this.donationServer = donationServer;
        System.out.println("Donation- DonationRpcConcurrentServer");
    }

    @Override
    protected Thread createWorker(Socket client) {
        DonationClientRpcWorker worker=new DonationClientRpcWorker(donationServer, client);
        Thread tw=new Thread(worker);
        return tw;
    }

    @Override
    public void stop(){
        System.out.println("Stopping services ...");
    }
}
