package start;

import org.springframework.web.client.RestClientException;
import rest.client.RefereeClient;
import triathlon.model.Game;
import triathlon.model.Referee;

public class StartRestClient {
    private final static RefereeClient refereeClient = new RefereeClient();

    public static void main(String[] args) {
        try {
            System.out.println("\nSearch referee with id {1}:");
            Referee referee = refereeClient.getById(1L);
            System.out.println(referee.toString());

            System.out.println("\nView all referees");
            for (Object r : refereeClient.getAll()) {
                System.out.println(r);
            }

            System.out.println("\nAdd referee");
            Referee addReferee = refereeClient.create(new Referee(new Game(2L),
                    "newReferee", "newReferee", "newReferee123"));
            System.out.println("Referee added: " + addReferee.toString());

            System.out.println("\nView all referees again");
            for (Object r : refereeClient.getAll()) {
                System.out.println(r);
            }

            System.out.println("\nUpdate referee");
            Referee updateReferee = new Referee(addReferee.getId(), addReferee.getGame(),
                    "updateReferee", "updateReferee", "updateReferee123");
            refereeClient.update(updateReferee);
            System.out.println("Referee updated: " + updateReferee.toString());

            System.out.println("\nView all referees again and again");
            for (Object r : refereeClient.getAll()) {
                System.out.println(r);
            }

            System.out.println("\nDelete referee");
            refereeClient.delete(addReferee.getId());
            System.out.println("Referee deleted!");

            System.out.println("\nView all referees again and again and again");
            for (Object r : refereeClient.getAll()) {
                System.out.println(r);
            }
        } catch (RestClientException ex) {
            System.out.println("Exception ... " + ex.getMessage());
        }
    }
}
