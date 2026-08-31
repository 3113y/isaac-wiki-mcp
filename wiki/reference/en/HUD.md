---
tags:
  - Class
---
# Class "HUD"

???+ info
    You can get this class by using the following function:

    * [Game.GetHUD()](Game.md#gethud)

    ???+ example "Example Code"
        `Game():GetHUD()`

## Functions

### Assign·Player·HUDs () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AssignPlayerHUDs ( ) {: .copyable aria-label='Functions' }
Refreshes the HUD (e.g. Characters that have Parent specified no longer show their health in the main HUD).
___

### Flash·Charge·Bar () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void FlashChargeBar ( [EntityPlayer](EntityPlayer.md) Player, [ActiveSlot](enums/ActiveSlot.md) ActiveSlot ) {: .copyable aria-label='Functions' }
Causes the charge bar of the active item in the specified slot to blink as if it had gained charges

___

### Invalidate·Active·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void InvalidateActiveItem ( [EntityPlayer](EntityPlayer.md) Player, [ActiveSlot](enums/ActiveSlot.md) ActiveSlot ) {: .copyable aria-label='Functions' }
Forces the specified active item slot to update, this might be useful for functions that modify an active item slot without directly giving or removing items

___

### Invalidate·Crafting·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void InvalidateCraftingItem ( [EntityPlayer](EntityPlayer.md) Player ) {: .copyable aria-label='Functions' }
Forces the crafting output from Bag of Crafting to update (this might become useful in the future)

___

### Is·Visible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean IsVisible ( ) {: .copyable aria-label='Functions' }
Returns false if HUD is invisible and true otherwise.
___

### Post·Update () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void PostUpdate ( ) {: .copyable aria-label='Functions' }
___

### Render () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void Render ( ) {: .copyable aria-label='Functions' }
___

### Set·Visible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetVisible ( boolean Visible = false ) {: .copyable aria-label='Functions' }
Turns the HUD on or off.
___

### Show·Fortune·Text () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void ShowFortuneText ( string MainString, string SecondaryString, ... ) {: .copyable aria-label='Functions' }
Allows to display fortune streak with text. Accepts unlimited amount of arguments.
___

### Show·Item·Text () {: aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void ShowItemText ( [EntityPlayer](EntityPlayer.md) Player, [ItemConfigItem](ItemConfig_Item.md) Item, boolean StackUpText ) {: .copyable aria-label='Functions' }

Displays "streak text". You can use this to simulate the player picking up an item without them actually picking anything up.

This method is overloaded, meaning that you can use two different sets of parameters, depending on your needs. (See the previous section.)

For example:

```lua
local function showSadOnionText()
  local game = Game()
  local hud = game:GetHUD()
  local itemConfig = Isaac.GetItemConfig()

  local player = Isaac.GetPlayer()
  local itemConfigItem = itemConfig:GetCollectible(CollectibleType.COLLECTIBLE_SAD_ONION)
  hud:ShowItemText(player, itemConfigItem)
end
```

___

### Update () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void Update ( ) {: .copyable aria-label='Functions' }

<div class="rgon-only" markdown="1">

### FlashRedHearts () {: aria-label='Functions' }
#### void FlashRedHearts ( [EntityPlayer](EntityPlayer.md) Player ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBossHPBarFill () {: aria-label='Functions' }
#### float GetBossHPBarFill ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets the fill amount of the boss HP bar.
___

### GetCardsPillsSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetCardsPillsSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sprite object used to render pills, cards, and runes in the HUD.
___

### GetChargeBarSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetChargeBarSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCoopMenuSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetCoopMenuSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sprite object used to render the co-op player selection menu.
___

### GetCraftingSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetCraftingSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sprite object used for the Bag of Crafting HUD.
___

### GetFortuneSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetFortuneSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sprite object used for the Fortune popup window.
___

### GetHeartsSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetHeartsSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetInventorySprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetInventorySprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sprite object used for Tainted Isaac inventory system.
___

### GetPickupsHUDSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetPickupsHUDSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPlayerHUD () {: aria-label='Functions' }
#### [PlayerHUD](PlayerHUD.md) GetPlayerHUD ( int Index = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPlayerStreakSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetPlayerStreakSprite ( int Index = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
A set of 4 Sprite objects used for the "mini" Repentance+ item text streaks displayed near the players' individual HUDs. Valid indexes are 0~3.

Used in place of the sprites provided by [GetStackedStreakSprite](HUD.md#getstackedstreaksprite) during co-op.

___

### GetPoopSpellSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetPoopSpellSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sprite object for Tainted Blue Baby's poop spell.

___

### GetStackedStreakSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetStackedStreakSprite ( int Index = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Provides access to the Sprite objects used for the new "stacked" Repentance+ item text streaks. Valid indexes are 0~5.

During co-op, the Sprites provided by [GetPlayerStreakSprite](HUD.md#getplayerstreaksprite) are used instead.

___

### GetStreakSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetStreakSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sprite object used for text streak popups. As of Repentance+, this seems to be used only for the floor name popup, as item-related popups use the Sprites from either [GetStackedStreakSprite](HUD.md#getstackedstreaksprite) or [GetPlayerStreakSprite](HUD.md#getplayerstreaksprite).

___

### SetBossHPBarFill () {: aria-label='Functions' }
#### void SetBossHPBarFill ( float percent ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the fill amount of the boss HP bar. Accepts values between 0 and 1. Numbers below 0 cause the boss HP bar not to be rendered.
___

### GetHistoryHUD () {: aria-label='Functions' }
#### [HistoryHUD](HistoryHUD.md) GetHistoryHUD ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
