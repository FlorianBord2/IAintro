from bord_src import my_utils as mu

def play_white(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            position = mu.most_suspect_around(game_state, data)
            return position
        else:
            position = mu.join_suspect(game_state, data)
            if position == -1:
                position = 0
            return position
    else:
        if scream_number > (suspect_number/2):
            print('__case__3')
            position = mu.most_suspect_around(game_state, data)
            return position
        else:
            print('__case__4')
            position = mu.move_to_dark(game_state, data)
            if position == -1:
                position = mu.join_someone(game_state, data)
                if position == -1:
                    position = 0
            return position

def play_white_power(game_state, data):
    return 0
    #  if actual_card_played['suspect'] == True:
    #     if scream_number > (suspect_number/2):
    #         print('__case__1')
    #         return position
    #     else:
    #         print('__case__2')
    #         return position
    # else:
    #     if scream_number > (suspect_number/2):
    #         print('__case__3')
    #     else:
    #         print('__case__4')
    #         return position
    # return 0