---
tags:
  - Class
---
# Class "EntityBomb"

???+ info
    你可以通过以下函数获取此类：

    * [Entity.ToBomb()](Entity.md#tobomb)
    * [EntityPlayer.FireBomb()](EntityPlayer.md#firebomb)

    ???+ example "Example Code"
        `local entity = Isaac.GetPlayer():FireBomb(Vector(0,0), Vector(1,1))`

## Class Diagram
--8<-- "zh/snippets/EntityClassDiagram.md"

## Functions

### Add·Tear·Flags () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddTearFlags ( [TearFlags](enums/TearFlags.md) Flags ) {: .copyable aria-label='Functions' }

___

### Clear·Tear·Flags () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void ClearTearFlags ( [TearFlags](enums/TearFlags.md) Flags ) {: .copyable aria-label='Functions' }

___

### Has·Tear·Flags () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasTearFlags ( [TearFlags](enums/TearFlags.md) Flags ) {: .copyable aria-label='Functions' }

___

### Set·Explosion·Countdown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetExplosionCountdown ( int Countdown ) {: .copyable aria-label='Functions' }

___
## Variables

### Explosion·Damage {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float ExplosionDamage  {: .copyable aria-label='Variables' }

___

### Flags {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [TearFlags](enums/TearFlags.md) Flags  {: .copyable aria-label='Variables' }

使用[TearFlags](enums/TearFlags.md)来改变炸弹的行为。
___

### Is·Fetus {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsFetus  {: .copyable aria-label='Variables' }

___

### Radius·Multiplier {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float RadiusMultiplier  {: .copyable aria-label='Variables' }

___

<div class="rgon-only" markdown="1">

### GetCostumeLayerSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetCostumeLayerSprite ( [BombCostumeLayer](enums/BombCostumeLayer.md) LayerID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetExplosionCountdown () {: aria-label='Functions' }
#### int GetExplosionCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetFallAcceleration () {: aria-label='Functions' }
#### float GetFallAcceleration ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetFallSpeed () {: aria-label='Functions' }
#### float GetFallSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetHitList () {: aria-label='Functions' }
#### int[] GetHitList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.

___

### GetRocketAngle () {: aria-label='Functions' }
#### float GetRocketAngle ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
火箭炸弹的目标角度，会影响其移动方向和精灵图的朝向。

___

### GetRocketSpeed () {: aria-label='Functions' }
#### float GetRocketSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
火箭炸弹的目标速度。在自然情况下，其速度每帧增加 1。

___

### GetScale () {: aria-label='Functions' }
#### float GetScale ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于应用炸弹外观的动画集。

___

### IsLoadingCostumes () {: aria-label='Functions' }
#### boolean IsLoadingCostumes ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回该炸弹是否通过天使棱镜效果创建。

___

### SetFallAcceleration () {: aria-label='Functions' }
#### void SetFallAcceleration ( float Acceleration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetFallSpeed () {: aria-label='Functions' }
#### void SetFallSpeed ( float Speed ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetLoadCostumes () {: aria-label='Functions' }
#### void SetLoadCostumes ( boolean Load = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetPrismTouched () {: aria-label='Functions' }
#### void SetPrismTouched ( boolean IsTouched ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置该炸弹是否通过天使棱镜效果创建。

___

### SetRocketAngle () {: aria-label='Functions' }
#### void SetRocketAngle ( float Angle ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置火箭炸弹的目标角度，会影响其移动方向和精灵图的朝向。

___

### SetRocketSpeed () {: aria-label='Functions' }
#### void SetRocketSpeed ( float Speed ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置火箭炸弹的目标速度。请注意，在自然情况下，其速度每帧会增加 1。

___

### SetScale () {: aria-label='Functions' }
#### void SetScale ( float Scale ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
应与 [SetLoadCostumes](#setloadcostumes) 方法配合使用。

___

### UpdateDirtColor () {: aria-label='Functions' }
#### void UpdateDirtColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

</div>
