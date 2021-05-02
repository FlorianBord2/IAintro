from bord_src import my_utils as mu

def play_blue(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            #join alone or dark
            position = mu.join_alone(game_state, data)
            if position == -1:
                position = mu.move_to_dark(game_state, data)
                if position == -1:
                    return 0
            return position
        else:
            #join scream
            position = mu.join_suspect_scream(game_state, data)
            if position == -1:
                position = 0
            return position
    else:
        #join non suspect or alone or dark
        if scream_number > (suspect_number/2):
            position = mu.move_to_empty_room(game_state, data)
            if position == -1:
                position = mu.join_alone(game_state, data)
                if position == -1:
                    position = mu.move_to_dark(game_state, data)
                    if position == -1:
                        return 0
            return position
        else:
            #join scream
            position = mu.join_suspect_scream(game_state, data)
            if position == -1:
                position = 0
            return position

def play_blue_power(game_state, data):
    return 0