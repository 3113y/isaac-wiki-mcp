---
tags:
  - Class
---
# Class "EntityKnife"

???+ info
    You can get this class by using the following function:

    * [Entity.ToKnife()](Entity.md#toknife)
    * [EntityPlayer.FireKnife()](EntityPlayer.md#fireknife)

    ???+ example "Example Code"
        `local knifeEntity = Isaac.GetPlayer():FireKnife(Isaac.GetPlayer())`

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

### Get·Knife·Distance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### float GetKnifeDistance ( ) {: .copyable aria-label='Functions' }

___

### Get·Knife·Velocity () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### float GetKnifeVelocity ( ) {: .copyable aria-label='Functions' }

___

### Get·Render·Z () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetRenderZ ( ) {: .copyable aria-label='Functions' }

___

### Has·Tear·Flags () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasTearFlags ( [TearFlags](enums/TearFlags.md) Flags ) {: .copyable aria-label='Functions' }

___

### Is·Flying () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsFlying ( ) {: .copyable aria-label='Functions' }

___

### Reset () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Reset ( ) {: .copyable aria-label='Functions' }
用于主刀（master knifes），以使其返回到玩家。
___

### Set·Path·Follow·Speed () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetPathFollowSpeed ( float Speed ) {: .copyable aria-label='Functions' }

___

### Shoot () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Shoot ( float Charge, float Range ) {: .copyable aria-label='Functions' }

___
## Variables

### Charge {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Charge  {: .copyable aria-label='Variables' }

___

### Max·Distance {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float MaxDistance  {: .copyable aria-label='Variables' }

___

### Path·Follow·Speed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float PathFollowSpeed  {: .copyable aria-label='Variables' }
Unit speed of path moving knifes.
___

### Path·Offset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float PathOffset  {: .copyable aria-label='Variables' }

___

### Rotation {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Rotation  {: .copyable aria-label='Variables' }

___

### Rotation·Offset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float RotationOffset  {: .copyable aria-label='Variables' }

___

### Scale {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Scale  {: .copyable aria-label='Variables' }

___

### Tear·Flags {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [TearFlags](enums/TearFlags.md) TearFlags  {: .copyable aria-label='Variables' }

___

<div class="rgon-only" markdown="1">

### FireSplitTear () {: aria-label='Functions' }
#### [EntityTear](EntityTear.md) FireSplitTear ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, float DamageMultiplier = 0.5, float SizeMultiplier = 0.6, int Variant = 0, [SplitTearType](enums/SplitTearType.md) splitType = SplitTearType.SPLIT_GENERIC ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Fire a new tear that inherits many attributes from this knife (flags, damage, size, color, etc).

This will also trigger the `MC_POST_FIRE_SPLIT_TEAR` callback. For custom effects, a string may be passed in place of the [SplitTearType](enums/SplitTearType.md).

___

### GetHitboxParentKnife () {: aria-label='Functions' }
#### [EntityKnife](EntityKnife.md) GetHitboxParentKnife ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
对于由近战武器“挥砍”（骨棒、灵魂之剑等）创建的“hitbox” [EntityKnife](EntityKnife.md)（[KnifeSubType.CLUB_HITBOX](enums/KnifeSubType.md)），此函数会返回该近战武器的“主” [EntityKnife](EntityKnife.md)。其他情况下返回 `nil`；通过其他方式生成的 hitbox 实体也会返回 `nil`。

___

### GetHitList () {: aria-label='Functions' }
#### int[] GetHitList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.

___

### GetIsSpinAttack () {: aria-label='Functions' }
#### boolean GetIsSpinAttack ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetIsSwinging () {: aria-label='Functions' }
#### boolean GetIsSwinging ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsMultidimensionalTouched () {: aria-label='Functions' }
#### boolean IsMultidimensionalTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回该匕首是否由“多维宝贝”效果创建。

___

### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回该匕首是否由“天使棱镜”效果创建。

___

### SetHitboxParentKnife () {: aria-label='Functions' }
#### void SetHitboxParentKnife ( [EntityKnife](EntityKnife.md) Knife ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
允许为 `GetHitboxParentKnife` 设置自定义值。此功能仅适用于让近战武器（骨棒、灵魂之剑等）的“hitbox” [EntityKnife](EntityKnife.md)（[KnifeSubType.CLUB_HITBOX](enums/KnifeSubType.md)）指向其“主” [EntityKnife](EntityKnife.md)。

请注意，设置此值不会影响任何原版逻辑；该引用仅为方便模组作者而存在，请合理使用。

___

### SetIsSpinAttack () {: aria-label='Functions' }
#### void SetIsSpinAttack ( boolean isSpinAttack ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetIsSwinging () {: aria-label='Functions' }
#### void SetIsSwinging ( boolean isSwinging ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetMultidimensionalTouched () {: aria-label='Functions' }
#### void SetMultidimensionalTouched ( boolean IsTouched ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置该匕首是否由“多维宝贝”效果创建。

___

### SetPrismTouched () {: aria-label='Functions' }
#### void SetPrismTouched ( boolean IsTouched ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置该匕首是否由“天使棱镜”效果创建。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

### SetKnifeDistance () {: aria-label='Functions' }
#### void SetKnifeDistance ( float Distance ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetKnifeVelocity () {: aria-label='Functions' }
#### void SetKnifeVelocity ( float Velocity ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
