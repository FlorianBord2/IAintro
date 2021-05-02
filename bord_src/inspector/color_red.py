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