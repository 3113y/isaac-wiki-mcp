---
tags:
  - Enum
---
# Enum "GridRooms"

## Example
???- example "Example Code"
    This code checks if the player is inside an "I Am Error" room.

    ```lua
    local level = Game():GetLevel()
    local curRoom = level:GetCurrentRoomDesc()
    if curRoom.GridIndex == GridRooms.ROOM_ERROR_IDX then
      print("Success")
    end
    ```

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|-99999 |NO_ROOM_IDX  |  |
|[ ](#)|-1 |ROOM_DEVIL_IDX  |  |
|[ ](#)|-2 |ROOM_ERROR_IDX  |  |
|[ ](#)|-3 |ROOM_DEBUG_IDX  | Rooms visited via `goto` command |
|[ ](#)|-4 |ROOM_DUNGEON_IDX  | |
|[ ](#)|-5 |ROOM_BOSSRUSH_IDX  |  |
|[ ](#)|-6 |ROOM_BLACK_MARKET_IDX  |  |
|[ ](#)|-7 |ROOM_MEGA_SATAN_IDX  |  |
|[ ](#)|-8 |ROOM_BLUE_WOOM_IDX  |  |
|[ ](#)|-9 |ROOM_THE_VOID_IDX  |  |
|[ ](#)|-10 |ROOM_SECRET_EXIT_IDX  |  |
|[ ](#)|-11 |ROOM_GIDEON_DUNGEON_IDX  |  |
|[ ](#)|-12 |ROOM_GENESIS_IDX  |  |
|[ ](#)|-13 |ROOM_SECRET_SHOP_IDX  |  |
|[ ](#)|-14 |ROOM_ROTGUT_DUNGEON1_IDX  |  |
|[ ](#)|-15 |ROOM_ROTGUT_DUNGEON2_IDX  |  |
|[ ](#)|-16 |ROOM_BLUE_ROOM_IDX  |  |
|[ ](#)|-17 |ROOM_EXTRA_BOSS_IDX  |  |
|[ ](#)|-18 |ROOM_ANGEL_SHOP_IDX  | Stairway room |
|[ ](#)|-19 |ROOM_DEATHMATCH_IDX  |  |
|[ ](#)|-20 |ROOM_LIL_PORTAL_IDX  |  |
|[ ](#)|-100 |ROOM_MIRROR_IDX  | Not real room index, doors that point to this have special behavior |
|[ ](#)|-101 |ROOM_MINESHAFT_IDX  | Not real room index, doors that point to this have special behavior |
|[ ](#)|18 |NUM_OFF_GRID_ROOMS  |  |
|[ ](#)|20 |NUM_OFF_GRID_ROOMS  |  |
|[ ](#)|507 |MAX_GRID_ROOMS  |  |
|[ ](#)|525 |MAX_ROOMS  |  |
