from bord_src import my_utils as mu

def play_red(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            #Join empty room
            print('__case__1')
            position = mu.move_to_empty_room(game_state, data)
            if position == -1:
                #move dans unesalle avec au moins 2 suspect
                position = mu.move_to_dark(game_state, data)
                if position == -1:
                    position = 0
            return position
        else:
            #join un suspect qui ne cri pas
            print('__case__2')
            position = mu.join_suspect_not_scream(game_state, data)
            if position == -1:
                position = 0
            return position
    else:
        if scream_number > (suspect_number/2):
            #Join clean room
            print('__case__3')
            position = mu.join_clean(game_state, data)
            if position == -1:
                position = 0
            return position
        else:
            #Join suspect color
            print('__case__4')
            position = mu.join_suspect_scream(game_state, data)
            if position == -1:
                position = 0
            return position

def play_red_power(game_state, data, color, suspect_number, scream_number):
    if color['suspect'] == True:
        if scream_number > (suspect_number/2):
            #si suspect activer dans la sale avec le plus desuspect
            position = mu.find_most_suspect_room(data,game_state)
            return position
        else:
            #Activer dans une salle avec personne ou des personnages non suspects
            position = mu.move_to_empty_room(game_state, data)
            return position
    else:
        if scream_number > (suspect_number/2):
            position = mu.find_most_suspect_room(data,game_state)
            return position
        else:
            position = mu.move_to_empty_room(game_state, data)
            return position
    return 0