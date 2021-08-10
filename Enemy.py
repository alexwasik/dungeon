import random
import config
import Controls
import Functions
import numpy as np


def populateBaddies():
    numBaddies = random.randint(1, 3)
    print('numBaddies', numBaddies)
    numArrays = len(config.myarr)

    r1 = random.randint(1, numArrays-2)
    r2 = random.randint(1, numArrays-2)

    indices1 = [i for i, x in enumerate(config.myarr[r1]) if x == "0"]
    indices2 = [i for i, x in enumerate(config.myarr[r2]) if x == "0"]
    randIndex1 = random.choice(indices1)
    randIndex2 = random.choice(indices2)

    config.myarr[r1][randIndex1] = "@"
    config.baddie1["position"]["x"] = r1
    config.baddie1["position"]["y"] = randIndex1

    config.myarr[r2][randIndex2] = "@"
    config.baddie2["position"]["x"] = r2
    config.baddie2["position"]["y"] = randIndex2


def checkEnemy():
    if (config.nextTile == '@'):
        print('baddie ahead')
        baddie1Position = []
        baddie2Position = []
        for key, value in config.baddie1["position"].items():
            print(key, value)
            baddie1Position.append(value)
        print('config.baddie1', baddie1Position)
        for key, value in config.baddie2["position"].items():
            print(key, value)
            baddie2Position.append(value)
        print('baddie2', baddie2Position)

        if (np.array_equal(baddie1Position, config.nextPosition)):
            print('baddie in position')
            Controls.attack(config.baddie1)
        elif (np.array_equal(baddie2Position, config.nextPosition)):
            print('baddie in position')
            Controls.attack(config.baddie2)
