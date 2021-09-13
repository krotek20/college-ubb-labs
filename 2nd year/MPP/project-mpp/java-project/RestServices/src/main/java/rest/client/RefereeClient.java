package rest.client;

import org.hibernate.service.spi.ServiceException;
import org.springframework.web.client.RestTemplate;
import triathlon.model.Referee;

import java.util.concurrent.Callable;

public class RefereeClient {
    public static final String URL = "http://localhost:8080/triathlon/referees";

    private final RestTemplate restTemplate = new RestTemplate();

    private <T> T execute(Callable<T> callable) {
        try {
            return callable.call();
        } catch (Exception e) {
            throw new ServiceException(e.getMessage());
        }
    }

    public Iterable getAll() {
        return execute(() -> restTemplate.getForObject(URL, Iterable.class));
    }

    public Referee getById(Long id) {
        return execute(() -> restTemplate.getForObject(String.format("%s/%s", URL, id), Referee.class));
    }

    public Referee create(Referee referee) {
        return execute(() -> restTemplate.postForObject(URL, referee, Referee.class));
    }

    public void update(Referee referee) {
        execute(() -> {
            restTemplate.put(String.format("%s/%s", URL, referee.getId()), referee);
            return null;
        });
    }

    public void delete(Long id) {
        execute(() -> {
            restTemplate.delete(String.format("%s/%s", URL, id));
            return null;
        });
    }
}
