# Space-Invaders
Modifying the classic arcade game, Space Invaders, to get a better grasp of the library "Pygame."

## Game Mechanics & Demo

![Space Invaders Demo GIF](https://media.giphy.com/media/twfPUhE4wvRZM3fKS3/giphy.gif)

**Movement Controls**

The player controls the spaceship (displayed below) using these controls:

<img align="left" width="125" height="125" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_ship_yellow.png">

```bash
a: right
w: forwards/up
s: backwards/down
d: left

space: shoot a laser
```

**Damage**

If lasers (listed below) hit the spaceship, it loses part of its healthbar.

<!--Laser PNG Display-->

<br clear="left"/>
<img align="left" width="100" height="100" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_laser_blue.png">
<img align="left" width="100" height="100" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_laser_green.png">
<img align="left" width="100" height="100" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_laser_red.png">
<br clear="left"/>

*OR*

Players could crash the spaceship into the aliens (listed below) to sacrifice health but get rid of the alien in return.

<!--Alien PNG Display-->

<br clear="left"/>
<img align="left" width="100" height="100" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_ship_blue_small.png">
<img align="left" width="100" height="100" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_ship_green_small.png">
<img align="left" width="100" height="100" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_ship_red_small.png">
<br clear="left"/>

<!--
<img align="left" width="100" height="100" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_laser_blue.png">
<img align="left" width="100" height="100" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_ship_blue_small.png">
<img align="left" width="100" height="100" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_laser_yellow.png">
<img align="left" width="100" height="100" src="https://github.com/HermesBonilla/Space-Invaders/blob/master/assets/pixel_ship_yellow.png">
-->

<br clear="left"/>

**How to Lose**

Game Over occurs when *either* :

- Health bar turns completely red (ran out of health)
- Lives ran out (aliens went past you)

## Installation

```bash
git clone https://github.com/HermesBonilla/Space-Invaders.git
```

or

Fork the repository by [pressing the button](https://github.com/HermesBonilla/Space-Invaders/fork) on the top left of the repository.

## Acknowledgments
I'd like to give special thanks to [Tech With Tim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg) and his [PyGame tutorial](https://youtu.be/Q-__8Xw9KTM).
