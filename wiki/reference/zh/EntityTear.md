---
tags:
  - Class
---
# Class "EntityTear"

???+ info
    You can get this class by using the following function:

    * [Entity.ToTear()](Entity.md#totear)
    * [EntityFamiliar.FireProjectile()](EntityFamiliar.md#fireprojectile)
    * [EntityPlayer.FireTear()](EntityPlayer.md#firetear)

    ???+ example "Example Code"
        `local tearEntity = Isaac.GetPlayer():FireTear( Vector(0,0), Vector(1, 1) )`

## Class Diagram
--8<-- "zh/snippets/EntityClassDiagram.md"
## Functions

### Add·Tear·Flags () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddTearFlags ( [TearFlags](enums/TearFlags.md) Flags ) {: .copyable aria-label='Functions' }

___

### Change·Variant () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ChangeVariant ( [TearVariant](enums/TearVariant.md) NewVariant ) {: .copyable aria-label='Functions' }

___

### Clear·Tear·Flags () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void ClearTearFlags ( [TearFlags](enums/TearFlags.md) Flags ) {: .copyable aria-label='Functions' }

___

### Has·Tear·Flags () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasTearFlags ( [TearFlags](enums/TearFlags.md) Flags ) {: .copyable aria-label='Functions' }

___

### Reset·Sprite·Scale () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ResetSpriteScale ( ) {: .copyable aria-label='Functions' }
Resets the tear sprite animation depending on scale.
___

<div class="rgon-extension" markdown="1">

### ResetSpriteScale () {: aria-label='Modified Functions' }
#### void ResetSpriteScale ( boolean Force = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
现在接受一个 `Force` 参数，用于强制眼泪重新评估应该播放哪种眼泪缩放动画。

___
## Functions

</div>

### Set·Dead·Eye·Intensity () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetDeadEyeIntensity ( float Intensity ) {: .copyable aria-label='Functions' }

___

### Set·Knockback·Multiplier () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetKnockbackMultiplier ( float Multiplier ) {: .copyable aria-label='Functions' }

___

### Set·Parent·Offset () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetParentOffset ( [Vector](Vector.md) Offset ) {: .copyable aria-label='Functions' }

___

### Set·Wait·Frames () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetWaitFrames ( int Value ) {: .copyable aria-label='Functions' }

___
## Variables

### Base·Damage {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const float BaseDamage  {: .copyable aria-label='Variables' }

___

### Base·Scale {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const float BaseScale  {: .copyable aria-label='Variables' }

___

### Bounced {: aria-label='Variables' }
[ ](#){: .abp .tooltip .badge }
#### boolean Bounced  {: .copyable aria-label='Variables' }
true if tear bounced off something.

This attribute got removed with Repentance.
___

### Can·Trigger·Streak·End {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanTriggerStreakEnd  {: .copyable aria-label='Variables' }
For Onan's strak and Dead Eye.
___

### Continue·Velocity {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) ContinueVelocity  {: .copyable aria-label='Variables' }

___

### Falling·Acceleration {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float FallingAcceleration  {: .copyable aria-label='Variables' }

___

### Falling·Speed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float FallingSpeed  {: .copyable aria-label='Variables' }

___

### Height {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Height  {: .copyable aria-label='Variables' }

___

### Homing·Friction {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float HomingFriction  {: .copyable aria-label='Variables' }

___

### Knockback·Multiplier {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float KnockbackMultiplier  {: .copyable aria-label='Variables' }

___

### Parent·Offset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) ParentOffset  {: .copyable aria-label='Variables' }
Used for Position adjustment (vs PositionOffset which is a render offset)
___

### Pos·Displacement {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) PosDisplacement  {: .copyable aria-label='Variables' }

___

### Rotation {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Rotation  {: .copyable aria-label='Variables' }

___

### Scale {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Scale  {: .copyable aria-label='Variables' }

___

### Stick·Diff {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) StickDiff  {: .copyable aria-label='Variables' }

___

### Stick·Target {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) StickTarget  {: .copyable aria-label='Variables' data-altreturn='nil' }

___

### Stick·Timer {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int StickTimer  {: .copyable aria-label='Variables' }

___

### Tear·Flags {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [TearFlags](enums/TearFlags.md) TearFlags {: .copyable aria-label='Variables' }

___

### Tear·Index {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const int TearIndex  {: .copyable aria-label='Variables' }
- In each run, the game keeps track of how many tears have been fired by the player in total.
- `TearIndex` represents this tear counter.
- It is 0-indexed, meaning that the first tear fired by the player on a run will have a `TearIndex` of 0, the second tear fired by the player on a run will have a `TearIndex` of 1, and so on.
___

### Wait·Frames {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int WaitFrames  {: .copyable aria-label='Variables' }

___

<div class="rgon-only" markdown="1">

### FireSplitTear () {: aria-label='Functions' }
#### [EntityTear](EntityTear.md) FireSplitTear ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, float DamageMultiplier = 0.5, float SizeMultiplier = 0.6, int Variant = 0, [SplitTearType](enums/SplitTearType.md) splitType = SplitTearType.SPLIT_GENERIC ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
发射一颗继承该眼泪诸多属性（标记、伤害、大小、颜色等）的新眼泪。

此操作还会触发 `MC_POST_FIRE_SPLIT_TEAR` 回调。对于自定义效果，可以传入字符串代替 [SplitTearType](enums/SplitTearType.md)。

___

### GetDeadEyeIntensity () {: aria-label='Functions' }
#### float GetDeadEyeIntensity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回眼泪因“死亡之眼”道具产生的强度值，该值介于 `0` 和 `1` 之间。

___

### GetDeadEyeSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetDeadEyeSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回“死亡之眼”道具使用的红色光环精灵图。

___

### GetHitList () {: aria-label='Functions' }
#### int[] GetHitList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个数组，其中包含使用其 [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) 字段标识的已命中实体。


___

### GetTearEffectSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetTearEffectSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回像“火焰意志”和“神秘液体”等眼泪变体所使用的眼泪特效精灵图。

___

### GetTearHaloSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetTearHaloSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回“神性”眼泪所使用的眼泪光晕精灵图。

___

### IsMultidimensionalTouched () {: aria-label='Functions' }
#### boolean IsMultidimensionalTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回该眼泪是否是通过“多维宝宝”效果创建的。

___

### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回该眼泪是否是通过“天使棱镜”效果创建的。

___

### MakeMultidimensionalCopy () {: aria-label='Functions' }
#### [EntityTear](EntityTear.md) MakeMultidimensionalCopy ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
复制该眼泪并为其应用黑白效果，此效果与“多维宝宝”跟班所使用的效果相同。

___

### SetMultidimensionalTouched () {: aria-label='Functions' }
#### void SetMultidimensionalTouched ( boolean IsTouched ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置该眼泪是否是通过“多维宝宝”效果创建的。

___

### SetPrismTouched () {: aria-label='Functions' }
#### void SetPrismTouched ( boolean IsTouched ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置该眼泪是否是通过“天使棱镜”效果创建的。

___

### SetInitSound () {: aria-label='Functions' }
#### void SetInitSound ( [SoundEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/SoundEffect.html) SoundID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置眼泪生成时自动播放的声音。可以设为 `SoundEffect.SOUND_NULL` 以不播放声音。

应在 [MC_POST_TEAR_INIT](https://wofsauge.github.io/IsaacDocs/rep/enums/ModCallbacks.html#mc_post_tear_init) 中设置，或在眼泪第一次 Update 之前的任意时间设置，否则不会生效。

???-info "Example"
    ```lua
      ---Makes all tears play the Fart Sound on spawn
      ---@param tear EntityTear
      function mod:TearInit(tear)
          tear:SetInitSound(SoundEffect.SOUND_FART)
      end

      mod:AddCallback(ModCallbacks.MC_POST_TEAR_INIT, mod.TearInit)
    ```

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

### ClearHitList () {: aria-label='Functions' }
#### void ClearHitList ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Clears the array of hit entities, allowing them to be hit again.

___

</div>
