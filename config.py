import json
f = open('weapons.json')
weapon_data = json.load(f)

# turtle settings
bgcolor = 'black'

# app vars
myarr = []
col = 1
row = 1
nextTile = 0
nextPosition = [0, 0]
attackState = 'peaceful'

# baddies
baddie1 = {
    "type": "baddie",
    "name": "Baddie 1",
    "hp": 5,
    "position": {
        "x": 0,
        "y": 0
    },
}
baddie2 = {
    "type": "baddie",
    "name": "Baddie 2",
    "hp": 6,
    "position": {
        "x": 0,
        "y": 0
    },
}

# player

player = {
    "type": "player",
    "name": "Player 1",
    "hp": 100,
    "position": {
        "x": 0,
        "y": 0
    },
    "weapon": {
        'name': weapon_data['fists']['name'],
        'damage': weapon_data['fists']['damage'],
    }
}
