# red_light-green_light
> it's my first game, written for Yeelight lamp

 __This project is licensed under the MIT license__
 
 __WRITTEN ON PYTHON__
 ___
# How to install
To install this project you need Yeelight RGB smart bulb

I recommend to use phone for control this game

I use Termux

Termux
---

  If you doesn't have python in Termux, write:

    pkg install python

  If error write:

    pkg update && pkg upgrade
    
  Then repeat:

    pkg install python

  Then write:

    pip install yeelight

Open main.py and set bulb local IP address

Save code main.py on your device and open it by Python

Linux
---

Python installed on most Linux distributions and you only need to install yeelight module

    pip install yeelight

Open main.py and set bulb local IP address

Save code main.py on your PC and open it by Python

# Rules of the game
 * if light is red player must stop
 * if light is green player can go
 * it's game for 2 or above peoples
 * the player can go if the light is green and must stop, if the light is red or warden must restart game and player must go to the start position
 * warden must observe the player
 * task of the player is go to opposite side of the room

> It's like Squid Game
