---
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
tags:
  - Global
  - Class
---
# Global Class "CharacterMenu"

???+ info
    你可以通过全局表 `CharacterMenu` 获取此类。

    **注意：调用这些函数时，必须使用 .（句点）而非 :（冒号）！**
    
    ???+ example "Example Code"
        ```lua
        local sprite = CharacterMenu.GetBGSprite()
        ```

## Functions

<div class="rgon-only" markdown="1">

### GetActiveStatus () {: aria-label='Functions' }
#### [CharacterMenuStatus](../enums/CharacterMenuStatus.md) GetActiveStatus ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBigCharPageSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetBigCharPageSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBGSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetBGSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCharacterPortraitSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetCharacterPortraitSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCharacterWheelDepth () {: aria-label='Functions' }
#### float GetCharacterWheelDepth ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the depth of the character selection wheel object.

___

### GetCharacterWheelWidth () {: aria-label='Functions' }
#### float GetCharacterWheelWidth ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the width of the character selection wheel object.

___

### GetDifficulty () {: aria-label='Functions' }
#### int GetDifficulty ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDifficultyPageSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetDifficultyPageSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDifficultyOverlaySprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetDifficultyOverlaySprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
The blood stain when selecting Hard mode / Greedier.

___

### GetEasterEggPageSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetEasterEggPageSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetIsCharacterUnlocked () {: aria-label='Functions' }
#### boolean GetIsCharacterUnlocked ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetGreedDecoSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetGreedDecoSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Displayed when greedmode is selected.

___

### GetNumCharacters () {: aria-label='Functions' }
#### int GetNumCharacters ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Number of characters in the wheel. 

___

### GetPageSwapWidgetSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetPageSwapWidgetSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPlayerTypeFromCharacterMenuID () {: aria-label='Functions' }
#### [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) GetPlayerTypeFromCharacterMenuID ( int CharacterMenuID, boolean Tainted ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
`Tainted` boolean defaults to current menu if unspecified.

___

### GetScrollSpeed () {: aria-label='Functions' }
#### float GetScrollSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the speed of the animation playing when rotating the character selection wheel.

___

### GetSeedEntrySprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetSeedEntrySprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSeedPageSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetSeedPageSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSeedUnlockPageSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetSeedUnlockPageSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSelectedCharacterMenu () {: aria-label='Functions' }
#### int GetSelectedCharacterMenu ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
`0` for Normal, `1` for Tainted.

___

### GetSelectedCharacterID () {: aria-label='Functions' }
#### int GetSelectedCharacterID ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetTaintedBGDecoSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetTaintedBGDecoSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetWinStreakPageSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetWinStreakPageSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetActiveStatus () {: aria-label='Functions' }
#### void SetActiveStatus ( [CharacterMenuStatus](../enums/CharacterMenuStatus.md) Status ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetCharacterWheelDepth () {: aria-label='Functions' }
#### void SetCharacterWheelDepth ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Set the depth of the character selection wheel object.

___

### SetCharacterWheelWidth () {: aria-label='Functions' }
#### void SetCharacterWheelWidth ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Set the width of the character selection wheel object.

___

### SetDifficulty () {: aria-label='Functions' }
#### void SetDifficulty ( [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) Difficulty ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetIsCharacterUnlocked () {: aria-label='Functions' }
#### void SetIsCharacterUnlocked ( boolean IsUnlocked ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetScrollSpeed () {: aria-label='Functions' }
#### void SetScrollSpeed ( float Speed ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Set the speed of the animation playing when rotating the character selection wheel.

___

### SetSelectedCharacterMenu () {: aria-label='Functions' }
#### void SetSelectedCharacterMenu ( int Menu ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
`0` for Normal, `1` for Tainted.

___

### SetSelectedCharacterID () {: aria-label='Functions' }
#### void SetSelectedCharacterID ( int CharacterID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCharacterMenuIDFromPlayerType () {: aria-label='Functions' }
#### int GetCharacterMenuIDFromPlayerType ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCompletionMarksSprite () {: aria-label='Functions' }
#### [Sprite](../Sprite.md) GetCompletionMarksSprite ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSelectedCharacterPlayerType () {: aria-label='Functions' }
#### [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) GetSelectedCharacterPlayerType ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the PlayerType for the character currently selected in the menu.

___

</div>
