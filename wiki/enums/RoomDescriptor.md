---
tags:
  - Enum
---
# Enum "RoomDescriptor"

The "RoomDescriptor" Class has separate Enums that are used for special information handling.

Even though they have different prefixes, all enums on this page are part of the "**RoomDescriptor**" enum.

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|0 |DISPLAY_NONE  |  |
|[ ](#)|1 |DISPLAY_BOX  |  |
|[ ](#)|2 |DISPLAY_LOCK  |  |
|[ ](#)|3 |DISPLAY_ICON  |  |
|[ ](#)|4 |DISPLAY_ALL  |  |

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|1 << 0 |FLAG_CLEAR  | Room is clear, don't spawn enemies when visiting |
|[ ](#)|1 << 1 |FLAG_PRESSURE_PLATES_TRIGGERED  |  All pressure plates have been triggered in this room. This won't be set if there are no trigger pressure plates in the first place. |
|[ ](#)|1 << 2 |FLAG_SACRIFICE_DONE  | Sacrifice room has paid out |
|[ ](#)|1 << 3 |FLAG_CHALLENGE_DONE  | Challenge room finished |
|[ ](#)|1 << 4 |FLAG_SURPRISE_MINIBOSS  | Load Greed/Krampus instead of the room specified by Type, Variant |
|[ ](#)|1 << 5 |FLAG_HAS_WATER  | Pits in this room contain water |
|[ ](#)|1 << 6 |FLAG_ALT_BOSS_MUSIC  | Play alternate boss music in this room |
|[ ](#)|1 << 7 |FLAG_NO_REWARD  | Don't pay out with a reward when clearing this room, used for traps that lock the player in the room when triggered |
|[ ](#)|1 << 8 |FLAG_FLOODED  | Was flooded by an item (i.e. Flush) |
|[ ](#)|1 << 9 |FLAG_PITCH_BLACK  | Complete darkness |
|[ ](#)|1 << 10 |FLAG_RED_ROOM  | Room spawned by Red Key |
|[ ](#)|1 << 11 |FLAG_DEVIL_TREASURE  | Treasure room transformed by Devil's Crown |
|[ ](#)|1 << 12 |FLAG_USE_ALTERNATE_BACKDROP  | Use an alternate backdrop (this is used by some floors such as Dross and Ashpit) |
|[ ](#)|1 << 13 |FLAG_CURSED_MIST  | Room is covered in cursed mist, player is temporarily reduced to base items and stats |
|[ ](#)|1 << 14 |FLAG_MAMA_MEGA  | Mama Mega has activated in this room |
|[ ](#)|1 << 15 |FLAG_NO_WALLS  | Don't generate walls (for Beast arena) |
|[ ](#)|1 << 16 |FLAG_ROTGUT_CLEARED  | Rotgut's heart was killed, immediately play Rotgut's death animation when reentering this room |
|[ ](#)|1 << 17 |FLAG_PORTAL_LINKED  | A portal spawned by Lil Portal now links to this room, don't create more portals that link to it |
|[ ](#)|1 << 18 |FLAG_BLUE_REDIRECT  | If walking into this room through a door, redirect to a Blue Womb room instead (this is used by Blue Key) |
