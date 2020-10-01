#!/usr/bin/env python3
import logging, sys
from termcolor import colored

FORMAT = '%(levelname)s:    %(asctime)s - %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=FORMAT)

class Tile(object):

    COLORS_ENUM = {
        'YELLOW': 1,
        'BLUE': 2,
        'RED': 3,
        'BLACK': 4
    }

    def __init__(self, color, identifier):
        self.color = color
        self.identifier = identifier
        self.color_num = self.COLORS_ENUM[color]
        # self.colored = self.get_colored_value(color)

    @property
    def colored(self):
        # return colored("●", color.lower())
        return self.color
