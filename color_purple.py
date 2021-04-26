import my_utils as mu

def play_purple(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            print('__case__1')
            if mu.if_color_scream(game_state['characters'], 'purple', game_state):
                print('__case__1.1')
                print('purple can SCREAMMMMMM !!!!!')
            else:
                print('__case__1.2')
                print('Purple can"t scream .....')
        else:
            print('__case__2')
            return position
    else:
        if scream_number > (suspect_number/2):
            print('__case__3')
            return position
        else:
            print('__case__4')
            return position

def play_purple_power(game_state, data):
    return 0