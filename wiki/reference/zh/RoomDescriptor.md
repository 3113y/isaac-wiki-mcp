---
tags:
  - Class
---
# Class "RoomDescriptor"

???+ info
    You can get this class by using the following functions:

    * [Level:GetCurrentRoomDesc()](Level.md#getcurrentroomdesc)
    * [Level:GetLastRoomDesc()](Level.md#getlastroomdesc)
    * [Level:GetRoomByIdx()](Level.md#getroombyidx)

    ???+ example "Example Code"
        ```lua
        local level = Game():GetLevel()
        local roomDescriptor = level:GetCurrentRoomDesc()
        ```

## Variables

### Allowed·Doors {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### DoorSet AllowedDoors  {: .copyable aria-label='Variables' }
Contains data swapped just on load (in cases like minibosses, or other such events)

???+ bug "Bug"
    This variable contains userdata and is therefore not useable.
___

<div class="rgon-extension" markdown="1">

### AllowedDoors {: aria-label='Modified Variables' }
#### DoorSet AllowedDoors [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Variables' }
现在可以正确返回值。

返回一个位掩码，表示当前启用的门槽位。

通常只有当前实际存在门时，该门才会包含在此位掩码中，即使房间允许在该槽位设置门也是如此。

???+ example "Example"
    This tests if the DoorSlot `LEFT0` is enabled.
    ```lua
    if roomDesc.AllowedDoors & (1 << DoorSlot.LEFT0) ~= 0 then
        print("Room has a door in slot LEFT0")
    end
    ```

___

## Functions

</div>

### Award·Seed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int AwardSeed  {: .copyable aria-label='Variables' }
used to spawn clear awards (normal, miniboss, boss rooms) and initialize shop items (shop, devil rooms)
___

### Challenge·Done {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean ChallengeDone  {: .copyable aria-label='Variables' }

___

### Clear {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean Clear  {: .copyable aria-label='Variables' }

___

### Clear·Count {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ClearCount  {: .copyable aria-label='Variables' }
room is clear, don't spawn enemies when visiting
___

### Data {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [RoomConfigRoom](RoomConfig_Room.md) Data  {: .copyable aria-label='Variables' }

___

### Decoration·Seed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int DecorationSeed  {: .copyable aria-label='Variables' }
used for cosmetic stuff like backdrops, room decorations, shopkeeper skins
___

### Delirium·Distance {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int DeliriumDistance  {: .copyable aria-label='Variables' }
Helper for The Void stage, holds the distance to the Delirium boss in room nr.
___

### Display·Flags {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int DisplayFlags  {: .copyable aria-label='Variables' }

Indicates what is visible on the minimap.
**Display Flags (bitwise):**
```lua
1 << -1 -- Invisible
1 << 0 -- Visible
1 << 1 -- Room Shadow
1 << 2 -- Show Icon
```

???- example "Examples"
    The flags are hard to interpret, but here are some examples:

    **000** = invisible, this is how most rooms start

    **101** = standard room visibility, this includes rooms that are adjacent and you haven't actively visited. This will usually show icons.

    **011** = secret room, locked rooms, sac rooms pre-entry*

    **111** = 011 rooms after entry, but also the rooms directly adjacent to them* (applied after entry)

    \* If you have Spelunker Hat, bit 1 is completely unused. All special rooms will have the normal behavior of either 000 or 101. This is unique to Spelunker Hat; mapping items follow the normal rules.

???+ quote "Quote from User 'Budj'"
    From this my best guess is that bits 1 and 2 are special rendering (display) flags that may have more meaning down below.

    The important bit for using them is minding that they're used differently mostly for special rooms.

    As far as I've seen, 001 is completely unused.
    010, 100, and 110 may be used for compass or blue map, I don't remember. I think they use 100.
___

### Flags {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [RoomDescriptor](enums/RoomDescriptor.md) Flags  {: .copyable aria-label='Variables' }
The RoomDescriptor flags for the room.
___

### Grid·Index {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int GridIndex  {: .copyable aria-label='Variables' }

Describes the index of the room on the level grid (13 by 13 cells). The index is the cell number on the grid, when counting them row by row from left to right.

- For a 1x1 room, this is equal to the 1x1 grid index of the room.
- For a room bigger than a 1x1 room, this is equal to the top left 1x1 quadrant.
- For `RoomType.ROOMSHAPE_LTL` rooms (i.e. rooms that look like a "J"), this is equal to the 1x1 quadrant where the gap in the room is. In other words, it is a 1x1 quadrant that is not actually contained within the room.
- Note that **this value is different** than the value returned by `Level:GetCurrentRoomIndex()`. (That function returns the 1x1 quadrant that the room was entered in.)
- Data structures that store data per room should use `ListIndex` as a key instead of `GridIndex`, since the former is unique across different dimensions.

???- note "Notes"
    ![Room Grid indices](images/infographics/RoomGridIndices.png)

???- example "Get dimension example code"
    A level can have multiple dimensions, which act as separate and independent level grids. Because of this, a room in dimension 1 can share the same grid index as a different room in dimension 2. Repentogon provides a GetDimension method, but if you don’t have access to it, you can use the following function to determine the dimension of a given room descriptor.

    ```lua
    -- requirements: a room that actually exists on the map, or one of the game's special rooms that exist outside the map
    local function getDimension(roomDesc)
      -- 0: main dimension
      -- 1: secondary dimension, used by downpour mirror dimension and mines escape sequence
      -- 2: death certificate dimension
      for i = 0, 2 do
        if GetPtrHash(roomDesc) == GetPtrHash(Game():GetLevel():GetRoomByIdx(roomDesc.SafeGridIndex, i)) then
          return i
        end
      end
      return -1
    end

    getDimension(Game():GetLevel():GetCurrentRoomDesc()) -- returns 0, 1, or 2 depending on where you're at
    getDimension(Game():GetLevel():GetRoomByIdx(GridRooms.ROOM_DEVIL_IDX)) -- special rooms outside the map return 0
    ```
___

### Has·Water {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasWater  {: .copyable aria-label='Variables' }

___

### List·Index {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ListIndex  {: .copyable aria-label='Variables' }

The index for this room corresponding to the `Level.GetRooms().Get()` method. In other words, this is equal to the order that the room was created by the floor generation algorithm.

Use this as an index for data structures that store data per room, since it is unique across different dimensions.

___

### No·Reward {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean NoReward  {: .copyable aria-label='Variables' }

___

### Override·Data {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [RoomConfigRoom](RoomConfig_Room.md) OverrideData  {: .copyable aria-label='Variables' }
The room variant is in Data. Because Room::Init uses a mix of data, one from level layout and one from replacement data like minibosses, we need to hold the new room data somewhere.
___

### Pits·Count {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int PitsCount  {: .copyable aria-label='Variables' }

___

### Poop·Count {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int PoopCount  {: .copyable aria-label='Variables' }

___

### Pressure·Plates·Triggered {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean PressurePlatesTriggered  {: .copyable aria-label='Variables' }

___

### Sacrifice·Done {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean SacrificeDone  {: .copyable aria-label='Variables' }

___

### Safe·Grid·Index {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int SafeGridIndex  {: .copyable aria-label='Variables' }

- For a 1x1 room, this is equal to the 1x1 grid index of the room.
- For a room bigger than a 1x1 room, this is equal to the top left 1x1 quadrant.
- For `RoomType.ROOMSHAPE_LTL` rooms (i.e. rooms that look like a "J"), this is equal to the top right 1x1 quadrant.
- Note that **this value is different** than the value returned by `Level:GetCurrentRoomIndex()`. (That function returns the 1x1 quadrant that the room was entered in.)
- Data structures that store data per room should use `ListIndex` as a key instead of `SafeGridIndex`, since the former is unique across different dimensions.

???- note "Notes"
    ![Room Grid indices](images/infographics/RoomGridIndices.png)
___

### Shop·Item·Discount·Idx {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ShopItemDiscountIdx  {: .copyable aria-label='Variables' }
- The index that denotes which shop item(s) will be discounted.
- Can be a value from -1 to 7.
- All items in the room with this ShopItemId will be affected by the discount.
    - This is noticeable when there are more than 8 shop items in a room.
- A value of -1 means there is no discounted item.
- This value is unaffected by Steam Sale.
- Defaults to -1 in non-shop rooms.
- Can be modified by accessing the writable version of the RoomDescriptor like this:

```lua
local level = Game():GetLevel()
local room = level:GetCurrentRoom()

-- this returns a writable RoomDescriptor for the current Room.
local writableRoomDesc = level:GetRoomByIdx(level:GetCurrentRoomIndex())

-- Sets the current Room's ShopItemDiscountIdx to 0.
-- All items with ShopItemId 0 will be discounted.
writableRoomDesc.ShopItemDiscountIdx = 0

-- update the Room using Update() to have the change take effect.
room:Update()
```

___

### Shop·Item·Idx {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ShopItemIdx  {: .copyable aria-label='Variables' }
- The ShopItemId value of the next shop item to add to the room.
    - If this is set to 1 in a Room and another shop item is created, the new item will have a ShopItemId of 1, and the Room's ShopItemIdx will then be 2.
- Can be used as the total number of items in the shop, up to 7 items.
- Can be a value between 0 and 7.
- For every 8 items in a shop, this value resets itself to 0.
    - For example, if a custom shop has 9 items, the 1st and 9th items will share the same ShopItemId of 0, and the RoomDescriptor ShopItemIdx value will be 1.
- Defaults to -1 in non-shop rooms.
- Can be modified by accessing the writable version of the RoomDescriptor like this:

```lua
local level = Game():GetLevel()
local room = level:GetCurrentRoom()

-- this returns a writable RoomDescriptor for the current Room.
local writableRoomDesc = level:GetRoomByIdx(level:GetCurrentRoomIndex())

-- Sets the current Room's ShopItemIdx to 0.
writableRoomDesc.ShopItemIdx = 0

-- update the Room using Update() to have the change take effect.
room:Update()
```

???- note "Notes"
    - In the image below, each item's ShopItemId is written underneath it.
    - Notice how all items that share a ShopItemId have the same PickupVariant, but aren't identical.
    - ShopItemDiscountIdx is 2, so all shop items with a ShopItemId of 2 are on sale.
    - After all items are created, the ShopItemIdx for this room is 0.
    ![ShopItemIdx Example](images/shopItemIdxDiagram.png)
___

### Spawn·Seed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int SpawnSeed  {: .copyable aria-label='Variables' }
used to spawn entities at room load and initialize enemy drop seeds
___

### Surprise·Miniboss {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean SurpriseMiniboss  {: .copyable aria-label='Variables' }
___

### Visited·Count {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int VisitedCount  {: .copyable aria-label='Variables' }
how often the room has been visited
___

<div class="rgon-only" markdown="1">

### AddRestrictedGridIndex () {: aria-label='Functions' }
#### void AddRestrictedGridIndex ( int GridIndex ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDecoSaveState () {: aria-label='Functions' }
#### [EntitiesSaveStateVector](EntitiesSaveStateVector.md) GetDecoSaveState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDimension () {: aria-label='Functions' }
#### [Dimension](https://wofsauge.github.io/IsaacDocs/rep/enums/Dimension.html) GetDimension ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回该房间所在的 [Dimension](enums/Dimension.md)。

### GetEntitiesSaveState () {: aria-label='Functions' }
#### [EntitiesSaveStateVector](EntitiesSaveStateVector.md) GetEntitiesSaveState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetGridEntitiesSaveState () {: aria-label='Functions' }
#### [GridEntitiesSaveStateVector](GridEntitiesSaveStateVector.md) GetGridEntitiesSaveState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetNeighboringRooms () {: aria-label='Functions' }
#### table GetNeighboringRooms ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
if roomType == RoomType.ROOM_SECRET or roomType == RoomType.ROOM_SUPERSECRET or roomType == RoomType.ROOM_ULTRASECRET then
return false
返回一个表，将 [DoorSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/DoorSlot.html) 映射到该房间当前所有邻居的 [RoomDescriptor](https://wofsauge.github.io/IsaacDocs/rep/RoomDescriptor.html)。
end
遍历此表时不要使用 `ipairs`，应使用 `pairs`！
```lua
local function HasSecretRoomNeighbor(roomDesc)
local roomType = neighborDesc.Data.Type
return true
-- Returns true if the room has a neighboring secret room.
for doorSlot, neighborDesc in pairs(roomDesc:GetNeighboringRooms()) do
???- example "Example Code"
```

### GetRestrictedGridIndexes () {: aria-label='Functions' }
#### int[] GetRestrictedGridIndexes ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetTaintedKeeperCoinSpawns () {: aria-label='Functions' }
#### int GetTaintedKeeperCoinSpawns ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
当计数器达到 10 时，防止玩家重新进入房间时被击杀的敌人生成硬币。

___

### InitSeeds () {: aria-label='Functions' }
#### void InitSeeds ( [RNG](RNG.md) RNG ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetTaintedKeeperCoinSpawns () {: aria-label='Functions' }
#### void SetTaintedKeeperCoinSpawns ( int Num ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

## Variables

### BossDeathSeed {: aria-label='Variables' }
#### const int BossDeathSeed [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### Doors {: aria-label='Variables' }
#### const int[] Doors [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
用于检查房间中的每个 [DoorSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/DoorSlot.html) 连接到哪个关卡网格索引。

例如，`roomdesc.Doors[DoorSlot.UP0]` 会返回上方门所连接的关卡网格索引。

如果 [RoomShape](https://wofsauge.github.io/IsaacDocs/rep/enums/RoomShape.html) 不允许在该槽位设置门，则值为 `-1`。

请注意，即使当前没有门，或房间本身不允许在该槽位设置门，此属性通常仍会提供有效索引。

___

### GetErrorTrinketEffect () {: aria-label='Functions' }
#### [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) GetErrorTrinketEffect ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the current effect that would be mimicked by the "Error" trinket (`TrinketType.TRINKET_ERROR`) for a player in this room.

Note that this effect is based entirely on the [SpawnSeed](https://wofsauge.github.io/IsaacDocs/rep/RoomDescriptor.html#spawnseed).

### GetValidNeighborPlacementLocations () {: aria-label='Functions' }
#### int[] GetValidNeighborPlacementLocations ( [RoomConfigRoom](https://wofsauge.github.io/IsaacDocs/rep/RoomConfig_Room.html) RoomConfig, boolean AllowMultipleDoors = true, boolean AllowSpecialNeighbors = false ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
#### int[] GetValidNeighborPlacementLocations ( [RoomShape](https://wofsauge.github.io/IsaacDocs/rep/enums/RoomShape.html) RoomShape = 1, [DoorMask](enums/DoorMask.md) DoorMask = -1, boolean AllowMultipleDoors = true, boolean AllowSpecialNeighbors = false ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of room grid indices that would be valid locations to place the specified room as a neighbor of this room using [TryPlaceRoom](Level.md#tryplaceroom).

See [TryPlaceRoom](Level.md#tryplaceroom) for more information on room placement and example code.

___

### GetGroup () {: aria-label='Functions' }
#### int GetGroup () [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

???- "Usage"
    `Group` is only used by effects that need to randomly select a room to warp to (e.g. Teleport, Gold Pill Teleport, etc.).
    A room can only be selected if its group is either RoomGroup.GROUP_NONE or matches the current room's group.

    By default, all rooms use `RoomGroup.GROUP_NONE`. The only exception is Ultra Secret Rooms, which are assigned a different group by the game during level generation.

___

### SetGroup () {: aria-label='Functions' }
#### void SetGroup ( int group ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

It is suggested to use CreateGroup instead of setting an arbitrary group.

???- "Usage"
    `Group` is only used by effects that need to randomly select a room to warp to (e.g. Teleport, Gold Pill Teleport, etc.).
    A room can only be selected if its group is either RoomGroup.GROUP_NONE or matches the current room's group.

    By default, all rooms use `RoomGroup.GROUP_NONE`. The only exception is Ultra Secret Rooms, which are assigned a different group by the game during level generation.

___

### CreateGroup () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge }
#### static int CreateGroup ( string groupName ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

Creates a new unique group ID for `SetGroup`.

???+ warning "Errors"
    The function will error if a group with the specified name already exists.

___

### GetGroupByName () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge }
#### static int? GetGroupByName ( string groupName ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

Returns the group id tied to the specified name.

Returns `nil` if the name has not been registered.

___

## Variables

</div>
