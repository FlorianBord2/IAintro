from bord_src import my_utils as mu

def play_purple(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            print('__case__1')
            if not mu.if_color_scream(game_state['characters'], 'purple', game_state):
                print('__case__1.1')
                print('purple can"t SCREAMMMMMM !!!!!')
            else:
                print('__case__1.2')
                position = mu.move_to_empty_room(game_state, data)
                if position == -1:
                    position = mu.move_to_dark(game_state, data)
                    if position == -1:
                        position = 0
            return position
        else:
            print('__case__2')
            if mu.if_color_scream(game_state['characters'], 'purple', game_state):
                print('__case__2.1')
                return 0
            else:
                print('__case__2.2')
                position = mu.join_clean(game_state, data)
                if position == -1:
                    position = mu.join_suspect(game_state,data)
                    if position == -1:
                        position = 0
            return position
    else:
        if scream_number > (suspect_number/2):
            print('__case__3')
            if mu.if_color_scream(game_state['characters'], 'purple', game_state):
                print('__case__3.1')
                return 0
            else:
                print('__case__3.2')
                position = mu.move_to_empty_room(game_state, data)
                if position == -1:
                    position = mu.move_to_dark(game_state,data)
                    if position == -1:
                        position = mu.join_clean(game_state,data)
                        if position == -1:
                            position = 0
            return position
        else:
            print('__case__4')
            if not mu.if_color_scream(game_state['characters'], 'purple', game_state):
                print('__case__4.1')
                return 0
            else:
                print('__case__4.2')
                position = mu.join_suspect_scream(game_state,data)
                if position == -1:
                    position = 0
            return position

def play_purple_power(game_state, data):
    return 0