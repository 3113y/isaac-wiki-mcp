---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "PlayerHUD"

???+ info
    You can obtain this class using the following function:

    * [HUD.GetPlayerHUD()](HUD.md#getplayerhud)

    ???+ example "Example Code"
        ```lua
        local playerHud = Game():GetHUD():GetPlayerHUD(0)
        ```

## Functions

<div class="rgon-only" markdown="1">

### GetHeartByIndex () {: aria-label='Functions' }
#### [PlayerHUDHeart](PlayerHUDHeart.md) GetHeartByIndex ( int Index ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetHearts () {: aria-label='Functions' }
#### [PlayerHUDHeart](PlayerHUDHeart.md)[] GetHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table containing [PlayerHUDHeart](PlayerHUDHeart.md) objects.

___

### GetHUD () {: aria-label='Functions' }
#### [HUD](HUD.md) GetHUD ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetIndex () {: aria-label='Functions' }
#### int GetIndex ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetLayout () {: aria-label='Functions' }
#### [PlayerHUDLayout](enums/PlayerHUDLayout.md) GetLayout ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPlayer () {: aria-label='Functions' }
#### [EntityPlayer](EntityPlayer.md) GetPlayer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### RenderActiveItem () {: aria-label='Functions' }
#### void RenderActiveItem ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot, [Vector](Vector.md) Position, float Alpha = 1.0, float Scale = 1.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
