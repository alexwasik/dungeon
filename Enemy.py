import random
import config
import Controls
import numpy as np


def populateBaddies():
    numBaddies = random.randint(1, 4)
    print('numBaddies', numBaddies)
    numArrays = len(config.myarr)

    for i in range(numBaddies):
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
        elif i == 3:
            config.baddie2["position"]["x"] = globals()['r%s' % i]
            config.baddie2["position"]["y"] = globals()['randIndex%s' % i]


def checkEnemy():
    if (config.nextTile == '@'):
        # refactor to use globals
        baddie0Position = []
        baddie1Position = []
        baddie2Position = []
        baddie3Position = []
        for _, value in config.baddie0["position"].items():
            baddie0Position.append(value)
        for _, value in config.baddie1["position"].items():
            baddie1Position.append(value)
        for _, value in config.baddie2["position"].items():
            baddie2Position.append(value)
        for _, value in config.baddie2["position"].items():
            baddie3Position.append(value)

        if (np.array_equal(baddie0Position, config.nextPosition)):
            Controls.attack(config.baddie0)
        elif (np.array_equal(baddie1Position, config.nextPosition)):
            Controls.attack(config.baddie1)
        elif (np.array_equal(baddie2Position, config.nextPosition)):
            Controls.attack(config.baddie2)
        elif (np.array_equal(baddie3Position, config.nextPosition)):
            Controls.attack(config.baddie3)
