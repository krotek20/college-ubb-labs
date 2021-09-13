package org.game.controller;

import domain.InitialCard;
import domain.Move;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import repository.GameRepository;
import repository.MoveRepository;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

@CrossOrigin
@RestController
@RequestMapping("gameapp")
public class GameRestController {
    @Autowired
    private GameRepository gameRepository;
    @Autowired
    private MoveRepository moveRepository;

    @GetMapping("/initialCards")
    public Map<String, List<String>> getInitialCards(@RequestParam (value = "game") Long idJoc) {
        Map<String, List<String>> ret = new HashMap<>();
        Set<InitialCard> initialCards = gameRepository.findOne(idJoc).getInitialCards();
        for (InitialCard i : initialCards) {
            String username = i.getPlayer().getUsername();
            if (!ret.containsKey(username)) {
                ret.put(username, new ArrayList<>());
            }
            ret.get(username).add(i.getCard1());
            ret.get(username).add(i.getCard2());
            ret.get(username).add(i.getCard3());
        }
        return ret;
    }

    @GetMapping("/sentCards")
    public List<Move> getSentCards(@RequestParam (value = "game") Long idJoc, @RequestParam (value = "player") Long idJucator) {
        return StreamSupport.stream(moveRepository.findAll().spliterator(), false)
                .filter(x -> x.getPlayer().getId().equals(idJoc)
                        && x.getPlayer().getId().equals(idJucator))
                .collect(Collectors.toList());
    }
}
