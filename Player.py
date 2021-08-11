import config


def printPlayerData():
    return (
        config.player["name"] + "\n" +
        "HP: " + str(config.player["hp"]) + "\n" +
        "Weapon: " + config.player["weapon"]["name"] + "\n" +
        "Damage: " + str(config.player["weapon"]["damage"]) + "\n" +
        "Gold: " + str(config.gold) + "\n"
    )


def getInventory():
    return config.gold
