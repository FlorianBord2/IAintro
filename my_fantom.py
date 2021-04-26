import json
import logging
import os
import random
import socket
from logging.handlers import RotatingFileHandler
import time

import protocol

import my_utils as mu

#REAME ! Pour chaque couleur, importer les fonctions comme cela
# import FILENAME as RACOURCIE

import color_pink_brown as PB
import color_grey as G
import color_purple as P

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

        #Ordre des couleur pour le fantome
        self.char_order = ['grey', 'blue', 'white', 'purple', 'black', 'red', 'pink', 'brown']
        self.actual_card_played = None

    def connect(self):
        self.socket.connect((host, port))

    def reset(self):
        self.socket.close()
    
    #Ici on a une condition pour chaque couleur, ici on ne s'occupe des des déplacement.
    def play_color(self, game_state, data):
        suspect_number = mu.suspect_number(game_state)
        #print('Nombre de suspect :', suspect_number)
        scream_number = mu.scream_number(game_state)
        #print('Nombre de personne qui peuvent crier :', scream_number')
        color = self.actual_card_played['color']
        if color == "grey":
            position = G.play_grey(suspect_number, scream_number, game_state, self.actual_card_played, data)
            print('move to ', position)
            return position
        if color == "blue":
            return 0
        if color == "white":
            return 0
        if color == "purple":
            return P.play_purple(suspect_number, scream_number, game_state, self.actual_card_played, data)
        if color == "black":
            return 0
        if color == "red":
            return 0
        if color == "pink" or color == "brown":
            return PB.play_pink_brown(suspect_number, scream_number, game_state, self.actual_card_played, data)
        return 0

    #Ici on ajoute une condition pour chaque pouvoir, exemple : le serveur envoie "grey character power" -> on apelle G.play_grey_power()
    def play_color_power(self, question, suspect_number, scream_number, game_state, data):
        if question['question type'] == "grey character power":
            print('_____',question['question type'], '_____')
            print(data)
            position = G.play_grey_power(game_state, data, self.actual_card_played, suspect_number, scream_number)
            print(position)
            return position

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
            res, self.actual_card_played = mu.choose_character(data)
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

    #On touche pas
    def handle_json(self, data):
        data = json.loads(data)
        response = self.answer(data)
        # send back to server
        bytes_data = json.dumps(response).encode("utf-8")
        protocol.send_json(self.socket, bytes_data)

    #On touche pas
    def run(self):

        self.connect()

        while self.end is not True:
            received_message = protocol.receive_json(self.socket)
            if received_message:
                self.handle_json(received_message)
            else:
                print("no message, finished learning")
                self.end = True

#On touche pas
p = Player()
#On touche pas
p.run()
