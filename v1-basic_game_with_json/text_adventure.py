import json

 
def load_game(game_data):
    with open(game_data, 'r') as f:
        data = json.load(f)

    return data


def show_title_screen(data):
    title = data['title']
    author = data['author']

    print(title)
    print('  by ' + author)
    print()
    input('Press ENTER to begin...')
    print()


def get_location_by_id(data, num):
    locations = data['locations']
    
    for location in data['locations']:
        if location['id'] == num:
            return location


def show_description(location):
    print(location['description'])
    print()


def show_menu(location):
    options = location['options']
    choices = list(options.keys())
    
    print('You have the following options:')
    for i, choice in enumerate(choices, start=1):
        print(f'  {i}. {choice}')

    print()
    
def get_decision(location):
    options = location['options']
    destinations = list(options.values())

    choice = input('What do you want to do? ')
    print()
    
    index = int(choice) - 1
    
    return destinations[index]


def show_end_screen():
    print('Goodbye.')


# Let's do this!
path = 'games/spooky_mansion.json'

data = load_game(path)

show_title_screen(data)

current_loc_id = data['start']

while current_loc_id != -1:
    location = get_location_by_id(data, current_loc_id)
    
    show_description(location)
    show_menu(location)
    current_loc_id = get_decision(location)
        
show_end_screen()
