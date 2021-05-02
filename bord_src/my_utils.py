passages = [{1, 4}, {0, 2}, {1, 3}, {2, 7}, {0, 5, 8},
            {4, 6}, {5, 7}, {3, 6, 9}, {4, 9}, {7, 8}]
passages_map = {
    0:[1,4],
    1:[2,0],
    2:[1,3],
    3:[2,7],
    4:[0,5,8],
    5:[4,6],
    6:[5,7],
    7:[3,6,9],
    8:[4,9],
    9:[7,8]
}
# ways for the pink character
pink_passages = [{1, 4}, {0, 2, 5, 7}, {1, 3, 6}, {2, 7}, {0, 5, 8, 9},
                 {4, 6, 1, 8}, {5, 7, 2, 9}, {3, 6, 9, 1}, {4, 9, 5},
                 {7, 8, 4, 6}]

#Choose the card to play
def choose_character(data, char_order, fantom):
    print('Choose character posibility :', data)
    for color in char_order:
        i = 0
        for each in data:
            if each['color'] == fantom:
                return i, each
            if (each['color'] == color):
                return i, each
            i = i + 1

#Is the color alone in room ?
def is_alone(color, card):
    for each in card:
        if each['position'] == color['position'] and each['color'] != color['color']:
            return False
    return True

def is_alone_or_dark(color, card, game_state):
    dark = game_state['shadow']
    for each in card:
        if each['position'] == color['position'] and each['color'] != color['color']:
            if color['position'] == dark:
                return True
            else:
                return False
    return True

#How many people are able to scream
def scream_number(data):
    scream_number = 0
    dark = data['shadow']
    card = data['characters']
    for color in card:
        if is_alone(color, card) == True and color['suspect'] == True:
            scream_number = scream_number + 1
        elif color['suspect'] == True and color['position'] == dark:
            scream_number = scream_number + 1
    return scream_number

#How many suspect still in the game
def suspect_number(data):
    suspects = 0
    for each in data['characters']:
        if each['suspect'] is True:
            suspects = suspects + 1
    return suspects

#move to empty room
def move_to_empty_room(game_state, data):
    for room in data:
        if room_is_empty(room, game_state):
            print(room," is an empty room")
            return room
    print('All near room are occuped, move to :', data[0],'\n')
    return -1

#Find a room with nb suspect
def join_nb_suspect(game_state, data, nb):
    for room in data:
        sus_in_room = 0
        for color in game_state['characters']:
            if color['position'] == room and color['suspect'] == True:
                sus_in_room = sus_in_room + 1
        if sus_in_room >= nb:
            print('We found ',sus_in_room, ' in room ', room)
            return room
    print('we didint found a room with ',nb,' suspect inside\n')
    return -1


#Join suspect
def join_suspect(game_state, data):
    for room in data:
        if suspect_inside(room, game_state):
            print('Suspect found in room ', room, '\n')
            return room
    print('No suspect found, go to :', data[0],'\n')
    return data[0]

#Join suspect
def join_suspect_scream(game_state, data):
    for room in data:
        if suspect_inside_alone(room, game_state):
            return room
    print('No alone suspect found\n')
    return -1

#Join suspect qui ne crei pas
def join_suspect_not_scream(game_state, data):
    for room in data:
        if not suspect_inside_alone(room, game_state):
            return room
    print('No screamer suspect found\n')
    return -1

#Join clean
def join_clean(game_state, data):
    for room in data:
        if not suspect_inside(room, game_state):
            print('Clean found in room ', room, '\n')
            return room
    print('No clean found\n')
    return -1

#join someone
def join_someone(game_state, data):
    for room in data:
        for color in game_state['characters']:
            if color['position'] == room :
                return room
    print('Nobody nearby\n')
    return -1

