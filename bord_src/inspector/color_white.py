from bord_src import my_utils as mu

def play_white(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            print('__case__1')
            position = mu.join_someone(game_state, data)
            return position
        else:
            print('__case__2')
            position = mu.join_special_suspect(game_state, data)
            if position == -1:
                position = 0
            return position
    else:
        if scream_number > (suspect_number/2):
            print('__case__3')
            position = mu.join_suspect_scream(game_state, data)
            return position
        else:
            print('__case__4')
            position = mu.join_special_suspect(game_state, data)
            if position == -1:
                position = 0
            return position

def play_white_power(game_state, data):
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            print('__case__1')
            return 0
        else:
            print('__case__2')
            return 1
    else:
        if scream_number > (suspect_number/2):
            print('__case__3')
            return 0
        else:
            print('__case__4')
           return 1