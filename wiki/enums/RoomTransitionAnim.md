---
tags:
  - Enum
---
# Enum "RoomTransitionAnim"
|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|0 |WALK  | Mostly when using doors. Will play the correct walk animation regardless of the direction you use, as long as the direction is in the same axis as the room you're traveling too. So if the room is on the left, it'll play the correct animation whether you use Direction.LEFT or Direction.RIGHT. If you put in the wrong direction, it'll just fade to the next room (not fade to black, just fade). If you put in Direction.NO_DIRECTION it'll play a fade to black regardless. |
|[ ](#)|1 |FADE  | Fadein/fadout used for Mom's Hand. Will play a fade to black regardless of the direction. If the direction is Direction.NO_DIRECTION the fade will be shorter. |
|[ ](#)|2 |PIXELATION  | Fade+pixelation effect used for secret item dungeon. Will play the usual pixelation regardless of the direction. |
|[ ](#)|3 |TELEPORT  | Will play the teleport animation and sound, then it'll play the walk animation using the direction you inputted. If Direction.NO_DIRECTION is used, it'll play a short fade to white instead of the walk animation. |
|[ ](#)|4 |MAZE  | For curse of the maze. Like RoomTransitionAnim.WALK but better, as it will always play the walk animation you put into it. Using Direction.NO_DIRECTION will play a short fade to black. |
|[ ](#)|5 |ANKH  | Works like RoomTransitionAnim.MAZE. |
|[ ](#)|6 |DEAD_CAT  | Works like RoomTransitionAnim.MAZE. |
|[ ](#)|7 |ONE_UP  | Works like RoomTransitionAnim.MAZE but plays the one up sound upon entering the room. |
|[ ](#)|8 |COLLAR  | Works like RoomTransitionAnim.MAZE. |
|[ ](#)|9 |JUDAS_SHADOW  | Works like RoomTransitionAnim.MAZE. |
|[ ](#)|10 |LAZARUS  | Works like RoomTransitionAnim.MAZE. |
|[ ](#)|11 |WOMB_TELEPORT  | For Ventricle razor teleport. Makes the player invisible and plays a fade to black. If used to change into the same room, the player's visibility won't be restored. If Direction.NO_DIRECTION is used, it'll play a shorter fade to black. |
|[ ](#)|12 |GLOWING_HOURGLASS  | For glowing hourglass teleport. Basically the same as using the glowing hourglass item, further testing should be done to see if there are any differences. Ignores the direction and the room index inputted. |
|[ ](#)|13 |D7  | The same as RoomTransitionAnim.TELEPORT, but on Direction.NO_DIRECTION it'll play a fade to black, instead of a fade to white. |
|[ ](#)|14 |MISSING_POSTER  | Works like RoomTransitionAnim.MAZE. |
|[ ](#)|15 |BOSS_FORCED  | No transition, goes directly to boss intro (for backasswards challenge). Plays a walk animation twice. If used with Direction.NO_DIRECTION plays a short fade to black. Doesnt even skip the boss vs screen. |
|[ ](#)|16 |PORTAL_TELEPORT  | For card reading teleport. Works like RoomTransitionAnim.WOMB_TELEPORT. |
|[ ](#)|17 |FORGOTTEN_TELEPORT  | For the Forgotten's birthright. Works like RoomTransitionAnim.FADE. |
|[ ](#)|18 |FADE_MIRROR  | Plays the mirror exit sound and a fade to white animation. If used with Direction.NO_DIRECTION, the fade to white is shorter. |
|[ ](#)|19 |MINECART  | Works like RoomTransitionAnim.FADE. |
|[ ](#)|20 |DEATH_CERTIFICATE  | The player lies down, then there's a fade to black and the player appears lying down again and gets up. Ignores the direction, but using Direction.NO_DIRECTION will make the fade shorter. The game is paused during the lying down and getting up animation. |
