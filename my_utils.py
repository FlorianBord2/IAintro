passages = [{1, 4}, {0, 2}, {1, 3}, {2, 7}, {0, 5, 8},
            {4, 6}, {5, 7}, {3, 6, 9}, {4, 9}, {7, 8}]
# ways for the pink character
pink_passages = [{1, 4}, {0, 2, 5, 7}, {1, 3, 6}, {2, 7}, {0, 5, 8, 9},
                 {4, 6, 1, 8}, {5, 7, 2, 9}, {3, 6, 9, 1}, {4, 9, 5},
                 {7, 8, 4, 6}]

#move to empty room
def move_to_empty_room(game_state, data):
    #near_room = find_near_room(color)
    #print (color['color'], ' is in room ', color['position'], ' and he can go to ', near_room, '\n')
    for room in data:
        if room_is_empty(room, game_state):
            #print('Move to ', room, '\n')
            return room
    #print('All near room are occuped, move to :', data[0],'\n')
    return data[0]

#Join suspect
def join_suspect(color, game_state, data):
    for room in data:
        if suspect_inside(room, game_state):
            print('Suspect found in room ', room, '\n')
            return room
    print('No suspect found, go to :', data[0],'\n')
    return data[0]

#Join clean
def join_clean(color, game_state, data):
    for room in data:
        if suspect_inside(room, game_state):
            print('Clean found in room ', room, '\n')
            return room
    print('No clean found, go to :', data[0],'\n')
    return data[0]

def clean_inside(room, game_state):
    for color in game_state['characters']:
        if color['position'] == room and color['suspect'] == False:
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
    print("we found ",last_suspect, " in room ", most_suspect_room)
    return most_suspect_room









def find_near_room(color):
    position = color['position']
    posibility = []
    for doors in passages:
        if position in doors:
            for room in doors:
                if room != position and room not in posibility:
                    posibility.append(room)
    return posibility