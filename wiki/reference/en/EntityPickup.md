---
tags:
  - Class
---
# Class "EntityPickup"

???+ info
    You can get this class by using the following function:

    * [Entity.ToPickup()](Entity.md#topickup)

    ???+ example "Example Code"
        `local entity = Isaac.GetRoomEntities()[1]:ToPickup()`

## Class Diagram
--8<-- "en/snippets/EntityClassDiagram.md"
## Functions

### Appear·Fast () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AppearFast ( ) {: .copyable aria-label='Functions' }

___

### Can·Reroll () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanReroll ( ) {: .copyable aria-label='Functions' }

___

<div class="rgon-extension" markdown="1">

### CanReroll () {: aria-label='Functions' }
#### boolean CanReroll ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>

### Get·Coin·Value () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetCoinValue ( ) {: .copyable aria-label='Functions' }
If this is a coin, return its face value, else zero.
___

### Is·Shop·Item () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsShopItem ( ) {: .copyable aria-label='Functions' }

___

### Morph () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void Morph ( [EntityType](enums/EntityType.md) Type, int Variant, int SubType, boolean KeepPrice = false, boolean KeepSeed = false, boolean IgnoreModifiers = false ) {: .copyable aria-label='Functions' }
**KeepSeed**: If set to true, keeps the initial RNG seed of the pickup instead of rerolling it

**IgnoreModifiers**: If set to true, ignores item effects that might turn this pickup into something other than the specificed variant and sub-type. Specifically, this can be used to prevent a collectible from being affected by Tainted Isaac's rotation mechanic. (For example, if you manually spawn a quest collectible such as a Polaroid, it will be affected by Tainted Isaac's rotation mechanic, which is normally undesired. To fix this, you can immediately morph it into the same entity type / variant /sub-type after spawning with this argument set to true.)
___

### Play·Drop·Sound () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PlayDropSound ( ) {: .copyable aria-label='Functions' }

___

### Play·Pickup·Sound () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PlayPickupSound ( ) {: .copyable aria-label='Functions' }

___

### Try·Open·Chest () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean TryOpenChest ( [EntityPlayer](EntityPlayer.md) Player = nil ) {: .copyable aria-label='Functions' }
**Player**: The player that opened this chest
___
## Variables

### Auto·Update·Price {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean AutoUpdatePrice  {: .copyable aria-label='Variables' }

___

### Charge {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Charge  {: .copyable aria-label='Variables' }

___

### OptionsPickupIndex {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int OptionsPickupIndex  {: .copyable aria-label='Variables' }
Any non-zero value causes the item to form an option group with any other item with the same OptionsPickupIndex value.

When an item belonging to an option group is picked up, all other items belonging to the same group disappear.

0 is the default value and means the item doesn't belong to any group.
___

### Price {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Price  {: .copyable aria-label='Variables' }
Price of the pickup in shops.

???- info "Tainted Keeper Info"
    On Tainted Keeper, all items are supposed to have a price. But any items spawned with Lua does not comply with this rule, so you have to manually set a price. On the next frame after assigning a price (for example `1`), it will snap to the correct price it would have for Tainted Keeper (e.g. 15). This is because of the AutoUpdatePrice feature.

    This method works most of the time. However, it breaks in special rooms (e.g. Angel Rooms) such that sometimes, the price will snap to wrong values, such as 24, 99, and so on. The fix for this, set ShopItemId to an arbitrary negative value (e.g. -1).

___

### Shop·Item·Id {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ShopItemId  {: .copyable aria-label='Variables' }

If in a shop, this value describes which slot the item is for sale in. For example, if the shop has 6 things for sale, the pickups in the room will have shop item IDs of 0, 1, 2, 3, 4, and 5.

When spawning a new collectible item, the ShopItemId will be 0 by default. This has a side effect of making the D6 roll the collectible into a red heart. By setting shop item id to -1, it will fix this behavior such that the collectible will properly roll into another collectible. However, non-collectible pickups may reroll into collectibles through a D20 or similar.

By setting shop item id to -2, automatic prices will be devil deal prices. Otherwise this is identical to -1.

Other negative values act identically to -1.

___

### State {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int State  {: .copyable aria-label='Variables' }

___

### Timeout {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Timeout  {: .copyable aria-label='Variables' }

Causes the pickup to blink and then disappear after a certain amount of time like the temporary health dropped from tainted maggy. The value decreases by 1 every game frame and after hitting 0 the pickup disappears. If the Timeout is set to -1(the default value for normal pickups) the pickup will act normally and not disappear.

___

### Touched {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean Touched  {: .copyable aria-label='Variables' }

Used to identify whether a collectible has been raised once, affecting Transformation Progress.

Since using Morph() alone does not initialize Touched, you must manually set Touched if you want to advance the transformation progress after rerolling a collectible and then acquiring it.

???+ example "Example Code"
    ```lua
        pickup:Morph(EntityType.ENTITY_PICKUP, PickupVariant.PICKUP_COLLECTIBLE, newItemId, true)
        pickup.Touched = false
    ```

___

### Wait {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Wait  {: .copyable aria-label='Variables' }

Used with collectibles to enforce a period of time where the player will not automatically pick up the collectible. New collectibles spawn with a `Wait` value of 20 (which corresponds to 20 game frames). The value will automatically decrement as game frames pass.

It is unknown whether or not this value is used for pickups other than collectibles.

___

<div class="rgon-only" markdown="1">

### AddCollectibleCycle () {: aria-label='Functions' }
#### boolean AddCollectibleCycle ( int id ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetAlternatePedestal () {: aria-label='Functions' }
#### int GetAlternatePedestal ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollectibleCycle () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)[] GetCollectibleCycle ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table containing all [CollectibleTypes](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) used in its collectible cycle (for example, Glitched Crown).

