import json
import logging
import os
import random
import socket
from logging.handlers import RotatingFileHandler
import time

import protocol

host = "localhost"
port = 12000
# HEADERSIZE = 10

"""
set up fantom logging
"""
fantom_logger = logging.getLogger()
fantom_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s :: %(levelname)s :: %(message)s", "%H:%M:%S")
# file
if os.path.exists("./logs/fantom.log"):
    os.remove("./logs/fantom.log")
file_handler = RotatingFileHandler('./logs/fantom.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
fantom_logger.addHandler(file_handler)
# stream
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
fantom_logger.addHandler(stream_handler)


class Player():

    def __init__(self):

        self.end = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.char_order = ['grey', 'blue', 'white', 'purple', 'black', 'red', 'pink', 'brown']
        self.actual_card_played = None

    def connect(self):
        self.socket.connect((host, port))

    def reset(self):
        self.socket.close()

    #Choose the card to play
    def choose_character(self, data):
        for color in self.char_order:
            for each in data:
                if (each['color'] == color):
                    return each

    #Is the color alone in room ?
    def is_alone(self, color, card):
        for each in card:
            if each['position'] == color['position'] and each['color'] != color['color']:
                return False
        return True

    #How many people are able to scream
    def scream_number(self, data):
        scream_number = 0
        card = data['characters']
        for color in card:
            if self.is_alone(color, card) == True:
                if color['suspect'] == True:
                    scream_number = scream_number + 1
        return scream_number

    #How many suspect still in the game
    def suspect_number(self, data):
        suspects = 0
        for each in data['characters']:
            if each['suspect'] is True:
                suspects = suspects + 1
        return suspects
    
    #qyestion type select char
    def select_character(self, data):
        print("select character")
        color = self.choose_character(data)
        self.actual_card_played = color
        print(color)
        return color
    
    #question type select position
    def select_position(self, game_state):
        suspect_number = self.suspect_number(game_state)
        print('Nombre de suspect :', suspect_number, '\n')
        scream_number = self.scream_number(game_state)
        print('Nombre de personne qui peuvent crier :', scream_number, '\n')

    def answer(self, question):
        # work
        print(question)
        data = question["data"]
        game_state = question["game state"]
        if (question['question type'] == "select character"):
            return self.select_character(data)
        if (question['question type'] == "select position"):
            return self.select_position(game_state)
        return 0

    def handle_json(self, data):
        data = json.loads(data)
        response = self.answer(data)
        # send back to server
        bytes_data = json.dumps(response).encode("utf-8")
        protocol.send_json(self.socket, bytes_data)

    def run(self):

        self.connect()

        while self.end is not True:
            received_message = protocol.receive_json(self.socket)
            if received_message:
                self.handle_json(received_message)
            else:
                print("no message, finished learning")
                self.end = True


p = Player()

p.run()
