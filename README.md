## Very Basic 2D Dungeon Crawler Game

![alt Screenshot of Map](/images/mapdemo.png)
![alt Screenshot of Map](/images/itempickup.png)

## Description

This game is a _very_ basic 2D Dungeon Crawler built with Python and [Turtle](https://docs.python.org/3/library/turtle.html). The game includes 3 maps with randomly generated treasure and Baddies to battle and 4 different weapon types randomly dropped. Fight your way through the maps, explore new rooms and collect Gold and Weapons. **NOTE: This game is currently unfinished and may contain minor bugs or issues.**

## Install and Run

Python3 and Pipenv are required to run this game. Be sure you have python3 installed. Please check [python.org](https://www.python.org/downloads/) documentation for installation instructions.

### To install Pipenv:

```
pip install --user pipenv
```

To run, navigate to repo directory and type in your console:

```
pipenv run dungeon
```

## Controls

- Up: ↑
- Down: ↓
- Left: ←
- Right: →
- Equip: `e`

Other than _some_ confirmation boxes, this game is entirely keyboard based. Use the _Arrow Keys_ to navigate the maps, **Up, Down, Left, Right.**

The `e` key will bring up the **Inventory** dialog to select a weapon drop that has been picked up. Select your weapon and click **OK** or press **Enter** to equip.

## Known Issues

_you know... because this game is unfinished..._

- There are only 3 maps. After completing the 3rd map, the game will throw an error that there is not another map to load.
- Expanding the Game Window to full screen causes the Inventory Equip dialog to go full screen **and** will not equip weapon ¯\\_(ツ)_/¯
- Layout and formatting of dialog boxes can be hella ugly.

## Incomplete Implementations in Code

- Level change at each 100 point score intervals but there are not enough Baddies yet to change level
- Weapons have levels they are available at, but this feature has not yet been implemented.
- Many "refactor this" comments and `print` statements for debugging have been left in for future consideration.