___

### GetDropDelay () {: aria-label='Functions' }
#### int GetDropDelay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetFlipCollectible () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetFlipCollectible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) if a Flip save state exists; otherwise, returns `nil`.

___

### GetLootList () {: aria-label='Functions' }
#### [LootList](LootList.md) GetLootList ( boolean shouldAdvance = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a **read-only** version of the pickup's [LootList](LootList.md). Loot inside pickups can be seen through use of the Guppy's Eye collectible.

`shouldAdvance` determines whether the loot RNG advances.
___

### GetMegaChestLeftCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md) GetMegaChestLeftCollectible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
If called on an EntityPickup on the right side of an open Mega Chest, returns the collectible on the left. Otherwise, returns `nil`.

___

### GetMegaChestOtherCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md), boolean GetMegaChestRightCollectible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
If called on an EntityPickup belonging to an open Mega Chest, returns the other collectible and a boolean indicating whether the current collectible is on the right. Otherwise, returns `nil`.

___

### GetMegaChestRightCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md) GetMegaChestRightCollectible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
If called on an EntityPickup on the left side of an open Mega Chest, returns the collectible on the right. Otherwise, returns `nil`.

___

### GetPickupGhost () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) GetPickupGhost ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the `EffectVariant.PICKUP_GHOST` EntityEffect visible through Guppy's Eye. If not visible, returns `nil`.

___

### GetPriceSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetPriceSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRandomPickupVelocity () {: aria-label='Functions' }
#### [Vector](Vector.md) GetRandomPickupVelocity ( [Vector](Vector.md) Position, [RNG](RNG.md) RNG = nil, int VelocityType = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
`VelocityType` 0 will shoot pickups in a random direction around the wanted position.
`VelocityType` 1 will shoot pickups in a cone pointing down, mostly used for Beggar payouts.
`VelocityType` also seems to affect pickups in Challenge Rooms, causing them to have a weaker velocity.

???+ warning "Warning"
    This is a static function and must be called via `EntityPickup.GetRandomPickupVelocity(Position, RNG, VelocityType)`.

___

### GetVarData () {: aria-label='Functions' }
#### int GetVarData ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### HasFlipData () {: aria-label='Functions' }
#### boolean HasFlipData ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if pickup is collectible and has Flip save state.

___

### InitFlipState () {: aria-label='Functions' }
#### void InitFlipState ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) = CollectibleType.COLLECTIBLE_NULL, boolean SetupCollectibleGraphics = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Initiates the flip state for the pickup with the provided [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html).

___

### IsBlind () {: aria-label='Functions' }
#### boolean IsBlind ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if the pickup is a collectible pedestal and is hidden. Always returns `false` for non-collectible EntityPickups.

???+ warning "Warning"
    This value does not account for curse of the blind, it only reflects the blind state of pickups that are normally blind without curses involved. Ex: alt path's extra item.
___

### MakeShopItem () {: aria-label='Functions' }
#### void MakeShopItem ( int ShopItemID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ReloadGraphics () {: aria-label='Functions' }
#### void ReloadGraphics ( boolean IgnoreBlind ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### RemoveCollectibleCycle () {: aria-label='Functions' }
#### void RemoveCollectibleCycle ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetAlternatePedestal () {: aria-label='Functions' }
#### void SetAlternatePedestal ( int PedestalType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the graphics of the item pedestal. Does nothing for non-collectible EntityPickups.

___

### SetDropDelay () {: aria-label='Functions' }
#### void SetDropDelay ( int Delay ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetForceBlind () {: aria-label='Functions' }
#### void SetForceBlind ( boolean SetBlind ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Hides pedestal items similar to Curse of the Blind. Does nothing for non-collectible EntityPickups.

___

### SetNewOptionsPickupIndex () {: aria-label='Functions' }
#### int SetNewOptionsPickupIndex ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the new pickup index.
___

### SetupCollectibleGraphics () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge }
#### static void SetupCollectibleGraphics ( [Sprite](Sprite.md) Sprite, integer Layer, [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean Blind = false, integer Seed = Random(), boolean LoadGraphics = false  ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Static method. Replaces the specified layer's spritesheet on the sprite object with the collectible sprite. Seed is used to choose a random collectible in the April Fools challenge.

___

### SetVarData () {: aria-label='Functions' }
#### void SetVarData ( int VarData ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### TriggerTheresOptionsPickup () {: aria-label='Functions' }
#### void TriggerTheresOptionsPickup ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Removes pickups with the same option group (OptionsPickupIndex) as the target pickup.

___

### TryFlip () {: aria-label='Functions' }
#### boolean TryFlip ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Will try to flip the collectible, such as when using the Flip item on a collectible pedestal with a second, holographic collectible present behind the first one. Returns `true` if successful, `false` otherwise or if used on non-collectible EntityPickups.

___

### TryInitOptionCycle () {: aria-label='Functions' }
#### boolean TryInitOptionCycle ( int NumCycle ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Causes the collectible pedestal to start cycling through the specified amount of collectibles, including its own collectible type.

___

### TryRemoveCollectible () {: aria-label='Functions' }
#### boolean TryRemoveCollectible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Attempts to remove the collectible from an item pedestal.

Returns `true` if a collectible was successfully removed from the pedestal. Returns `false` if the pedestal was already empty, or if called on a non-collectible EntityPickup.

___

### UpdatePickupGhosts () {: aria-label='Functions' }
#### void UpdatePickupGhosts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Updates the `EffectVariant.PICKUP_GHOST` EntityEffect according to the pickup's current [LootList](LootList.md).

___

</div>
