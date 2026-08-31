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
--8<-- "en/snippets/EntityClassDiagram.md"
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
Now accepts a `Force` argument to force the tear into re-evaluating what tear scale animation it should play.

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
Fire a new tear that inherits many attributes from this tear (flags, damage, size, color, etc).

This will also trigger the `MC_POST_FIRE_SPLIT_TEAR` callback. For custom effects, a string may be passed in place of the [SplitTearType](enums/SplitTearType.md).

___

### GetDeadEyeIntensity () {: aria-label='Functions' }
#### float GetDeadEyeIntensity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the intensity value of the tear as a result of the Dead Eye collectible. It is between `0` and `1`.

___

### GetDeadEyeSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetDeadEyeSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the red aura sprite used by the Dead Eye collectible.

___

### GetHitList () {: aria-label='Functions' }
#### int[] GetHitList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.

___

### GetTearEffectSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetTearEffectSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the tear effect sprite used by tear variants like Fire Mind and Mysterious Liquid.

___

### GetTearHaloSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetTearHaloSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the tear halo sprite used by Godhead tears.

___

### IsMultidimensionalTouched () {: aria-label='Functions' }
#### boolean IsMultidimensionalTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns whether the tear was created through the Multi Dimensional Baby effect.

___

### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns whether the tear was created through the Angelic Prism effect.

___

### MakeMultidimensionalCopy () {: aria-label='Functions' }
#### [EntityTear](EntityTear.md) MakeMultidimensionalCopy ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Copies the tear and applies a black and white effect to it. This effect is the same one used by the Multidimensional Baby familiar.

___

### SetMultidimensionalTouched () {: aria-label='Functions' }
#### void SetMultidimensionalTouched ( boolean IsTouched ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets whether the tear was created through the Multi Dimensional Baby effect.

___

### SetPrismTouched () {: aria-label='Functions' }
#### void SetPrismTouched ( boolean IsTouched ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets whether the tear was created through the Angelic Prism effect.

___

### SetInitSound () {: aria-label='Functions' }
#### void SetInitSound ( [SoundEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/SoundEffect.html) SoundID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the sound that will be automatically played when the tear is spawned. Can be set to `SoundEffect.SOUND_NULL` to make no sound play.

Should be set on [MC_POST_TEAR_INIT](https://wofsauge.github.io/IsaacDocs/rep/enums/ModCallbacks.html#mc_post_tear_init) or at any point prior to the tear's first Update, otherwise it will have no effect.

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

### ClearHitList () {: aria-label='Functions' }
#### void ClearHitList ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Clears the array of hit entities, allowing them to be hit again.

___

</div>
