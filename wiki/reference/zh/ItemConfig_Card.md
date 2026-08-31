---
tags:
  - Class
---
# Class "ItemConfigCard"

???+ info
    You can get this class by using the following function:

    * [ItemConfig.GetCard()](ItemConfig.md#getcard)

    ???+ example "Example Code"
        `Isaac.GetItemConfig():GetCard(Card.CARD_FOOL)`

## Functions
___

### Is·Available () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean IsAvailable ( ) {: .copyable aria-label='Functions' }

___

### Is·Card () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean IsCard ( ) {: .copyable aria-label='Functions' }

___

### Is·Rune () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean IsRune ( ) {: .copyable aria-label='Functions' }

___
## Variables

### Achievement·ID {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int AchievementID  {: .copyable aria-label='Variables' }
Returns the ID of the achievement that unlocks the card. Returns ``:::lua -1`` if the card is unlocked by default.

___

### Announcer·Delay {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int AnnouncerDelay  {: .copyable aria-label='Variables' }

___

### Announcer·Voice {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int AnnouncerVoice  {: .copyable aria-label='Variables' }

___

### Card·Type {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int CardType {: .copyable aria-label='Variables' }

___

### Description {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### string Description  {: .copyable aria-label='Variables' }

Returns the description of the card.

???- warning "Warning"
    In Repentance, this function now returns ``#[CARD_NAME]_DESCRIPTION``
___

### Greed·Mode·Allowed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean GreedModeAllowed  {: .copyable aria-label='Variables' }

Returns whether or not the item can appear in Greed or Greedier mode.
___

### Hud·Anim {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### string HudAnim  {: .copyable aria-label='Variables' }

Returns the name of the animation in `ui_cardfronts.anm2`.

???- bug "Bugs"
    This will return a blank string unless used on a modded card. Standard cards will return nothing.
___

### ID {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ID  {: .copyable aria-label='Variables' }

Returns the ID of the given card.
___

### Mimic·Charge {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int MimicCharge {: .copyable aria-label='Variables' }

___

### Name {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### string Name  {: .copyable aria-label='Variables' }

Returns the name of the given card.
???- warning "Warning"
    In Repentance, this function now returns ``#[CARD_NAME]_NAME``

___

### Pickup·Subtype {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int PickupSubtype {: .copyable aria-label='Variables' }

___

<div class="rgon-only" markdown="1">

### SetAvailabilityCondition

#### void SetAvailabilityCondition ( function AvailabilityCondition ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }

Sets an additional function that runs when [IsAvailable()](https://wofsauge.github.io/IsaacDocs/rep/ItemConfig_Card.html#isavailable) is called, internally or through the Lua API.

The function must return a boolean that determines whether or not the card is available.

This function is only checked after the GreedModeAllowed, Achievement, and Hidden checks have all passed, so it cannot be used to override those checks.

???+ warning "Function Errors"
    If the function errors at any point while it is being executed, it is treated as though `true` was returned.

    If this is not the intended behavior, wrap your actual function in a `pcall` or `xpcall` and return `false` if the call fails.


    ```lua
    local function AvailabilityCondition()
        -- Your code here
    end


    local function AvailabilityWrapper()
        -- Call function with pcall to catch errors
        local success, result = pcall(AvailabilityCondition)

        if success then
            return result  -- Return result if no error
        else
            local errorMessage = 'Error whilst checking Availability of card "Your Card": ' .. result
            Console.PrintError(errorMessage) -- Print the error message
            Isaac.DebugString(errorMessage) -- Log the error message
            return false
        end
    end

    Isaac.GetItemConfig():GetCard(YourCardId):SetAvailabilityCondition(AvailabilityWrapper)
    ```
___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

### ClearAvailabilityCondition

#### void ClearAvailabilityCondition ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }

Sets the availability condition to `nil`, which is useful when the condition is no longer needed and can improve performance.
___

### GetAvailabilityCondition

#### function GetAvailabilityCondition ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }

Returns `nil` if no AvailabilityCondition is set or if it has been cleared.
___

## Variables

### Hidden {: aria-label='Variables' }

#### const boolean Hidden [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### InitialWeight {: aria-label='Variables' }

#### const float InitialWeight [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### ModdedCardFront {: aria-label='Variables' }

#### [Sprite](Sprite.md) ModdedCardFront [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### Weight {: aria-label='Variables' }

#### float Weight [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

Can be set to a value to increase or decrease the chance of this card being randomly picked
___

</div>
