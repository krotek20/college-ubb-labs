package triathlon.services.rest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import triathlon.model.Referee;
import triathlon.persistence.RefereeRepository;
import triathlon.persistence.RepositoryException;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/triathlon/referees")
public class RefereeController {
    private final RefereeRepository refereeRepository;

    @Autowired
    public RefereeController(RefereeRepository refereeRepository) {this.refereeRepository = refereeRepository;}

    @GetMapping
    public Iterable<Referee> getAll() {
        Iterable<Referee> referees = refereeRepository.findAll();
        return referees;
    }

    @GetMapping("/{refereeId}")
    public ResponseEntity<?> getOne(@PathVariable Long refereeId) {
        Referee referee = refereeRepository.findOne(refereeId);
        if (referee == null) return new ResponseEntity<String>("Referee not found!", HttpStatus.NOT_FOUND);
        else return new ResponseEntity<Referee>(referee, HttpStatus.OK);
    }

    @PostMapping
    public Referee create(@RequestBody Referee referee) {
        refereeRepository.save(referee);
        return referee;
    }

    @PutMapping("/{refereeId}")
    public Referee update(@RequestBody Referee referee, @PathVariable String refereeId) {
        refereeRepository.update(referee);
        return referee;
    }

    @DeleteMapping("/{refereeId}")
    public ResponseEntity<?> delete(@PathVariable Long refereeId) {
        try {
            refereeRepository.delete(refereeId);
            return new ResponseEntity<Referee>(HttpStatus.OK);
        } catch (RepositoryException ex) {
            return new ResponseEntity<String>(ex.getMessage(), HttpStatus.BAD_REQUEST);
        }
    }
}
