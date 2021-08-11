import random
import config
import Controls
import numpy as np


def populateBaddies():
    numBaddies = random.randint(1, 3)
    print('numBaddies', numBaddies)
    numArrays = len(config.myarr)

    for i in range(numBaddies):
        print('i', i)
        globals()['r%s' % i] = random.randint(1, numArrays - 2)
        globals()['indices%s' % i] = [h for h, x in enumerate(
            config.myarr[globals()['r%s' % i]]) if x == "0"]
        globals()['randIndex%s' % i] = random.choice(
            globals()['indices%s' % i])
        config.myarr[globals()['r%s' % i]][globals()['randIndex%s' % i]] = "@"
        if i == 0:
            config.baddie0["position"]["x"] = globals()['r%s' % i]
            config.baddie0["position"]["y"] = globals()['randIndex%s' % i]
        elif i == 1:
            config.baddie1["position"]["x"] = globals()['r%s' % i]
            config.baddie1["position"]["y"] = globals()['randIndex%s' % i]
        elif i == 2:
            config.baddie2["position"]["x"] = globals()['r%s' % i]
            config.baddie2["position"]["y"] = globals()['randIndex%s' % i]


def checkEnemy():
    if (config.nextTile == '@'):
        print('baddie ahead')
        baddie0Position = []
        baddie1Position = []
        baddie2Position = []
        for key, value in config.baddie0["position"].items():
            print(key, value)
            baddie0Position.append(value)
        print('baddie0', baddie0Position)
        for key, value in config.baddie1["position"].items():
            print(key, value)
            baddie1Position.append(value)
        print('baddie1', baddie1Position)
        for key, value in config.baddie2["position"].items():
            print(key, value)
            baddie2Position.append(value)
        print('baddie2', baddie2Position)

        if (np.array_equal(baddie0Position, config.nextPosition)):
            print('baddie in position')
            Controls.attack(config.baddie0)
        elif (np.array_equal(baddie1Position, config.nextPosition)):
            print('baddie in position')
            Controls.attack(config.baddie1)
        elif (np.array_equal(baddie2Position, config.nextPosition)):
            print('baddie in position')
            Controls.attack(config.baddie2)
