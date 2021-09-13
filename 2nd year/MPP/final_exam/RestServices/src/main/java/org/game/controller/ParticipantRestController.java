package org.game.controller;

import domain.Nota;
import domain.Participant;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import repository.ParticipantRepository;

import java.util.Map;
import java.util.stream.Collectors;

@CrossOrigin
@RestController
@RequestMapping("talentshow/participanti")
public class ParticipantRestController {
    @Autowired
    private ParticipantRepository participantRepository;

    @GetMapping("/{participantId}")
    public ResponseEntity<?> getOne(@PathVariable Long participantId) {
        Participant participant = participantRepository.findOne(participantId);
        if (participant == null) return new ResponseEntity<String>("Participantul nu exista!", HttpStatus.NOT_FOUND);
        else return new ResponseEntity<Map<String, Integer>>(participant.getNote()
                .stream().collect(Collectors.toMap(x -> x.getJurat().getUsername(), Nota::getNota)),
                HttpStatus.OK);
    }
}
