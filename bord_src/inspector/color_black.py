from bord_src import my_utils as mu

def play_black(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            #Se déplace dans une salle avec nombre de suspect autour ~= (crie – (suspect/2) - 1) + lumière true
            print('__case__1')
            position = mu.most_suspect_around(game_state,data)
            if position == -1:
                position = 0
            return position
        else:
            #join empty room
            print('__case__2')
            position = mu.move_to_empty_room(game_state, data)
            if position == -1:
                position = 0
            return position
    else:
        if scream_number > (suspect_number/2):
            #Se déplace dans une salle avec nombre de suspect autour ~= (crie – (suspect/2)) + lumière true
            print('__case__3')
            position = mu.most_suspect_around(game_state, data)
            if position == -1:
                position = 0
            return position
        else:
            #Déplacer dans une salle sans suspect qui crie
            print('__case__4')
            position = mu.join_suspect_scream(game_state, data)
            if position == -1:
                position = 0
            return position

def play_black_power(game_state, data, color, suspect_number, scream_number):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            return 1
        else:
            return 0
    else:
        if scream_number > (suspect_number/2):
            return 1
        else:
            return 0