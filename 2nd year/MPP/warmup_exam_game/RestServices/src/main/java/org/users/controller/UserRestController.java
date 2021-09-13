package org.users.controller;

import domain.Participant;
import domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import repository.ParticipantRepository;
import repository.UserRepository;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

@CrossOrigin
@RestController
@RequestMapping("judgeapp/judging")
public class UserRestController {
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private ParticipantRepository participantRepository;

    @GetMapping
    public List<User> getAllUsers() {
        return StreamSupport.stream(userRepository.findAll().spliterator(), false).collect(Collectors.toList());
    }

    @GetMapping("/note")
    public ResponseEntity<?> getAllNote(@RequestParam (value = "organizator") Long organizator) {
        if (null == userRepository.findOne(organizator)) {
            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(StreamSupport.stream(participantRepository.findAll().spliterator(), false).filter((x) -> {
            if (organizator == 1 && x.getNota1() != null)
                return true;
            if (organizator == 2 && x.getNota2() != null)
                return true;
            if (organizator == 3 && x.getNota3() != null)
                return true;
            return false;
        }).map((x) -> {
            if (organizator == 1)
                return Map.entry(x.getNume(), x.getNota1());
            if (organizator == 2)
                return Map.entry(x.getNume(), x.getNota2());
            if (organizator == 3)
                return Map.entry(x.getNume(), x.getNota3());
            return  Map.entry(x.getNume(), 0);
        }).collect(Collectors.toMap((entry) -> entry.getKey(), (entry) -> entry.getValue())), HttpStatus.OK);
    }

    @GetMapping("/participanti")
    public ResponseEntity<?> getNoteParticipant(@RequestParam (value = "participant") Long participant) {
        Participant p = participantRepository.findOne(participant);
        if (null == p) {
            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(p, HttpStatus.OK);
    }

//    @GetMapping
//    public ResponseEntity<?> getById(@RequestParam (value = "id", required = false)Long id) {
//        if (id == null) {
//            return new ResponseEntity<>(StreamSupport.stream(excursieRepository.findAll().spliterator(), false).collect(Collectors.toList()), HttpStatus.OK);
//        }
//        Excursie excursie = excursieRepository.findOne(id);
//        if (null == excursie) {
//            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
//        }
//        return new ResponseEntity<>(excursie, HttpStatus.OK);
//    }
//
//    @PostMapping
//    public Excursie create(@RequestBody Excursie excursie) {
//        return excursieRepository.save(excursie);
//    }
//
//    @PutMapping
//    public ResponseEntity<Excursie> update(@RequestBody Excursie excursie) {
//        Excursie retVal = excursieRepository.update(excursie);
//        if (null == retVal) {
//            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
//        }
//        return new ResponseEntity<>(retVal, HttpStatus.OK);
//    }
//
//    @DeleteMapping
//    public ResponseEntity<Excursie> delete(@RequestParam (value="id") Long id) {
//        Excursie excursie = excursieRepository.delete(id);
//        if (null == excursie) {
//            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
//        }
//        return new ResponseEntity<>(excursie, HttpStatus.OK);
//    }
}
