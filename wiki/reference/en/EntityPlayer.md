---
tags:
  - Class
  - Player
---
# Class "EntityPlayer"

???+ info
    You can get this class by using the following function:

    * [Entity.ToPlayer()](Entity.md#toplayer)
    * [EntityFamiliar.Player](EntityFamiliar.md#player)
    * [EntityPlayer.GetMainTwin()](EntityPlayer.md#getmaintwin)
    * [EntityPlayer.GetOtherTwin()](EntityPlayer.md#getothertwin)
    * [EntityPlayer.GetSubPlayer()](EntityPlayer.md#getsubplayer)
    * [Game.GetNearestPlayer()](Game.md#getnearestplayer)
    * [Game.GetPlayer()](Game.md#getplayer)
    * [Game.GetRandomPlayer()](Game.md#getrandomplayer)
    * [Isaac.GetPlayer()](Isaac.md#getplayer)

    ???+ example "Example Code"
        `local player = Isaac.GetPlayer()`

## Class Diagram
--8<-- "en/snippets/EntityClassDiagram.md"
## Functions

### Add·Black·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddBlackHearts ( int BlackHearts ) {: .copyable aria-label='Functions' }

Adds Black hearts to the player. 1 unit is half a heart. Remove them with negative numbers.

???- example "Example Code"
    This code adds 1 full black heart to the player.
    ```lua
    Isaac.GetPlayer():AddBlackHearts(2)
    ```

___

### Add·Blood·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddBloodCharge ( int Amount ) {: .copyable aria-label='Functions' }

Adds to the amount of Blood Charge the player has. Blood Charge does not do anything on characters besides Tainted Bethany.

___

### Add·Blue·Flies () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) AddBlueFlies ( int Amount, [Vector](Vector.md) Position, [Entity](Entity.md) Target ) {: .copyable aria-label='Functions' }
???- info "Amount"
    The trinket **Fish Tail** will always double the `amount` of flies added by this function.

___

### Add·Blue·Spider () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) AddBlueSpider ( [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }

???- example "Example Code"
    This code spawns 3 blue spiders at the player's position.
    ```lua
    local player = Isaac.GetPlayer()
    for _ = 1, 3 do
	player:AddBlueSpider(player.Position)
    end
    ```

___

### Add·Bombs () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddBombs ( int Amount ) {: .copyable aria-label='Functions' }

Adds bombs to the player. Remove them with negative numbers.

???- example "Example Code"
    This code removes 1 bomb from the player.
    ```lua
    Isaac.GetPlayer():AddBombs(-1)
    ```

___

### Add·Bone·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddBoneHearts ( int Hearts ) {: .copyable aria-label='Functions' }

Adds bone hearts to the player. 1 unit is a single bone heart. Remove them with negative numbers.

???- example "Example Code"
    This code adds 1 bone heart to the player.
    ```lua
    Isaac.GetPlayer():AddBoneHearts(1)
    ```

___

### Add·Broken·Hearts () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddBrokenHearts ( int BrokenHearts ) {: .copyable aria-label='Functions' }

Adds broken hearts to the player. 1 unit is one broken heart. Broken hearts can be removed with negative numbers.
???- example "Example Code"
	This code adds 1 broken heart to the player, then takes it away.
	```lua
	Isaac.GetPlayer():AddBrokenHearts(1)
	Isaac.GetPlayer():AddBrokenHearts(-1)
	```
___

### Add·Cache·Flags () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCacheFlags ( [CacheFlag](enums/CacheFlag.md) CacheFlag ) {: .copyable aria-label='Functions' }
Will reevaluate the cache flags provided in the next cache reevaluation.

???- example "Example Code"
    This code will add several cacheflags.
    ```lua
    Isaac.GetPlayer():AddCacheFlags(CacheFlag.CACHE_DAMAGE | CacheFlag.CACHE_FIREDELAY | CacheFlag.CACHE_LUCK)
    ```
___

<div class="rgon-extension" markdown="1">

### AddCacheFlags () {: aria-label='Modified Functions' }
#### void AddCacheFlags ( [CacheFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/CacheFlag.html) CacheFlag, boolean EvaluateItems = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Now accepts an optional `bool` to determine if [EntityPlayer](EntityPlayer.md):EvaluateItems() should be automatically called after adding cache flags. In most cases, you'll want to do this.

___

</div>

### Add·Card () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCard ( [Card](enums/Card.md) ID ) {: .copyable aria-label='Functions' }

___

### Add·Coins () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCoins ( int Amount ) {: .copyable aria-label='Functions' }

Adds coins to the player. Remove them with negative numbers.

???- example "Example Code"
    This code adds 1 coin to the player.
    ```lua
    Isaac.GetPlayer():AddCoins(1)
    ```

___

### Add·Collectible () {: aria-label='Functions' }
[ ](#){: .rep .tooltip .badge }
#### void AddCollectible ( [CollectibleType](enums/CollectibleType.md) Type, int Charge = 0, boolean FirstTimePickingUp = true, [ActiveSlot](enums/ActiveSlot.md) Slot = ActiveSlot.SLOT_PRIMARY, int VarData = 0) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void AddCollectible ( [CollectibleType](enums/CollectibleType.md) Type, int Charge = 0, boolean FirstTimePickingUp = true, [ActiveSlot](enums/ActiveSlot.md) Slot = ActiveSlot.SLOT_PRIMARY, int VarData = 0, [ItemPoolType](enums/ItemPoolType.md) PoolType ) {: .copyable aria-label='Functions' }

Setting **FirstTimePickingUp** to false will not add the consumables (keys, bombs,...) of the item and will cause it to not count towards transformations.

- Slot 0 is default (normal active item)
- Slot 1 is used by Schoolbag
- Slot 2 is used for pocket active items

???- note "Notes"
	Slot 2 cannot be used if character did not start with a pocket active

VarData is used for the storage of a persistent context-sensitive value

???- note "Notes"
	This is a list of all items that make use of VarData:

    - Jar of Wisps: Wisps spawned on next use (Max 12)
	- D Infinity, Blank Card, Clear Rune, Placebo: Current maximum charge (Any value above 0)
	- Hold: Stored poop
	    - Poop Types:
	    - [0] None
	    - [1] Normal
	    - [2] Flies
	    - [3] Fire
	    - [4] Petrified
	    - [5] Toxic
	    - [6] Black
	    - [7] Holy
	    - [8] X-Lax
	    - [9] Fart
	    - [10] Bomb
	    - [11] Explosive Diarrhea
	    - [12+] Empty

___

### Add·Controls·Cooldown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddControlsCooldown ( int Cooldown ) {: .copyable aria-label='Functions' }

___

### Add·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCostume ( [ItemConfigItem](ItemConfig_Item.md) Item, boolean ItemStateOnly ) {: .copyable aria-label='Functions' }

___

### Add·Curse·Mist·Effect () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddCurseMistEffect ( ) {: .copyable aria-label='Functions' }

___

### Add·Dead·Eye·Charge () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddDeadEyeCharge ( ) {: .copyable aria-label='Functions' }

___

### Add·Dollar·Bill·Effect () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddDollarBillEffect ( ) {: .copyable aria-label='Functions' }

___

### Add·Eternal·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddEternalHearts ( int EternalHearts ) {: .copyable aria-label='Functions' }

Adds eternal hearts to the player. 1 unit is half a heart. Remove them with negative numbers.

(Note that eternal hearts automatically turn to full hearts, when you have more than one.)

???- example "Example Code"
    This code adds 1 eternal heart to the player.
    ```lua
    Isaac.GetPlayer():AddEternalHearts(1)
    ```

___

### Add·Friendly·Dip () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) AddFriendlyDip ( int Subtype, [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }

???- note "Dip Subtypes"
    ```lua
    0: normal
    1: red
    2: corny
    3: golden
    4: rainbow
    5: black
    6: holy
    12: stone
    13: flaming
    14: poison
    20: brownie
    ```
___

### Add·Giga·Bombs () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddGigaBombs ( int GigaBombs ) {: .copyable aria-label='Functions' }

???- note "Notes"
	Giga bombs do not add to the bomb counter, make sure to increase the bomb count beforehand!
	You can't add more giga bombs than player's current bomb count.

___

### Add·Golden·Bomb () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddGoldenBomb ( ) {: .copyable aria-label='Functions' }

___

### Add·Golden·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddGoldenHearts ( int Hearts ) {: .copyable aria-label='Functions' }

Adds golden hearts to the player. 1 unit is a single gold heart. Remove them with negative numbers.

???- example "Example Code"
    This code adds 1 golden heart to the player.
    ```lua
    Isaac.GetPlayer():AddGoldenHearts(1)
    ```

___

### Add·Golden·Key () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddGoldenKey ( ) {: .copyable aria-label='Functions' }

___

### Add·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddHearts ( int Hearts ) {: .copyable aria-label='Functions' }

Adds red hearts to the player if there are any empty heart containers. 1 unit is half a heart. Remove health with negative numbers.

???- example "Example Code"
    This code adds 1 full red heart to the player.
    ```lua
    Isaac.GetPlayer():AddHearts(2)
    ```

___

### Add·Item·Wisp () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) AddItemWisp ( [CollectibleType](enums/CollectibleType.md) Collectible, [Vector](Vector.md) Position, boolean AdjustOrbitLayer = false ) {: .copyable aria-label='Functions' }

___

### Add·Jar·Flies () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddJarFlies ( int Flies ) {: .copyable aria-label='Functions' }

___

### Add·Jar·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddJarHearts ( int Hearts ) {: .copyable aria-label='Functions' }

___

### Add·Keys () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddKeys ( int Amount ) {: .copyable aria-label='Functions' }

Adds keys to the player. Remove them with negative numbers.

???- example "Example Code"
    This code adds 1 key to the player.
    ```lua
    Isaac.GetPlayer():AddKeys(1)
    ```

___

### Add·Max·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddMaxHearts ( int MaxHearts, boolean IgnoreKeeper ) {: .copyable aria-label='Functions' }

Adds heart containers to the player. 2 units is a full heart container. Remove them with negative numbers.

???- note "Notes"
    It is possible to add a half heart container to the player. This will appear as a regular heart container but can only be filled half-way.

???- example "Example Code"
    This code adds 1 heart container to the player.
    ```lua
    Isaac.GetPlayer():AddMaxHearts(2, true)
    ```


???+ bug "Bugs"
    IgnoreKeeper does not appear to work as intended.

    Max hearts can be added or removed from Keeper regardless of what this boolean is.
    If Keeper has Greed's Gullet and this boolean is set to false, max hearts cannot be added to Keeper, but can be removed normally.
    If Keeper has Greed's Gullet and this boolean is set to true, Max hearts can be added or removed from Keeper normally.

___

### Add·Minisaac () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) AddMinisaac ( [Vector](Vector.md) Position, boolean PlayAnim = true ) {: .copyable aria-label='Functions' }

___

### Add·Null·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddNullCostume ( [NullItemID](enums/NullItemID.md) NullId ) {: .copyable aria-label='Functions' }

___

### Add·Pill () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddPill ( [PillColor](enums/PillColor.md) Pill ) {: .copyable aria-label='Functions' }

___

### Add·Player·Form·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddPlayerFormCostume ( [PlayerForm](enums/PlayerForm.md) Form ) {: .copyable aria-label='Functions' }
Adds the costume of the given transformation.

___

### Add·Poop·Mana () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddPoopMana ( int Num ) {: .copyable aria-label='Functions' }
Adds (or remove) poop consumables from the player.

___

### Add·Pretty·Fly () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddPrettyFly ( ) {: .copyable aria-label='Functions' }

___

### Add·Rotten·Hearts () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddRottenHearts ( int RottenHearts ) {: .copyable aria-label='Functions' }
Adds rotten hearts to the player. 1 unit is half a heart. Remove rotten hearts with negative numbers.

???- example "Example Code"
    This code adds 1 full rotten heart to the player.
    ```lua
    Isaac.GetPlayer():AddRottenHearts(2)
    ```

___

### Add·Soul·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddSoulCharge ( int Amount ) {: .copyable aria-label='Functions' }

Adds Soul Charge to the player. Soul Charge does not do anything on characters besides Bethany.

___

### Add·Soul·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddSoulHearts ( int SoulHearts ) {: .copyable aria-label='Functions' }

Adds soul hearts to the player. 1 unit is half a heart. Remove them with negative numbers.

???- example "Example Code"
    This code adds 1 full soul heart to the player.
    ```lua
    Isaac.GetPlayer():AddSoulHearts(2)
    ```

___

### Add·Swarm·Fly·Orbital () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) AddSwarmFlyOrbital ( [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }

___

### Add·Trinket () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddTrinket ( [TrinketType](enums/TrinketType.md) Type, boolean FirstTimePickingUp = true ) {: .copyable aria-label='Functions' }

- If the player does not have any open trinket slots, this function will do nothing.
- If the player has an open trinket slot but already has a trinket, the new trinket will go to the first slot and the existing trinket will get pushed back to the second slot.
- If you provide an argument of 0 or an otherwise invalid trinket ID, the game will crash.
- Setting **FirstTimePickingUp** to false will not spawn or add pickups for the item and will not cause it to count towards transformations.

???- example "Example Code"
    This code adds the golden variant of the Swallowed Penny trinket to the player.
    ```lua
    Isaac.GetPlayer():AddTrinket(TrinketType.TRINKET_SWALLOWED_PENNY | TrinketType.TRINKET_GOLDEN_FLAG)
    ```

___

### Add·Wisp () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) AddWisp ( [CollectibleType](enums/CollectibleType.md) Collectible, [Vector](Vector.md) Position, boolean AdjustOrbitLayer = false, boolean DontUpdate = false ) {: .copyable aria-label='Functions' }
The type of Wisp can be defined with the Collectible. If the ID is not corresponding to an active item with a special wisp, it will default to the regular blue wisp.

To access special wisp variant like Delirious forms, you need to add `65536` (1 << 16) to the id. Example: Delirious Monstro has `id = s14`, so the wisps id is `65550`.

___

### Animate·Appear () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateAppear ( ) {: .copyable aria-label='Functions' }
Play the animation that is normally played at the beginning of a stage.
___

### Animate·Card () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AnimateCard ( [Card](enums/Card.md) ID, string AnimName = "Pickup" ) {: .copyable aria-label='Functions' }

___

### Animate·Collectible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AnimateCollectible ( [CollectibleType](enums/CollectibleType.md) Collectible, string AnimName = "Pickup", string SpriteAnimName = "PlayerPickupSparkle" ) {: .copyable aria-label='Functions' }
`AnimName` refers to an animation name in `001.000_player.anm2` (e.g. `Pickup` or `UseItem`). `SpriteAnimName` refers to an animation name in `005.100_collectible.anm2` (e.g. `PlayerPickup` or `PlayerPickupSparkle`).

___

### Animate·Happy () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateHappy ( ) {: .copyable aria-label='Functions' }
Plays the happy animation, played when taking a positive pill.

???- example "Example Code"
    This code plays the happy animation.
    ```lua
    Isaac.GetPlayer():AnimateHappy()
    ```

### Animate·Light·Travel () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateLightTravel ( ) {: .copyable aria-label='Functions' }
Plays the animation that is played when entering the light in the ascent, or entering the cathedral.

???- example "Example Code"
	Plays the animation.
	```lua
	Isaac.GetPlayer():AnimateLightTravel()
	```

___

### Animate·Pickup () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AnimatePickup ( [Sprite](Sprite.md) sprite, boolean HideShadow = false, string AnimName = "Pickup" ) {: .copyable aria-label='Functions' }
Plays a pickup animation using any supplied Sprite object
HideShadow should be usually set to true when rendering a sprite with a custom shadow layer

___

### Animate·Pill () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AnimatePill ( [PillColor](enums/PillColor.md) Pill, string AnimName = "Pickup" ) {: .copyable aria-label='Functions' }

___

### Animate·Pitfall·In () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimatePitfallIn ( ) {: .copyable aria-label='Functions' }
Does 1/2 heart of damage and plays the animation of falling into a pitfall.
___

### Animate·Pitfall·Out () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimatePitfallOut ( ) {: .copyable aria-label='Functions' }
The animation of jumping back out of a pitfall.
___

### Animate·Sad () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateSad ( ) {: .copyable aria-label='Functions' }
Plays the sad animation, played when taking a negative pill.

???- example "Example Code"
	Plays the sad animation.
	```lua
	Isaac.GetPlayer():AnimateSad()
	```
___

### Animate·Teleport () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateTeleport ( boolean Up ) {: .copyable aria-label='Functions' }
The animation played when teleporting into another room.

___

### Animate·Trapdoor () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateTrapdoor ( ) {: .copyable aria-label='Functions' }
Plays the animation of the player jumping down a trapdoor.

???- example "Example Code"
	Plays the animation of jumping down a trapdoor.
	```lua
	Isaac.GetPlayer():AnimateTrapdoor()
	```

___

### Animate·Trinket () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AnimateTrinket ( [TrinketType](enums/TrinketType.md) Trinket, string AnimName = "Pickup", string SpriteAnimName = "PlayerPickupSparkle" ) {: .copyable aria-label='Functions' }

___

### Are·Controls·Enabled () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean AreControlsEnabled ( ) {: .copyable aria-label='Functions' }

___

### Are·Opposing·Shoot·Directions·Pressed () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean AreOpposingShootDirectionsPressed ( ) {: .copyable aria-label='Functions' }
Returns the non-zero joystick direction from the most recent movement input, but goes to zero after the player comes to a stop.
___

### Can·Add·Collectible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean CanAddCollectible ( [CollectibleType](enums/CollectibleType.md) Type = CollectibleType.COLLECTIBLE_NULL ) {: .copyable aria-label='Functions' }

___

### Can·Pick·Black·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickBlackHearts ( ) {: .copyable aria-label='Functions' }
returns true if player has room for more black hearts
___

### Can·Pick·Bone·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickBoneHearts ( ) {: .copyable aria-label='Functions' }
returns true if player has room for more bone hearts
___

### Can·Pick·Golden·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickGoldenHearts ( ) {: .copyable aria-label='Functions' }
returns true if player has room for more golden hearts
___

### Can·Pick·Red·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickRedHearts ( ) {: .copyable aria-label='Functions' }

___

### Can·Pick·Rotten·Hearts () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean CanPickRottenHearts ( ) {: .copyable aria-label='Functions' }
Returns true if player has room for more rotten hearts

___

### Can·Pick·Soul·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickSoulHearts ( ) {: .copyable aria-label='Functions' }
Returns true if player has room for more soul hearts
___

### Can·Pickup·Item () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickupItem ( ) {: .copyable aria-label='Functions' }
Can Player pick up an item right now?
___

### Can·Shoot () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanShoot ( ) {: .copyable aria-label='Functions' }

___

### Can·Turn·Head () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanTurnHead ( ) {: .copyable aria-label='Functions' }
Returns true if head should react to keys or false otherwise
___

### Change·Player·Type () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void ChangePlayerType ( [PlayerType](enums/PlayerType.md) PlayerType ) {: .copyable aria-label='Functions' }
Used to change one player into another player type. For example turning Cain into Maggy.

Changing the player type within MC_POST_PLAYER_INIT will result in the player getting the default items for that character. E.g. Maggy will get her Yum Heart without you having to explicitly add it. Exceptions here include unlockable items (e.g. Isaac's D6) and default numbers of hearts/keys/bombs/coins. You can change the player type after init, but then you're generally responsible for adding any items you might associate with that character.

Changing the player Type into Jacob will also spawn Esau.

___

### Check·Familiar () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void CheckFamiliar ( [FamiliarVariant](enums/FamiliarVariant.md) FamiliarVariant, int TargetCount, [RNG](RNG.md) rng, [ItemConfigItem](ItemConfig_Item.md) SourceItemConfigItem = nil, int FamiliarSubType = -1 ) {: .copyable aria-label='Functions' }

Call this method to spawn the appropriate amount of familiars associated with a custom collectible.

- If the target count specified is less than the current amount of familiars, it will spawn more until the target count is met.
- If the target count specified is than the current amount of familiars, it will despawn familiars until the target count is met.

This is meant to be called in the EvaluateCache callback (when the cache flag is equal to `CacheFlag.CACHE_FAMILIARS`).

In most cases, [:material-language-typescript:IsaacScript](https://isaacscript.github.io/) users should use the [`checkFamiliarFromCollectibles`](https://isaacscript.github.io/isaacscript-common/modules/functions_familiars.html#checkFamiliarFromCollectibles) helper function instead of using this method directly, as it automatically calculates the appropriate target count.

**FamiliarVariant**: In most cases, use the familiar variant for your custom familiar.

**TargetCount**: The expected amount of this FamiliarVariant that this EntityPlayer should have. This argument can simply be how many of an item that the current EntityPlayer owns. However, if you want your familiar to synergize with Monster Manual and Box of Friends, then this argument should be  `EntityPlayer:GetCollectibleNum(collectibleType) + EntityPlayer:GetEffects():GetCollectibleEffectNum(collectibleType)`.

**rng**: Can just be the RNG object from `EntityPlayer.GetCollectibleRNG` of the collectible that spawns the familiar.

**SourceItemConfigItem**: The `ItemConfigItem` that this familiar was created by. This is nil by default, but it should always be specified so that Sacrificial Altar will work properly. (It informs the game which collectible should be removed if the familiar is tagged with the "cansacrifice" entity tag.) This can be obtained with: `Isaac.GetItemConfig():GetCollectible(collectibleType)`

**FamiliarSubType**: The subtype of the familiar to check. -1 matches any subtype.

???- example "Example Code"
    This code spawns 3 "Sister Maggy" familiars.
    ```lua
    local player = Isaac.GetPlayer()
    local sourceCollectibleID = CollectibleType.COLLECTIBLE_SAD_ONION
    local collectibleRNG = player:GetCollectibleRNG(sourceCollectibleID)
    local itemConfig = Isaac.GetItemConfig():GetCollectible(sourceCollectibleID)

    player:CheckFamiliar(FamiliarVariant.SISTER_MAGGY, 3, collectibleRNG, itemConfig)
    ```

___

### Clear·Costumes () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ClearCostumes ( ) {: .copyable aria-label='Functions' }
Removes all costumes.
___

### Clear·Dead·Eye·Charge () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ClearDeadEyeCharge ( ) {: .copyable aria-label='Functions' }

___

<div class="rgon-extension" markdown="1">

### ClearDeadEyeCharge () {: aria-label='Modified Functions' }
#### void ClearDeadEyeCharge ( boolean Force = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Now accepts a `Force` argument to forcefully reset the charge instead of only rolling for a change to reset.

___

</div>

### Clear·Temporary·Effects () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ClearTemporaryEffects ( ) {: .copyable aria-label='Functions' }
Will be called when player exits the room.

___

### Discharge·Active·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void DischargeActiveItem ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }
Sets the charge of your active item to 0 without triggering the active item effect.

___

### Donate·Luck () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void DonateLuck ( int Luck ) {: .copyable aria-label='Functions' }
Unlike the Luck property which should be set in MC_EVALUATE_CACHE, this method can be used anywhere and will automatically remember any additional luck added.

___

### Do·Zit·Effect () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void DoZitEffect ( [Vector](Vector.md) Direction ) {: .copyable aria-label='Functions' }
Fires a creep shot, same as the one fired by the item "Large Zit".

___

### Drop·Pocket·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void DropPocketItem ( int PocketNum, [Vector](Vector.md) Pos ) {: .copyable aria-label='Functions' }
Drops a held pocketitem (Card, Pill, Rune... from the given itemslot at the given position. Possible pocketnumbers are [0, 1, 2, 3].  Dropping pocket active items or dice bag dices does not work.

___

### Drop·Trinket () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void DropTrinket ( [Vector](Vector.md) DropPos, boolean ReplaceTick ) {: .copyable aria-label='Functions' }

___

### Evaluate·Items () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void EvaluateItems ( ) {: .copyable aria-label='Functions' }
Triggers a cache reevaluation. Will trigger the MC_EVALUATE_CACHE callback.

Before you use this function, you need to set the appropriate cache flags first. See the example below.

???- example "Example Code"
    This code re-evaluates all of the stats for the player.
    ```lua
    local player = Isaac.GetPlayer()
    player:AddCacheFlags(CacheFlag.CACHE_ALL)
    player:EvaluateItems()
    ```

___

### Fire·Bomb () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityBomb](EntityBomb.md) FireBomb ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, Entity Source = nil ) {: .copyable aria-label='Functions' }

___

### Fire·Brimstone () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityLaser](EntityLaser.md) FireBrimstone ( [Vector](Vector.md) Direction, Entity Source = nil, float DamageMultiplier = 1 ) {: .copyable aria-label='Functions' }

___

### Fire·Delayed·Brimstone () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityLaser](EntityLaser.md) FireDelayedBrimstone ( float Angle, [Entity](Entity.md) Parent ) {: .copyable aria-label='Functions' }

___

### Fire·Knife () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityKnife](EntityKnife.md) FireKnife ( [Entity](Entity.md) Parent, float RotationOffset = 0, boolean CantOverwrite = false, int SubType = 0, int Variant = 0 ) {: .copyable aria-label='Functions' }

???- note "Knife Variants"
    ```lua
    0: Mom's Knife
    1: Bone Club
    2: Bone Scythe
    3: Berserk Club
    4: Bag of Crafting
    5: Sumptorium
    9: Notched Axe
    10: Spirit Sword
    11: Tech Sword
    ```

___

### Fire·Tear () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityTear](EntityTear.md) FireTear ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, boolean CanBeEye = true, boolean NoTractorBeam = false, boolean CanTriggerStreakEnd = true, Entity Source = nil, float DamageMultiplier = 1 ) {: .copyable aria-label='Functions' }
- `CanBeEye`: If the player has the Evil Eye item, passing true allows the tear to have a chance of being an eye.
- `NoTractorBeam`: If the player has the Tractor Beam item, passing true means that the tear will be exempt from the beam.
- `CanTriggerStreakEnd`: If the player has the Dead Eye item, passing false means that the tear will be exempt from ending the streak.

___

### Fire·Tech·Laser () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityLaser](EntityLaser.md) FireTechLaser ( [Vector](Vector.md) Position, [LaserOffset](enums/LaserOffset.md) OffsetID, [Vector](Vector.md) Direction, boolean LeftEye, boolean OneHit = false, Entity Source = nil, float DamageMultiplier = 1 ) {: .copyable aria-label='Functions' }

???+ bug "Bugs"
    The `DamageMultiplier` parameter doesn't do anything when supplying [LASER_TECH2_OFFSET](enums/LaserOffset.md) as the offset.

___

### Fire·Tech·XLaser () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityLaser](EntityLaser.md) FireTechXLaser ( [Vector](Vector.md) Position, [Vector](Vector.md) Direction, float Radius, Entity Source = nil, float DamageMultiplier = 1 ) {: .copyable aria-label='Functions' }

___

### Flush·Queue·Item () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean FlushQueueItem ( ) {: .copyable aria-label='Functions' }
called after animation is finished, or on special occasions to prevent bugs
___

### Full·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean FullCharge ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY, int Force = false ) {: .copyable aria-label='Functions' }
Fully charges the active item. Returns true if the item was fully charged, false otherwise. If player has battery it will first try to fill first charge slot, then the battery slot.

**Force**: If set, items will always be charged even if they normally cannot be recharged by batteries

???- info "ActiveSlot"
    Setting the ActiveSlot argument to `-1` will recharge items in all slots.

___

### Get·Active·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetActiveCharge ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

Get the current charge of your active item.
___

### Get·Active·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetActiveItem ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' data-altreturn='0' }
Returns the currently held item. Returns `0` when no item is held.

___

### Get·Active·Sub·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetActiveSubCharge ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

Get the current items subcharge.

???+ bug "Bug"
    This function seems to always return 0. Use EntityPlayer:GetActiveCharge() to get any type of charges instead. Use EntityPlayer:GetBatteryCharge() to get the charge of the second charge bar.

___

### Get·Active·Weapon·Entity () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) GetActiveWeaponEntity ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

___

### Get·Aim·Direction () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetAimDirection ( ) {: .copyable aria-label='Functions' }

___

### Get·Baby·Skin () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [BabySubType](enums/BabySubType.md) GetBabySkin ( ) {: .copyable aria-label='Functions' }

___

### Get·Battery·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetBatteryCharge ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

Get the current charge progress of the second charge of your current active item. This bar is only active, when you have the Collectible "The Battery"
___

### Get·Black·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetBlackHearts ( ) {: .copyable aria-label='Functions' }
This does not return the number of black hearts; it returns the bit mask for which soul hearts are black hearts.

???- example "Example"
    Imagine we have the following setup of hearts, where S is a soul heart and B is a black heart:

    ```
    B S S B B S S B B
    ```

    Calling the function will return:

    ```lua
    Isaac.GetPlayer():GetBlackHearts() -- returns 409, which is 0001 1001 1001 in binary. Therefore, the read order is right to left.
    ```

    Quick code example to parse soul hearts vs black hearts:

    ```lua
    -- if you setup your hearts as described above then you'll get the following values
    -- GetSoulHearts = 18
    -- GetBlackHearts = 409
    local tbl = {}
    local player = Isaac.GetPlayer()
    -- loop over all the soul hearts
    -- divide by 2 because we need to go from half to whole hearts
    -- math.ceil to make sure we account for a possible half heart at the end
    for i = 0, math.ceil(player:GetSoulHearts() / 2) - 1 do
      -- you can also use BitSet128 here if you want: BitSet128(player:GetBlackHearts(),0):Get(i)
      table.insert(tbl, (player:GetBlackHearts() & (1 << i)) > 0 and 'B' or 'S')
    end
    if player:GetSoulHearts() % 2 ~= 0 then
      tbl[#tbl] = string.lower(tbl[#tbl]) -- lowercase to indicate half heart at end
    end
    print(table.concat(tbl, ' ')) -- prints: B S S B B S S B B
    ```

___

### Get·Blood·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetBloodCharge ( ) {: .copyable aria-label='Functions' }

Returns the amount of Blood Charge the player has.

___

### Get·Body·Color () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [SkinColor](enums/SkinColor.md) GetBodyColor ( ) {: .copyable aria-label='Functions' }

___

### Get·Bomb·Flags () {: aria-label='Functions' }
[ ](#){: .abp .tooltip .badge }
#### int GetBombFlags ( ) {: .copyable aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetBombFlags ( boolean IsFetus = false ) {: .copyable aria-label='Functions' }

**IsFetus**: If set to true, can set flags from bomb collectibles at random chance.
___

### Get·Bomb·Variant () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [BombVariant](enums/BombVariant.md) GetBombVariant ( [TearFlags](enums/TearFlags.md) TearFlags, boolean ForceSmallBomb ) {: .copyable aria-label='Functions' }
Pass tear flags to add extra effects to the bomb visual like burn -> hot bombs, even if player doesn't have Hot Bombs collectible. ForceSmallBomb will override large bomb variants for TEAR_PERSISTENT.

___

### Get·Bone·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetBoneHearts ( ) {: .copyable aria-label='Functions' }

Returns the amount of bone hearts that the player has. This is not doubled like the `EntityPlayer.GetMaxHearts` method is, so if e.g. the player has 3 bone hearts, this will return 3.

Also see the `EntityPlayer.GetEffectiveMaxHearts` method, which accounts for bone hearts.

___

### Get·Broken·Hearts () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetBrokenHearts ( ) {: .copyable aria-label='Functions' }

Returns the amount of broken hearts that the player has. This is not doubled like the `EntityPlayer.GetMaxHearts` method is, so if e.g. the player has 3 broken hearts, this will return 3.

___

### Get·Card () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Card](enums/Card.md) GetCard ( int SlotId ) {: .copyable aria-label='Functions' data-altreturn='0' }

Gets the ID of the card the player is holding in the given itemslot (0 = Main slot, 1 = secondary slot, 2 or 3). Returns `0` when no card is held in the slot.
___

### Get·Card·RNG () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [RNG](RNG.md) GetCardRNG ( [Card](enums/Card.md) ID ) {: .copyable aria-label='Functions' }

___

### Get·Collectible·Count () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetCollectibleCount ( ) {: .copyable aria-label='Functions' }

___

### Get·Collectible·Num () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetCollectibleNum ( [CollectibleType](enums/CollectibleType.md) Type, boolean OnlyCountTrueItems = false ) {: .copyable aria-label='Functions' }
**OnlyCountTrueItems**: If set to true, the function only counts collectibles that the player actually owns and ignores things like Lilith's Incubus, items granted by 3 Dollar Bill, and so forth.
___

<div class="rgon-extension" markdown="1">

### GetCollectibleNum () {: aria-label='Modified Functions' }
#### int GetCollectibleNum ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean OnlyCountTrueItems = false, bool IgnoreSpoof = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Now accepts an `IgnoreSpoof` argument that ignores innate items.

___

</div>

### Get·Collectible·RNG () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [RNG](RNG.md) GetCollectibleRNG ( [CollectibleType](enums/CollectibleType.md) ID ) {: .copyable aria-label='Functions' }
Gets the [RNG](RNG.md) object of a collectible.
???- example "Example Code"
    this code gives you the RNG object of the "Sad Onion" collectible.
    ```lua
    local player = Isaac.GetPlayer()
    local collectibleRNG = player:GetCollectibleRNG(CollectibleType.COLLECTIBLE_SAD_ONION)
    ```

___

### Get·Costume·Null·Pos () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetCostumeNullPos ( string NullFrameName, boolean HeadScale, [Vector](Vector.md) Direction ) {: .copyable aria-label='Functions' }

___

### Get·Damage·Cooldown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetDamageCooldown ( ) {: .copyable aria-label='Functions' }

When the player is hit, they will flash a different color and receive invulnerability frames. This method returns the amount of invulnerability frames. Normally, the player will receive 60 invulnerability frames when dealt a half-heart of damage or 120 invulnerability frames when dealt a full heart of damage. Additionally, the Blind Rage trinket can affect how invulnerability frames are granted.

Note that the frames returned by this function are render frames, not game frames.

___

### Get·Effective·Blood·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetEffectiveBloodCharge ( ) {: .copyable aria-label='Functions' }

Returns the amount of Blood Charge the player has. If playing as any other character besides Tainted Bethany, this will return `0`.

___

### Get·Effective·Max·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetEffectiveMaxHearts ( ) {: .copyable aria-label='Functions' }

Returns the amount of Red Hearts the player can contain in their Heart Containers and Bone Hearts. 1 unit is half a red heart.
**Example:** you have 3 red heart container and one bone heart. 6(red) + 2(bone) = 8

___

### Get·Effective·Soul·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetEffectiveSoulCharge ( ) {: .copyable aria-label='Functions' }

Returns the amount of Soul Charge the player has. If playing as any other character besides Bethany, this will return `0`.

___

### Get·Effects () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [TemporaryEffects](TemporaryEffects.md) GetEffects ( ) {: .copyable aria-label='Functions' }

___

### Get·Eternal·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetEternalHearts ( ) {: .copyable aria-label='Functions' }

Returns the amount of eternal hearts the player has.
___

### Get·Extra·Lives () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetExtraLives ( ) {: .copyable aria-label='Functions' }
Returns the number of extra lives the player currently has.

___

### Get·Fire·Direction () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Direction](enums/Direction.md) GetFireDirection ( ) {: .copyable aria-label='Functions' }

___

### Get·Flying·Offset () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetFlyingOffset ( ) {: .copyable aria-label='Functions' }

___

### Get·Golden·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetGoldenHearts ( ) {: .copyable aria-label='Functions' }

Returns the amount of golden hearts the player has.
___

### Get·Greed·Donation·Break·Chance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### float GetGreedDonationBreakChance ( ) {: .copyable aria-label='Functions' }

___

### Get·Head·Color () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [SkinColor](enums/SkinColor.md) GetHeadColor ( ) {: .copyable aria-label='Functions' }

___

### Get·Head·Direction () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Direction](enums/Direction.md) GetHeadDirection ( ) {: .copyable aria-label='Functions' }

___

### Get·Heart·Limit () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetHeartLimit ( ) {: .copyable aria-label='Functions' }

___

### Get·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetHearts ( ) {: .copyable aria-label='Functions' }

Returns the amount of red hearts the player has inside their heart containers and bone hearts. 1 unit is half a heart.
___

### Get·Item·State () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetItemState ( ) {: .copyable aria-label='Functions' }

___

### Get·Jar·Flies () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetJarFlies ( ) {: .copyable aria-label='Functions' }

___

### Get·Jar·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetJarHearts ( ) {: .copyable aria-label='Functions' }

___

### Get·Laser·Offset () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetLaserOffset ( [LaserOffset](enums/LaserOffset.md) ID, [Vector](Vector.md) Direction ) {: .copyable aria-label='Functions' }

___

### Get·Last·Action·Triggers () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetLastActionTriggers ( ) {: .copyable aria-label='Functions' }

___

### Get·Last·Damage·Flags () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetLastDamageFlags ( ) {: .copyable aria-label='Functions' }

___

### Get·Last·Damage·Source () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [EntityRef](EntityRef.md) GetLastDamageSource ( ) {: .copyable aria-label='Functions' }

___

### Get·Last·Direction () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetLastDirection ( ) {: .copyable aria-label='Functions' }

___

### Get·Main·Twin () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityPlayer](EntityPlayer.md) GetMainTwin ( ) {: .copyable aria-label='Functions' }

Returns the main player of pair characters or the main form of characters with multiple forms.

- When called on Jacob or Esau, returns Jacob.
- When called on Tainted Forgotten or Tainted Forgotten's Soul, returns Tainted Forgotten.
- When called on Tainted Lazarus or Dead Tainted Lazarus, returns themself. If the player has Birthright, then it will return Tainted Lazarus.
- When called on any other character, returns that character.

___

### Get·Max·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetMaxHearts ( ) {: .copyable aria-label='Functions' }

Returns the amount of Heart Containers the player has. 1 unit is half a heart container.
___

### Get·Max·Pocket·Items () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetMaxPocketItems ( ) {: .copyable aria-label='Functions' }

Get the number of Pickup items you can carry. (1 on default. 2 with polydactyly or similar)

If you have a pocket active, it also increments the number by one.

___

<div class="rgon-extension" markdown="1">

### GetMaxPocketItems () {: aria-label='Functions' }
#### int GetMaxPocketItems ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>

### Get·Max·Poop·Mana () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetMaxPoopMana ( ) {: .copyable aria-label='Functions' }

Returns the max amount of poop consumables that can be held by the player

___

### Get·Max·Trinkets () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetMaxTrinkets ( ) {: .copyable aria-label='Functions' }

Get the number of trinkets you can carry. (1 on default. 2 with moms purse or similar)

___

### Get·Modeling·Clay·Effect () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetModelingClayEffect ( ) {: .copyable aria-label='Functions' }

___

### Get·Movement·Direction () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Direction](enums/Direction.md) GetMovementDirection ( ) {: .copyable aria-label='Functions' }

___

### Get·Movement·Input () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetMovementInput ( ) {: .copyable aria-label='Functions' }

___

### Get·Movement·Joystick () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetMovementJoystick ( ) {: .copyable aria-label='Functions' }

___

### Get·Movement·Vector () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetMovementVector ( ) {: .copyable aria-label='Functions' }

___

### Get·Multi·Shot·Params () {: aria-label='Functions' }
[ ](#){: .rep .tooltip .badge }
#### MultiShotParams GetMultiShotParams ( [WeaponType](enums/WeaponType.md) WeaponType = WeaponType.WEAPON_TEARS ) {: .copyable aria-label='Functions' }
???+ bug "Bug"
    Since it returns UserData which cant be edited directly, the return value of this function can only be used in combination with the [GetMultiShotPositionVelocity()](#getmultishotpositionvelocity) function.
___

<div class="rgon-extension" markdown="1">

### GetMultiShotParams () {: aria-label='Modified Functions' }
#### [MultiShotParams](MultiShotParams.md) GetMultiShotParams ( [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) WeaponType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Now returns a proper `MultiShotParams` object.

___

</div>

### Get·Multi·Shot·Position·Velocity () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### [PosVel](PlayerTypes_PosVel.md) GetMultiShotPositionVelocity ( int LoopIndex, [WeaponType](enums/WeaponType.md) Weapon, [Vector](Vector.md) ShotDirection, float ShotSpeed, MultiShotParams params ) {: .copyable aria-label='Functions' }
Call this function in a loop, where the LoopIndex is a number between 0 and the amount of tears the current MultiShotParams contains. Since MultiShotParams is currently not accessable via the modding api, you need to find other ways to get the amount.

???+ bug "Removed Function"
    This function no longer exists since Repentance version `v1.7.9b.J835`!

___

<div class="rgon-extension" markdown="1">

### GetMultiShotPositionVelocity () {: aria-label='Modified Functions' }
#### [PosVel](https://wofsauge.github.io/IsaacDocs/rep/PlayerTypes_PosVel.html) GetMultiShotPositionVelocity ( int LoopIndex, [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) WeaponType, [Vector](Vector.md) ShotDirection, float ShotSpeed, [MultiShotParams](MultiShotParams.md) Params ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
This disappeared from the API sometime after 1.7.8.

Compared to the vanilla function, this implementation has been further augmented to throw an error if LoopIndex is higher than [MultiShotParams:GetNumTears()](MultiShotParams.md#getnumtears).

___

</div>

### Get·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### string GetName ( ) {: .copyable aria-label='Functions' }

Returns the name of the player. (Isaac, Cain, Azazel,...)
___

### Get·NPCTarget () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) GetNPCTarget ( ) {: .copyable aria-label='Functions' }
Normally, this function returns the player. However, in some cases, NPCs can be redirected to attack another target, in which case this function will return the alternate target (e.g. after using Best Friend).
___

### Get·Num·Blue·Flies () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetNumBlueFlies ( ) {: .copyable aria-label='Functions' }

___

### Get·Num·Blue·Spiders () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetNumBlueSpiders ( ) {: .copyable aria-label='Functions' }

___

### Get·Num·Bombs () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetNumBombs ( ) {: .copyable aria-label='Functions' }

___

### Get·Num·Coins () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetNumCoins ( ) {: .copyable aria-label='Functions' }

___

### Get·Num·Giga·Bombs () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetNumGigaBombs ( ) {: .copyable aria-label='Functions' }

___

### Get·Num·Keys () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetNumKeys ( ) {: .copyable aria-label='Functions' }

___

### Get·Other·Twin () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityPlayer](EntityPlayer.md) GetOtherTwin ( ) {: .copyable aria-label='Functions' }

Returns the other player of pair characters or the other form of characters with multiple forms.

- When called on Jacob, returns Esau.
- When called on Esau, returns Jacob.
- When called on Tainted Forgotten, returns Tainted Forgotten's Soul.
- When called on Tainted Forgotten's Soul, returns Tainted Forgotten.
- When called on Tainted Lazarus, it will only return the Flip Lazarus, if the player has the Birthright item. Otherwise it returns nil.
- When called on any other character, returns nil.
___

### Get·Pill () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [PillColor](enums/PillColor.md) GetPill ( int SlotId ) {: .copyable aria-label='Functions' data-altreturn='0' }

Gets the ID of the pill the player is holding in the given itemslot (0 = Main slot, 1 = secondary slot, 2 or 3) Returns `0` when no pill is held in the given slot.
___

### Get·Pill·RNG () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [RNG](RNG.md) GetPillRNG ( [PillEffect](enums/PillEffect.md) ID ) {: .copyable aria-label='Functions' }

___

### Get·Player·Type () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [PlayerType](enums/PlayerType.md) GetPlayerType ( ) {: .copyable aria-label='Functions' }

___

### Get·Pocket·Item () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const PlayerPocketItem GetPocketItem ( int SlotId ) {: .copyable aria-label='Functions' }

Get the userdata of the pocketitem (Card, Pill, Rune) in a said slot.

???+ bug "Bugs"
    This function returns userdata, which can't be processed. It is therefore broken and should not be used!
___

<div class="rgon-extension" markdown="1">

### GetPocketItem () {: aria-label='Modified Functions' }
#### [PocketItem](PocketItem.md) GetPocketItem ( [PillCardSlot](enums/PillCardSlot.md) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Gets the card/pill/rune in the specified pocket slot.

Now returns a proper `PocketItem` object.

___

</div>

### Get·Poop·Mana () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetPoopMana ( ) {: .copyable aria-label='Functions' }

Returns how many poop consumables the player is currently holding

___

### Get·Poop·Spell () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [PoopSpellType](enums/PoopSpellType.md) GetPoopSpell ( int Position ) {: .copyable aria-label='Functions' }

Returns the poop spell at the given position in the player's spell queue

___

### Get·Recent·Movement·Vector () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetRecentMovementVector ( ) {: .copyable aria-label='Functions' }
Returns the joystick direction that drives player movement, taking into account certain modifiers like disabled controls and seed effects.

___

### Get·Rotten·Hearts () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetRottenHearts ( ) {: .copyable aria-label='Functions' }

___

### Get·Shooting·Input () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetShootingInput ( ) {: .copyable aria-label='Functions' }

Returns a vector that corresponds to the shooting inputs that this player is pressing.

???- info "Shooting Angle diagram"
    ![GetShootingInput diagram](images/infographics/GetShootingInput.png){: width='250' }

___

### Get·Shooting·Joystick () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetShootingJoystick ( ) {: .copyable aria-label='Functions' }

Returns a vector that corresponds to the shooting inputs that this player is holding.

See the image for the [GetShootingInput](#getshootinginput) method.

___

### Get·Smooth·Body·Rotation () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### float GetSmoothBodyRotation ( ) {: .copyable aria-label='Functions' }

___

### Get·Soul·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetSoulCharge ( ) {: .copyable aria-label='Functions' }

Returns the amount of Soul Charge the player has.

___

### Get·Soul·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetSoulHearts ( ) {: .copyable aria-label='Functions' }

Returns the amount of Soul Hearts the player has. 1 unit is half a heart.

???- note "Notes"
    Black Hearts count toward this total, as the game sees them as soul hearts.

___

### Get·Sub·Player () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityPlayer](EntityPlayer.md) GetSubPlayer ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

Returns the other form of The Forgotten.

___

### Get·Tear·Hit·Params () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [TearParams](TearParams.md) GetTearHitParams ( [WeaponType](enums/WeaponType.md) WeaponType, float DamageScale = 1, int TearDisplacement = 1, Entity Source = nil ) {: .copyable aria-label='Functions' }
Used for tear parameters that are calculated on hit (ex: Tough love, Common cold), DamageScale is used for scale calculation based on damage

___

### Get·Tear·Movement·Inheritance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetTearMovementInheritance ( [Vector](Vector.md) ShotDirection ) {: .copyable aria-label='Functions' }

___

### Get·Tear·Poison·Damage () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### float GetTearPoisonDamage ( ) {: .copyable aria-label='Functions' }

___

### Get·Tear·Range·Modifier () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetTearRangeModifier ( ) {: .copyable aria-label='Functions' }
For Experimental Treatement, returns `-1`, `0` or `1` depending on the range rolled.

___

<div class="rgon-extension" markdown="1">

### GetTearRangeModifier () {: aria-label='Functions' }
#### int GetTearRangeModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

Adds `2.5 * modifier` to the player's TearRange.

Experimental Treatment adds `-1`, `0` or `1` depending on the range rolled. Void may randomly add `1`.

___

</div>

### Get·Total·Damage·Taken () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetTotalDamageTaken ( ) {: .copyable aria-label='Functions' }

___

### Get·Tractor·Beam () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) GetTractorBeam ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

___

### Get·Trinket () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [TrinketType](enums/TrinketType.md) GetTrinket ( int TrinketIndex ) {: .copyable aria-label='Functions' data-altreturn='0' }

Gets the ID of the trinket the player is holding in the given trinketslot (0 or 1). Returns `0` when no trinket is held in the given slot.
___

### Get·Trinket·Multiplier () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetTrinketMultiplier ( [TrinketType](enums/TrinketType.md) TrinketID ) {: .copyable aria-label='Functions' }
Gets the multiplier of a given Trinket effect. This is analog to the number of times the trinket effect is applied.

???- info "Multiplier Breakdown"
    * Per normal trinket of this type equipped / gulped : +1
    * Per golden trinket of this type equipped / gulped : +2
    * Mom's Box equipped : +1 (does not stack)
___

### Get·Trinket·RNG () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [RNG](RNG.md) GetTrinketRNG ( [TrinketType](enums/TrinketType.md) TrinketID ) {: .copyable aria-label='Functions' }

___

### Get·Velocity·Before·Update () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetVelocityBeforeUpdate ( ) {: .copyable aria-label='Functions' }

___

### Get·Zodiac·Effect () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetZodiacEffect ( ) {: .copyable aria-label='Functions' }

___

### Has·Collectible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasCollectible ( [CollectibleType](enums/CollectibleType.md) Type, boolean IgnoreModifiers = false ) {: .copyable aria-label='Functions' }
**IgnoreModifiers**: If set to true, only counts collectibles the player actually owns and ignores effects granted by items like Zodiac, 3 Dollar Bill and Lemegeton

___

<div class="rgon-extension" markdown="1">

### HasCollectible () {: aria-label='Modified Functions' }
#### boolean HasCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean IgnoreModifiers = false, boolean IgnoreSpoof = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Now accepts a `IgnoreSpoof` argument that ignores innate items.

___

</div>

### Has·Curse·Mist·Effect () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasCurseMistEffect ( ) {: .copyable aria-label='Functions' }

___

### Has·Full·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasFullHearts ( ) {: .copyable aria-label='Functions' }

___

### Has·Full·Hearts·And·Soul·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasFullHeartsAndSoulHearts ( ) {: .copyable aria-label='Functions' }

___

### Has·Golden·Bomb () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasGoldenBomb ( ) {: .copyable aria-label='Functions' }

___

### Has·Golden·Key () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasGoldenKey ( ) {: .copyable aria-label='Functions' }

___

### Has·Invincibility () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasInvincibility ( [DamageFlag](enums/DamageFlag.md) Flags = 0 ) {: .copyable aria-label='Functions' }
returns true when player is in an invincibility state
___

### Has·Player·Form () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasPlayerForm ( [PlayerForm](enums/PlayerForm.md) Form ) {: .copyable aria-label='Functions' }

___

### Has·Timed·Item () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasTimedItem ( ) {: .copyable aria-label='Functions' }
Returns true if you have a timed active item *(such as Brown Nugget)* in the first active slot

___

### Has·Trinket () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasTrinket ( [TrinketType](enums/TrinketType.md) Type, boolean IgnoreModifiers = false ) {: .copyable aria-label='Functions' }
**IgnoreModifiers**: If set to true, only counts trinkets the player actually holds and ignores effects granted by other items

___

### Has·Weapon·Type () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasWeaponType ( [WeaponType](enums/WeaponType.md) WeaponType ) {: .copyable aria-label='Functions' }

___

### Init·Baby·Skin () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void InitBabySkin ( ) {: .copyable aria-label='Functions' }

___

### Is·Black·Heart () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsBlackHeart ( int Heart ) {: .copyable aria-label='Functions' }
This can be used instead of GetBlackHearts to figure out which soul hearts are black hearts.

???- example "Example"
    Imagine we have the following setup of hearts, where S is a soul heart and B is a black heart:

    ```
    B S S B B S S B B
    ```

    Each soul heart is composed of two halves. Only the odd numbers seem to trigger this function. Even numbers always return false. The following assumes that the indexing starts at 1 rather than 0, but regardless, it's the odd numbers that work here. The indexing here only applies to your soul/black hearts. It doesn't matter if you have other red/bone/etc hearts.

    ```
    B(1,2) S(3,4) S(5,6) B(7,8) B(9,10) S(11,12) S(13,14) B(15,16) B(17,18)
    ```

    ```lua
    Isaac.GetPlayer():IsBlackHeart(1) -- returns true (black heart)
    Isaac.GetPlayer():IsBlackHeart(2) -- returns false (not useful)
    Isaac.GetPlayer():IsBlackHeart(3) -- returns false (soul heart)
    -- 1,7,9,15,17 all return true (black hearts)
    ```

    Quick code example to parse soul hearts vs black hearts:

    ```lua
    -- if you setup your hearts as described above then you'll get the following value
    -- GetSoulHearts = 18
    local tbl = {}
    local player = Isaac.GetPlayer()
    -- loop over all the soul heart odd indexes
    for i = 1, player:GetSoulHearts(), 2 do
      table.insert(tbl, player:IsBlackHeart(i) and 'B' or 'S')
    end
    if player:GetSoulHearts() % 2 ~= 0 then
      tbl[#tbl] = string.lower(tbl[#tbl]) -- lowercase to indicate half heart at end
    end
    print(table.concat(tbl, ' ')) -- prints: B S S B B S S B B
    ```

___

### Is·Bone·Heart () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsBoneHeart ( int heart ) {: .copyable aria-label='Functions' }
This can be used to figure out the ordering of bone hearts amongst soul/black hearts.

???- example "Example"
    Imagine we have the following setup of hearts:

    ```
    BONE SOUL BONE BLACK BONE
    ```

    The indexing here is for whole hearts, and the index starts at 0. The indexing takes into account bone/soul/black hearts. It doesn't matter if you have other heart types (e.g. red hearts).

    ```lua
    Isaac.GetPlayer():IsBoneHeart(0) -- returns true (bone heart)
    Isaac.GetPlayer():IsBoneHeart(1) -- returns false (soul heart)
    Isaac.GetPlayer():IsBoneHeart(3) -- returns false (black heart)
    -- 0,2,4 all return true (bone hearts)
    ```

    Quick code example to parse soul hearts vs black hearts vs bone hearts:

    ```lua
    -- if you setup your hearts as described above then you'll get the following values
    -- GetSoulHearts = 4
    -- GetBoneHearts = 3
    local tbl = {}
    local player = Isaac.GetPlayer()
    -- first, figure out the soul/black heart order
    for i = 1, player:GetSoulHearts(), 2 do
      table.insert(tbl, player:IsBlackHeart(i) and 'BLACK' or 'SOUL')
    end
    if player:GetSoulHearts() % 2 ~= 0 then
      tbl[#tbl] = string.lower(tbl[#tbl]) -- lowercase to indicate half heart at end
    end
    -- second, figure out where bone hearts fit into the soul/black/bone heart order
    -- divide soul hearts by 2 to get whole hearts, bone hearts are already in whole heart increments
    for i = 0, math.ceil(player:GetSoulHearts() / 2) + player:GetBoneHearts() - 1 do
      if player:IsBoneHeart(i) then
        table.insert(tbl, i + 1, 'BONE')
      end
    end
    print(table.concat(tbl, ' ')) -- prints: BONE SOUL BONE BLACK BONE
    ```

___

### Is·Coop·Ghost () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean IsCoopGhost ( ) {: .copyable aria-label='Functions' }
In a multiplayer game, if a player dies, they will return as a tiny ghost. This method returns true if the player is a co-op ghost.

___

### Is·Extra·Animation·Finished () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsExtraAnimationFinished ( ) {: .copyable aria-label='Functions' }

___

### Is·Full·Sprite·Rendering () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsFullSpriteRendering ( ) {: .copyable aria-label='Functions' }

___

### Is·Held·Item·Visible () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsHeldItemVisible ( ) {: .copyable aria-label='Functions' }

___

### Is·Holding·Item () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsHoldingItem ( ) {: .copyable aria-label='Functions' }
Is Player holding up an item (card/collectible/etc)
___

### Is·Item·Queue·Empty () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsItemQueueEmpty ( ) {: .copyable aria-label='Functions' }

___

### Is·P2Appearing () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsP2Appearing ( ) {: .copyable aria-label='Functions' }

___

### Is·Pos·In·Spot·Light () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsPosInSpotLight ( [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }
Returns true if the `position` is in the AOE of the **Night Light** item.

___

### Is·Sub·Player () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsSubPlayer ( ) {: .copyable aria-label='Functions' }
Returns true if the player object was returned from the `EntityPlayer.GetSubPlayer` method. (This method is not related to multiplayer.)

Additionally, this also returns true for the player object representing Dead Tainted Lazarus that fires at the beginning of the run in the PostPlayerInit callback. (The PostPlayerInit callback fires first for Dead Tainted Lazarus before firing for the normal Tainted Lazarus.)

___

### Needs·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean NeedsCharge ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

This will always return false for active items that have `chargetype="special"` set in the `items.xml` file, even if they are not fully charged.

___

### Play·Extra·Animation () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PlayExtraAnimation ( string Animation ) {: .copyable aria-label='Functions' }

___

### Queue·Extra·Animation () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void QueueExtraAnimation ( string Animation ) {: .copyable aria-label='Functions' }

___

### Queue·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void QueueItem ( [ItemConfigItem](ItemConfig_Item.md) Item, int Charge = 0, boolean Touched = false, boolean Golden = false, int VarData = 0 ) {: .copyable aria-label='Functions' }
When the player touches a collectible or trinket, they are not granted it immediately. Instead, the item is queued for the duration of the animation where the player holds the item above their head. When the animation is finished, the item in the queue will be granted. This method adds a new item to the item queue. If the player is not currently playing an animation, then the queued item will simply be awarded instantly.

Also see `FlushQueueItem()`, `IsItemQueueEmpty()`, and `QueuedItem`.
___

### Remove·Black·Heart () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveBlackHeart ( int BlackHeart ) {: .copyable aria-label='Functions' }

___

### Remove·Blue·Fly () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveBlueFly ( ) {: .copyable aria-label='Functions' }

___

### Remove·Blue·Spider () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveBlueSpider ( ) {: .copyable aria-label='Functions' }

___

### Remove·Collectible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void RemoveCollectible ( [CollectibleType](enums/CollectibleType.md) Type, boolean IgnoreModifiers = false, [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY, boolean RemoveFromPlayerForm = true ) {: .copyable aria-label='Functions' }
**IgnoreModifiers**: Ignores collectible effects granted by other items (i.e. Void)

**Slot**: Sets the active slot this collectible should be removed from

**RemoveFromPlayerForm**: If successfully removed and part of a transformation, decrease that transformation's counter by 1
___

### Remove·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveCostume ( [ItemConfigItem](ItemConfig_Item.md) Item ) {: .copyable aria-label='Functions' }
Removes a given costume based on its item config entry.

???- example "Example code"
    This code removes the costume of the Spoon Bender collectible.
    ```lua
    local player = Isaac.GetPlayer()
    local itemConfig = Isaac.GetItemConfig()
    local itemConfigItem = itemConfig:GetCollectible(CollectibleType.COLLECTIBLE_SPOON_BENDER)
    player:RemoveCostume(itemConfigItem)
    ```

___

### Remove·Curse·Mist·Effect () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void RemoveCurseMistEffect ( ) {: .copyable aria-label='Functions' }

___

### Remove·Golden·Bomb () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveGoldenBomb ( ) {: .copyable aria-label='Functions' }

___

### Remove·Golden·Key () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveGoldenKey ( ) {: .copyable aria-label='Functions' }

___

### Remove·Skin·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveSkinCostume ( ) {: .copyable aria-label='Functions' }
Removes player-specific costumes like Magdalene's hair or Cain's eyepatch.

___

### Render·Body () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderBody ( [Vector](Vector.md) position ) {: .copyable aria-label='Functions' }

___

### Render·Glow () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderGlow ( [Vector](Vector.md) position ) {: .copyable aria-label='Functions' }

___

### Render·Head () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderHead ( [Vector](Vector.md) position ) {: .copyable aria-label='Functions' }

___

### Render·Top () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderTop ( [Vector](Vector.md) position ) {: .copyable aria-label='Functions' }

___

### Replace·Costume·Sprite () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ReplaceCostumeSprite ( [ItemConfigItem](ItemConfig_Item.md) Item, string SpritePath, int SpriteId ) {: .copyable aria-label='Functions' }
???+ bug "Bugs"
	The `SpriteId` parameter is ignored and will replace all layers of the item's costume. Usage of this function should be limited to costumes with only one spritesheet to avoid issues.
___

### Reset·Damage·Cooldown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ResetDamageCooldown ( ) {: .copyable aria-label='Functions' }

___

### Reset·Item·State () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ResetItemState ( ) {: .copyable aria-label='Functions' }
[Room](Room.md) transitions call this to prevent lock ups.
___

### Respawn·Familiars () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RespawnFamiliars ( ) {: .copyable aria-label='Functions' }
Respawns all familiars associated to the player.

___

### Revive () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Revive ( ) {: .copyable aria-label='Functions' }
Revives the player.

???+ bug "Bugs"
    Exiting the run at any point after this function is called will make it so that the run can't be continued.
___

### Set·Active·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetActiveCharge ( int Charge, [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

___

### Set·Blood·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetBloodCharge ( int Amount ) {: .copyable aria-label='Functions' }

Sets the amount of Blood Charge the player has. Blood Charge does not do anything on characters besides Tainted Bethany.

___

### Set·Card () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetCard ( int SlotId, [Card](enums/Card.md) ID ) {: .copyable aria-label='Functions' }

Change the card/rune the player is holding in the given itemslot (0 or 1).
___

### Set·Full·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetFullHearts ( ) {: .copyable aria-label='Functions' }

___

### Set·Min·Damage·Cooldown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetMinDamageCooldown ( int DamageCooldown ) {: .copyable aria-label='Functions' }

___

### Set·Pill () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetPill ( int SlotId, [PillColor](enums/PillColor.md) Pill ) {: .copyable aria-label='Functions' }

Change the pill the player is holding in the given itemslot (0 or 1).

___

### Set·Pocket·Active·Item() {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetPocketActiveItem ( [CollectibleType](enums/CollectibleType.md) Type, [ActiveSlot](enums/ActiveSlot.md) Slot, boolean KeepInPools ) {: .copyable aria-label='Functions' }

Sets the player's pocket active item to the given active item.
Slot can be either SLOT_POCKET or SLOT_POCKET2.
Items added to SLOT_POCKET2 will always be removed upon being used.
If KeepInPools is set to true, the item will not be removed from the item pools.
Use this to let the player start with a custom active item in their pocket active slot right away.

???+ bug "Bugs"
    Calling this function inside PostPlayerInit callback causes a crash when continuing a saved run after closing and reopening the game, unless KeepInPools argument is set to true.
___

### Set·Shooting·Cooldown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetShootingCooldown ( int Cooldown ) {: .copyable aria-label='Functions' }

___

### Set·Soul·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetSoulCharge ( int Amount ) {: .copyable aria-label='Functions' }

Sets the amount of Soul Charge the player has. Soul Charge does not do anything on characters besides Bethany.

___

### Set·Target·Trap·Door () {: aria-label='Functions' }
[ ](#){: .abp .tooltip .badge }
#### void SetTargetTrapDoor ( [GridEntity](GridEntity.md) TrapDoor ) {: .copyable aria-label='Functions' }

This function got removed with Repentance.

___

### Shoot·Red·Candle () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ShootRedCandle ( [Vector](Vector.md) Direction ) {: .copyable aria-label='Functions' }
for ghost pepper item + poop and farts
___

<div class="rgon-extension" markdown="1">

### ShootRedCandle () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) ShootRedCandle ( [Vector](Vector.md) Direction ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Now returns the EntityEffect for the flame.

___

</div>

### Spawn·Maw·Of·Void () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityLaser](EntityLaser.md) SpawnMawOfVoid ( int Timeout ) {: .copyable aria-label='Functions' }

___

### Stop·Extra·Animation () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void StopExtraAnimation ( ) {: .copyable aria-label='Functions' }

___

### Swap·Active·Items () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SwapActiveItems ( ) {: .copyable aria-label='Functions' }
Swaps active items in the **Schoolbag** activeslot

___

### Throw·Blue·Spider () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) ThrowBlueSpider ( [Vector](Vector.md) Position, [Vector](Vector.md) Target ) {: .copyable aria-label='Functions' }

___

### Throw·Friendly·Dip () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) ThrowFriendlyDip ( int Subtype, [Vector](Vector.md) Position, [Vector](Vector.md) Target ) {: .copyable aria-label='Functions' }

???- note "Dip Subtypes"
    ```lua
    0: normal
    1: red
    2: corny
    3: golden
    4: rainbow
    5: black
    6: holy
    12: stone
    13: flaming
    14: poison
    20: brownie
    ```
___

### Throw·Held·Entity () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [Entity](Entity.md) ThrowHeldEntity ( [Vector](Vector.md) Velocity ) {: .copyable aria-label='Functions' }

___

### Trigger·Book·Of·Virtues () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void TriggerBookOfVirtues ( [CollectibleType](enums/CollectibleType.md) Type = CollectibleType.COLLECTIBLE_NULL, int Charge = 0 ) {: .copyable aria-label='Functions' }
Works only if the player has the **Book of Virtues** item, otherwise does nothing

___

### Try·Hold·Entity () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean TryHoldEntity ( [Entity](Entity.md) Entity ) {: .copyable aria-label='Functions' }

___

### Try·Hold·Trinket () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean TryHoldTrinket ( [TrinketType](enums/TrinketType.md) Type ) {: .copyable aria-label='Functions' }
Returns true if an active item pickup cooldown is over. returns true if trinket can be added, else false
___

### Try·Remove·Collectible·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void TryRemoveCollectibleCostume ( [CollectibleType](enums/CollectibleType.md) Collectible, boolean KeepPersistent ) {: .copyable aria-label='Functions' }
Tries to remove a costume of the given collectible. `KeepPersistent` is used to define if persistent costumes should be removed. If its set to `false`, it will only remove temporary costumes.

???- example "Example code"
    This code removes the costume of the Spoon Bender collectible.
    ```lua
    local player = Isaac.GetPlayer()
    player:TryRemoveCollectibleCostume(CollectibleType.COLLECTIBLE_SPOON_BENDER, false)
    ```
___

### Try·Remove·Null·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void TryRemoveNullCostume ( [NullItemID](enums/NullItemID.md) NullId ) {: .copyable aria-label='Functions' }

___

### Try·Remove·Trinket () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean TryRemoveTrinket ( [TrinketType](enums/TrinketType.md) Type ) {: .copyable aria-label='Functions' }

___

### Try·Remove·Trinket·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void TryRemoveTrinketCostume ( [TrinketType](enums/TrinketType.md) Trinket ) {: .copyable aria-label='Functions' }
Tries to remove a trinket costume
___

### Try·Use·Key () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean TryUseKey ( ) {: .copyable aria-label='Functions' }

___

### Update·Can·Shoot () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void UpdateCanShoot ( ) {: .copyable aria-label='Functions' }

___

### Use·Active·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void UseActiveItem ( [CollectibleType](enums/CollectibleType.md) Item, [UseFlags](enums/UseFlag.md) UseFlags = 0, [ActiveSlot](enums/ActiveSlot.md) Slot = -1, int CustomVarData = 0 ) {: .copyable aria-label='Functions' }

#### void UseActiveItem ( [CollectibleType](enums/CollectibleType.md) Item, boolean ShowAnim = false, boolean KeepActiveItem = false, boolean AllowNonMainPlayer = true, boolean ToAddCostume = false, [ActiveSlot](enums/ActiveSlot.md) Slot = -1, int CustomVarData = 0 ) {: .copyable .secondH4 aria-label='Functions' }
**Slot**: The active slot this item was used from (set to -1 if this item wasn't triggered by any active slot)

**CustomVarData**: `UseFlag.USE_CUSTOMVARDATA` needs to be provided in `UseFlags` otherwise this field is ignored

???- note "Notes"
	This method will increment the number of CollectibleEffects (see [Temporary Effects](TemporaryEffects.md)) of the passed item by 1 for the current room, and will trigger any associated MC_USE_ITEM callbacks. As of Repentance, this method can also be used on Passive and Familiar ItemTypes.
___

<div class="rgon-extension" markdown="1">

### UseActiveItem () {: aria-label=' Modified Functions' }
#### [UseActiveItemResultFlags](enums/UseActiveItemResultFlag.md) UseActiveItem ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Item, [UseFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/UseFlag.html) UseFlags = 0, [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot = -1, int CustomVarData = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Now has a return value, a bitmask of [UseActiveItemResultFlags](enums/UseActiveItemResultFlag.md).

???+ note "Return behavior"
	`UseActiveItemResultFlags.REMOVE` is possible to not be passed even if the item would be removed normally. It will not be passed if any of the following conditions are met:
	- `UseFlag.USE_OWNED` is not passed for vanilla items.
	- `UseFlag.USE_VOID` is passed for any items.
___

## Modified Variables
___

</div>

### Use·Card () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void UseCard ( [Card](enums/Card.md) ID, [UseFlags](enums/UseFlag.md) UseFlags = 0 ) {: .copyable aria-label='Functions' }

___

### Use·Pill () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void UsePill ( [PillEffect](enums/PillEffect.md) ID, [PillColor](enums/PillColor.md) PillColor, [UseFlags](enums/UseFlag.md) UseFlags = 0  ) {: .copyable aria-label='Functions' }

___

### Use·Poop·Spell () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void UsePoopSpell ( [PoopSpellType](enums/PoopSpellType.md) type ) {: .copyable aria-label='Functions' }
Triggers one of Tainted ???'s poop spells (see [PoopSpellType](enums/PoopSpellType.md) enum)

___

### Will·Player·Revive () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean WillPlayerRevive ( ) {: .copyable aria-label='Functions' }
This function will return true if the player has one or more extra lives or if a conditional revival item will work on the next death.

Right now, there are 3 items that grant conditional extra lives:

* Guppy's Collar - This function will successfully predict whether or not the next revive from Guppy's Collar will work or not. (50% chance)
* Broken Ankh - This function will successfully predict whether or not the next revive from Broken Ankh will work or not. (22.22% chance)
* Mysterious Paper - This function will only successfully predict the revive from Missing Poster every 4 frames, because it evaluates only one of its 4 possible item effects each frame.

___
## Variables

### Baby·Skin {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [BabySubType](enums/BabySubType.md) BabySkin  {: .copyable aria-label='Variables' }
P2 Skin section Used to hold the selected skin (in case of glitched baby it will pick a random one)

???+ bug "Bugs"
    This variable actually contains userdata and is not usable within API. Attempt to change it will results in a crash.

___

<div class="rgon-extension" markdown="1">

### BabySkin {: aria-label='Modified Variables' }
#### [BabySubType](https://wofsauge.github.io/IsaacDocs/rep/enums/BabySubType.html) BabySkin [ ](#){: .rgonorplus .tooltip .badge }  {: .copyable aria-label='Modified Variables' }
Same as default, but now returns a proper integer value instead of userdata.

___

</div>

### Can·Fly {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanFly  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. Can the player fly over rocks and pits?
___

### Controller·Index {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const int ControllerIndex  {: .copyable aria-label='Variables' }

___

### Controls·Cooldown {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ControlsCooldown  {: .copyable aria-label='Variables' }
Specifies the number of frames the player's controls should be disabled. Decrements by 1 every frame, until it reaches 0. Used by the paralysis pill effect.

At 0 or less, does not block player control.
___

### Controls·Enabled {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean ControlsEnabled  {: .copyable aria-label='Variables' }

___

### Damage {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Damage  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Damage Stat.**  How much damage do the players tears or other main weapons do?
___

### Fire·Delay {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float FireDelay  {: .copyable aria-label='Variables' }
How long until the player can spawn their next tear?

???- note "Version Difference"
	In the Afterbirth+ version of the modding api, this variable is an integer

___

### Friend·Ball·Enemy {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const EntityDesc FriendBallEnemy  {: .copyable aria-label='Variables' }

???+ bug "Bugs"
    This function returns userdata that cant be edited or accessed.
___

<div class="rgon-extension" markdown="1">

### FriendBallEnemy {: aria-label='Modified Variables' }
#### [EntityDesc](EntityDesc.md) FriendBallEnemy [ ](#){: .rgonorplus .tooltip .badge }  {: .copyable aria-label='Modified Variables' }
Same as default, but now returns a proper class instead of userdata.

___


## Functions

</div>

### Head·Frame·Delay {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int HeadFrameDelay  {: .copyable aria-label='Variables' }
Specifies the number of frames the player's head should be playing the shooting animation. Decrements by 1 every frame, until it reaches -1.

At negative values, the player's head does not play the shooting animation.
___

### IBS·Charge {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### float IBSCharge  {: .copyable aria-label='Variables' }
Internally used by IBS, increases based on damage dealt, range is 0-1
___

### Item·Hold·Cooldown {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ItemHoldCooldown  {: .copyable aria-label='Variables' }
Used for avoiding player get stucked between rocks when switching a flying item with other active item.
___

### Laser·Color {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Color](Color.md) LaserColor  {: .copyable aria-label='Variables' }

___

### Luck {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Luck  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Luck Stat.**  Better luck generally means better random events.
___

### Max·Fire·Delay {: aria-label='Variables' }
[ ](#){: .abp .tooltip .badge }
#### int MaxFireDelay  {: .copyable aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### float MaxFireDelay  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How long must the player wait between each firing each tear?

???+ info "Info"
    This stat is equal to `30 / tears stat - 1`.

???- example "Example Code"
    This code converts between max fire delay and tears stat and increases fire rate by 1. Note that this applies after the soft tear cap and tear multipliers such as the ones from Polyphemus and Soy Milk.

    ```lua
    FIRE_RATE_CAP = 120

    function get_fire_rate(player)
	    return 30 / (player.MaxFireDelay + 1)
    end

    function set_fire_rate(player, fire_rate)
        local fire_rate = math.min(fire_rate, FIRE_RATE_CAP) -- Apply fire rate cap.
        player.MaxFireDelay = 30 / fire_rate - 1
    end

    function mod:OnEvaluateFireRate(player, flag)
        local old_fire_rate = get_fire_rate(player)
        set_fire_rate(player, old_fire_rate + 1)
    end

    mod:AddCallback(ModCallbacks.MC_EVALUATE_CACHE, mod.OnEvaluateFireRate, CacheFlag.CACHE_FIREDELAY)
    ```

___

### Move·Speed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float MoveSpeed  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Speed Stat.**  How fast can the player move?
___

### Queued·Item {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [QueueItemData](QueueItemData.md) QueuedItem  {: .copyable aria-label='Variables' }

- When Isaac picks up a collectible or a trinket, he holds it above his head for a while. At this point, the collectible/trinket is not actually put into his inventory yet.
- In other words, the item is queued for insertion until the animation completes, at which point the queue is processed and the item is inserted.
- `QueuedItem` holds a object of type `QueueItemData` that describes the item that a player is currently holding above their head.
- `QueuedItem` is never nil, even if the player is not currently holding up any item. (However, `player.QueuedItem.Item` will be nil if they are not currently holding up any item.)
- This only stores data for collectibles and trinkets. It does not store any data for pocket items (even though Isaac plays a similar "holding above head" animation for pocket items).
- Also see `FlushQueueItem()`, `IsItemQueueEmpty()`, and `QueueItem()`.
___

### Samson·Berserk·Charge {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int SamsonBerserkCharge  {: .copyable aria-label='Variables' }
Internally used by Tainted Samson, increases based on damage dealt, range is 0-100000
___

### Secondary·Active·Item {: aria-label='Variables' }
[ ](#){: .abp .tooltip .badge }
#### [ActiveItemDesc](PlayerTypes_ActiveItemDesc.md) SecondaryActiveItem  {: .copyable aria-label='Variables' data-altreturn='nil' }

???+ bug "Bug"
    This function does not exist anymore in Repentance. As of right now, there is no other function to get the [ActiveItemDesc](PlayerTypes_ActiveItemDesc.md) of any active item the player holds. Until this is fixed, this info will stay here.
___

### Shot·Speed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float ShotSpeed  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the ShotSpeed Stat.**

Defines how fast the tear travel when spawned.

The default velocity of a tear shot is 10 times the players ShotSpeed.

___

### Tear·Color {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Color](Color.md) TearColor  {: .copyable aria-label='Variables' }

___

### Tear·Falling·Acceleration {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float TearFallingAcceleration  {: .copyable aria-label='Variables' }

___

### Tear·Falling·Speed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float TearFallingSpeed  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How fast is the tear moving up or down when it spawns? Affects range.
___

### Tear·Flags {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [TearFlags](enums/TearFlags.md) TearFlags {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. Various [TearFlags](enums/TearFlags.md).

???- example "Example Code"
    This code makes Isaac's tears spectral.
    ```lua

    function mod:OnEvaluateTearFlags(player, flag)
        player.TearFlags = player.TearFlags | TearFlags.TEAR_SPECTRAL
    end
    mod:AddCallback(ModCallbacks.MC_EVALUATE_CACHE, mod.OnEvaluateTearFlags, CacheFlag.CACHE_TEARFLAG)
    ```

___

### Tear·Height {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float TearHeight  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How high above the ground is the tear when it spawns?

???- example "Example Code"
    This code gives Isaac a +5 range up.

    ```lua
    function mod:OnEvaluateRange(player, flag)
        -- we give -5 because the TearHeight stat is always negative; the lower the number - the further the tear travels
        player.TearHeight = player.TearHeight - 5
    end
    mod:AddCallback(ModCallbacks.MC_EVALUATE_CACHE, mod.OnEvaluateRange, CacheFlag.CACHE_RANGE)
    ```

___

### Tear·Range {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### float TearRange  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How far should a tear go when it spawns?

???+ info "Info"
    This stat needs to be multiplied by 40, because it calculates the range based on tile length.

???- example "Example Code"
    This code gives Isaac a +2 range up.

    ```lua
    function mod:OnEvaluateRange(player, flag)
        player.TearRange = player.TearRange + (2 * 40)
    end
    mod:AddCallback(ModCallbacks.MC_EVALUATE_CACHE, mod.OnEvaluateRange, CacheFlag.CACHE_RANGE)
    ```

___

### Tears·Offset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) TearsOffset  {: .copyable aria-label='Variables' }

<div class="rgon-only" markdown="1">

### AddCollectibleEffect () {: aria-label='Modified Functions' }
#### void AddCollectibleEffect ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) CollectibleType, bool ApplyCostume = false, int Cooldown = VanillaCooldown, bool Additive = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Shortcut of TemporaryEffects:AddCollectibleEffect with extra arguments to handle cooldown. The additive parameter determines whether the cooldown should be added to the pre-existing cooldown value or set as that value. You can use negative cooldown values with additive to reduce the pre-existing cooldown.

___

### AddNullItemEffect () {: aria-label='Modified Functions' }
#### void AddNullItemEffect ( [NullItemID](https://wofsauge.github.io/IsaacDocs/rep/enums/NullItemID.html) NullItemID, bool ApplyCostume = false, int Cooldown = VanillaCooldown, bool Additive = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Shortcut of TemporaryEffects:AddNullItemEffect with extra arguments to handle cooldown. The additive parameter determines whether the cooldown should be added to the pre-existing cooldown value or set as that value. You can use negative cooldown values with additive to reduce the pre-existing cooldown.

___

### AddTrinketEffect () {: aria-label='Modified Functions' }
#### void AddTrinketEffect ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) TrinketType, bool ApplyCostume = false, int Cooldown = VanillaCooldown, bool Additive = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Shortcut of TemporaryEffects:AddTrinketEffect with extra arguments to handle cooldown. The additive parameter determines whether the cooldown should be added to the pre-existing cooldown value or set as that value. You can use negative cooldown values with additive to reduce the pre-existing cooldown.

___

### AddActiveCharge () {: aria-label='Functions' }
#### int AddActiveCharge ( int Charge, [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot = ActiveSlot.SLOT_PRIMARY, boolean FlashHUD = true, boolean Overcharge = false, boolean Force = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the true amount of charge added, which may have been capped by the targeted item's MaxCharge.

???- info "Info"
    `FlashHUD` appears to be redundant. Chargebar flashes regardless of using `true` or `false`.

___

### AddBoneOrbital () {: aria-label='Functions' }
#### [EntityFamiliar](EntityFamiliar.md) AddBoneOrbital ( [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### AddCandyHeartBonus () {: aria-label='Functions' }
#### void AddCandyHeartBonus ( [CacheFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/CacheFlag.html) CacheFlag = 0, int Amount = 1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Adds a random stat bonus as if the player had collected a heart with Candy Heart. Can specify a CacheFlag to force the bonus onto a specific stat. Stats are only applied while the player has Candy Heart.

___

### AddCustomCacheTag () {: aria-label='Functions' }
#### void AddCustomCacheTag ( string OR \{string, string, ...\}, boolean EvaluateItems = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Add CustomCacheTag(s) to be evaluated next time EvaluateItems runs (which is right now, if the optional boolean is passed).

See [items.xml](xml/items.md) for more information on custom caches.

___

### AddInnateCollectible () {: aria-label='Functions' }
#### void AddInnateCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, int Amount = 1, string GroupKey = "", int Duration = -1, bool AddCostume = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
"GroupKey" is used to distinguish separate "groups" of innate items. Innate item functions can only modify items added under the specified group. Use a distinct GroupKey string to isolate your innate items from other sources, avoiding conflicts and making tracking easier.

If a GroupKey other than the default empty string is used, the innate item will persist across quit & continue, and interact properly with save state mechanics such as Glowing Hourglass.

Items added with a positive duration will automatically remove themselves (30 duration = 1 second).

___

### AddLeprosy () {: aria-label='Functions' }
#### void AddLeprosy ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "Info"
    This is currently still capped at a max of three familiars, and would require further modification to change this.

___

### AddLocust () {: aria-label='Functions' }
#### void AddLocust ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???- info "Supported Items"
    There are a few items which spawn unique locusts.
    
    - Breakfast (default)
    - The Inner Eye
    - Spoon Bender
    - Cricket's Head
    - Number One
    - Blood of the Martyr
    - Halo of Flies
    - The Common Cold
    - Brimstone
    - Ipecac
    - Mutant Spider
    - Fire Mind
    - Scorpio
    - Holy Light
    - Jacob's Ladder
    - 120 Volt

___

### AddSmeltedTrinket () {: aria-label='Functions' }
#### boolean AddSmeltedTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, boolean FirstTimePickingUp = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Adds a smelted trinket directly to the player's inventory.

Returns ``true`` if the trinket was successfully added, otherwise ``false``.

___

### AddSoulLocketBonus () {: aria-label='Functions' }
#### void AddSoulLocketBonus ( [CacheFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/CacheFlag.html) CacheFlag = 0, int Amount = 1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Adds a random stat bonus as if the player had collected a heart with Soul Locket. Can specify a CacheFlag to force the bonus onto a specific stat. Stats are only applied while the player has Soul Locket.

___

### AddUrnSouls () {: aria-label='Functions' }
#### void AddUrnSouls ( int Count = 0 ) {: .copyable aria-label='Functions' }   [ ](#){: .rgonorplus .tooltip .badge }

___

### BlockCollectible () {: aria-label='Functions' }
#### void BlockCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) {: .copyable aria-label='Functions' }   [ ](#){: .rgonorplus .tooltip .badge }
Blocks the provided [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html). This will make it so the game thinks you don't have the item, even if it's in your inventory.

___

### CanAddCollectibleToInventory () {: aria-label='Functions' }
#### boolean CanAddCollectibleToInventory ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used to determine which items can be added to Tainted Isaac's limited inventory.

___

### CanCrushRocks () {: aria-label='Functions' }
#### boolean CanCrushRocks ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???- info "Info"
    Returns `true` if the player has one of the following items / effects / transformations.
    
    - The Nail
    - Leo
    - Thunder Thighs
    - Mega Mush
    - Stompy

___

### CanOverrideActiveItem () {: aria-label='Functions' }
#### boolean CanOverrideActiveItem ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if the active slot is empty, or contains only Book of Virtues or Book of Belial from Judas' Birthright.

___

### CanUsePill () {: aria-label='Functions' }
#### boolean CanUsePill ( [PillEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/PillEffect.html) ID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Determines whether a player can use a given pill effect based on certain conditions, usually health-related.

___

### CheckFamiliarEx () {: aria-label='Functions' }
#### [EntityFamiliar](EntityFamiliar.md)[] CheckFamiliarEx ( int [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) Familiar, int TargetCount, [RNG](RNG.md) rng, [ItemConfigItem](ItemConfig_Item.md) SourceItemConfigItem = nil, int FamiliarSubType = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

A version of [CheckFamiliar](https://wofsauge.github.io/IsaacDocs/rep/EntityPlayer.html#checkfamiliar) that returns all familiars spawned by the function as a table.

___

### ClearCollectibleAnim () {: aria-label='Functions' }
#### void ClearCollectibleAnim ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ClearQueueItem () {: aria-label='Functions' }
#### void ClearQueueItem ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CreateAfterimage () {: aria-label='Functions' }
#### void CreateAfterimage ( int Duration, [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Creates an afterimage of the player that fades over the course of the given duration, similar to those created by items such as A Pony and Mars.

___

### DropCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md) DropCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, [EntityPickup](EntityPickup.md) ExistingPedestal = nil, boolean RemoveFromPlayerForm = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

If `ExistingPedestal` is set, the collectible it contains will be swapped out for the dropped collectible instead of a new pedestal spawning.

___

### DropCollectibleByHistoryIndex () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md) DropCollectibleByHistoryIndex ( int Idx, [EntityPickup](EntityPickup.md) ExistingPedestal = nil ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

If `ExistingPedestal` is set, the collectible it contains will be swapped out for the dropped collectible instead of a new pedestal spawning.

___

### EnableWeaponType () {: aria-label='Functions' }
#### void EnableWeaponType ( [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) Weapon, boolean Set ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### FireBrimstoneBall () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) FireBrimstoneBall ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, [Vector](Vector.md) Offset = Vector.Zero ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "Info"
    If the player has Tech X, this function will fire an [EntityLaser](EntityLaser.md) as well. The laser will have the Brimstone ball effect as a parent, it's unclear if the effect also links back to the laser.

___

### GetActionHoldDrop () {: aria-label='Functions' }
#### int GetActionHoldDrop ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
How long the player holds the drop-button.
___

### GetActiveItemDesc () {: aria-label='Functions' }
#### [ActiveItemDesc](https://wofsauge.github.io/IsaacDocs/rep/PlayerTypes_ActiveItemDesc.html) GetActiveItemDesc ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot = ActiveSlot.SLOT_PRIMARY ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetActiveItemSlot () {: aria-label='Functions' }
#### [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) GetActiveItemSlot ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetActiveMaxCharge () {: aria-label='Functions' }
#### int GetActiveMaxCharge ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetActiveMinUsableCharge () {: aria-label='Functions' }
#### int GetActiveMinUsableCharge ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetActiveWeaponNumFired () {: aria-label='Functions' }
#### int GetActiveWeaponNumFired ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBagOfCraftingContent () {: aria-label='Functions' }
#### [BagOfCraftingPickup](enums/BagOfCraftingPickup.md)[] GetBagOfCraftingContent ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBagOfCraftingOutput () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetBagOfCraftingOutput ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBagOfCraftingSlot () {: aria-label='Functions' }
#### [BagOfCraftingPickup](enums/BagOfCraftingPickup.md) GetBagOfCraftingSlot ( int SlotID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets the current content of the bag in the given `SlotID`.
___

### GetBladderCharge () {: aria-label='Functions' }
#### int GetBladderCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the current charge for when the player stops shooting and charges the Kidney Stone item.

___

### GetBlinkLockTime () {: aria-label='Functions' }
#### int GetBlinkLockTime ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
How long the player's head will play the fired-frame sprite.

___

### GetBloodLustCounter () {: aria-label='Functions' }
#### int GetBloodLustCounter ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBodyMoveDirection () {: aria-label='Functions' }
#### [Vector](Vector.md) GetBodyMoveDirection ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBombPlaceDelay () {: aria-label='Functions' }
#### int GetBombPlaceDelay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Default bomb place delay is `30 frames`.

___

### GetBodySprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetBodySprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Temporary copy of body player sprite while null animation is active.

___

### GetCambionConceptionState () {: aria-label='Functions' }
#### int GetCambionConceptionState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns how many times the player has taken damage with the Cambion Conception item.

___

### GetCandyHeartBonus () {: aria-label='Functions' }
#### table GetCandyHeartBonus ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of fields corresponding to each stat that Candy Heart can increase and the active amount of bonuses tied to each stat.

The fields are: `FireDelay`, `Damage`, `TearRange`, `ShotSpeed`, `Luck`, `MoveSpeed`.

___

### GetCambionPregnancyLevel () {: aria-label='Functions' }
#### int GetCambionPregnancyLevel ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Corresponds to the current visible state of Cambion Conception's costume (0-2).

___

### GetCharmOfTheVampireKills () {: aria-label='Functions' }
#### int GetCharmOfTheVampireKills ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollectiblesList () {: aria-label='Functions' }
#### table GetCollectiblesList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table with the amount of each collectible the player has, without counting innate items.

???- example "Example Code"
    This code prints how many sad onions the player has.

    ```lua
    local collectiblesList = player:GetCollectiblesList()

    print(collectiblesList[CollectibleType.COLLECTIBLE_SAD_ONION])
    ```

___

### GetConceptionFamiliarFlags () {: aria-label='Functions' }
#### [ConceptionFamiliarFlag](enums/ConceptionFamiliarFlag.md) GetConceptionFamiliarFlags ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the bitmask corresponding to which familiars have been spawned by Cambion/Immaculate Conception. The additional familiars provided by this bitmask are spawned during familiar cache evaluation, but only while the player has one of those two items.

___

### GetCostumeLayerMap () {: aria-label='Functions' }
#### table GetCostumeLayerMap ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns table of player sprite layers data for costumes with the following fields:

|Field|Type|Comment|
|:--|:--|:--|
| costumeIndex | int | Index of active/visible costume for that layer.  `-1` if no costume is on that layer. |
| layerID | int | ID of the sprite's layer corresponding to its anm2 file. `-1` if no costume is on that layer. |
| priority | int | Costume's priority as listed in `costumes2.xml`. `-1` if no costume is on that layer. |
| isBodyLayer | boolean | `true` if the costume is a body costume. `false` if not or if no costume is on that layer. |

???- info "More Layer Map Info"

    The returned table's index order corresponds to PlayerSpriteLayer. However, due to the differences in the starting index of arrays between Lua and C++, CostumeLayerMap's index needs to be decreased by 1 and it's costumeIndex increased by 1 in order to get accurate information.

    Below is a snippet of code that displays all currently occupied costume layers.
    Prints are sectioned as such: PlayerSpriteLayer - Layer Name - Item Name/NullItemID - Anm2 filepath

    ???+ example "Example Code"
        ```lua
        local player = Isaac.GetPlayer()
        local map = Isaac.GetPlayer():GetCostumeLayerMap()
        print("-------------------------------------------------------------------")
        local costumeSpriteDescs = player:GetCostumeSpriteDescs()
        for layer, mapData in ipairs(map) do
            if mapData.costumeIndex == -1 then goto continue end
            local costumeSpriteDesc = costumeSpriteDescs[mapData.costumeIndex + 1]
            local sprite = costumeSpriteDesc:GetSprite()
            local itemConfig = costumeSpriteDesc:GetItemConfig()
            local layerName = sprite:GetLayer(mapData.layerID):GetName()
            local costumeName = itemConfig.Name ~= "" and Isaac.GetString("Items", itemConfig.Name) or "NullItemID "..itemConfig.ID
            local spritePath = sprite:GetFilename()
            print(layer - 1, "-", layerName, "-", costumeName, "-", spritePath)
            ::continue::
        end
        print("-------------------------------------------------------------------")
        ```

___

### GetCostumeSpriteDescs () {: aria-label='Functions' }
#### [CostumeSpriteDesc](CostumeSpriteDesc.md)[] GetCostumeSpriteDescs ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of [CostumeSpriteDesc](CostumeSpriteDesc.md).

___

### GetCustomCacheValue () {: aria-label='Functions' }
#### float GetCustomCacheValue ( string CustomCacheTag ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the current cached value for the specified CustomCacheTag. Will return `0` by default if the provided tag has not been evaluated.

See [items.xml](xml/items.md) for more information on custom caches.

___

### GetD8DamageModifier () {: aria-label='Functions' }
#### float GetD8DamageModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetD8FireDelayModifier () {: aria-label='Functions' }
#### float GetD8FireDelayModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetD8RangeModifier () {: aria-label='Functions' }
#### float GetD8RangeModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetD8SpeedModifier () {: aria-label='Functions' }
#### float GetD8SpeedModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDamageModifier () {: aria-label='Functions' }
#### int GetDamageModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

The modifier is applied to the player's damage stat as flat damage.

Experimental Treatment adds `-1`, `0` or `1` depending on the damage rolled. Void may randomly add `1`.

___

### GetDeadEyeCharge () {: aria-label='Functions' }
#### int GetDeadEyeCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDeathAnimName () {: aria-label='Functions' }
#### string GetDeathAnimName ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the name of the player's death animation.

???+ info "Return info"
    This can return the following strings:

    - `Death` - The regular death animation name.
    - `LostDeath` - When playing as the Lost, under the Lost Curse, playing as Forgotten's Soul, or in Tainted Jacob's Ghost form.

___

### GetEdenDamage () {: aria-label='Functions' }
#### float GetEdenDamage ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the offset of the player's damage stat for Eden's random stats.

___

### GetEdenFireDelay () {: aria-label='Functions' }
#### float GetEdenFireDelay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the offset of the player's fire delay stat for Eden's random stats.

___

### GetEdenLuck () {: aria-label='Functions' }
#### float GetEdenLuck ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the offset of the player's luck stat for Eden's random stats.

___

### GetEdenRange () {: aria-label='Functions' }
#### float GetEdenRange ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the offset of the player's range stat for Eden's random stats.

___

### GetEdenShotSpeed () {: aria-label='Functions' }
#### float GetEdenShotSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the offset of the player's shot speed stat for Eden's random stats.

___

### GetEdenSpeed () {: aria-label='Functions' }
#### float GetEdenSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the offset of the player's speed stat for Eden's random stats.

___

### GetEnterPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetEnterPosition ( ) {: .copyable aria-label='Functions' }         [ ](#){: .rgonorplus .tooltip .badge }

___

### GetEntityConfigPlayer () {: aria-label='Functions' }
#### [EntityConfigPlayer](EntityConfigPlayer.md) GetEntityConfigPlayer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetEpiphoraCharge () {: aria-label='Functions' }
#### int GetEpiphoraCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetEveSumptoriumCharge () {: aria-label='Functions' }
#### int GetEveSumptoriumCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the current charge of Tainted Eve's innate Sumptorium ability.

___

### GetFireDelayModifier () {: aria-label='Functions' }
#### int GetFireDelayModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

Grants `0.5 * modifier` flat tears per second to the player.

Experimental Treatment adds `-1`, `0` or `1` depending on the fire delay rolled. Void may randomly add `1`.

___

### GetFlippedForm () {: aria-label='Functions' }
#### [EntityPlayer](EntityPlayer.md) GetFlippedForm ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns flipped form of the current character. (only used for Tainted Lazarus)

Otherwise, returns `nil`.

___

### GetFocusEntity () {: aria-label='Functions' }
#### [Entity](Entity.md) GetFocusEntity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the entity used by Active Camera to determine where the camera should focus. This can be either the [Marked](https://bindingofisaacrebirth.fandom.com/wiki/Marked) target [EntityEffect](EntityEffect.md) or a weapon's entity. 
If none of these exist, this returns `nil`.

___

### GetFootprintColor () {: aria-label='Functions' }
#### [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) GetFootprintColor ( boolean LeftFootprint ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetForgottenSwapFormCooldown () {: aria-label='Functions' }
#### int GetForgottenSwapFormCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetGlitchBabySubType () {: aria-label='Functions' }
#### int GetGlitchBabySubType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetGlyphOfBalanceDrop () {: aria-label='Functions' }
#### table GetGlyphOfBalanceDrop ( int Variant = -1, int SubType = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table containing the variant and subtype of the possible [Glyph of Balance](https://bindingofisaacrebirth.fandom.com/wiki/Glyph_of_Balance) drop.
___

### GetGnawedLeafTimer () {: aria-label='Functions' }
#### int GetGnawedLeafTimer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetGreedsGulletHearts () {: aria-label='Functions' }
#### int GetGreedsGulletHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetHallowedGroundCountdown () {: aria-label='Functions' }
#### int GetHallowedGroundCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the grace period countdown of retaining stats from the Hallowed Ground/Star of Bethlehem aura.

___

### GetHeadDirectionLockTime () {: aria-label='Functions' }
#### int GetHeadDirectionLockTime ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
How long the player's head should be forced to stay in its current direction. `-1` (or lower) indicates the direction is not currently locked.

___

### GetHealthType () {: aria-label='Functions' }
#### [HealthType](enums/HealthType.md) GetHealthType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetHeldEntity () {: aria-label='Functions' }
#### [Entity](Entity.md) GetHeldEntity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the Entity that the player is holding over their head, such as with throwable red bombs or [Suplex!](https://bindingofisaacrebirth.fandom.com/wiki/Suplex!)
Returns `nil` if no entity is currently being held.

___

### GetHeldSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetHeldSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets the [Sprite](Sprite.md) object used for when the player is doing an animation that involves holding a sprite over their head, such as active item usage.

___

### GetHistory () {: aria-label='Functions' }
#### [History](History.md) GetHistory ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetImmaculateConceptionState () {: aria-label='Functions' }
#### int GetImmaculateConceptionState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns how many hearts have been collected with the Immaculate Conception item. Resets to 0 after spawning a familiar/soul heart.

___

### GetItemStateCooldown () {: aria-label='Functions' }
#### int GetItemStateCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetKeepersSackBonus () {: aria-label='Functions' }
#### int GetKeepersSackBonus ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets the number of coins spent while possessing [Keeper's Sack](https://bindingofisaacrebirth.fandom.com/wiki/Keeper's_Sack).

___

### GetLaserColor () {: aria-label='Functions' }
#### [Color](Color.md) GetLaserColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetLuckModifier () {: aria-label='Functions' }
#### int GetLuckModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

The modifier is added directly to the player's Luck stat.

Experimental Treatment adds `-1`, `0` or `1` depending on the luck rolled. Void may randomly add `1`.

___

### GetMaggyHealthDrainCooldown () {: aria-label='Functions' }
#### int GetMaggyHealthDrainCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMaggySwingCooldown () {: aria-label='Functions' }
#### int GetMaggySwingCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the amount of frames left until Tainted Magdalene's swing attack from being damaged can be used again. Returns `0` if the player is not Tainted Magdalene.

___

### GetMarkedTarget () {: aria-label='Functions' }
#### [EntityEffect](https://wofsauge.github.io/IsaacDocs/rep/EntityEffect.html) GetMarkedTarget ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the entity effect representing the target of the [Marked](https://bindingofisaacrebirth.fandom.com/wiki/Marked) item. 
If the target is not displayed on the ground, this function returns `nil`.

___

### GetMaxBladderCharge () {: aria-label='Functions' }
#### int GetMaxBladderCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the maximum charge for when the player stops shooting and charges the Kidney Stone item.

___

### GetMaxBombs () {: aria-label='Functions' }
#### int GetMaxBombs ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the maximum number of bombs the player can currently hold.

___

### GetMaxCoins () {: aria-label='Functions' }
#### int GetMaxCoins ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the maximum number of coins the player can currently hold.

___

### GetMaxKeys () {: aria-label='Functions' }
#### int GetMaxKeys ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the maximum number of keys the player can currently hold.

___

### GetMaxPeeBurstCooldown () {: aria-label='Functions' }
#### int GetMaxPeeBurstCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the maximum attack duration of the Kidney Stone item.

___

### GetMegaBlastDuration () {: aria-label='Functions' }
#### int GetMegaBlastDuration ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMetronomeCollectibleID () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetMetronomeCollectibleID ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMovingBoxContents () {: aria-label='Functions' }
#### [EntitiesSaveStateVector](EntitiesSaveStateVector.md) GetMovingBoxContents ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the pickups that are stored on the player through the use of the Moving Box collectible.

___

### GetNextUrethraBlockFrame () {: aria-label='Functions' }
#### int GetNextUrethraBlockFrame ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the frame at which the player stops shooting and starts charging the [Kidney Stone](https://bindingofisaacrebirth.fandom.com/wiki/Kidney_Stone) item.

___

### GetPlanCKillCountdown () {: aria-label='Functions' }
#### int GetPlanCKillCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPeeBurstCooldown () {: aria-label='Functions' }
#### int GetPeeBurstCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the attack duration of the [Kidney Stone](https://bindingofisaacrebirth.fandom.com/wiki/Kidney_Stone) item.

___

### GetPotatoPeelerUses () {: aria-label='Functions' }
#### int GetPotatoPeelerUses ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used to increment [Cube of Meat](https://bindingofisaacrebirth.wiki.gg/wiki/Cube_of_Meat) familiar form.

___

### GetPlayerFormCounter () {: aria-label='Functions' }
#### int GetPlayerFormCounter ( [PlayerForm](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerForm.html) PlayerFormID ) {: .copyable aria-label='Functions' }  [ ](#){: .rgonorplus .tooltip .badge }
Returns the amount of collectibles the player has tied to the specified transformation.

___

### GetPlayerHUD () {: aria-label='Functions' }
#### [PlayerHUD](PlayerHUD.md) GetPlayerHUD ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPlayerIndex () {: aria-label='Functions' }
#### int GetPlayerIndex ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPonyCharge () {: aria-label='Functions' }
#### int GetPonyCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the amount of frames left until the charging effect from the A Pony or White Pony item deactivates.

___

### GetPurityState () {: aria-label='Functions' }
#### [PurityState](enums/PurityState.md) GetPurityState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the state in which the [Purity](https://bindingofisaacrebirth.fandom.com/wiki/Purity) item effect currently is. Returns `PurityState.BLUE` if the player does not have the Purity collectible.

___

### GetRedStewBonusDuration () {: aria-label='Functions' }
#### int GetRedStewBonusDuration ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the frames left until the damage bonus from Red Stew expires.

___

### GetRevelationCharge () {: aria-label='Functions' }
#### float GetRevelationCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomDamage () {: aria-label='Functions' }
#### float GetRockBottomDamage ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomLuck () {: aria-label='Functions' }
#### float GetRockBottomLuck ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomMaxFireDelay () {: aria-label='Functions' }
#### float GetRockBottomMaxFireDelay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomMoveSpeed () {: aria-label='Functions' }
#### float GetRockBottomMoveSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomShotSpeed () {: aria-label='Functions' }
#### float GetRockBottomShotSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomTearRange () {: aria-label='Functions' }
#### float GetRockBottomTearRange ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetShotSpeedModifier () {: aria-label='Functions' }
#### int GetShotSpeedModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

Adds `0.2 * modifier` to the player's ShotSpeed.

Experimental Treatment adds `-1`, `0` or `1` depending on the shot speed rolled. Void may randomly add `1`.

___

### GetSmeltedTrinkets () {: aria-label='Functions' }
#### table GetSmeltedTrinkets ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html)[] TrinketList = nil ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of smelted trinkets and their corresponding amounts. The returned table contains the following fields:

|Field|Type|Comment|
|:--|:--|:--|
| trinketAmount | int | |
| goldenTrinketAmount | int | |

The optional TrinketList param can be used as a filter to only return the provided TrinketTypes for better performance.

___

### GetSmeltedTrinketDesc () {: aria-label='Functions' }
#### table GetSmeltedTrinketDesc ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of the provided smelted trinket and their corresponding amounts. The returned table contains the following fields:

|Field|Type|Comment|
|:--|:--|:--|
| trinketAmount | int | |
| goldenTrinketAmount | int | |

___

### GetSoulLocketBonus () {: aria-label='Functions' }
#### table GetSoulLocketBonus ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of fields corresponding to each stat that Soul Locket can increase and the active amount of bonuses tied to each stat.

The fields are: `FireDelay`, `Damage`, `TearRange`, `ShotSpeed`, `Luck`, `MoveSpeed`.

___

### GetSpecialGridCollision () {: aria-label='Functions' }
#### int GetSpecialGridCollision ( [Vector](Vector.md) Position = self.Position ) {: .copyable aria-label='Functions' }       [ ](#){: .rgonorplus .tooltip .badge }

___

### GetSpeedModifier () {: aria-label='Functions' }
#### int GetSpeedModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

Adds `0.2 * modifier` to the player's MoveSpeed.

Experimental Treatment adds `-1`, `0` or `1` depending on the speed rolled. Void may randomly add `1`.

___

### GetSpoofedCollectiblesList () {: aria-label='Functions' }
#### table[] GetSpoofedCollectiblesList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

|Field|Type|Comment|
|:--|:--|:--|
| CollectibleID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | |
| AppendedCount | int | |
| IsBlocked | boolean | |

___

### GetStatMultiplier () {: aria-label='Functions' }
#### float GetStatMultiplier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the multiplier added to stats gained from any items.

???- info "Multipliers"
    - **Tainted Bethany**: x0.75
    - **Cracked Crown**: x1.2

___

### GetSuplexAimCountdown () {: aria-label='Functions' }
#### int GetSuplexAimCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSuplexLandPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetSuplexLandPosition ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSuplexState () {: aria-label='Functions' }
#### [SuplexState](enums/SuplexState.md) GetSuplexState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSuplexTargetPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetSuplexTargetPosition ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetTearDisplacement () {: aria-label='Functions' }
#### int GetTearDisplacement ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the player's TearDisplacement value, used to determine which eye the player is shooting from.

???+ info "Return info"
    - `1` Right eye
    - `-1` Left eye

___

### GetTearsCap () {: aria-label='Functions' }
#### int GetTearsCap ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the soft tears cap. Default is `5.0`. Not affected by firedelay modifiers.

___

### GetTotalActiveCharge () {: aria-label='Functions' }
#### int GetTotalActiveCharge ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetUrnSouls () {: aria-label='Functions' }
#### int GetUrnSouls ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetVoidedCollectiblesList () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)[] GetVoidedCollectiblesList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Retuns a table containing the [CollectibleTypes](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) of all voided Active items.

___

### GetWeapon () {: aria-label='Functions' }
#### [Weapon](Weapon.md) GetWeapon ( int Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the Weapon object in the corresponding slot, or `nil` if no Weapon can be found. Slot needs to be between `0` and `4`.

???- info "Info"
    Weapon slots and their descriptions:

    - `0` - Backup Weapon such as Notched Axe and Urn of Souls.
    - `1` - Primary Weapon.
    - `2` - Additional Weapon. Few instances of this exist in the vanilla game, but it can be populated by mods.
    - `3` - Additional Weapon.
    - `4` - Additional Weapon.

    Always check for `nil`, even for slot `1` as it can be deleted by mods via [Isaac.DestroyWeapon()](Isaac.md#destroyweapon).

___

### GetWeaponModifiers () {: aria-label='Functions' }
#### int GetWeaponModifiers ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a bitmask of [WeaponModifiers](enums/WeaponModifier.md).

___

### GetWildCardItem () {: aria-label='Functions' }
#### int GetWildCardItem ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the item that was last used by the player and would be activated again upon using Wild Card.

If the player used an active item, its `CollectibleType` is returned. If the player used a consumable, its variant is returned. If the player used ? Mark Card, returns `1`. If no active item had ever been used by the player before, turns `0`.

___

### GetWildCardItemType () {: aria-label='Functions' }
#### [PocketItemType](enums/PocketItemType.md) GetWildCardItemType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the type of item that was last used by the player and would be activated again upon using Wild Card.

If the player used a consumable (including ? Mark Card), returns `ItemType.ITEM_PASSIVE`. If no active item had been used by the player before, returns `255`.

___

### GetWispCollectiblesList () {: aria-label='Functions' }
#### table GetWispCollectiblesList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of [CollectibleTypes](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) corresponding to the item wisps the player has.

___

### HasCamoEffect () {: aria-label='Functions' }
#### boolean HasCamoEffect ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### HasChanceRevive () {: aria-label='Functions' }
#### boolean HasChanceRevive ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if a "?" would be displayed on the player's extra life count (ie, the player has Guppy's Collar, or a modded revive item with the `chancerevive` string in REPENTOGON's [customtags items.xml attribute](xml/items.md)).

___

### HasForcedCamoEffect () {: aria-label='Functions' }
#### boolean HasForcedCamoEffect ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### HasGoldenTrinket () {: aria-label='Functions' }
#### boolean HasGoldenTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if you have a golden variant of the provided [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html).

___

### HasInstantDeathCurse () {: aria-label='Functions' }
#### boolean HasInstantDeathCurse ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true when the player is in the Lost form triggered by either the white fire in Downpour or Soul of The Lost. (or when in Tainted Jacob's ghost form when being touched by Dark Esau)

___

### HasPoisonImmunity () {: aria-label='Functions' }
#### boolean HasPoisonImmunity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???- info "Info"
    Returns `true` if the player has one of the following items / effects / transformations.

	- Bob transformation
    - Bob's Curse
    - Jupiter

___

### IncrementPlayerFormCounter () {: aria-label='Functions' }
#### void IncrementPlayerFormCounter ( [PlayerForm](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerForm.html) Form, int Count ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Increases or decreases the counter towards one of the player's transformations. `Count` can be negative to decrement the [PlayerForm](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerForm.html).

___

### InitPostLevelInitStats () {: aria-label='Functions' }
#### void InitPostLevelInitStats ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Call this after spawning characters with "special" tears (Forgotten, Lilith, Azazel etc) with InitTwin, or they won't have their proper tear type.

___

### InitTwin () {: aria-label='Functions' }
#### [EntityPlayer](EntityPlayer.md) InitTwin ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) PlayerType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Initializes a "twin" player that is controlled by the player's same controller, similarly to Jacob & Esau.

___

### IsCollectibleAnimFinished () {: aria-label='Functions' }
#### boolean IsCollectibleAnimFinished ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, string Animation ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if the animation associated with the collectible is visible.

___

### IsCollectibleBlocked () {: aria-label='Functions' }
#### boolean IsCollectibleBlocked ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if the [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) was blocked. Collectibles can only be blocked by use of [BlockCollectible](EntityPlayer.md#blockcollectible).

___

### IsCollectibleCostumeVisible () {: aria-label='Functions' }
#### boolean IsCollectibleCostumeVisible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, int PlayerSpriteLayerID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
#### boolean IsCollectibleCostumeVisible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, string PlayerSpriteLayerName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if the costume associated with the collectible is visible.

___

### IsEntityValidTarget () {: aria-label='Functions' }
#### boolean IsEntityValidTarget ( [Entity](Entity.md) Entity ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `false` for entities such as Dark Esau or Blood Puppy in its angered form.

___

### IsFootstepFrame () {: aria-label='Functions' }
#### boolean IsFootstepFrame ( int Foot = -1 ) {: .copyable aria-label='Functions' }        [ ](#){: .rgonorplus .tooltip .badge }
???+ info "Info"
    - `-1` - Returns true every 12 frames.
    - `0` - Returns true every 24 frames.
    - `1` - Always false.

___

### IsHeadless () {: aria-label='Functions' }
#### boolean IsHeadless ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` is the player is headless due to collectibles such as Guillotine, The Intruder, Scissors, and Decap Attack.

___

### IsHologram () {: aria-label='Functions' }
#### boolean IsHologram ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if the player is the non-active form of Tainted Lazarus with Birthright.

___

### IsInvisible () {: aria-label='Functions' }
#### boolean IsInvisible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if the player has the Faded Polaroid / Camo Undies effect active.

___

### IsItemCostumeVisible () {: aria-label='Functions' }
#### boolean IsItemCostumeVisible ( [ItemConfig_Item](ItemConfig_Item.md) Item, int PlayerSpriteLayerID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
#### boolean IsItemCostumeVisible ( [ItemConfig_Item](ItemConfig_Item.md) Item, int PlayerSpriteLayerName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsLocalPlayer () {: aria-label='Functions' }
#### boolean IsLocalPlayer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
For online play. Returns `true` if you're a local player, `false` otherwise.

___

### IsNullItemCostumeVisible () {: aria-label='Functions' }
#### boolean IsNullItemCostumeVisible ( int nullItem, int layerID = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
#### boolean IsNullItemCostumeVisible ( int nullItem, string layerName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsPacifist () {: aria-label='Functions' }
#### boolean IsPacifist ( ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsPostLevelInitFinished () {: aria-label='Functions' }
#### boolean IsPostLevelInitFinished ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsUrethraBlocked () {: aria-label='Functions' }
#### boolean IsUrethraBlocked ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true when the player can no longer shoot due to charging the [Kidney Stone](https://bindingofisaacrebirth.fandom.com/wiki/Kidney_Stone) item.

___

### MorphToCoopGhost () {: aria-label='Functions' }
#### void MorphToCoopGhost ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Turns the player into a co-op ghost.

___

### PlayCollectibleAnim () {: aria-label='Functions' }
#### void PlayCollectibleAnim ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean CheckBodyLayers, string AnimationName, int Frame = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Plays an animation tied to the provided collectible.

___

### PlayDelayedSFX () {: aria-label='Functions' }
#### void PlayDelayedSFX ( [SoundEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/SoundEffect.html) ID, int SoundDelay = 0, int FrameDelay = 2, float Volume = 1.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Plays a sound effect after a delay.

___

### PlayItemNullAnimation () {: aria-label='Functions' }
#### boolean PlayItemNullAnimation ( string AnimationName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns ``true`` if animation was set successfully, ``false`` otherwise. Useful for item state/hold items.

___

### RemoveCollectibleByHistoryIndex () {: aria-label='Functions' }
#### void RemoveCollectibleByHistoryIndex ( int Index ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Removes the collectible from the player associated with the specified history index.

___

### RemovePocketItem () {: aria-label='Functions' }
#### void RemovePocketItem ( [PillCardSlot](enums/PillCardSlot.md) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### RemovePoopSpell () {: aria-label='Functions' }
#### void RemovePoopSpell ( int Position = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Removes the poop spell from the specified queue position and shifts all spells after it forward to fill the space. A new spell is randomly picked to fill the last position. Poop spells are only used by Tainted ???.

___

### RerollAllCollectibles () {: aria-label='Functions' }
#### void RerollAllCollectibles ( [RNG](RNG.md) rng, boolean includeActiveItems ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Rerolls all of the player's collectibles.

___

### ResetPlayer () {: aria-label='Functions' }
#### void ResetPlayer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Info"
    This is used by the Genesis active item.

___

### ReviveCoopGhost () {: aria-label='Functions' }
#### boolean ReviveCoopGhost ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SalvageCollectible () {: aria-label='Functions' }
#### void SalvageCollectible ( [EntityPickup](EntityPickup.md) Pickup, [RNG](RNG.md) rng = PickupDropRNG, [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) Pool = ItemPoolType.POOL_NULL) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
#### void SalvageCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, [Vector](Vector.md) position = playerPosition, [RNG](RNG.md) rng = PlayerDropRNG, [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) Pool = ItemPoolType.POOL_NULL ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Produces a random quantity of various pickups, similar to Tainted Cain's ability.

???+ info "Info"
    The provided [EntityPickup](EntityPickup.md) will be removed by this function. Use the override to avoid this.

___

### SetActionHoldDrop () {: aria-label='Functions' }
#### void SetActionHoldDrop ( int duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetActiveVarData () {: aria-label='Functions' }
#### void SetActiveVarData ( int VarData, [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBagOfCraftingContent () {: aria-label='Functions' }
#### void SetBagOfCraftingContent ( [BagOfCraftingPickup](enums/BagOfCraftingPickup.md)[] ContentTable ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the content of the bag to the content of the table. Table must use valid [BagOfCraftingPickup](enums/BagOfCraftingPickup.md) ids. Table can be shorter than 8, in which case the remaining indexes are set to empty.

___

### SetBagOfCraftingOutput () {: aria-label='Functions' }
#### void SetBagOfCraftingOutput ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the output of the player's Bag of Crafting to the specified collectible.

___

### SetBagOfCraftingSlot () {: aria-label='Functions' }
#### void SetBagOfCraftingSlot ( int SlotID, [BagOfCraftingPickup](enums/BagOfCraftingPickup.md) PickupID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the specified slot in the player's Bag of Crafting to the specified pickup.

If a slot is set to empty (0 - `BagOfCraftingPickup.BOC_NONE`) then all slots after it will automatically be shifted down to fill the empty space.

___

### SetBlackHeart () {: aria-label='Functions' }
#### void SetBlackHeart ( int BlackHeart ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBladderCharge () {: aria-label='Functions' }
#### void SetBladderCharge ( int Charge ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used by the [Kidney Stone](https://bindingofisaacrebirth.fandom.com/wiki/Kidney_Stone) item.

???+ bug "Bug"
    The player's head turns pitch black when this function is used without Kidney Stone.

___

### SetBlinkLockTime () {: aria-label='Functions' }
#### void SetBlinkLockTime ( int Time ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBloodLustCounter () {: aria-label='Functions' }
#### void SetBloodLustCounter ( int Counter ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBombPlaceDelay () {: aria-label='Functions' }
#### void SetBombPlaceDelay ( int Delay ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetCambionConceptionState () {: aria-label='Functions' }
#### void SetCambionConceptionState ( int State ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets how much damage has been taken for the Cambion Conception item.

Note that the game only spawns a familiar when the player takes damage, if this counter is now at 15, 30, 60 or 90. You cannot trigger a birth directly with this function.

___

### SetCanShoot () {: aria-label='Functions' }
#### boolean SetCanShoot ( boolean CanShoot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Instantaneously disables (or enables) the player's ability to shoot. The base game primarily uses this for special challenges.

___

### SetCharmOfTheVampireKills () {: aria-label='Functions' }
#### void SetCharmOfTheVampireKills ( int KillAmount ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetConceptionFamiliarFlags () {: aria-label='Functions' }
#### void SetConceptionFamiliarFlags ( [ConceptionFamiliarFlag](enums/ConceptionFamiliarFlag.md) Flags ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the bitmask corresponding to which familiars have been spawned by Cambion/Immaculate Conception. The additional familiars provided by this bitmask are spawned during familiar cache evaluation, but only while the player has one of those two items.

___

### SetControllerIndex () {: aria-label='Functions' }
#### void SetControllerIndex ( int Idx, boolean IncludePlayerOwned = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Changes the player's controller index.

If `IncludePlayerOwned` is set to true, also sets the ControllerIndex for the player's subplayer/twinplayer, if any.

___

### SetD8DamageModifier () {: aria-label='Functions' }
#### void SetD8DamageModifier ( float Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetD8FireDelayModifier () {: aria-label='Functions' }
#### void SetD8FireDelayModifier ( float Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetD8RangeModifier () {: aria-label='Functions' }
#### void SetD8RangeModifier ( float Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetD8SpeedModifier () {: aria-label='Functions' }
#### void SetD8SpeedModifier ( float Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetDamageModifier () {: aria-label='Functions' }
#### void SetDamageModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

Modifier is applied to the player as flat damage.

Experimental Treatment adds `-1`, `0` or `1` depending on the damage rolled. Void may randomly add `1`.

___

### SetEdenDamage () {: aria-label='Functions' }
#### void SetEdenDamage ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the offset of the player's damage stat for Eden's random stats. Has no effect on players that aren't Eden or Tainted Eden.

___

### SetEdenFireDelay () {: aria-label='Functions' }
#### void SetEdenFireDelay ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the offset of the player's fire delay stat for Eden's random stats. Has no effect on players that aren't Eden or Tainted Eden.

___

### SetEdenLuck () {: aria-label='Functions' }
#### void SetEdenLuck ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the offset of the player's luck stat for Eden's random stats. Has no effect on players that aren't Eden or Tainted Eden.

___

### SetEdenRange () {: aria-label='Functions' }
#### void SetEdenRange ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the offset of the player's range stat for Eden's random stats. Has no effect on players that aren't Eden or Tainted Eden.

___

### SetEdenShotSpeed () {: aria-label='Functions' }
#### void SetEdenShotSpeed ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the offset of the player's shot speed stat for Eden's random stats. Has no effect on players that aren't Eden or Tainted Eden.

___

### SetEdenSpeed () {: aria-label='Functions' }
#### void SetEdenSpeed ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the offset of the player's speed stat for Eden's random stats. Has no effect on players that aren't Eden or Tainted Eden.

___

### SetEveSumptoriumCharge () {: aria-label='Functions' }
#### void SetEveSumptoriumCharge ( int ChargeNum ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the current charge of Tainted Eve's innate Sumptorium ability.

___

### SetFireDelayModifier () {: aria-label='Functions' }
#### void SetFireDelayModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

Grants `0.5 * modifier` flat tears per second to the player.

Experimental Treatment adds `-1`, `0` or `1` depending on the fire delay rolled. Void may randomly add `1`.

___

### SetFootprintColor () {: aria-label='Functions' }
#### void SetFootprintColor ( [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) color, boolean RightFoot = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the player's footprint color.

___

### SetForceCamoEffect () {: aria-label='Functions' }
#### void SetForceCamoEffect ( boolean Force ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetForgottenSwapFormCooldown () {: aria-label='Functions' }
#### void SetForgottenSwapFormCooldown ( int Cooldown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetGnawedLeafTimer () {: aria-label='Functions' }
#### void SetGnawedLeafTimer ( int Timer ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetHallowedGroundCountdown () {: aria-label='Functions' }
#### void SetHallowedGroundCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the grace period countdown of retaining stats from the Hallowed Ground/Star of Bethlehem aura.

___

### SetHeadDirection () {: aria-label='Functions' }
#### void SetHeadDirection ( [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html) Direction, int Time, boolean Force = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Locks the player's head animation to the specified [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html). `Force` will override existing head direction locks, such as the one from firing Mom's Knife.

___

### SetHeadDirectionLockTime () {: aria-label='Functions' }
#### void SetHeadDirectionLockTime ( int Time ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
How long the player's head should be forced to stay in its current direction.

___

### SetImmaculateConceptionState () {: aria-label='Functions' }
#### void SetImmaculateConceptionState ( int State ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets how many hearts have been collected for the Immaculate Conception item.

Note that the game checks to spawn a familiar only when the player picks up a heart, so you cannot trigger that directly with this function.

If you set a value that is greater than 14, the value is automatically capped at 14, meaning that the next heart picked up will spawn a familiar.

___

### SetItemState () {: aria-label='Functions' }
#### void SetItemState ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Changes the player's item state to the specified collectible. This is usually used for collectibles that the player holds above their head before activating (i.e: Bob's Rotten Head, Glass Cannon).

___

### SetItemStateCooldown () {: aria-label='Functions' }
#### void SetItemStateCooldown ( int Cooldown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetKeepersSackBonus () {: aria-label='Functions' }
#### void SetKeepersSackBonus ( int Bonus ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the current coin bonus for the player's [Keeper's Sack](https://bindingofisaacrebirth.fandom.com/wiki/Keeper's_Sack) collectible.

___

### SetLaserColor () {: aria-label='Functions' }
#### void SetLaserColor ( [Color](Color.md) color ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the player's laser color.

___

### SetLuckModifier () {: aria-label='Functions' }
#### void SetLuckModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

The modifier is added directly to the player's Luck stat.

Experimental Treatment adds `-1`, `0` or `1` depending on the luck rolled. Void may randomly add `1`.

___

### SetMaggyHealthDrainCooldown () {: aria-label='Functions' }
#### void SetMaggyHealthDrainCooldown ( int Cooldown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetMaggySwingCooldown () {: aria-label='Functions' }
#### void SetMaggySwingCooldown ( int Cooldown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the cooldown of Tainted Magdalene's swing attack to the specified amount of frames.

___

### SetMaxBladderCharge () {: aria-label='Functions' }
#### void SetMaxBladderCharge ( int Charge ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the maximum charge for when the player stops shooting and charges the Kidney Stone item.

___

### SetMegaBlastDuration () {: aria-label='Functions' }
#### void SetMegaBlastDuration ( int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the duration of the Mega Blast laser to the specified amount of frames. Setting the duration above zero will activate the effect if it wasn't already active.

???+ bug "Bug"
	If the Mega Blast laser is active and you call the function again with a lower duration, the laser will persist even after the amount of frames has passed until the player leaves the room.

___

### SetNextUrethraBlockFrame () {: aria-label='Functions' }
#### void SetNextUrethraBlockFrame ( int Frame ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the frame at which the player stops shooting and starts charging the Kidney Stone item.

___

### SetPlanCKillCountdown () {: aria-label='Functions' }
#### void SetPlanCKillCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetPonyCharge () {: aria-label='Functions' }
#### void SetPonyCharge ( int Time ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the duration of the charge effect from the A Pony and White Pony to the specified amount of frames.

___

### SetPoopSpell () {: aria-label='Functions' }
#### void SetPoopSpell ( int Slot, [PoopSpellType](https://wofsauge.github.io/IsaacDocs/rep/enums/PoopSpellType.html) PoopSpellType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the specified slot in the poop list to a type of poop. This is only used by Tainted ???.

___

### SetPotatoPeelerUses () {: aria-label='Functions' }
#### void SetPotatoPeelerUses ( int Amount ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetPurityState () {: aria-label='Functions' }
#### void SetPurityState ( [PurityState](enums/PurityState.md) State ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the state of the [Purity](https://bindingofisaacrebirth.fandom.com/wiki/Purity) item effect.

___

### SetRedStewBonusDuration () {: aria-label='Functions' }
#### void SetRedStewBonusDuration ( int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the duration of the damage bonus given by the Red Stew collectible to the specified amount of frames. Setting the duration above 0 will activate the effect if it wasn't active already.

___

### SetRevelationCharge () {: aria-label='Functions' }
#### void SetRevelationCharge ( float Charge ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomDamage () {: aria-label='Functions' }
#### void SetRockBottomDamage ( float Damage ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomLuck () {: aria-label='Functions' }
#### void SetRockBottomLuck ( float Luck ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomMaxFireDelay () {: aria-label='Functions' }
#### void SetRockBottomMaxFireDelay ( float MaxFireDelay ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomMoveSpeed () {: aria-label='Functions' }
#### void SetRockBottomMoveSpeed ( float MoveSpeed ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomShotSpeed () {: aria-label='Functions' }
#### void SetRockBottomShotSpeed ( float ShotSpeed ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomTearRange () {: aria-label='Functions' }
#### void SetRockBottomTearRange ( float TearRange ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetShotSpeedModifier () {: aria-label='Functions' }
#### void SetShotSpeedModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

Adds `0.2 * modifier` to the player's ShotSpeed.

Experimental Treatment adds `-1`, `0` or `1` depending on the shot speed rolled. Void may randomly add `1`.

___

### SetSpeedModifier () {: aria-label='Functions' }
#### void SetSpeedModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

Adds `0.2 * modifier` to the player's MoveSpeed.

Experimental Treatment adds `-1`, `0` or `1` depending on the speed rolled. Void may randomly add `1`.

___

### SetSuplexAimCountdown () {: aria-label='Functions' }
#### void SetSuplexAimCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetSuplexLandPosition () {: aria-label='Functions' }
#### void SetSuplexLandPosition ( [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetSuplexState () {: aria-label='Functions' }
#### void SetSuplexState ( [SuplexState](enums/SuplexState.md) State ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetSuplexTargetPosition () {: aria-label='Functions' }
#### void SetSuplexTargetPosition ( [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetTearPoisonDamage () {: aria-label='Functions' }
#### void SetTearPoisonDamage ( float Damage ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetTearRangeModifier () {: aria-label='Functions' }
#### void SetTearRangeModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

Adds `2.5 * modifier` to the player's TearRange.

Experimental Treatment adds `-1`, `0` or `1` depending on the range rolled. Void may randomly add `1`.

___

### SetUrethraBlock () {: aria-label='Functions' }
#### void SetUrethraBlock ( boolean Blocked ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets whether the tear spam attack from the Kidney Stone collectible is about to activate. If the player does not have the Kidney Stone collectible, the effect is immediately activated.

???+ bug "Bug"
	Setting the `Blocked` argument to `false` seems to do nothing at all.

___

### SetWeapon () {: aria-label='Functions' }
#### void SetWeapon ( [Weapon](Weapon.md) Weapon, int WeaponSlot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the active Weapon in the assigned `WeaponSlot`.

???- info "Info"
    Weapon slots and their descriptions:

    - `0` - Backup Weapon such as Notched Axe and Urn of Souls.
    - `1` - Primary Weapon.
    - `2` - Additional Weapon. Few instances of this exist in the vanilla game, but it can be populated by mods.
    - `3` - Additional Weapon.
    - `4` - Additional Weapon.

    Always check for `nil`, even for slot `1` as it can be deleted by mods via [Isaac.DestroyWeapon()](Isaac.md#destroyweapon).

___

### ShootBlueCandle () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) ShootBlueCandle ( [Vector](Vector.md) Direction ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Makes the player shoot a blue flame from the Candle collectible.

___

### ShuffleCostumes () {: aria-label='Functions' }
#### void ShuffleCostumes ( int Seed = Random( ) ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Randomizes the current costumes.

___

### SpawnAquariusCreep () {: aria-label='Functions' }
#### [EntityEffect](https://wofsauge.github.io/IsaacDocs/rep/EntityEffect.html) SpawnAquariusCreep ( [TearParams](https://wofsauge.github.io/IsaacDocs/rep/TearParams.html) TearParams = self.TearParams) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Spawns a creep effect that acts like the ones created by Aquarius, including inheriting the player's `TearParams`. Supports passing a custom `TearParams` instead.

???+ info "Info"
    For reference, this is how the game calculates the `TearParams` for this normally:
	
	``player->GetTearHitParams(&params, WeaponType.WEAPON_TEARS, (*player->GetTearPoisonDamage() * 0.666f) / player->_damage, -(int)(-Isaac::Random(2) != 0) & 2 - 1, nil)``

___

### SpawnClot () {: aria-label='Functions' }
#### void SpawnClot ( [Vector](Vector.md) pos, boolean AllowPlayerDeath = false ) {: .copyable aria-label='Functions' }  [ ](#){: .rgonorplus .tooltip .badge }

Acts like a use of Sumptorium, removing health and spawning a clot with the type of health removed. If `AllowPlayerDeath` is set, a clot will spawn even if the health drained will kill the player.

___

### SpawnSaturnusTears () {: aria-label='Functions' }
#### int SpawnSaturnusTears ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Spawns a ring of tears that orbit around the player akin to the Saturnus collectible.

___

### SwapForgottenForm () {: aria-label='Functions' }
#### boolean SwapForgottenForm ( boolean Force = false, boolean NoEffects = false) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
If the player is The Forgotten/The Soul, the two will swap forms. Otherwise, this function does nothing.

`Force` will swap even if the subplayer doesn't have any health, or while a room/stage transition is active. `NoEffects` will disable the dust effect & fade from white when switching from The Soul to The Forgotten.

Returns `true` on success, otherwise `false`.

___

### SyncConsumableCounts () {: aria-label='Functions' }
#### void SyncConsumableCounts ( [EntityPlayer](EntityPlayer.md) Player, int CollectibleFlags ) {: .copyable aria-label='Functions' }       [ ](#){: .rgonorplus .tooltip .badge }

___

### Teleport () {: aria-label='Functions' }
#### void Teleport ( [Vector](Vector.md) Position, boolean DoEffects = true, boolean TeleportTwinPlayers = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Teleports the player to a position within the room. 

`DoEffects` controls whether the teleport animation and sound plays. `TeleportTwinPlayers` controls whether twin players (e.g. Esau, Tainted Lazarus w/ Birthright) are teleported alongside this one.

___

### TriggerRoomClear () {: aria-label='Functions' }
#### void TriggerRoomClear ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Triggers effects on the player as if a room was cleared (i.e. Charging actives).

___

### TryAddToBagOfCrafting () {: aria-label='Functions' }
#### boolean TryAddToBagOfCrafting ( [EntityPickup](EntityPickup.md) Pickup ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Tries to add the specified pickup to the player's Bag of Crafting. Returns true if successful.

___

### TryDecreaseGlowingHourglassUses () {: aria-label='Functions' }
#### void TryDecreaseGlowingHourglassUses ( int Uses, boolean ForceHourglass = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Attempts to decrease the uses left for the Glowing Hourglass collectible, if the player has it. `ForceHourglass` instantly removes all the charges and turns Glowing Hourglass into its regular Hourglass form.

???+ bug "Bug"
	`Uses` are only decreased by 1 regardless of how large of a number you tell it to remove.
	
___

### TryFakeDeath () {: aria-label='Functions' }
#### boolean TryFakeDeath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Spawns a copy of the player at its current position and plays the death animation and sound.

___

### TryForgottenThrow () {: aria-label='Functions' }
#### boolean TryForgottenThrow ( [Vector](Vector.md) Direction ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
If the player is holding Tainted Forgotten, he is thrown towards the specified direction.

___

### TryPreventDeath () {: aria-label='Functions' }
#### boolean TryPreventDeath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Adds a heart container to a character if there are none left to prevent death, depending on its [HealthType](enums/HealthType.md).

Returns `true` on success, otherwise `false`.

___

### TryRemoveSmeltedTrinket () {: aria-label='Functions' }
#### void TryRemoveSmeltedTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) ID ) {: .copyable aria-label='Functions' }     [ ](#){: .rgonorplus .tooltip .badge }
Tries to remove the specified smelted trinket from the player.

___

### UnblockCollectible () {: aria-label='Functions' }
#### void UnblockCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Unblocks the [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) that was blocked through [BlockCollectible](EntityPlayer.md#blockcollectible).

___

### UpdateIsaacPregnancy () {: aria-label='Functions' }
#### void UpdateIsaacPregnancy ( boolean UpdateCambion ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Set `true` if you want to update the [Cambion Conception](https://bindingofisaacrebirth.fandom.com/wiki/Cambion_Conception) costume, otherwise updates the [Immaculate Conception](https://bindingofisaacrebirth.fandom.com/wiki/Immaculate_Conception) costume.

___

### VoidHasCollectible () {: aria-label='Functions' }
#### boolean VoidHasCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if the specified collectible has been consumed by the Void collectible.

___

### AddInnateTrinket () {: aria-label='Functions' }
#### void AddInnateTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, int Amount = 1, string GroupKey = "", int Duration = -1, bool AddCostume = true ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Same as AddInnateCollectible but for trinkets. Note that golden trinkets must be added/removed separately.

___

### BlockTrinket () {: aria-label='Functions' }
#### void BlockTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket ) {: .copyable aria-label='Functions' }   [ ](#){: .rgonplus .tooltip .badge }
Blocks the provided [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html). This will make it so the game thinks you don't have the trinket, even if it's in your inventory.

___

### ClearInnateItemGroup () {: aria-label='Modified Functions' }
#### void ClearInnateItemGroup ( string GroupKey ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Remove all innate collectibles and trinkets added under the specified group.

___

### CalculateBagOfCraftingOutput () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge }
#### static [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html), [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) CalculateBagOfCraftingOutput ( [BagOfCraftingPickup](enums/BagOfCraftingPickup.md)[] pickups ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBloodGushSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetBloodGushSprite ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sprite used for things like Scissors and The Intruder.

___

### GetDonateLuck () {: aria-label='Functions' }
#### int GetDonateLuck ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetErrorTrinketEffect () {: aria-label='Functions' }
#### [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) GetErrorTrinketEffect ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the current trinket effect that would be mimicked by the "Error" trinket (`TrinketType.TRINKET_ERROR`), regardless of if the player has it.

Note that this effect is based entirely on the current room's [SpawnSeed](https://wofsauge.github.io/IsaacDocs/rep/RoomDescriptor.html#spawnseed), and can be also obtained from [RoomDescriptor](RoomDescriptor.md#geterrortrinketeffect). This player function is just provided as a convenience.

___

### GetImExcitedSpeedupCountdown () {: aria-label='Functions' }
#### int GetImExcitedSpeedupCountdown ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetInnateCollectibleCount () {: aria-label='Functions' }
#### int GetInnateCollectibleCount ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, string GroupKey = "" ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns how many innate copies of this collectible are currently in the specified group.

___

### GetInnateCollectibleGroup () {: aria-label='Functions' }
#### table GetInnateCollectibleGroup ( string GroupKey ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of the innate collectibles currently in the specified group.

The returned table has [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) as the keys and current counts as the values. If no copies of the item are in the group, it will not have an entry in the table.

___

### GetInnateTrinketCount () {: aria-label='Functions' }
#### int GetInnateTrinketCount ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, string GroupKey = "" ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns how many innate copies of this trinket are currently in the specified group.

Note that golden trinkets are counted separately.

___

### GetInnateTrinketGroup () {: aria-label='Functions' }
#### table GetInnateTrinketGroup ( string GroupKey ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of the innate trinket currently in the specified group.

The returned table has [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) as the keys and current counts as the values. If no copies of the item are in the group, it will not have an entry in the table.

Note that golden trinkets are counted separately.

___

### GetMawOfTheVoidCharge () {: aria-label='Functions' }
#### int GetMawOfTheVoidCharge ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMontezumaRevengeCharge () {: aria-label='Functions' }
#### int GetMontezumaRevengeCharge ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRUAWizardTimer () {: aria-label='Functions' }
#### int GetRUAWizardTimer ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsTrinketBlocked () {: aria-label='Functions' }
#### boolean IsTrinketBlocked ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if the [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) was blocked. Collectibles can only be blocked by use of [BlockTrinket](EntityPlayer.md#blocktrinket).

___

### RemoveInnateCollectible () {: aria-label='Functions' }
#### int RemoveInnateCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, int Amount = 1, string GroupKey = "" ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Removes innate collectibles from the specified group. Returns the actual number of innate items removed.

___

### RemoveInnateTrinket () {: aria-label='Functions' }
#### int RemoveInnateTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, int Amount = 1, string GroupKey = "" ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Removes innate trinkets from the specified group. Returns the actual number of innate items removed.

Note that golden trinkets must be added/removed separately.

___

### SetDonateLuck () {: aria-label='Functions' }
#### void SetDonateLuck ( int Value ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Does not trigger cache evaluation.

For simply incrementing this luck, consider the [DonateLuck](https://wofsauge.github.io/IsaacDocs/rep/EntityPlayer.html?h=donateluck#donateluck) function instead.

___

### SetImExcitedSpeedupCountdown () {: aria-label='Functions' }
#### void SetImExcitedSpeedupCountdown ( int Countdown ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetInnateCollectibleCount () {: aria-label='Functions' }
#### int SetInnateCollectibleCount ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, int NewCount, string GroupKey = "", boolean AddCostume = true ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Changes the current count of an innate collectible in the specified group. Triggers cache evals and callbacks appropriately if any items needed to be added or removed to reach the desired count, and returns the number of items added or removed (removals are negative). Does nothing if the count is already the desired value.

___

### SetInnateCollectibleGroup () {: aria-label='Functions' }
#### void SetInnateCollectibleGroup ( string GroupKey, table NewCounts, boolean AddCostume = true ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Updates the contents of the specified innate collectible group to match the provided table. The table must use [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) for the keys and the desired counts as the values.

Any items currently in the group but not specified in the table are removed. Triggers cache evals and callbacks appropriately if any items need to be added or removed to reach their desired count.

___

### SetInnateTrinketCount () {: aria-label='Functions' }
#### int SetInnateTrinketCount ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, int NewCount, string GroupKey = "", boolean AddCostume = true ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Changes the current count of an innate trinket in the specified group. Automatically triggers cache evals and callbacks appropriately if any items needed to be added or removed to reach the desired count, and returns the number of items added or removed (removals are negative). Does nothing if the count is already the desired value.

Note that golden trinkets are counted separately.

___

### SetInnateTrinketGroup () {: aria-label='Functions' }
#### void SetInnateTrinketGroup ( string GroupKey, table NewCounts, boolean AddCostume = true ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Updates the contents of the specified innate collectible group to match the provided table. The table must use [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) for the keys and the desired counts as the values.

Any items currently in the group but not specified in the table are removed. Triggers cache evals and callbacks appropriately if any items need to be added or removed to reach their desired count.

Note that golden trinkets are counted separately.

___

### SetMawOfTheVoidCharge () {: aria-label='Functions' }
#### void SetMawOfTheVoidCharge ( int Charge ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetMontezumaRevengeCharge () {: aria-label='Functions' }
#### void SetMontezumaRevengeCharge ( int Charge ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRUAWizardTimer () {: aria-label='Functions' }
#### void SetRUAWizardTimer ( int timer ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetTearDisplacement () {: aria-label='Functions' }
#### void SetTearDisplacement ( int Displacement ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the player's TearDisplacement value, which represents which eye the player is shooting from.

Note that the game will typically alternate this value BEFORE shooting a tear.

???+ info "TearDisplacement"
    - `1` Right eye
    - `-1` Left eye

___

### UnblockTrinket () {: aria-label='Functions' }
#### void UnblockTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Unblocks the [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) that was blocked through [BlockTrinket](EntityPlayer.md#blocktrinket).

___

</div>
