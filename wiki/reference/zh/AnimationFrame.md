---
tags:
  - Class
---
# Class "AnimationFrame"

来自 ANM2 文件的动画某一层单个帧的缓存数据。由所有使用相同 ANM2 的精灵共享，且不可修改。

请注意，插值和根动画已预先计算并包含在这些值中。

此外，这些值与 ANM2 编辑器中显示的值相对应，命名方式也相同。

可通过 [AnimationLayer:GetFrame()](AnimationLayer.md#getframe) 获取.

## Functions

<div class="rgon-only" markdown="1">

### GetColor () {: aria-label='Functions' }
#### [const Color](Color.md) GetColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCrop () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetCrop ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetEndFrame () {: aria-label='Functions' }
#### int GetEndFrame ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
也就是说，本动画帧（AnimationFrame）从此帧开始将不再显示。
请注意，“结束帧”是下一动画帧（AnimationFrame）的起始帧。

### GetHeight () {: aria-label='Functions' }
#### float GetHeight ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPivot () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetPivot ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPos () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetPos ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRotation () {: aria-label='Functions' }
#### float GetRotation ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetScale () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetScale ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetStartFrame () {: aria-label='Functions' }
#### int GetStartFrame ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetWidth () {: aria-label='Functions' }
#### float GetWidth ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsInterpolated () {: aria-label='Functions' }
#### boolean IsInterpolated ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsVisible () {: aria-label='Functions' }
#### boolean IsVisible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

</div>
