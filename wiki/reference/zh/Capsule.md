---
tags:
  - Class
---
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

# Class "Capsule"

[这里](./examples/Capsules.md)可以找到一个使用 Capsule 类的示例模组。

???+ info

    你可以通过以下函数获取此类：
    * [Entity:GetCollisionCapsule()](Entity.md#getcollisioncapsule)
    * [Entity:GetNullCapsule()](Entity.md#getnullcapsule)
        
## Constructors

<div class="rgon-only" markdown="1">

### Capsule () {: aria-label='Constructors' }
#### [Capsule](Capsule.md) Capsule ( [Vector](Vector.md) Position, [Vector](Vector.md) SizeMult, float Rotation, float Size ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constructors' }
## Functions

### Collide () {: aria-label='Functions' }
#### boolean Collide ( [Capsule](Capsule.md) Capsule, [Vector](Vector.md) Point ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDirection () {: aria-label='Functions' }
#### [Vector](Vector.md) GetDirection ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetF1 () {: aria-label='Functions' }
#### float GetF1 ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回胶囊体的大小（与构造函数中的 `size` 一致）。

### GetF2 () {: aria-label='Functions' }
#### float GetF2 ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetPosition ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetVec2 () {: aria-label='Functions' }
#### [Vector](Vector.md) GetVec2 ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回胶囊体的起始位置（可以通过 `position` 设置）。

### GetVec3 () {: aria-label='Functions' }
#### [Vector](Vector.md) GetVec3 ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回胶囊体的结束位置（可以通过 `targetposition` 设置）。

</div>
