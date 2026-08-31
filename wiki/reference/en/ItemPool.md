---
tags:
  - Class
---
# Class "ItemPool"

???+ info
    You can get this class by using the following function:

    * [Game:GetItemPool()](Game.md#getitempool)

    ???+ example "Example Code"
        `Game():GetItemPool()`

## Functions

### Add·Bible·Upgrade () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddBibleUpgrade ( int Add, [ItemPoolType](enums/ItemPoolType.md) PoolType ) {: .copyable aria-label='Functions' }

___

<div class="rgon-extension" markdown="1">

### AddBibleUpgrade () {: aria-label='Functions' }
#### void AddBibleUpgrade ( int Add, [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>

### Add·Room·Blacklist () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddRoomBlacklist ( [CollectibleType](enums/CollectibleType.md) Item ) {: .copyable aria-label='Functions' }
Adds a given item to the blacklist. This item can no longer be chosen from itempools while the player is inside the current room. This effectively prevents the item from appearing.

When the player changes the room, the Blacklist gets reset.

___

### Force·Add·Pill·Effect () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [PillColor](enums/PillColor.md) ForceAddPillEffect ( [PillEffect](enums/PillEffect.md) ID ) {: .copyable aria-label='Functions' }
Forces a pill effect to be in the pool, usually for challenges, returns PillColor for that effect.
___

### Get·Card () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Card](enums/Card.md) GetCard ( int Seed, boolean Playing, boolean Rune, boolean OnlyRunes ) {: .copyable aria-label='Functions' }

___

### Get·Collectible () {: aria-label='Functions' }
[ ](#){: .rep .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetCollectible ( [ItemPoolType](enums/ItemPoolType.md) PoolType, boolean Decrease = false, int Seed = Random(), [CollectibleType](enums/CollectibleType.md) DefaultItem = CollectibleType.COLLECTIBLE_NULL ) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetCollectible ( [ItemPoolType](enums/ItemPoolType.md) PoolType, boolean Decrease = false, int Seed = Random(), [CollectibleType](enums/CollectibleType.md) DefaultItem = CollectibleType.COLLECTIBLE_NULL, [ItemPoolType](enums/ItemPoolType.md) BackupPoolType = ItemPoolType.POOL_NULL ) {: .copyable aria-label='Functions' }

???- note "Notes"
    Already accounts for effects such as NO!, Chaos, Sacred Orb, T.Lost's Better Items, Magic Skin and Rosary Beads, alongside all of the specific character and challenge restrictions.

    If **DefaultItem** is set to CollectibleType.COLLECTIBLE_NULL and the item pool has run out of repicks, then the game will first try to get a collectible from the Treasure Pool (in Repentance+ can specified with **BackupPoolType**, unless **ItemPoolType** is already the Treasure Pool). If that fails then Breakfast is returned (assuming it doesn't get modified into Magic Skin or Rosary later on).

    If **DefaultItem** is set to anything other than CollectibleType.COLLECTIBLE_NULL, this entire process (excluding the potential Magic Skin or Rosary modification) is skipped, and the specified collectible is returned instead.

___

<div class="rgon-extension" markdown="1">

### GetCollectible () {: aria-label='Modified Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetCollectible ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType, boolean Decrease = false, int Seed = Random(), [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) DefaultItem = CollectibleType.COLLECTIBLE_NULL, [GetCollectibleFlag](enums/GetCollectibleFlag.md) Flags = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Now gives access to the Flags parameter.

???+ warning "Setting both Ban Flags"
    Setting both the `BAN_ACTIVE` and the `BAN_PASSIVE` flag will cause the function to always return either the `DefaultItem` or `CollectibleType.COLLECTIBLE_BREAKFAST`

___
## Functions

</div>

### Get·Last·Pool () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [ItemPoolType](enums/ItemPoolType.md) GetLastPool ( ) {: .copyable aria-label='Functions' }

___

### Get·Pill () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [PillColor](enums/PillColor.md) GetPill ( int Seed ) {: .copyable aria-label='Functions' }

___

### Get·Pill·Effect () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [PillEffect](enums/PillEffect.md) GetPillEffect ( [PillColor](enums/PillColor.md) PillColor, [EntityPlayer](EntityPlayer.md) Player = nil ) {: .copyable aria-label='Functions' }

Will return the pill effect that corresponds to the passed pill color. This will work properly even if the player has not yet identified the pill color (by using one or more pills of that color). It is recommended to always pass the corresponding player because if a player has Lucky Foot, PHD, Virgo, or False PHD, the resolved pill effect will change from what was assigned by default at the beginning of the run.

Returns -1 if passed `PillColor.NULL` (0) or a value of 2048. Returns `PillEffect.BAD_GAS` (0) if passed an invalid pill color (e.g. 15 through 2047 or 2063+).

___

### Get·Pool·For·Room () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [ItemPoolType](enums/ItemPoolType.md) GetPoolForRoom ( [RoomType](enums/RoomType.md) RoomType, int Seed ) {: .copyable aria-label='Functions' }

___

### Get·Trinket () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [TrinketType](enums/TrinketType.md) GetTrinket ( boolean DontAdvanceRNG = false ) {: .copyable aria-label='Functions' }

___

### Identify·Pill () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void IdentifyPill ( [PillColor](enums/PillColor.md) PillColor ) {: .copyable aria-label='Functions' }

___

### Is·Pill·Identified () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsPillIdentified ( [PillColor](enums/PillColor.md) PillColor ) {: .copyable aria-label='Functions' }

Once the player takes PHD, Virgo, or False PHD, this method will always return true, even if the player has not already seen or used the pill on the run thus far. (This is because this method dictates when the "???" text should be shown as the pill description, and these collectibles will always show the "revealed" text.)

___

### Remove·Collectible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean RemoveCollectible ( [CollectibleType](enums/CollectibleType.md) Collectible ) {: .copyable aria-label='Functions' }
Removes a collectible from the itempool. Returns true if given item did exist in the pool before.

___

### Remove·Trinket () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean RemoveTrinket ( [TrinketType](enums/TrinketType.md) Trinket ) {: .copyable aria-label='Functions' }

___

### Reset·Room·Blacklist () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ResetRoomBlacklist ( ) {: .copyable aria-label='Functions' }
Clears the current item black list.

When the player changes the room, this function gets called automatically.

___

### Reset·Trinkets () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ResetTrinkets ( ) {: .copyable aria-label='Functions' }

___

<div class="rgon-only" markdown="1">

### AddCollectible () {: aria-label='Functions' }
#### void AddCollectible ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType, table | table[] PoolItems ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

Adds the provided Lua PoolItem objects to the specified Pool permanently, as if they were defined in a `itempools.xml` file.

The `PoolItems` parameter can be either a single Lua PoolItem object or an array of them.

???- info "Lua PoolItem format"
    |Field|Type|Comment|
    |:--|:--|:--|
    | itemID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | `Default = COLLECTIBLE_NULL` |
    | name | string | `Optional`<br /> Alternative to `itemID` |
    | weight | float | `Default = 1.0` |
    | decreaseBy | float | `Default = 0.5` |
    | removeOn | float | `Default = 0.1` |

    All field names are case insensitive

___

### AddTemporaryCollectible () {: aria-label='Functions' }
#### void AddTemporaryCollectible ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType, table | table[] PoolItems ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

Adds the provided Lua PoolItem objects to the specified Pool, but only for the current run.

The `PoolItems` parameter can be either a single Lua PoolItem object or an array of them.

???- info "Lua PoolItem format"
    |Field|Type|Comment|
    |:--|:--|:--|
    | itemID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | `Default = COLLECTIBLE_NULL` |
    | name | string | `Optional`<br /> Alternative to `itemID` |
    | weight | float | `Default = 1.0` |
    | decreaseBy | float | `Default = 0.5` |
    | removeOn | float | `Default = 0.1` |

    All field names are case insensitive

???- info "Temporary Collectible behavior"
    Temporary collectibles are automatically added and removed when continuing or exiting a run, as well as when returning to a previous state that did or did not contain the collectible while using Glowing Hourglass.

___

### CanSpawnCollectible () {: aria-label='Functions' }
#### boolean CanSpawnCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean ignoreLocked ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "IgnoreLocked"
    If `IgnoreLocked` is set to true, this function will return true for items that could appear but are locked behind achievements.

    It will still return false if the item was removed from the item pool or if it can't appear because other effects (Tainted Lost offensive items mechanic or NO! trinket effect).

___

### GetBibleUpgrades () {: aria-label='Functions' }
#### int GetBibleUpgrades ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the number of Bible collectibles added to a pool.

___

### GetCardEx () {: aria-label='Functions' }
#### [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) GetCardEx ( int Seed, int SpecialChance, int RuneChance, int SuitChance, boolean AllowNonCards ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
A more sophisticated version of [ItemPool:GetCard()](https://wofsauge.github.io/IsaacDocs/rep/ItemPool.html#getcard) that allows individual chances to be defined.

___

### GetCollectibleFromList () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetCollectibleFromList ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)[] ItemList, int Seed = Random(), [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) DefaultItem = CollectibleType.COLLECTIBLE_BREAKFAST, boolean AddToBlacklist = true, boolean ExcludeActiveItems = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollectiblesFromPool () {: aria-label='Functions' }
#### table GetCollectiblesFromPool ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of collectibles registered in the specified pool. The table contains the following fields

|Field|Type|Comment|
|:--|:--|:--|
| itemID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | |
| initialWeight | float | |
| weight | float | |
| decreaseBy | float | |
| removeOn | float | |
| isUnlocked | boolean | |

___

### GetNumAvailableTrinkets () {: aria-label='Functions' }
#### int GetNumAvailableTrinkets ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the amount of trinkets available in the item pool.

___

### GetNumItemPools () {: aria-label='Functions' }
#### int GetNumItemPools ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Retrieves the total number of item pools in the game, including custom item pools.

___

### GetPillColor () {: aria-label='Functions' }
#### [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) GetPillColor ( [PillEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/PillEffect.html) ID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the `PillColor` matching the specified `PillEffect`, or `-1` if the effect is not in the rotation.

This is currently unaffected by pill modifiers such as PHD and False PHD.

___

### GetRandomPool () {: aria-label='Functions' }
#### [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) GetRandomPool ( [RNG](RNG.md) RNG, boolean AdvancedSearch = false, [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html)[] Filter = {}, boolean IsWhitelist = false) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Picks a random pool in an identical manner to Chaos, where pools with more items have a higher probability of being chosen compared to those with fewer items.

By default, this function follows the same rules as Chaos, so it can return only pools for the current mode. Set `Advanced Search` to true to bypass these restrictions.

???+ info "Advanced Search"
    Setting `Advanced Search` to true allows you to make use of the `Filter` parameter.

    Normally, `Filter` acts as a blacklist of unwanted item pools. Setting `IsWhitelist` to true instead makes it the list of pools to choose from.

???+ example "Pick Pool From List"
    This code picks a random pool from the available Beggar pools.

    ```lua
    local PoolList = {
        ItemPoolType.POOL_BEGGAR,
        ItemPoolType.POOL_DEMON_BEGGAR,
        ItemPoolType.POOL_KEY_MASTER,
        ItemPoolType.POOL_BATTERY_BUM,
        ItemPoolType.POOL_BOMB_BUM,
        ItemPoolType.POOL_ROTTEN_BEGGAR
    }

    local rng = RNG() -- replace this with your own rng
    local randomPool = Game():GetItemPool():GetRandomPool(rng, true, PoolList, true)
    ```

???+ example "Pick Pool From Vanilla"
    This code picks a random pool from the vanilla pools.

    ```lua
    local itemPool = Game():GetItemPool()

    local CustomPools = {}

    -- Put all custom pools within the Filter
    for i = 31, itemPool:GetNumItemPools() - 1 do
        table.insert(CustomPools, i)
    end

    local rng = RNG(Random()) -- replace this with your own rng
    local randomPool = Game():GetItemPool():GetRandomPool(rng, true, CustomPools, false)
    ```

___

### GetRemovedCollectibles () {: aria-label='Functions' }
#### table GetRemovedCollectibles ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of [collectibles](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) removed from all pools.

???- example "Example Code"
    This code checks if the sad onion has been removed.

    ```lua
    local removedCollectibles = itemPool:GetRemovedCollectibles()

    if removedCollectibles[CollectibleType.COLLECTIBLE_SAD_ONION] then
      print("Sad onion removed!")
    end
    ```

___

### GetRoomBlacklistedCollectibles () {: aria-label='Functions' }
#### table GetRoomBlacklistedCollectibles ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of [collectibles](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) blacklisted in the current room.

???- example "Example Code"
    This code checks if the sad onion has been removed.

    ```lua
    local blacklistedCollectibles = itemPool:GetRoomBlacklistedCollectibles()

    if blacklistedCollectibles[CollectibleType.COLLECTIBLE_SAD_ONION] then
      print("Sad onion blacklisted!")
    end
    ```

___

### HasCollectible () {: aria-label='Functions' }
#### boolean HasCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if collectible is available in item pools, `false` otherwise.

___

### HasTrinket () {: aria-label='Functions' }
#### boolean HasTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if trinket is currently available in trinket pool, `false` otherwise.

___

### PickCollectible () {: aria-label='Functions' }
#### table PickCollectible ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType, boolean Decrease = false, [RNG](RNG.md) RNG = RNG(), [GetCollectibleFlag](enums/GetCollectibleFlag.md) Flags = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the raw result of [GetCollectible()](ItemPool.md#getcollectible), without any of the filtering applied by the original function.
If the pool has completely ran out of repicks then this function will return `nil`.

If `RNG` is not set, it is initialized with `RNG(Random(), 4)`.

The table contains the following fields:

|Field|Type|Comment|
|:--|:--|:--|
| itemID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | |
| initialWeight | float | |
| weight | float | |
| decreaseBy | float | |
| removeOn | float | |
| isUnlocked | boolean | |

???+ info "Differences with GetCollectible"
    For reference GetCollectible() **Gives Up** after either this function has failed to pick an Unlocked collectible 20 times in a row or has failed to produce any result at all (nil).
    
    - Does not generate a [Glitched Item](ProceduralItem.md) when having the `CollectibleType.COLLECTIBLE_TMTRAINER` effect.
    
    - Does not randomize the pool when having the `CollectibleType.COLLECTIBLE_CHAOS` effect.
    
    - Does not attempt to get a collectible from `ItemPoolType.POOL_TREASURE` if **Giving up**.
    
    - Does not morph the collectible into `CollectibleType.COLLECTIBLE_BREAKFAST` if **Giving up**.
    
    - Does not attempt to morph the collectible into `CollectibleType.COLLECTIBLE_BIBLE`, `CollectibleType.COLLECTIBLE_MAGIC_SKIN` or `CollectibleType.COLLECTIBLE_ROSARY`
    
    - Does not trigger the [MC_PRE_GET_COLLECTIBLE](https://wofsauge.github.io/IsaacDocs/rep/enums/ModCallbacks.html?h=modcall#mc_post_get_collectible) and [MC_POST_GET_COLLECTIBLE](https://wofsauge.github.io/IsaacDocs/rep/enums/ModCallbacks.html?h=modcall#mc_post_get_collectible) callback.

___

### RemoveTemporaryCollectible () {: aria-label='Functions' }
#### void RemoveTemporaryCollectible ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) PoolType, table | table[] PoolItems ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

Removes the provided Temporary Collectibles from the specified Pool, assuming they exist.

The PoolItem object **MUST** be equal (in terms of field values) to the one that was added in [AddTemporaryCollectible](ItemPool.md#addtemporarycollectible)

The `PoolItems` parameter can be either a single Lua PoolItem object or an array of them.

???- info "Lua PoolItem format"
    |Field|Type|Comment|
    |:--|:--|:--|
    | itemID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | `Default = COLLECTIBLE_NULL` |
    | name | string | `Optional`<br /> Alternative to `itemID` |
    | weight | float | `Default = 1.0` |
    | decreaseBy | float | `Default = 0.5` |
    | removeOn | float | `Default = 0.1` |

    All field names are case insensitive

___

### ResetCollectible () {: aria-label='Functions' }
#### void ResetCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Makes the collectible available again, allowing it to spawn naturally even if it was previously removed. It also restores all instances of the collectible to their **initialWeight** in every item pool.

___

### SetLastPool () {: aria-label='Functions' }
#### void SetLastPool ( [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### UnidentifyPill () {: aria-label='Functions' }
#### void UnidentifyPill ( [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) Pill ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Resets a pill to its unidentified (???) state.

___

</div>