#Join clean alone
def join_clean_alone(game_state, data):
    card = game_state['characters']
    for room in data:
        i = 0
        for each in card:
            if each['position'] == room and each['suspect'] == False:
                i = i + 1
            if each['position'] == room and each['suspect'] == True:
                i = i + 2
        if i == 1:
            return room
    return -1

def join_alone(game_state, data):
    card = game_state['characters']
    for room in data:
        i = 0
        for each in card:
            if each['position'] == room:
                i = i + 1
        if i == 1:
            return room
    return -1

def clean_inside(room, game_state):
    for color in game_state['characters']:
        if color['position'] == room and color['suspect'] == False:
            return True
    return False

def suspect_inside_alone(room, game_state):
    card = game_state['characters']
    for color in game_state['characters']:
        if color['position'] == room and color['suspect'] == True and is_alone_or_dark(color, card, game_state):
            return True
    return False

def suspect_inside(room, game_state):
    for color in game_state['characters']:
        if color['position'] == room and color['suspect'] == True:
            return True
    return False

def room_is_empty(room, game_state):
    #print(game_state)
    for color in game_state['characters']:
        if color['position'] == room:
            return False
    return True

#if color scream:
def if_color_scream(characters, target, game_state):
    #et etre suspect
    for each in characters:
        if each['color'] == target:
            color = each
            if color['suspect'] == False:
                return False
            #dans le noir
            if color['position'] == game_state['shadow']:
                return True
            #Seul ?
            for each in game_state['characters']:
                if each['position'] == color['position']:
                    return False
            return True
    
#find most suspec room
def find_most_suspect_room(rooms, game_state):
    last_suspect = 0
    most_suspect_room = None
    for room in rooms:
        suspect_nb = 0
        for color in game_state['characters']:
            if color['position'] == room and color['suspect'] == True:
                suspect_nb = suspect_nb + 1
        if suspect_nb > last_suspect:
            last_suspect = suspect_nb
            most_suspect_room = room
    print("The most suspect room is ",most_suspect_room, " with ", last_suspect, " suspect inside")
    return most_suspect_room

#Join the dark room:
def move_to_dark(game_state, data):
    dark = game_state['shadow']
    if dark in data:
        return dark
    return -1

#trouve la sale avec le plus grand nombre de suspect autour
def most_suspect_around(game_state, data):
    most_suspect_around_saved = None
    last_nb_suspect = 0
    for room in data:
        nb_suspect = 0
        for map_room in passages_map[room]:
            for color in game_state['characters']:
                if color['position'] == map_room and color['suspect'] == True:
                    nb_suspect = nb_suspect + 1
        if nb_suspect > last_nb_suspect:
            last_nb_suspect = nb_suspect
            most_suspect_around_saved = room
    print('DANS most SUSPECT ON TROUVE ROOM :',most_suspect_around_saved)
    return most_suspect_around_saved

#trouve la sale avec le moins grand nombre de suspect autour
def less_suspect_around(game_state, data):
    most_suspect_around_saved = None
    last_nb_suspect = 100
    for room in data:
        nb_suspect = 0
        for map_room in passages_map[room]:
            for color in game_state['characters']:
                if color['position'] == map_room and color['suspect'] == True:
                    nb_suspect = nb_suspect + 1
        if nb_suspect < last_nb_suspect:
            last_nb_suspect = nb_suspect
            most_suspect_around_saved = room
    print('DANS LESS SUSPECT ON TROUVE ROOM :',most_suspect_around_saved)
    return most_suspect_around_saved

#Se déplacer dans une salle avec le nombre de suspect dans la salle ~= (crie – (suspect/2) – 1) 
def join_special_suspect(game_state, data, scream_number, suspect_number, value):
    goal = (suspect_number/2) - scream_number + value
    for room in data:
        #cb de suspect 
        nb_suspect = 0
        for color in game_state['characters']:
                if color['position'] == room and color['suspect'] == True:
                    nb_suspect = nb_suspect + 1
        if nb_suspect == goal:
            return room
    return -1

