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


def show_end_screen():
    print('Goodbye.')


def get_location_by_id(data, loc_id):
    locations = data['locations']

    for location in locations:
        if location['id'] == loc_id:
            return location


def show_description(location):
    print(location['description'])
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
    room_commands = list(options.keys())
    anytime_commands = ['inventory']

    # if 'item' in location:
    #     item = location['item']
    #     commands += list(item.keys())

    while True:
        command = input('What do you want to do? ')
        command = filter_command(command)
        
        if command in  room_commands or command in anytime_commands:
            return command
        else:
            print('I don\'t understand. Please try something else.')


def process_command(location, command):
    options = location['options']
    return options[command]


def show_inventory(items):
    if len(items) > 0:
        item_str = ', '.join(items)
        print(f'You have the following items: {item_str}.')


def play(data):
    current_loc_id = data['start']
    items = []

    while current_loc_id != 'Quit': # Need a better idea here
        location = get_location_by_id(data, current_loc_id)
        show_description(location)
        command = get_command(location)

        if command == 'inventory':
            show_inventory(items)
        else:
            current_loc_id = process_command(location, command)

        if 'get' in command:
            location['description'] = location['description-item-taken']
            item = location['options'][command]
            items.append(item)
            del location['options'][command]
        elif 'description-visited' in location:
            location['description'] = location['description-visited']

        
# Let's do this!
path = 'games/spooky_mansion.json'
data = load_game(path)

show_title_screen(data)
play(data) 
show_end_screen()
