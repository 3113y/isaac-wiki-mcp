---
tags:
  - Global
  - Class
---
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。
# Global Class "Minimap"

???+ info
    可以通过 `Minimap` 全局表获取此类。

    **注意：调用这些函数时，必须使用 .（句点）而非 :（冒号）！**
    
    ???+ example "Example Code"
        ```lua
        local size = Minimap.GetDisplayedSize()
        ```
        
## Functions

<div class="rgon-only" markdown="1">

### GetDisplayedSize () {: aria-label='Functions' }
#### [Vector](Vector.md) GetDisplayedSize ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回小地图当前的显示尺寸。小地图未展开时，尺寸始终为 `Vector(47,47)`。

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