#trouver une couleur non seul:
def find_color_not_alone(game_state, data, color):
    card = game_state['characters']
    for each in card:
        if each['position'] == color['position'] and each['color'] != color['color']:
                return each['color']
    return -1


def find_color_alone(game_state, data, color):
    card = game_state['characters']
    for each in card:
        if is_alone(each, card):
            return each['color']
    return -1

def find_scream(game_state, data, color):
    card = game_state['characters']
    for each in card:
        if is_alone(each, card) == True:
            if each['suspect'] == True and each['color'] != color['color']:
                return each['color']
    return -1

def find_cant_scream(game_state, data,color):
    card = game_state['characters']
    for each in card:
        if is_alone(each, card) == False:
            if each['suspect'] == True and each['color'] != color['color']:
                return each['color']
    return -1

def find_near_room(color):
    position = color['position']
    posibility = []
    for doors in passages:
        if position in doors:
            for room in doors:
                if room != position and room not in posibility:
                    posibility.append(room)
    return posibility


def print_map( map):
    i = 0
    for each in map['characters']:
        print(i,each['color'], each['position'], "suspect:", each['suspect'])
        i = i + 1

# data = {'question type': 'select character',
# 'data': [
#     {'color': 'brown', 'suspect': False, 'position': 8, 'power': False},
#     {'color': 'blue', 'suspect': True, 'position': 8, 'power': False},
#     {'color': 'white', 'suspect': True, 'position': 1, 'power': False}],
#     'game state':
#     {'position_carlotta': 6, 'exit': 22, 'num_tour': 1, 'shadow': 1,
#      'blocked': [4, 8], 
#      'characters': [{'color': 'pink', 'suspect': True, 'position': 3, 'power': False},
#      {'color': 'white', 'suspect': True, 'position': 1, 'power': False},
#      {'color': 'purple', 'suspect': True, 'position': 2, 'power': False},
#      {'color': 'blue', 'suspect': True, 'position': 8, 'power': False},
#      {'color': 'brown', 'suspect': True, 'position': 8, 'power': False},
#      {'color': 'grey', 'suspect': True, 'position': 1, 'power': False},
#      {'color': 'red', 'suspect': True, 'position': 0, 'power': False},
#      {'color': 'black', 'suspect': True, 'position': 0, 'power': False}],
#      'character_cards': [{'color': 'black', 'suspect': True, 'position': 0, 'power': False},
#      {'color': 'brown', 'suspect': True, 'position': 8, 'power': False},
#      {'color': 'blue', 'suspect': True, 'position': 8, 'power': False},
#      {'color': 'white', 'suspect': True, 'position': 1, 'power': False},
#      {'color': 'red', 'suspect': True, 'position': 0, 'power': False},
#      {'color': 'purple', 'suspect': True, 'position': 2, 'power': False},
#      {'color': 'pink', 'suspect': True, 'position': 3, 'power': False},
#      {'color': 'grey', 'suspect': True, 'position': 1, 'power': False}],
#      'active character_cards': [
#          {'color': 'brown', 'suspect': True, 'position': 8, 'power': False},
#          {'color': 'blue', 'suspect': True, 'position': 8, 'power': False},
#          {'color': 'white', 'suspect': True, 'position': 1, 'power': False}], 
#      'fantom': 'white'}}
# print('Dark room;', data['game state']['shadow'])
# game_state = data["game state"]
# data = data['data']

# card = game_state['characters']

# color = card[0]

# print_map(game_state)
# for each in card:
#     print('alone ',is_alone(each, card))

# data = [8,4]
# print(data)
#print('scream number :',scream_number(game_state))
#print('suspect number  :',suspect_number(game_state))
#print(move_to_empty_room(game_state, [1,4,6]))
#print(join_nb_suspect(game_state, data, 1))
#print(move_to_empty_room(game_state, data))
#print(join_suspect(game_state, data))
#print(join_suspect_scream(game_state,data))
