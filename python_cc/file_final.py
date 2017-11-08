# final program
import json

def get_stored():
    file_json = ('your_num.json')
    try:
        with open(file_json) as f_obj:
            user_num = json.load(f_obj)
    except:
        return None
    else:
        return user_num



def new_num():
    user_num = input ('Plase add your favourite number: ')
    file_json = ('your_num.json')
    with open(file_json, 'w') as f:
        json.dump(user_num, f) 
    return user_num


def rem_num():
    user_num = get_stored()
    if user_num:
        print ('We now your favourite number is ', user_num)
    else:
        user_num = new_num()
        print('Your favourite number is stored as ', user_num)


rem_num() 
        
