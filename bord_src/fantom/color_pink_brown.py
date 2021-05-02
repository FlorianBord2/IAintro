from bord_src import my_utils as mu

def play_pink_brown(suspect_number, scream_number, game_state, actual_card_played, data):
    if actual_card_played['suspect'] == True:
        if scream_number > (suspect_number/2):
            #move to empty room or dark room
            print('___case___1')
            position = mu.move_to_empty_room(game_state, data)
            if position == -1:
                position = mu.move_to_dark(game_state, data)
                if position == -1:
                    position = 0
            return position
        else:
            #join someone suspect qui ne crie pas
            print('___case___2')
            position = mu.join_suspect_scream(game_state, data)
            if position == -1:
                position = 0
            return position
    else:
        if scream_number > (suspect_number/2):
            #déplacer dans une salle avec un personnage non suspect ou seul
            print('___case___3')
            print("Data contient ", data)
            position = mu.join_clean_alone(game_state, data)
            if position == -1:
                position = mu.join_alone(game_state, data)
                if position == -1:
                    position = 0
            return position
        else:
            #join someone suspect
            print('___case___4')
            print("Data contient ", data)
            position = mu.join_suspect_scream(game_state, data)
            if position == -1:
                position = 0
            return position