import json
f = open('weapons.json')
weapon_data = json.load(f)

# turtle settings
bgcolor = '#a9adb6'

# app vars
myarr = []
col = 1
row = 1
nextTile = 0
nextPosition = [0, 0]
attackState = 'peaceful'

# baddies
baddie0 = {
    "type": "baddie",
    "name": "Baddie 1",
    "hp": 5,
    "position": {
        "x": 0,
        "y": 0
    },
}
baddie1 = {
    "type": "baddie",
    "name": "Baddie 2",
    "hp": 6,
    "position": {
        "x": 0,
        "y": 0
    },
}
baddie2 = {
    "type": "baddie",
    "name": "Baddie 3",
    "hp": 7,
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
        'name': weapon_data['brass_knuckles']['name'],
        'damage': weapon_data['brass_knuckles']['damage'],
    }
}
