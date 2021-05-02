import json
import logging
import os
import random
import socket
from logging.handlers import RotatingFileHandler
import sys

import protocol

sys.path.insert(0, '/bord_src')
from bord_src import my_utils as mu

from bord_src.inspector import color_red as R

host = "localhost"
port = 12000
# HEADERSIZE = 10

"""
set up inspector logging
"""
inspector_logger = logging.getLogger()
inspector_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s :: %(levelname)s :: %(message)s", "%H:%M:%S")
# file
if os.path.exists("./logs/inspector.log"):
    os.remove("./logs/inspector.log")
file_handler = RotatingFileHandler('./logs/inspector.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
inspector_logger.addHandler(file_handler)
# stream
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
inspector_logger.addHandler(stream_handler)


class Player():

    def __init__(self):

        self.end = False
        # self.old_question = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.char_order = ['red', 'grey', 'black', 'white', 'purple', 'blue', 'pink', 'brown']
        self.actual_card_played = None

    def connect(self):
        self.socket.connect((host, port))

    def reset(self):
        self.socket.close()

    def get_index(self, reponse, data):
        i = 0
        if reponse not in data:
            print('response =', reponse)
            return 0
        while data[i] != reponse:
            i = i + 1
        return i

    #Ici on a une condition pour chaque couleur, ici on ne s'occupe des des déplacement.
    def play_color(self, game_state, data):
        suspect_number = mu.suspect_number(game_state)
        #print('Nombre de suspect :', suspect_number)
        scream_number = mu.scream_number(game_state)
        #print('Nombre de personne qui peuvent crier :', scream_number')
        color = self.actual_card_played['color']
        print('data =', data)
        if color == "grey":
            return 0
        if color == "blue":
            return 0
        if color == "white":
            return 0
        if color == "purple":
            return 0
        if color == "black":
            return 0
        if color == "red":
            position = R.play_red(suspect_number, scream_number, game_state, self.actual_card_played, data)
            return self.get_index(position, data)
        if color == "pink" or color == "brown":
            return 0
        return 0

    #Ici on ajoute une condition pour chaque pouvoir, exemple : le serveur envoie "grey character power" -> on apelle G.play_grey_power()
    def play_color_power(self, question, suspect_number, scream_number, game_state, data):
        print(question['question type'], " ------------------------------------")
        print('Data=',data)
        if question['question type'] == "grey character power":
            return 0
        if question['question type'] == "active black power":
            position = B.play_black_power(game_state, data, self.actual_card_played,suspect_number, scream_number)
            return self.get_index(position,data)

    #C'est ici que l'ont va voir ce que le serveur demande au travers de ces question, et les reponse attendue dans data
    def answer(self, question):
        # work
        #Data contient les reponse possible, exemple : [0,2,5,6]
        data = question["data"]
        #Game_state contient l'etat du jeux/plateau. On trouve dedans la position de toutes les couleurs,
        #si elle sont suspect ou pas et +. Hésitez pas a le print pour le comprendre
        game_state = question["game state"]
        #Si il faut choisir une couleur parmis les 4 carte a jouer
        if (question['question type'] == "select character"):
            print('\n')
            print('_____Select Color_____')
            res, self.actual_card_played = mu.choose_character(data, self.char_order)
            print('Color choose:',res, ' aka ', self.actual_card_played['color'])
            return res
        #Si il faut déplacer la couleur
        if (question['question type'] == "select position"):
            print('_____Select position_____')
            res = self.play_color(game_state, data)
            print('----On va dans la sale :', res,'----')
            return res

        #On s'occupe maintenant des pouvoir, on re calcul le nombre de couleurs qui peuvent cries, et le nombre de suspect.
        suspect_number = mu.suspect_number(game_state)
        scream_number = mu.scream_number(game_state)
        #print('Nombre de suspect :', suspect_number)
        #print('Nombre de personne qui peuvent crier :', scream_number)
        return self.play_color_power(question, suspect_number, scream_number, game_state, data)

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
