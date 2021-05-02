from bord_src import my_utils as mu

def play_purple(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            position = mu.join_someone(game_state, data)
            if position == -1:
                position = 0
            return position
        else:
            print('__case__2')
            position = mu.move_to_empty_room(game_state,data)
            if position == -1:
                position = 1
            return position
    else:
        if scream_number > (suspect_number/2):
            print('__case__3')
            position = mu.join_suspect(game_state,data)
            if position == -1:
                position = 0
            return position
        else:
            print('__case__4')
            position = mu.join_clean(game_state, data)
            if position == -1:
                position = 0
            return position

def play_purple_power(game_state, data, color, suspect_number, scream_number):
    if color['suspect'] == True:
        if scream_number > (suspect_number/2):
            if mu.if_color_scream(game_state['characters'], 'puple', game_state):
                return 1
            else:
                return 0
        else:
            if not mu.if_color_scream(game_state['characters'], 'puple', game_state):
                return 1
            else:
                return 0
    else:
        if scream_number > (suspect_number/2):
            if not mu.is_alone(color, game_state['characters']):
                return 1
            else:
                return 0
        else:
            if mu.is_alone(color, game_state['characters']):
                return 1
            else:
                return 0
    return 0

def play_purple_character(game_state, data, color, suspect_number, scream_number):
    if color['suspect'] == True:
        if scream_number > (suspect_number/2):
            #echange avec un personnage non seul
            return mu.find_color_not_alone(game_state, data, color)
        else:
            return mu.find_color_alone(game_state, data, color)
    else:
        if scream_number > (suspect_number/2):
            #echnage avec un suspect qui crie
            return mu.find_scream(game_state, data, color)
        else:
            return mu.find_cant_scream(game_state,data, color)
            #echnage avec un suspect qui ne crie pas
    return 0
