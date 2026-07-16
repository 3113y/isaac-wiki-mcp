---
tags:
  - Enum
---
# Enum "EntityGridCollisionClass"
|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|0 |GRIDCOLL_NONE  |  |
|[ ](#)|1 |GRIDCOLL_WALLS_X  | only collide with vertical walls |
|[ ](#)|2 |GRIDCOLL_WALLS_Y  | only collide with horizontal walls |
|[ ](#)|3 |GRIDCOLL_WALLS  | only collide with walls |
|[ ](#)|4 |GRIDCOLL_BULLET  | detect collision with solids (no pits), don't correct position |
|[ ](#)|5 |GRIDCOLL_GROUND  | collide with all grid entities (rocks, pits, ..), correct position |
|[ ](#)|6 |GRIDCOLL_NOPITS  | collide with all grid entities except pits and correct position |
|[ ](#)|7 |GRIDCOLL_PITSONLY  | moving inside a pit, collide with everything else, correct position |