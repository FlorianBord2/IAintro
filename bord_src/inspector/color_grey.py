from bord_src import my_utils as mu

def play_grey(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            #Join someone
            print('__case__1')
            position = mu.join_someone(game_state,data)
            if position == -1:
                position = 0
            return position
        else:
            #join empty
            print('__case__2')
            position = mu.move_to_empty_room(game_state,data)
            if position == -1:
                position = 0
            return position
    else:
        if scream_number > (suspect_number/2):
            #Join clean room
            print('__case__3')
            position = mu.join_someone(game_state, data)
            if position == -1:
                position = 0
            return position
        else:
            #Join suspect color
            print('__case__4')
            position = mu.move_to_empty_room(game_state, data)
            if position == -1:
                position = 0
            return position

def play_grey_power(game_state, data, color, suspect_number, scream_number):
    if color['suspect'] == True:
        if scream_number > (suspect_number/2):
            #activer dans une salle clean ou une salle vide
            position = mu.join_clean(game_state,data)
            if position == -1:
                position = mu.move_to_empty_room(game_state,data)
            return position
        else:
            #Activer dans une salle avec personne ou des personnages non suspects
            position = mu.join_special_suspect(game_state, data, scream_number, suspect_number,0)
            if position == -1:
                position = mu.move_to_empty_room(game_state, data)
                if position == -1:
                    position = 0
            return position
    else:
        if scream_number > (suspect_number/2):
            #Activer dans une salle sans suspect ou une salle vide
            position = mu.join_clean(game_state, data)
            if position == -1:
                position = mu.move_to_empty_room(game_state, data)
            return position
        else:
            #Activer dans une salle avec personne ou des personnages non suspects
            position = mu.join_special_suspect(game_state, data, scream_number, suspect_number,0)
            if position == -1:
                position = mu.move_to_empty_room(game_state, data)
                if position == -1:
                    position = 0
            return position
    return 0