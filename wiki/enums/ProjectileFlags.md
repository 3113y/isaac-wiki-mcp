---
tags:
  - Enum
---
# Enum "ProjectileFlags"

???+ tip "Bitset Calculator"
    [](#)

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|1 << 0 |SMART  | follow player |
|[ ](#)|1 << 1 |EXPLODE  | explode on impact |
|[ ](#)|1 << 2 |ACID_GREEN  | acid splat on impact |
|[ ](#)|1 << 3 |GOO  | goo splat on impact |
|[ ](#)|1 << 4 |GHOST  | slide through solid entities |
|[ ](#)|1 << 5 |WIGGLE  |  |
|[ ](#)|1 << 6 |BOOMERANG  | come back |
|[ ](#)|1 << 7 |HIT_ENEMIES  | can hit enemies |
|[ ](#)|1 << 8 |ACID_RED  | blood acid |
|[ ](#)|1 << 9 |GREED  | Greed projectiles have same effect as Greed enemy's bullets. |
|[ ](#)|1 << 10 |RED_CREEP  | Bullet leaves a red creep |
|[ ](#)|1 << 11 |ORBIT_CW  | Bullet orbits a point clockwise and passes through walls similar to Tiny Planet |
|[ ](#)|1 << 12 |ORBIT_CCW  | Bullet orbits a point counter-clockwise and passes through walls similar to Tiny Planet |
|[ ](#)|1 << 13 |NO_WALL_COLLIDE  |  |
|[ ](#)|1 << 14 |CREEP_BROWN  | Bullet leaves a brown creep |
|[ ](#)|1 << 15 |FIRE  | Projectile was cast by a fireplace |
|[ ](#)|1 << 16 |BURST  | Bursts into more bullets |
|[ ](#)|1 << 17 |ANY_HEIGHT_ENTITY_HIT  | Bullets that can hit at any height |
|[ ](#)|1 << 18 |CURVE_LEFT  | Bullets curve slightly on a circular path |
|[ ](#)|1 << 19 |CURVE_RIGHT  | Bullets curve slightly on a circular path |
|[ ](#)|1 << 20 |TURN_HORIZONTAL  | Bullets turn and go horizontally and increase in speed when they pass the const static uint64_t player on either side |
|[ ](#)|1 << 21 |SINE_VELOCITY  | Bullet velocity varies over time as a function of a wave |
|[ ](#)|1 << 22 |MEGA_WIGGLE  | Like wiggle worm but the wiggling increases in amplitude over time |
|[ ](#)|1 << 23 |SAWTOOTH_WIGGLE  | Bullets travel on a sawtooth shaped path |
|[ ](#)|1 << 24 |SLOWED  |  |
|[ ](#)|1 << 25 |TRIANGLE  |  |
|[ ](#)|1 << 26 |MOVE_TO_PARENT  |  |
|[ ](#)|1 << 27 |ACCELERATE  |  |
|[ ](#)|1 << 28 |DECELERATE  |  |
|[ ](#)|1 << 29 |BURST3  |  |
|[ ](#)|1 << 30 |CONTINUUM  | Bullets reappear from the opposite side as they leave the screen |
|[ ](#)|1 << 31 |CANT_HIT_PLAYER  |  |
|[ ](#)|1 << 32 |CHANGE_FLAGS_AFTER_TIMEOUT  | "Change" flags will change the bullet's behavior after a timeout. change m_ProjectileFlags to m_TimeoutProjectileFlags. |
|[ ](#)|1 << 33 |CHANGE_VELOCITY_AFTER_TIMEOUT  | "Change" flags will change the bullet's behavior after a timeout. |
|[ ](#)|1 << 34 |STASIS  |  |
|[ ](#)|1 << 35 |FIRE_WAVE  |  |
|[ ](#)|1 << 36 |FIRE_WAVE_X  |  |
|[ ](#)|1 << 37 |ACCELERATE_EX  |  |
|[ ](#)|1 << 38 |BURST8  |  |
|[ ](#)|1 << 39 |FIRE_SPAWN  |  |
|[ ](#)|1 << 40 |ANTI_GRAVITY  |  |
|[ ](#)|1 << 41 |TRACTOR_BEAM  |  |
|[ ](#)|1 << 42 |BOUNCE  |  |
|[ ](#)|1 << 43 |BOUNCE_FLOOR  |  |
|[ ](#)|1 << 44 |SHIELDED  |  |
|[ ](#)|1 << 45 |BLUE_FIRE_SPAWN  |  |
|[ ](#)|1 << 46 |LASER_SHOT  |  |
|[ ](#)|1 << 47 |GODHEAD  |  |
|[ ](#)|1 << 48 |SMART_PERFECT  |  |
|[ ](#)|1 << 49 |BURSTSPLIT  |  |
|[ ](#)|1 << 50 |WIGGLE_ROTGUT  |  |
|[ ](#)|1 << 51 |FREEZE  |  |
|[ ](#)|1 << 52 |ACCELERATE_TO_POSITION  |  |
|[ ](#)|1 << 53 |BROCCOLI  |  |
|[ ](#)|1 << 54 |BACKSPLIT  |  |
|[ ](#)|1 << 55 |SIDEWAVE  |  |
|[ ](#)|1 << 56 |ORBIT_PARENT  |  |
|[ ](#)|1 << 57 |FADEOUT  |
