---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "EntityConfigPlayer"

???+ info
    You can obtain this class with the following functions:

    * [EntityConfig.GetPlayer()](EntityConfig.md#getplayer)

    ???+ example "Example Code"
        ```lua
        local cainConfig = EntityConfig.GetPlayer(PlayerType.PLAYER_CAIN)
        ```
        
## Functions

<div class="rgon-only" markdown="1">

### CanShoot () {: aria-label='Functions' }
#### boolean CanShoot ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetAchievementID () {: aria-label='Functions' }
#### [Achievement](enums/Achievement.md) GetAchievementID ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns -1 if the character is not locked behind a vanilla achievement, or -2 for a "hidden" vanilla character.

___

### GetBirthrightDescription () {: aria-label='Functions' }
#### string GetBirthrightDescription ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBlackHearts () {: aria-label='Functions' }
#### int GetBlackHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBombs () {: aria-label='Functions' }
#### int GetBombs ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBrokenHearts () {: aria-label='Functions' }
#### int GetBrokenHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCard () {: aria-label='Functions' }
#### [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) GetCard ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns 0 if the character does not start with a vanilla card.

Does not include starting cards obtained through unlocks or cards added by mods.

___

### GetCoins () {: aria-label='Functions' }
#### int GetCoins ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollectibles () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)[] GetCollectibles ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table containing the [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) values for the character's starting items.

___

### GetCostumeID () {: aria-label='Functions' }
#### int GetCostumeID ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns -1 if the character has no XML-defined starting costume (such as Maggy's hair).

___

### GetCostumeSuffix () {: aria-label='Functions' }
#### string GetCostumeSuffix ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Directory suffix for character-specific costume sprites.

___

### GetExtraPortraitPath () {: aria-label='Functions' }
#### string GetExtraPortraitPath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Path to the `.anm2` file displayed over the character's level-transition and boss VS-screen portrait.

___

### GetKeys () {: aria-label='Functions' }
#### int GetKeys ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetModdedControlsSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedControlsSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the Sprite used for a modded character's starting room controls.

Note that this Sprite is shared by other characters from the same mod - there is an animation with the same name as this character.

Returns nil for vanilla characters, or characters with no corresponding animation.

___

### GetModdedCoopMenuSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedCoopMenuSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the Sprite used for a modded character's icon in the co-op character select wheel.

Note that this Sprite is shared by other characters from the same mod - there is an animation with the same name as this character.

Returns nil for vanilla characters, or characters with no corresponding animation.

___

### GetModdedGameOverSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedGameOverSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the Sprite used for a modded character's game over screen (ie, their name).

Note that this Sprite is shared by other characters from the same mod - there is an animation with the same name as this character.

Returns nil for vanilla characters, or characters with no corresponding animation.

___

### GetModdedMenuBackgroundSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedMenuBackgroundSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the Sprite used for a modded character's character select screen.

Note that this Sprite is shared by other characters from the same mod - there is an animation with the same name as this character.

Returns nil for vanilla characters, or characters with no corresponding animation.

___

### GetModdedMenuPortraitSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedMenuPortraitSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the Sprite used for a modded character's character select portrait.

Note that this Sprite is shared by other characters from the same mod - there is an animation with the same name as this character.

Returns nil for vanilla characters, or characters with no corresponding animation.

___

### GetName () {: aria-label='Functions' }
#### string GetName ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetNameImagePath () {: aria-label='Functions' }
#### string GetNameImagePath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Path to the PNG file used for the character's name on the boss VS screen.

___

### GetPill () {: aria-label='Functions' }
#### [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) GetPill ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Does not include starting pills obtained via unlocks.

___

### GetPlayerType () {: aria-label='Functions' }
#### int GetPlayerType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPocketActive () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetPocketActive ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Does not include items added by mods.

___

### GetPortraitPath () {: aria-label='Functions' }
#### string GetPortraitPath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Path to the PNG file used for the character's main level transition and boss VS screen portrait.

___

### GetRedHearts () {: aria-label='Functions' }
#### int GetRedHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSkinColor () {: aria-label='Functions' }
#### [SkinColor](https://wofsauge.github.io/IsaacDocs/rep/enums/SkinColor.html) GetSkinColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSkinPath () {: aria-label='Functions' }
#### string GetSkinPath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Path to the PNG file used for the character's main sprite sheet.

___

### GetSoulHearts () {: aria-label='Functions' }
#### int GetSoulHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetTaintedCounterpart () {: aria-label='Functions' }
#### [EntityConfigPlayer](EntityConfigPlayer.md) GetTaintedCounterpart ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
For non-tainted characters, returns their tainted counterpart, or returns nil if there is none.

For tainted characters, returns their non-tainted counterpart.

___

### GetTrinket () {: aria-label='Functions' }
#### [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) GetTrinket ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Does not include starting trinkets obtained via unlocks.

Does not include trinkets added by mods.

___

### IsHidden () {: aria-label='Functions' }
#### boolean IsHidden ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if the character is not visible/selectable from the character select screen.

Does not include characters that are hidden only until unlocked.

___

### IsTainted () {: aria-label='Functions' }
#### boolean IsTainted ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
