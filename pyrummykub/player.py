#!/usr/bin/env python3
import logging, sys, time

FORMAT = '%(levelname)s:    %(asctime)s - %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=FORMAT)

class Player(object):
    def __init__(self, hand):
        self.hand = hand
        self.hand.sort(key=lambda x:x.identifier)
        self.did_first_move = False

    def add_tile(self, tile):
        self.hand.append(tile)

    @property
    def hand_size(self):
        return len(self.hand)

    @property
    def get_hand(self):
        return [(x.colored, x.identifier) for x in self.hand]

    def is_a_set(self, tiles):
        # logging.debug("Input: {}".format([(x.color, x.identifier) for x in tiles]))

        if len(tiles) < 3:
            return False
        tiles.sort(key=lambda x:x.identifier)

        # all(x == items[0] for x in items)
        if all(x.color_num == tiles[0].color_num for x in tiles):
            # logging.debug("All tiles are the same color")
            if len(list(set([x.identifier for x in tiles]))) == len(tiles):
                if self.is_arithmetic_progression([x.identifier for x in tiles]):
                    logging.debug("Is a set: {}".format([(x.color, x.identifier) for x in tiles]))
                    return True
        elif len(list(set([x.color_num for x in tiles]))) == len(tiles):
            if all(x.identifier == tiles[0].identifier for x in tiles):
                logging.debug("Is a set: {}".format([(x.color, x.identifier) for x in tiles]))
                return True
        return False

    def is_arithmetic_progression(self, inp):
        # delta = inp[1] - inp[0]
        delta = 1
        for i in range(len(inp) - 1):
            if not (inp[i + 1] - inp[i] == delta):
                return False
        # time.sleep(9999)
        return True

    def first_move(self):
        res = []

        count = {}
        switch_1 = True
        while switch_1:
            set = []
            for ai, a in enumerate(self.hand):
                for bi, b in enumerate(self.hand):
                    for ci, c in enumerate(self.hand):
                        if self.is_a_set(tiles=[a, b, c]):
                            # res.append(a)
                            self.hand.remove(a)
                            # res.append(b)
                            self.hand.remove(b)
                            # res.append(c)
                            self.hand.remove(c)
                            set = [a, b, c]
                            switch_2 = True
                            while switch_2:
                                loop_flag = False
                                for di, d in enumerate(self.hand):
                                    if self.is_a_set(tiles=set+[d]):
                                        # set.remove(d)
                                        loop_flag = True
                                        self.hand.remove(d)
                                if not loop_flag:
                                    switch_2 = False
                            logging.debug("SET: {}".format([(x.color, x.identifier) for x in set]))
                            for tile in set:
                                res.append(tile)
            if not set:
                switch_1 = False
        if res:
            logging.debug("RES: {}".format([(x.color, x.identifier) for x in res]))
            if sum([x.identifier for x in res]) > 30:
                self.did_first_move = True
                return res
        return False

    def has_move(self, table):
        res = []
        return res
