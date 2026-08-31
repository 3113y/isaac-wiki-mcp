---
tags:
  - Global
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Global Class "Minimap"

???+ info
    You can access this class through the `Minimap` global table.

    **Note that to call these functions, you must use a `.` (period) instead of a `:` (colon)!**
    
    ???+ example "Example Code"
        ```lua
        local size = Minimap.GetDisplayedSize()
        ```
        
## Functions

<div class="rgon-only" markdown="1">

### GetDisplayedSize () {: aria-label='Functions' }
#### [Vector](Vector.md) GetDisplayedSize ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the minimap's current display size. When the minimap is not expanded, this is always `Vector(47,47)`.

___

### GetHoldTime () {: aria-label='Functions' }
#### int GetHoldTime ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetIconsSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetIconsSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetItemIconsSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetItemIconsSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetShakeDuration () {: aria-label='Functions' }
#### int GetShakeDuration ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetShakeOffset () {: aria-label='Functions' }
#### [Vector](Vector.md) GetShakeOffset ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetState () {: aria-label='Functions' }
#### [MinimapState](./enums/MinimapState.md) GetState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### Refresh () {: aria-label='Functions' }
#### void Refresh ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetHoldTime () {: aria-label='Functions' }
#### void SetHoldTime ( int Time ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetShakeDuration () {: aria-label='Functions' }
#### void SetShakeDuration ( int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetShakeOffset () {: aria-label='Functions' }
#### void SetShakeOffset ( [Vector](Vector.md) Offset ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetState () {: aria-label='Functions' }
#### void SetState ( [MinimapState](./enums/MinimapState.md) State ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
