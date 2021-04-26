import my_utils as mu

def play_grey(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            #Join empty room
            print('__case__1')
            position = mu.move_to_empty_room(game_state, data)
            return position
        else:
            #join suspect color
            print('__case__2')
            position = mu.join_suspect(actual_card_played, game_state, data)
            return position
    else:
        if scream_number > (suspect_number/2):
            #Join clean room
            print('__case__3')
            position = mu.join_clean(actual_card_played, game_state, data)
            return position
        else:
            #Join suspect color
            print('__case__4')
            position = mu.join_suspect(actual_card_played, game_state, data)
            return position

def play_grey_power(game_state, data, color, suspect_number, scream_number):
    if color['suspect'] == True:
        if scream_number > (suspect_number/2):
            #si suspect activer dans la sale avec le plus desuspect
            position = mu.find_most_suspect_room(data,game_state)
            return position
        else:
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