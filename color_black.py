import my_utils as mu

def play_black(suspect_number, scream_number, game_state, actual_card_played, data):
    position = 0
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            #Join empty room or dark room
            print('__case__1')
            position = mu.move_to_empty_room(game_state, data)
            if position == -1:
                position = mu.move_to_dark(game_state, data)
                if position == -1:
                    position = 0
            return position
        else:
            #se deplace dans une sale avec un nombre de suspect autour le plus grand posible 
            print('__case__2')
            position = mu.most_suspect_around(game_state, data)
            return position
    else:
        if scream_number > (suspect_number/2):
            #se deplace dans une sale avec un nombre de suspect autour le plus proche de 0
            print('__case__3')
            position = mu.less_suspect_around(game_state, data)
        else:
            #se deplace dans une sale avec un nombre de suspect autour le plus grand posible
            print('__case__4')
            position = mu.most_suspect_around(game_state, data)
            return position

def play_black_power(game_state, data, color, suspect_number, scream_number):
    position = 0
    if color['suspect'] == True:
        if scream_number > (suspect_number/2):
            print('Black dont use power ')
            return 0
        else:
            print('Black use power')
            return 1
    else:
        if scream_number > (suspect_number/2):
            print('Black use power')
            return 1
        else:
            print('Black use power')
            return 1
    return 0