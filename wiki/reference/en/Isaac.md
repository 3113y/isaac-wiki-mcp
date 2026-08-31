---
tags:
  - Globals
  - Class
  - Isaac
---
# Global Class "Isaac"

???+ info
    You can get this class by using the `Isaac` global table.

    **Note that to call these functions, you must use a `.` (period) instead of a `:` (colon)!**

    ???+ example "Example Code"
        ```lua
        local player = Isaac.GetPlayer()
        ```

## Functions

### Add·Callback () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCallback ( table modRef, [ModCallback](enums/ModCallbacks.md)|string callbackId, table callbackFn, int entityId ) {: .copyable aria-label='Functions' }

It is recommended to use the [AddCallback](ModReference.md#addcallback) function on a [Mod Reference](ModReference.md) instead.

___

### Add·Pill·Effect·To·Pool () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [PillColor](enums/PillColor.md) AddPillEffectToPool ( [PillEffect](enums/PillEffect.md) pillEffect ) {: .copyable aria-label='Functions' }
Returns the [PillColor](enums/PillColor.md) of the added pill.

___

### Add·Priority·Callback () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddPriorityCallback ( table modRef, [ModCallback](enums/ModCallbacks.md)|string callbackId, [CallbackPriority](enums/CallbackPriority.md) priority, table callbackFn, int entityId ) {: .copyable aria-label='Functions' }

It is recommended to use the [AddPriorityCallback](ModReference.md#addprioritycallback) function on a [Mod Reference](ModReference.md) instead.

___

### Console·Output () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ConsoleOutput ( string text ) {: .copyable aria-label='Functions' }

Prints a string into the Debug Console.

???- example "Example Code"
    You can use this example as an alternative.
    ```lua
    Isaac.ConsoleOutput("This is a Test.")
    -- Output: This is a Test.

    -- Alternatively:
    print("This is a Test.")
    -- Output: This is a Test.
    ```

___

### Count·Bosses () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int CountBosses ( ) {: .copyable aria-label='Functions' }

Returns the number of bosses in the current room.
___

### Count·Enemies () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int CountEnemies ( ) {: .copyable aria-label='Functions' }

Returns the number of enemies in the current room.
___

### Count·Entities () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int CountEntities ( [Entity](Entity.md) Spawner, [EntityType](enums/EntityType.md) Type = EntityType.ENTITY_NULL, int Variant = -1, int SubType = -1 ) {: .copyable aria-label='Functions' }

Returns the number of entities in the current room that fulfill the specified requirements.

- `Spawner` refers to an Entity object (can be `:::lua nil`).
- `Type` refers to the found entity's type (can be `:::lua EntityType.ENTITY_NULL`).
- `Variant` and `Subtype` refer to the found entity's `Variant` and `Subtype` (can be `:::lua -1`).

___

### Debug·String () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void DebugString ( string str ) {: .copyable aria-label='Functions' }

Prints a string into the log file. You can find this file here: `:::lua %systemdrive%\Users\%username%\Documents\My Games\Binding of Isaac Repentance\log.txt`

???- example "Example Code"
    This code prints `:::lua "This is a Test."` in the log.txt file.
    ```lua
    Isaac.DebugString("This is a Test.")
    -- Output: [INFO] - Lua Debug: This is a Test.
    ```

???+ warning "Warning"
    The max string size you can log is 10,219 bytes. If you go over this limit then the string will be truncated, but the newline character won't be appended to the end of your line and the next log line won't start on its own line.

    If you're logging english (or ascii) characters then each character is equal to 1 byte.

    If you're logging multi-byte characters (e.g. chinese characters that use 3 bytes in utf-8 encoding) then perform some simple math: 10219 / 3 = 3406 characters (rounded down)

    You can use `string.len` to get the number of bytes and `utf8.len` to get the number of characters in your string.

___

### Execute·Command () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### string ExecuteCommand ( string command ) {: .copyable aria-label='Functions' }

This function executes a debug console command. See the [Debug Console Tutorial](tutorials/DebugConsole.md) for informations on how to use commands.
___

### Explode () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Explode ( [Vector](Vector.md) pos, [Entity](Entity.md) source, float damage ) {: .copyable aria-label='Functions' }

Spawn an explosion on a specified location.
___

### Find·By·Type () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [Entity](Entity.md)[] FindByType ( [EntityType](enums/EntityType.md) Type, int Variant = -1, int SubType = -1, boolean Cache = false, boolean IgnoreFriendly = false ) {: .copyable aria-label='Functions' }
Returns entities based on Type, Variant, Subtype. If Variant and/or Subtype is -1 then everything is included. Use Cache flag for multiple calls per frame.

If an entity has `EntityFlag.FLAG_NO_QUERY` then it will be excluded from the results. If you need to get an entity with that flag then you should use `GetRoomEntities` instead.
___

<div class="rgon-extension" markdown="1">

### FindByType () {: aria-label='Modified Functions' }
#### [Entity](Entity.md)[] FindByType ( [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, int Variant = -1, int SubType = -1, boolean Cache = false, boolean IgnoreFriendly = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Same as vanilla, but much faster.

___

</div>

### Find·In·Radius () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [Entity](Entity.md)[] FindInRadius ( [Vector](Vector.md) Position, float Radius, [EntityPartition](enums/EntityPartition.md) Partitions = 0xFFFFFFFF  ) {: .copyable aria-label='Functions' }
Returns an array of all entities inside the range of Radius from Position filtered by Partitions mask. (include all = 0xffffffff)

This function does not return the entities sorted by nearest first, but based on the order they were loaded.
___

<div class="rgon-extension" markdown="1">

### FindInRadius () {: aria-label='Modified Functions' }
#### [Entity](Entity.md)[] FindInRadius ( [Vector](Vector.md) Position, float Radius, [EntityPartition](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityPartition.html) Partitions = 0xFFFFFFFF  ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Same as in vanilla, but much faster and with fixed search for effects.

___

</div>

### Get·Built·In·Callback·State () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean GetBuiltInCallbackState ( [ModCallbacks](enums/ModCallbacks.md) callbackId ) {: .copyable aria-label='Functions' }
Returns `true` if callbacks under `callbackId` will be ran by the game. This is normally only `false` if there are no callbacks added under `callbackId`.

___

### Get·Callbacks () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### table GetCallbacks ( [ModCallback](enums/ModCallbacks.md)|string callbackId, boolean createIfMissing = nil ) {: .copyable aria-label='Functions' }
Returns a list of callbacks added under `callbackId`. Callbacks are represented as a table, for more information [see the custom callback tutorial.](tutorials/CustomCallbacks.md#run-behavior)

The game holds all callbacks added to `callbackId` in a table, where the `callbackId` is the index, and the value is a table containing all callbacks added using said `callbackId`. If `createIfMissing` is `true`, and there are no added callbacks under `callbackId`, then the game will create an empty table for the `callbackId` for new callbacks to be added to. This empty table contains a metatable with a default `__matchParams` metamethod, which is called when checking if the extra parameter specified when adding the callback is valid. This function is also used with `createIfMissing` set to `true` by the game whenever any callback is added.

If `createIfMissing` is `false` or `nil` and there are no callbacks added under `callbackId`, this function will return an empty table.

___

### Get·Card·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Card](enums/Card.md) GetCardIdByName ( string cardHudName ) {: .copyable aria-label='Functions' }
Returns the [CardID](enums/Card.md) based on the "hud"-attribute defined in the "pocketitems.xml" file. Returns `-1` if no card with that "hud" attribute value could be found.

???+ warning "Warning"
    The name of this function is misleading, this function will only work with the "hud"-attribute value of a card and not the name of a card.

???+ bug "Bug"
    This function does not work for vanilla cards/runes, because they don't have the "hud" attribute defined in their entry in the pocketitems.xml file. You need to use the [Card](enums/Card.md) enum to get those vanilla IDs instead.

???- example "Example Code"
    This code gets the CardID of a modded card.
    ```xml
    <pocketitems>
        <card type="tarot" pickup="1" description="some description"  name="My new card" hud="my_modded_card" />
    </pocketitems>
    ```
    ```lua
    Isaac.GetCardIdByName("my_modded_card")
    ```

___

### Get·Challenge () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Challenge](enums/Challenge.md) GetChallenge ( ) {: .copyable aria-label='Functions' }
Returns the ID of a challenge the player is currently in. Returns 0 if the player is not playing any challenge.
___

### Get·Challenge·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Challenge](enums/Challenge.md) GetChallengeIdByName ( string challengeName ) {: .copyable aria-label='Functions' }

Returns the ChallengeID of a challenge based on its name. (File: challenges.xml) Returns `-1` if no challenge with that name could be found (Case sensitive).

???- example "Example Code"
    This code gets the ChallengeID of Aprils fool.
    ```lua
    Isaac.GetChallengeIdByName("Aprils fool")
    --Returns: 32
    ```

___

### Get·Costume·Id·By·Path () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetCostumeIdByPath ( string path ) {: .copyable aria-label='Functions' }

Returns the CostumeID of a costume based on its file path. (File: costumes2.xml) Returns `-1` if no costume with that path could be found.

???- example "Example Code"
    This code gets the CostumeID of the Poop transformation costume.
    ```lua
    Isaac.GetCostumeIdByPath("gfx/characters/n027_Transformation_Poop.anm2")
    --Returns: 27
    ```

___

### Get·Curse·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [LevelCurse](enums/LevelCurse.md) GetCurseIdByName ( string curseName ) {: .copyable aria-label='Functions' }

Returns the CurseID of a curse based on its name. (File: curses.xml) Returns `-1` if no curse with that name could be found.

???- example "Example Code"
    This code gets the CurseID of Curse of the Unknown.
    ```lua
    Isaac.GetCurseIdByName("Curse of the Unknown")
    --Returns: 4
    ```

___

### Get·Entity·Type·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityType](enums/EntityType.md) GetEntityTypeByName ( string entityName ) {: .copyable aria-label='Functions' }

Returns the EntityType of an entity based on its name. (File: entities2.xml) Returns `0` if no entity with that name could be found.

???- note "Notes"
    There is no SubType version of this function.

???- example "Example Code"
    This code gets the EntityType of Flaming Gaper.
    ```lua
    Isaac.GetEntityTypeByName("Flaming Gaper")
    --Returns: 10
    ```

___

### Get·Entity·Variant·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetEntityVariantByName ( string entityName ) {: .copyable aria-label='Functions' }

Returns the variant of an entity based on its name. (File: entities2.xml) Returns `-1` if no entity with that name could be found.

???- note "Notes"
    There is no SubType version of this function.

???- example "Example Code"
    This code gets the variant of Flaming Gaper.

    ```lua
    Isaac.GetEntityVariantByName("Flaming Gaper")
    --Returns: 2

    ```

___

### Get·Frame·Count () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetFrameCount ( ) {: .copyable aria-label='Functions' }

Returns the amount of frames the game as a whole is running. The counter increases even when the game is paused or when you are in the main menu!
1 second equals roughtly 60 frames.
This function therefore works drastically different than [`:::lua Game():GetFrameCount()`](Game.md#getframecount)

___

### Get·Free·Near·Position () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetFreeNearPosition ( [Vector](Vector.md) pos, float step ) {: .copyable aria-label='Functions' }

___

### Get·Item·Config () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [ItemConfig](ItemConfig.md) GetItemConfig ( ) {: .copyable aria-label='Functions' }

This is the only way to access the `ItemConfig` object.
___

### Get·Item·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetItemIdByName ( string itemName ) {: .copyable aria-label='Functions' }

Returns the ItemID of a Collectible. (File: items.xml) Returns `-1` if no item with that name could be found.

???- example "Example Code"
    This code gets the ItemID of Brimstone.

    ```lua
    Isaac.GetItemIdByName("Brimstone")
    --Returns: 118

    ```

___

### Get·Music·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Music](enums/Music.md) GetMusicIdByName ( string musicName ) {: .copyable aria-label='Functions' }

Returns the MusicID of a music track. (File: music.xml) Returns `-1` if no music with that name could be found.

???- example "Example Code"
    This code gets the MusicID of the Title Screen.

    ```lua
    Isaac.GetMusicIdByName("Title Screen")
    --Returns: 61

    ```

___

### Get·Pill·Effect·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [PillEffect](enums/PillEffect.md) GetPillEffectByName ( string pillEffect ) {: .copyable aria-label='Functions' }

Returns the PillEffectID based on its name. (File: pocketitems.xml) Returns `-1` if no pill with that name could be found.

???- example "Example Code"
    This code gets the PillEffectID of I can see forever!.

    ```lua
    Isaac.GetPillEffectByName("I can see forever!")
    --Returns: 23

    ```

___

### Get·Player () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityPlayer](EntityPlayer.md) GetPlayer ( int playerID = 0 ) {: .copyable aria-label='Functions' data-altreturn='nil' }

Returns the EntityPlayer that matches the provided player ID. Player IDs start at 0 and increment upwards. For example, when playing as Jacob & Esau, Jacob will have a player ID of 0 and Esau will have a player ID of 1.

If an invalid player ID is passed (such as -20 or 20), the function will instead assume a player index of 0.

This function can return `nil` if it is called before any player is initialized (i.e. if you call it in the main menu).

This function is the same as [`Game():GetPlayer()`](Game.md#getplayer).

???- example "Example Code"

    ```lua
    local function getPlayers()
      local game = Game()
      local numPlayers = game:GetNumPlayers()

      local players = {}
      for i = 0, numPlayers - 1 do
        local player = Isaac.GetPlayer(i)
        table.insert(players, player)
      end

      return players
    end
    ```

___

### Get·Player·Type·By·Name () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [PlayerType](enums/PlayerType.md) GetPlayerTypeByName ( string playerName , boolean Tainted = false ) {: .copyable aria-label='Functions' }

Returns the PlayerType (ID) of a character based on its name. (File: players.xml) Returns `-1` if no player with that name could be found.

???+ warning "Warning"
    In Repentance, character names where made translateable and therefore use the translation placeholder as their "base name". For example, to get the [PlayerType](enums/PlayerType.md) of Cain, you need to use this function with the character name `#AZAZEL_NAME` instead of `Azazel`.
    It is therefore recommended to use this function for modded characters, and use the [PlayerType](enums/PlayerType.md) enum directly, if you want to have the PlayerType of a vanilla character.

???- example "Example Code"
    This code gets the PlayerType of Azazel.

    ```lua
    -- REPENTANCE:
    Isaac.GetPlayerTypeByName("#AZAZEL_NAME") --Returns: 7

    -- AFTERBIRTH+:
    Isaac.GetPlayerTypeByName("Azazel") --Returns: 7

    ```

___

### Get·Random·Position () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetRandomPosition ( ) {: .copyable aria-label='Functions' }

Returns a random position inside the current room. The Return value is a Vector containing the position in world coordinates.
___

### Get·Room·Entities () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md)[] GetRoomEntities ( ) {: .copyable aria-label='Functions' }
Returns an iterable table containing all entities in the room at the time the function was called.

This behavior is different to [`Room::GetEntities()`](Room.md#getentities), which returns a raw pointer to the array that stores all entities of the room at any given time. **For most usecases, its advised to use [`Isaac.GetRoomEntities()`](Isaac.md#getroomentities)**!

???- example "Example Code"
    This code prints the Type, Variant and SubType of each entity in the room.

    ```lua
    for i, entity in ipairs(Isaac.GetRoomEntities()) do
        print(entity.Type, entity.Variant, entity.SubType)
    end

    ```

___

<div class="rgon-extension" markdown="1">

### GetRoomEntities () {: aria-label='Modified Functions' }
#### [Entity](Entity.md)[] GetRoomEntities ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Same as vanilla, but much faster.

___
## Functions

</div>

### Get·Screen·Height () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### float GetScreenHeight ( ) {: .copyable aria-label='Functions' }

___

### Get·Screen·Point·Scale () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### float GetScreenPointScale ( ) {: .copyable aria-label='Functions' }

Returns a number denoting how "zoomed in" the screen is. This can be `1.0` or `2.0`, depending on the resolution of the game window.

???- example "Video Demonstration"
    <figure class="video_container">
        <video controls="true" allowfullscreen="true" muted="true" style="width:25rem">
            <source src="./customData/screen-point-scale.mp4" type="video/mp4">
        </video>
        <figcaption>Demonstration of how the size of the game window changes the value this function returns.</figcaption>
    </figure>

___

### Get·Screen·Width () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### float GetScreenWidth ( ) {: .copyable aria-label='Functions' }

___

### Get·Sound·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [SoundEffect](enums/SoundEffect.md) GetSoundIdByName ( string soundName ) {: .copyable aria-label='Functions' }

Returns the [SoundEffect](enums/SoundEffect.md) of a sound based on its name. (File: sounds.xml) Returns `-1` if no sound with that name could be found.

???- example "Example Code"
    This code gets the SoundEffectID of a sound named "Custom Sound Effect"

    ```lua
    Isaac.GetSoundIdByName("Custom Sound Effect")

    ```

___

### Get·Text·Width () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetTextWidth ( string str ) {: .copyable aria-label='Functions' }

Returns the width of the given string in pixels based on the "terminus8" font (same font as used in Isaac.RenderText())

___

### Get·Time () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetTime ( ) {: .copyable aria-label='Functions' }

Returns the current time in milliseconds since the computer's operating system was started.

This is useful for measuring how much real time has passed independent of how many frames have passed. (Frames are not a very good indicator of how much time has passed, because the game locks up to load new data on every level transition and room transition.)

For example, you could use this to implement an on-screen speedrunning timer based on real-time, or to benchmark the performance impact of one function over another.

___

### Get·Trinket·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [TrinketType](enums/TrinketType.md) GetTrinketIdByName ( string trinketName ) {: .copyable aria-label='Functions' }

Returns the TrinketType of a trinket based on its name. (File: items.xml) Returns `-1` if no trinket with that name could be found.

???- example "Example Code"
    This code gets the TrinketType of Lucky Toe.

    ```lua
    Isaac.GetTrinketIdByName("Lucky Toe")
    --Returns: 42
    ```

___

### Grid·Spawn () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntity](GridEntity.md) GridSpawn ( [GridEntityType](enums/GridEntityType.md) gridEntityType, int variant, [Vector](Vector.md) position, boolean forced ) {: .copyable aria-label='Functions' }

Spawn a [GridEntity](GridEntity.md) at the given position (world coordinates).

???+ bug "Bugs"
    The "forced" argument can override the grid entity at the given location in certain cases. For example: it won't work with a rock, but will work with a rock that's been blown up. You can check the location with `Isaac.GetFreeNearPosition` to see if the game considers that location free. Check the returned grid entity's type to make sure the replacement happened. Otherwise, you may need to remove the grid entity at the given location before spawning something else in its place.

For example, to spawn a super secret rock in the center of the room:

```lua
local game = Game()
local room = game:GetRoom()
local centerPos = room:GetCenterPos()
Isaac.GridSpawn(GridEntityType.GRID_ROCK_SS, 0, centerPos, true)
```

___

### Has·Mod·Data () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasModData ( table modRef ) {: .copyable aria-label='Functions' }

Returns "true" if your mod has Data stored using the "SaveModData()" function. Aka. if there is a "saveX.dat" file in your mod folder.

There are 3 "saveX.dat" files, one per Savegame. The number indicates the savegame it corresponds to. The number will be determined automatically by the game.

For AB+, they are stored inside their mod's folder next to the "main.lua" file.

For Repentance, They are stored in the "data" folder next to the "mods" folder inside the game files.

It is recommended to use the [HasData](ModReference.md#hasdata) function on a [Mod Reference](ModReference.md) instead.
___

### Load·Mod·Data () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### string LoadModData ( table modRef ) {: .copyable aria-label='Functions' }

Returns a string that was stored in a "saveX.dat" file using the "SaveModData()" function. If there is no "saveX.dat" file in your mod, this function will return an empty string.
There are 3 "saveX.dat" files, one per Savegame. The number indicates the savegame it corresponds to. The number will be determined automatically by the game.

If you call this function in the main menu, it will return the save data for save slot 1 by default.

For AB+, they are stored inside their mod's folder next to the "main.lua" file.

For Repentance, They are stored in the "data" folder next to the "mods" folder inside the game files.

It is recommended to use the [LoadData](ModReference.md#loaddata) function on a [Mod Reference](ModReference.md) instead.
___

### Register·Mod () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RegisterMod ( table modRef, string modName, int apiVersion ) {: .copyable aria-label='Functions' }

Registers a table with the game to use as a [Mod Reference](ModReference.md).

It is recommended to use the global [RegisterMod](GlobalFunctions.md#registermod) function instead.

___

### Remove·Callback () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveCallback ( table modRef, [ModCallback](enums/ModCallbacks.md)|string callbackId, table callbackFn ) {: .copyable aria-label='Functions' }

It is recommended to use the [RemoveCallback](ModReference.md#removecallback) function on a [Mod Reference](ModReference.md) instead.

___

### Remove·Mod·Data () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveModData ( table modRef ) {: .copyable aria-label='Functions' }

Deletes the stored "saveX.dat" file if it exists.
There are 3 "saveX.dat" files, one per Savegame. They are stored in the mod's folder next to the "main.lua" file. The number indicates the savegame it corresponds to. The number will be determined automatically by the game.

It is recommended to use the [RemoveData](ModReference.md#removedata) function on a [Mod Reference](ModReference.md) instead.
___

### Render·Scaled·Text () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderScaledText ( string str, float X, float Y, float ScaleX, float ScaleY, float R, float G, float B, float A ) {: .copyable aria-label='Functions' }

Renders a scaled text on the Screen. X and Y coordinates need to be in screen coordinates ( x[0,~500) y [0,~350) ). ScaleX, ScaleY, R ,G ,B and A need to be between [0,1]. Some scale values can cause the font to display deformed and pixelated.

???- example "Example Code"
    This code renders the player position on the screen.

    ```lua
    local player = Isaac.GetPlayer()
    local text = "X: " .. player.Position.X .. ", Y: " .. player.Position.Y
    Isaac.RenderScaledText(text, 50, 50, 0.5, 0.5, 1, 1, 1, 1)
    ```

___

### Render·Text () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderText ( string str, float X, float Y, float R, float G, float B, float A ) {: .copyable aria-label='Functions' }

Renders a text with the default size on the Screen. X and Y coordinates need to be in screen coordinates ( x[0,~500) y [0,~350) ). R,G,B and A need to be between [0,1].

???- example "Example Code"
    This code renders the player position on the screen.

    ```lua
    local player = Isaac.GetPlayer()
    local pos = player.Position
    Isaac.RenderText("X: "..pos.X.." Y: "..pos.Y, 50, 50, 1 ,1 ,1 ,1 )

    ```

___

### Run·Callback () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void RunCallback ( [ModCallback](enums/ModCallbacks.md)|string callbackId ) {: .copyable aria-label='Functions' }
Runs all callbacks added under `callbackId`, breaking on the first return and returning that value.

___

### Run·Callback·With·Param () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void RunCallbackWithParam ( [ModCallback](enums/ModCallbacks.md)|string callbackId ) {: .copyable aria-label='Functions' }
Runs all callbacks added under `callbackId`, breaking on the first return and returning that value.

___

### Save·Mod·Data () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SaveModData ( table modRef, string data ) {: .copyable aria-label='Functions' }

Stores a string in a "saveX.dat" file. The stored Data persists thruout resets and game restart, so its perfect to store persistent data.

There are 3 "saveX.dat" files, one per Savegame. The number indicates the savegame it corresponds to. The number will be determined automatically by the game.

For AB+, they are stored inside their mod's folder next to the "main.lua" file.

For Repentance, They are stored in the "data" folder next to the "mods" folder inside the game files.

It is recommended to use the [SaveData](ModReference.md#savedata) function on a [Mod Reference](ModReference.md) instead.
___

### Screen·To·World () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) ScreenToWorld ( [Vector](Vector.md) pos ) {: .copyable aria-label='Functions' }

Transfers Screen (aka. Window coordinates) into Worldcoordinates. This can be used to get a specific location in the room in World coordnates The World coordinate system is x[0,inf) y[0,inf).
___

### Screen·To·World·Distance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) ScreenToWorldDistance ( [Vector](Vector.md) pos ) {: .copyable aria-label='Functions' }
___

### Set·Built·In·Callback·State () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetBuiltInCallbackState ( [ModCallbacks](enums/ModCallbacks.md) callbackId, boolean state ) {: .copyable aria-label='Functions' }
Sets whether callbacks under `callbackId` will be ran by the game. The game uses this to activate a [ModCallbacks](enums/ModCallbacks.md) once a callback is added under one, or deactivate them when those callbacks have been removed.

___

### Spawn () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) Spawn ( [EntityType](enums/EntityType.md) entityType, int entityVariant, int entitySubtype, [Vector](Vector.md) position, [Vector](Vector.md) velocity, [Entity](Entity.md) Spawner ) {: .copyable aria-label='Functions' }

Spawns the defined entity at the given location. If the position is not free, it spawns it in the nearest free position.

There are two spawn functions. [Isaac.Spawn()](Isaac.md#spawn) (this one), which spawns an entity with a random seed, and [Game():Spawn()](Game.md#spawn), which spawns an entity with a specific seed. However due to a bug, [Isaac.Spawn()](Isaac.md#spawn) has a chance to generate a seed of 0, which crashes the game. If you need to spawn an entity with a random seed, you should always use [Game():Spawn()](Game.md#spawn) with a helper function that calls [Random()](GlobalFunctions.md#random) and arbitrarily sets the seed to 1 when the seed is 0. ([IsaacScript](https://isaacscript.github.io/) users can just use the `spawn` helper function, which uses `Game.Spawn` under the hood.)

???- example "Example Code"
    This code spawns a random collectible at in center of the current room.
    ```lua
    Isaac.Spawn(EntityType.ENTITY_PICKUP, PickupVariant.PICKUP_COLLECTIBLE, 0, Vector(320,280), Vector(0,0), nil)
    ```

???+ bug "Bug"
    Because the random seed is generated using the [Random()](GlobalFunctions.md#random) function, there is a chance that the entity's InitSeed is set to 0, which causes a crash if the entity needs to use RNG.
___

### World·To·Render·Position () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) WorldToRenderPosition ( [Vector](Vector.md) pos ) {: .copyable aria-label='Functions' }

Transfers world (aka. game coordinates) into Rendercoordinates. This can be used to render things at fixed positions in a room. The Render coordinate system is x[0,inf) y[0,inf). It defines the Position on the rendering-plane in the current room.

???- example "Example Code"
    This code render "test" at the position of the mouse cursor independend on if the game is in full screen or not.
    ```lua
    local mousePos = Input.GetMousePosition(true)
    local renderpos = Isaac.WorldToRenderPosition(mousePos) * 2
    Isaac.RenderText("test", renderpos.X, renderpos.Y, 1 ,1 ,1 ,1 )
    ```

___

### World·To·Screen () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) WorldToScreen ( [Vector](Vector.md) pos ) {: .copyable aria-label='Functions' }

Transfers world (aka. game coordinates) into Screen (aka. Window) coordinates. This can be used to render things next to an entity. The Screen coordinate system is x[0,inf) y[0,inf). Normally, it goes till ~500x ~300y. The return vector contains integer values or numbers ending with .5

???- example "Example Code"
    This code render "test" at the position of the player. The text will move with isaac.
    ```lua
    local player = Isaac.GetPlayer()
    local screenpos = Isaac.WorldToScreen(player.Position)
    Isaac.RenderText("test", screenpos.X, screenpos.Y, 1 ,1 ,1 ,1 )
    ```

___

### World·To·Screen·Distance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) WorldToScreenDistance ( [Vector](Vector.md) pos ) {: .copyable aria-label='Functions' }

___

<div class="rgon-only" markdown="1">

### AllMarksFilled () {: aria-label='Functions' }
#### int AllMarksFilled ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Checks if a given character has completed all marks and returns an integer representing the highest difficulty it was accomplished in.

???- info "Note"
	The difficulties are as follows:

	- `0` - None
	- `1` - Normal
	- `2` - Hard

___

### AllTaintedCompletion () {: aria-label='Functions' }
#### int AllTaintedCompletion ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [TaintedMarksGroup](enums/TaintedMarksGroup.md) Group) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Checks if a given character has completed all the tainted unlock-related marks and returns an integer representing the highest difficulty it was accomplished in.

???- info "Note"
	The difficulties are as follows:

	- `0` - None
	- `1` - Normal
	- `2` - Hard

___

### CanStartTrueCoop () {: aria-label='Functions' }
#### boolean CanStartTrueCoop ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CenterCursor () {: aria-label='Functions' }
#### void CenterCursor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Moves the Windows mouse cursor to the center of the game window. This is a niche but useful feature if you want precise cursor control. It will not move the cursor if Isaac.exe loses focus.

???- info "Note"
    Keep in mind that the screen center is not necessarily the center of the room; it is the center of the game window (or the actual screen when running in fullscreen).

___

### ClearBossHazards () {: aria-label='Functions' }

#### void ClearBossHazards ( boolean IgnoreNPCs = false ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

清除所有弹幕。如果 `IgnoreNPCs` 为 false，还会清除所有能够关闭门的非友方 NPC。

___

### ClearChallenge () {: aria-label='Functions' }
#### void ClearChallenge ( int challengeid) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the challenge of the corresponding `challengeid` to completed.

___

### ClearCompletionMarks () {: aria-label='Functions' }
#### void ClearCompletionMarks ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Deletes all completion marks for a given character.

___

### CreateTimer () {: aria-label='Functions' }
#### [EntityEffect](https://wofsauge.github.io/IsaacDocs/rep/EntityEffect.html) CreateTimer ( function Function, int Interval, int Times, boolean Persistent ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Spawns a timer EntityEffect. This entity starts running the `Function` function after `Interval` frames and repeats it `Times` times. `Persistent` controls whether this timer "dies" in the current room or persists across rooms.

???- info "Timer behavior"
    This timer is called every game update. This means the timer only takes into consideration frames in which the game is actively running, not paused, and uses update frames for its Delay parameter (30 frames per second). 
	
	If your use case requires that a timer takes paused time into account, stick with a custom timer running on a RENDER callback.

___

### CreateWeapon () {: aria-label='Functions' }
#### [Weapon](Weapon.md) CreateWeapon ( [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) Type, [Entity](Entity.md) Owner ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Creates and returns a [Weapon](Weapon.md) object. It is not automatically useable by `owner` and [EntityPlayer:SetWeapon](EntityPlayer.md#setweapon) must be used in tandem.
___

### DestroyWeapon () {: aria-label='Functions' }
#### void DestroyWeapon ( [Weapon](Weapon.md) Weapon ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Destroys the provided [Weapon](Weapon.md) object.

___

### DrawLine () {: aria-label='Functions' }
#### void DrawLine ( [Vector](Vector.md) StartPos, [Vector](Vector.md) EndPos, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor) StartColor, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor) EndColor, int Thickness ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Draws a line between the two given positions this render frame.

___

### DrawQuad () {: aria-label='Functions' }
#### void DrawQuad ( [Vector](Vector.md) TopLeftPos, [Vector](Vector.md) TopRightPos, [Vector](Vector.md) BottomLeftPos, [Vector](Vector.md) BottomRightPos, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor) Color, int Thickness ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Draws a line between the two given positions this render frame. Internally the game uses its own struct for this, DestinationQuad, but I haven't gotten to adding that to Lua yet :crocodile:

___

### FillCompletionMarks () {: aria-label='Functions' }
#### void FillCompletionMarks ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Completes all completion marks for a given character.
___

### FindInCapsule () {: aria-label='Functions' }
#### [Entity](Entity.md)[] FindInCapsule ( [Capsule](Capsule.md) Capsule, [EntityPartitions](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityPartition.html) Partitions = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Return entities inside of given capsule, filtered by partitions mask.
___

### FindTargetPit () {: aria-label='Functions' }
#### int FindTargetPit ( [Vector](Vector.md) Position, [Vector](Vector.md) TargetPosition, int PitIndex = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetAchievementIdByName () {: aria-label='Functions' }
#### int GetAchievementIdByName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets the Achievement ID By Name.
___

### GetAllowedDoorsMaskForRoomShape () {: aria-label='Functions' }
#### [DoorMask](enums/DoorMask.md) GetAllowedDoorsMaskForRoomShape ( [RoomShape](https://wofsauge.github.io/IsaacDocs/rep/enums/RoomShape.html) RoomShape ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a [DoorMask](enums/DoorMask.md) representing all [DoorSlots](https://wofsauge.github.io/IsaacDocs/rep/enums/DoorSlot.html) allowed for the given [RoomShape](https://wofsauge.github.io/IsaacDocs/rep/enums/RoomShape.html).

___

### GetAxisAlignedUnitVectorFromDir () {: aria-label='Functions' }
#### [Vector](Vector.md) GetAxisAlignedUnitVectorFromDir ( [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html) Direction = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBackdropIdByName () {: aria-label='Functions' }
#### int GetBackdropIdByName ( string BackdropName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBossColorIdxByName () {: aria-label='Functions' }
#### int GetBossColorIdxByName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets the boss color index by name. The index is usually the subtype the boss needs to become the desired color. You must give your color entry a name in the XML for this to work; a suffix usually does not work because it is not mandatory.
___

### GetButtonsSprite () {: aria-label='Modified Functions' }
#### [Sprite](Sprite.md) GetButtonsSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the controller-buttons sprite.

___

### GetClipboard () {: aria-label='Functions' }
#### string GetClipboard ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets the contents of the clipboard as long as they are in text form, otherwise it will just return nil.
___

### GetCollectibleSpawnPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetCollectibleSpawnPosition ( [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCompletionMark () {: aria-label='Functions' }
#### int GetCompletionMark ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [CompletionType](enums/CompletionType.md) Mark) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets a completion mark value for a specific character, value from `0` to `2` (0 = not accomplished, 1 = normal, 2 = hard).

___

### GetCompletionMarks () {: aria-label='Functions' }
#### table GetCompletionMarks ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table containing all the marks for the character.

???- info "Table structure & usage"
	- The table has the following fields: 
		* PlayerType: containing the [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) associated to the marks
		* MomsHeart: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Isaac: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Satan: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* BossRush: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* BlueBaby: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Lamb: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* MegaSatan: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* UltraGreed: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Hush: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* UltraGreedier: Mostly redundant with UltraGreed when it has a value of 2, no need to set it
		* Delirium: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Mother: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Beast: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
			```lua
			local marks = Isaac.GetCompletionMarks(0)
			if (marks.MomsHeart > 0) then
				print("got mom")
			end
			if (marks.Lamb >= 2) then
				print("GOATED ON H4RD")
			end
			if (Isaac.GetCompletionMarks(0).Delirium > 0) then --doing it the lazy way, fitting deliriums theme
				print("Got Deli")
			end
			```

___

### GetCurrentStageConfigId () {: aria-label='Functions' }
#### [StbType](enums/StbType.md) GetCurrentStageConfigId ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets the current stageconfigId/stbType, or whatever you wanna call the id of the stages.xml, for the current stage.
___

### GetCursorSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetCursorSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the cursor sprite that is rendered when ``Options.MouseControl`` is set to true. 

___

### GetCutsceneIdByName () {: aria-label='Functions' }
#### table GetCutsceneIdByName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets the Cutscene ID By Name.

___

### GetDwmWindowAttribute () {: aria-label='Functions' }
#### [DwmWindowAttribute](enums/DwmWindowAttribute.md) GetDwmWindowAttribute ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetEntitySubTypeByName () {: aria-label='Functions' }
#### int GetEntitySubTypeByName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets the entity SubType by entity name.

___

### GetGiantBookIdByName () {: aria-label='Functions' }
#### int GetGiantBookIdByName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets a GiantBook Id by name. For vanilla giantbooks, the png filename, from the gfx xml attribute, is used as the giantbook name.

___

### GetLoadedModules () {: aria-label='Functions' }
#### table GetLoadedModules ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a key - value table containing all loaded script files, where the key is the name or path of a given script file, and the value the return value of that file after loading. (In most cases its true or a table)

___

### GetLocalizedString () {: aria-label='Functions' }
#### string GetLocalizedString ( string Category, string Key, int Language ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
#### string GetLocalizedString ( string Category, string Key, string LanguageCode ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the translation string associated with the given key in the given category. The translation is given in the language ID/language code given as parameter.

___

### GetModChallengeClearCount () {: aria-label='Functions' }
#### int GetModChallengeClearCount ( int challengeid ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the number of times a custom challenge was cleared. It resets if its ever set as not Done.
___

### GetNanoTime () {: aria-label='Functions'}
#### int GetNanoTime ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a high-resolution timestamp in nanoseconds. Useful for evaluating the performance cost of functions in a non-test environment or for high-precision clocks.

???- info "Note"
	The clock is precise enough to detect the time that passed between two subsequent calls of `Isaac.GetNanoTime()`

___

### GetNullItemIdByName () {: aria-label='Functions' }
#### int GetNullItemIdByName ( string NullItemName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPersistentGameData () {: aria-label='Functions' }
#### [PersistentGameData](PersistentGameData.md) GetPersistentGameData ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPoolIdByName () {: aria-label='Functions' }
#### [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) GetPoolIdByName ( string PoolName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the ID of a given custom pool. Returns `-1` if the pool is not found.

___

### GetRenderPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetRenderPosition ( [Vector](Vector.md) Position, boolean Scale = true ) {: .copyable aria-label='Functions' }        [ ](#){: .rgonorplus .tooltip .badge }

___

### GetString () {: aria-label='Functions' }
#### string GetString ( string Category, string Key ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the translation string associated with the given key in the given category. The translation is given in the currently selected language.

___

### GetWindowTitle () {: aria-label='Functions' }
#### string GetWindowTitle ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the appended text on the game's window title.

___

### IsChallengeDone () {: aria-label='Functions' }
#### boolean IsChallengeDone ( int challengeid ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if the challenge of the corresponding challengeid is completed.

___

### IsInGame () {: aria-label='Functions' }
#### boolean IsInGame ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if `Game` is non-nil and the current state is correct.

___

### LevelGeneratorEntry () {: aria-label='Functions' }
#### [LevelGeneratorEntry](LevelGeneratorEntry.md) LevelGeneratorEntry ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Creates a new blank [LevelGeneratorEntry](LevelGeneratorEntry.md) object.

___

### MarkChallengeAsNotDone () {: aria-label='Functions' }
#### void MarkChallengeAsNotDone ( int challengeid ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the challenge as not done.

___

### PlayCutscene () {: aria-label='Functions' }
#### int PlayCutscene ( int ID, boolean ClearGameState = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Plays the Cutscene of the provided ID. Use Isaac.GetCutsceneIdByName to get the IDs, or the enum for the vanilla ones if you prefer.

___

### RenderCollectionItem () {: aria-label='Functions' }
#### void RenderCollectionItem ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, [Vector](Vector.md) Position, [Vector](Vector.md) Scale = Vector.One, [Color](Color.md) Color = Color.Default ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Renders item collection sprite from collection menu/death screen. 
___

### ReworkBirthright () {: aria-label='Functions' }
#### void ReworkBirthright ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) playerType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Marks the player's birthright as reworked, making the game not execute the item's original passive logic.
Can only be set during mod load.

___

### ReworkCollectible () {: aria-label='Functions' }
#### void ReworkCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Marks the collectible as reworked, making the game not execute the item's original passive logic.
Can only be set during mod load.
**NOTE** Does not prevent the UseActiveItem logic from running.

___

### ReworkTrinket () {: aria-label='Functions' }
#### void ReworkTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) trinket ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Marks the trinket as reworked, making the game not execute the trinket's original passive logic.
Can only be set during mod load.

___

### SetClipboard () {: aria-label='Functions' }
#### boolean SetClipboard ( string ClipboardData ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the contents of the clipboard to the provided string.

___

### SetCompletionMark () {: aria-label='Functions' }
#### void SetCompletionMark ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [CompletionType](enums/CompletionType.md) Mark, int Value) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets a completion mark of a character to match a specific value from `0` to `2` (0 = not accomplished, 1 = normal, 2 = hard).

___

### SetCompletionMarks () {: aria-label='Functions' }
#### void SetCompletionMarks ( table Marks ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the completion marks of a character to match an input table. Requires a table containing all the marks for the character, getting it from [GetCompletionMarks](Isaac.md#getcompletionmarks) is advised for convenience.

???- info "Table structure & usage"
	- The table needs the following fields: 
		* PlayerType: containing the [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) asociated to the marks
		* MomsHeart: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Isaac: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Satan: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* BossRush: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* BlueBaby: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Lamb: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* MegaSatan: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* UltraGreed: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Hush: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* UltraGreedier: Mostly redundant with UltraGreed when it has a value of 2, no need to set it
		* Delirium: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Mother: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
		* Beast: value of [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 0-2 indicating the completion
			```lua
			local marks = Isaac.GetCompletionMarks(0) --getting the current table
			marks.MomsHeart = 2 --Isaac now will have the hard mark on MHeart
			marks.Satan = 1 --Isaac will now have the normal mark on Satan
			marks.BlueBaby = 0 --Removes the BlueBaby Mark if its present
			Isaac.SetCompletionMarks(marks) --Impacts the changes on the player
			```
___

### SetCurrentFloorBackdrop () {: aria-label='Functions' }
#### void SetCurrentFloorBackdrop ( int BackdropId ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Changes the default room backdrop for the current floor to match the input ID. This change does not persist when saving or continuing, so account for that.

___

### SetCurrentFloorMusic () {: aria-label='Functions' }
#### void SetCurrentFloorMusic ( int MusicId ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Changes the music track for the current floor to match the input ID. This change does not persist when saving or continuing, so account for that.
___

### SetCurrentFloorName () {: aria-label='Functions' }
#### void SetCurrentFloorName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Changes the display name for the current floor to match the input ID. This change does not persist when saving or continuing, so account for that.

___

### SetDwmWindowAttribute () {: aria-label='Functions' }
#### void SetDwmWindowAttribute ( [DwmWindowAttribute](enums/DwmWindowAttribute.md) Attribute ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetIcon () {: aria-label='Functions' }
#### void SetIcon ( int IsaacIcon OR string IconPath, boolean BypassSize) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the 16x16 icon located on the game window. Does not update the icon elsewhere, such as the task bar.

`IsaacIcon` is `0` for the normal icon, `1` for the Tainted icon.

`IconPath` accepts a path to a .ico file.

`BypassSize` bypasses the 16x16 resolution cap.

___

### SetWindowTitle () {: aria-label='Functions' }
#### void SetWindowTitle ( string Title ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the appended text on the game's window title.

___

### ShowErrorDialog () {: aria-label='Functions' }
#### [DialogReturn](enums/DialogReturn.md) ShowErrorDialog ( string Title, string Text, [DialogIcons](enums/DialogIcons.md) Icon = DialogIcons.ERROR, [DialogButtons](enums/DialogButtons.md) Buttons = DialogButtons.OK ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Displays a Win32 message box. Can be controlled with the `icon` and `buttons` parameters. Returns a [`DialogReturn`](enums/DialogReturn.md) value that indicates the button pressed.

???- info "Note"
	Keep in mind that a gamepad will not work for this popup; you will need to use a mouse, keyboard, or touchscreen. The window title may not appear in some environments, such as Steam Deck, so do not rely on it too heavily.
___

### SpawnBoss () {: aria-label='Functions' }
#### [EntityNPC](EntityNPC.md) SpawnBoss ( int Type, int Variant, int SubType, [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, [Entity](Entity.md) Spawner, int Seed = ? ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Spawns an NPC and forces it to be a boss. It returns true for IsBoss(), gives the entity a boss bar, plays the boss-end jingle on death in appropriate rooms, and provides other qualities expected of a boss entity, even if the entity is not normally a boss.

___

### StartNewGame () {: aria-label='Functions' }
#### void StartNewGame ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [Challenge](https://wofsauge.github.io/IsaacDocs/rep/enums/Challenge.html) Challenge = ChallengeType.CHALLENGE_NULL, [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) Mode = Difficulty.DIFFICULTY_NORMAL, int Seed = Random, boolean IsCustomRun = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
#### void StartNewGame ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [Challenge](https://wofsauge.github.io/IsaacDocs/rep/enums/Challenge.html) Challenge, [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) Mode, [Seeds](https://wofsauge.github.io/IsaacDocs/rep/Seeds.html) Seeds ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Starts a new game using the specified arguments. Can be used from the main menu.

Setting IsCustomRun to true will disable achievements for the run. Alternatively, an overload accepts a [Seeds](https://wofsauge.github.io/IsaacDocs/rep/Seeds.html) object to use the current seed and all of its modifiers.

___

### TriggerWindowResize () {: aria-label='Functions' }
#### void TriggerWindowResize ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Simulates a window resize, useful to refresh some option changes like `MaxRenderScale`.

___

### UnClearChallenge () {: aria-label='Functions' }
#### void UnClearChallenge ( int challengeid) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the challenge of the corresponding `challengeid` to not completed. While it does work with vanilla challenges, it is not recommended to use it on those, as there are no instances of challenges being uncompleted in vanilla, so it could lead to unexpected behaviour in specific scenarios. 

___

### WorldToMenuPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) WorldToMenuPosition ( [MainMenu](enums/MainMenuType.md) MenuId, [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Converts the World position from input to a pinned main menu position that varies depending on the enum selected. It's important to reconvert this every frame, in a similar fashion to WorldToRender, in order to properly render when menus are changed or the window is resized.

___

### RenderToWorld () {: aria-label='Functions' }
#### [Vector](Vector.md) RenderToWorld ( [Vector](Vector.md) Pos ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Transfers Render coordinates into World coordinates.

Unlike [Isaac.ScreenToWorld](https://wofsauge.github.io/IsaacDocs/rep/Isaac.html#screentoworld) (which transfers Window coordinates into World coordinates), this is the true inverse of [Isaac.WorldToScreen](https://wofsauge.github.io/IsaacDocs/rep/Isaac.html#worldtoscreen) (which transfers World coordinates into Render coordinates).

???- info "Screen coordinate systems"
	The game uses 2 distinct coordinate systems when interacting with the Screen:

	- "Window" coordinates: the actual pixel position within the game window (OS-level).
	- "Render" coordinates: an abstract coordinate system independent of window size or scaling.

	Almost all functions that are used to interact with the screen use or return a position in **Render** coordinates.
	The only 2 exceptions are:

	- `Isaac.ScreenToWorld`: which converts **Window** coordinates into World coordinates.
	- `Input.GetMousePosition(false)`: which returns the mouse position in **Window** coordinates.

???- info "Pixel snapping behavior"
	Alongside converting the World coordinates into Render coordinates, `Isaac.WorldToScreen` snaps the render coordinates to the closest pixel perfect position.
	This means that converting Render coordinates into World coordinates, then back into Render coordinates is not guaranteed to return the original result; unless
	it is in a pixel perfect position.

___

### LoadModDataFromFolder () {: aria-label='Functions' }
#### void LoadModDataFromFolder ( string FolderName ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Similar to [LoadModData](https://wofsauge.github.io/IsaacDocs/rep/Isaac.html#loadmoddata), but lets you read the saveX.dat file from any existing mod data folder, even if that mod is not currently enabled.

___

</div>
