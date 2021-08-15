import config


def printPlayerData():
    return (
        config.player["name"] + "\n" +
        "HP: " + str(config.player["hp"]) + "\n" +
        "Weapon: " + config.player["weapon"]["name"] + "\n\t" +
        "Damage: " + str(config.player["weapon"]["damage"]) + "\n\t" +
        "Condition: " + str(config.player["weapon"]["condition"]) + "\n" +
        "Gold: " + str(config.gold) + "\n"
    )


def getInventory():
    return config.gold
