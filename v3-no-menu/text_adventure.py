import json


def load_game(game_data):
    with open(game_data, 'r') as f:
        data = json.load(f)

    return data


def show_title_screen(data):
    title = data['title']
    author = data['author']
    year = str(data['year'])
    
    print(title)
    print('  by ' + author + ', ©' + year)
    print()
    input('Press ENTER to begin...')
    print()


def get_location_by_id(data, loc_id):
    locations = data['locations']
    
    for location in locations:
        if location['id'] == loc_id:
            return location


def show_description(location, visited):
    first_time_in_location = location['id'] not in visited
    no_second_description = 'description2' not in location
    
    if first_time_in_location or no_second_description:
        print(location['description1'])
    else:
        print(location['description2'])

    print()


def filter_command(text):
    common_words = ['a', 'an', 'the', 'on', 'in', 'through', 'at', 'to']

    text = text.lower()
    words = text.split()

    filtered_words = [w for w in words if w not in common_words]
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text


def get_command(location):
    options = location['options']
    commands = list(options.keys())
    destinations = list(options.values())

    while True:
        command = input('What do you want to do? ')
        command = filter_command(command)
        
        if command in commands:
            return options[command]
        else:
            print('I don\'t understand. Please try something else.')


def show_end_screen():
    print('Goodbye.')


# Let's do this!
path = 'games/spooky_mansion.json'
data = load_game(path)

show_title_screen(data)

current_loc_id = data['start']
visited = [] # Bug! - Won't reset on new game.

while current_loc_id != 'Quit':
    location = get_location_by_id(data, current_loc_id)
    
    show_description(location, visited)
    visited.append(current_loc_id)
    current_loc_id = get_command(location)
           
show_end_screen()
