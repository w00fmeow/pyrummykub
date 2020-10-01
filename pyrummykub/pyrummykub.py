#!/usr/bin/env python3
import random, logging, sys
from player import Player
from tile import Tile

FORMAT = '%(levelname)s:    %(asctime)s - %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=FORMAT)

class PyRummy(object):

    PLAYERS_LIMIT = (1, 4)
    IDENTIFIER_RANGE = (0, 14)
    COLORS = ['YELLOW','BLUE', 'RED', 'BLACK']
    HAND_SIZE = 14

    def __init__(self, number_of_players):
        if not self.PLAYERS_LIMIT[0] <= number_of_players <= self.PLAYERS_LIMIT[1]:
            logging.error("Number of players is not supported")
            sys.exit()

        self.draw_pile = self.create_pile()
        random.shuffle(self.draw_pile)
        self.players = []
        self.winner = None
        self.table = []
        for _ in range(0, number_of_players):
            self.players.append(Player(hand=self.create_hand()))
        # logging.debug("DRAW")
        self.play()

    def create_pile(self):
        l = []
        for lap in range(0, 2):
            for color in self.COLORS:
                for identifier in range(*self.IDENTIFIER_RANGE):
                    l.append(Tile(color=color, identifier=identifier))
        return l

    def create_hand(self):
        l = []
        for _ in range(0, self.HAND_SIZE):
            l.append(self.draw_pile.pop(random.randrange(len(self.draw_pile))))
        return l

    def get_draw_pile_size(self):
        return len(self.draw_pile)

    def get_draw_pile(self):
        return [(x.colored, x.identifier) for x in self.draw_pile]

    def get_table(self):
        return [(x.colored, x.identifier) for x in self.table]

    def play(self):
        turns = 0
        while not self.winner:
            for i, player in enumerate(self.players):
                turns += 1
                logging.info("*********** Turn #{}".format(turns))
                # logging.debug("draw_pile : {}".format(self.get_draw_pile()))
                logging.debug("table: {}".format(self.get_table()))
                logging.info("Player's #{} move".format(i))
                logging.debug("Player's hand on start of turn: {}".format(player.get_hand))

                move = None
                if player.did_first_move:
                    move = player.has_move(table=self.table)
                if not player.did_first_move:
                    first_move = player.first_move()
                    # logging.debug("HERE #1")
                    if first_move:
                        # logging.debug("players move: {}".format())
                        for tile in first_move:
                            self.table.append(tile)
                    else:
                        player.add_tile(self.draw_pile.pop(random.randrange(len(self.draw_pile))))
                elif move:
                    logging.debug("Move: {}".format([(x.colored, x.identifier) for x in move]))
                    for tile in move:
                        self.table.append(tile)
                else:
                    player.add_tile(self.draw_pile.pop(random.randrange(len(self.draw_pile))))

                logging.debug("Player's hand len in turn end: {}".format(player.get_hand))
                input("Press enter for next lap")







n = 4
p = PyRummy(number_of_players=n)
