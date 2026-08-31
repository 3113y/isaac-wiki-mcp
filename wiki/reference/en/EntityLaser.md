---
tags:
  - Class
---
# Class "EntityLaser"

???+ info
    You can get this class by using the following function:

    * [Entity.ToLaser()](Entity.md#tolaser)
    * [EntityPlayer.FireBrimstone()](EntityPlayer.md#firebrimstone)
    * [EntityPlayer.FireDelayedBrimstone()](EntityPlayer.md#firedelayedbrimstone)
    * [EntityPlayer.FireTechLaser()](EntityPlayer.md#firetechlaser)
    * [EntityPlayer.FireTechXLaser()](EntityPlayer.md#firetechxlaser)

    ???+ example "Example Code"
        `local brimstoneEntity = Isaac.GetPlayer():FireBrimstone(Vector(1, 0))`

## Class Diagram
--8<-- "en/snippets/EntityClassDiagram.md"
## Functions

### Add·Tear·Flags () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddTearFlags ( [TearFlags](enums/TearFlags.md) Flags ) {: .copyable aria-label='Functions' }

___

### Calculate·End·Point () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### static [Vector](Vector.md) CalculateEndPoint ( [Vector](Vector.md) Start, [Vector](Vector.md) Dir, [Vector](Vector.md) PositionOffset, [Entity](Entity.md) Parent, float Margin ) {: .copyable aria-label='Functions' }

___

### Clear·Tear·Flags () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void ClearTearFlags ( [TearFlags](enums/TearFlags.md) Flags ) {: .copyable aria-label='Functions' }

___

### Get·End·Point () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetEndPoint ( ) {: .copyable aria-label='Functions' }

___

### Get·Non·Optimized·Samples () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [VectorList](CppContainer_Vector_VectorList.md) GetNonOptimizedSamples ( ) {: .copyable aria-label='Functions' }

Returns a VectorList representing the path of the laser. Seems to typically return 51 evenly-spaced points along the laser's path, as opposed to [`GetSamples()`](#getsamples) which only returns the minimum needed points to represent the path of the laser.

???+ example "Example Usage"
    ```lua
    local samplePoints = laser:GetNonOptimizedSamples()

    for i=0, #samplePoints-1 do
        local pos = samplePoints:Get(i)
        ...
    end
    ```

___

### Get·Render·Z () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetRenderZ ( ) {: .copyable aria-label='Functions' }

___

### Get·Samples () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [VectorList](CppContainer_Vector_VectorList.md) GetSamples ( ) {: .copyable aria-label='Functions' }

Returns a VectorList representing the path of the laser. Unlike [`GetNonOptimizedSamples()`](#getnonoptimizedsamples), this function returns as few points as possible, while still correctly representing the path of the laser.

For example, for a completely straight laser, [`GetNonOptimizedSamples()`](#getnonoptimizedsamples) will still return 51 points as always, but this function only only return 2.

???+ example "Example Usage"
    ```lua
    local samplePoints = laser:GetSamples()

    for i=0, #samplePoints-1 do
        local pos = samplePoints:Get(i)
        ...
    end
    ```

___

### Has·Tear·Flags () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasTearFlags ( [TearFlags](enums/TearFlags.md) Flags ) {: .copyable aria-label='Functions' }

___

### Is·Circle·Laser () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsCircleLaser ( ) {: .copyable aria-label='Functions' }

???- note "Note"
    This function cannot differentiate between different types of Circle Laser, however these may be identified by their SubType:

    * 0 - Linear Laser (Typical laser with a start and end point)
    * 1 - Ring Ludovico (Controlled laser ring for Ludo synergies)
    * 2 - Ring Projectile (Tech X)
    * 3 - Ring Follow Parent (Maw of the Void)
    * 4 - No Impact (No impact splash, e.g. Tech Zero)

___

### Is·Sample·Laser () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsSampleLaser ( ) {: .copyable aria-label='Functions' }

___

### Set·Active·Rotation () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetActiveRotation ( int Delay, float AngleDegrees, float RotationSpd, boolean TimeoutComplete ) {: .copyable aria-label='Functions' }

___

### Set·Black·Hp·Drop·Chance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetBlackHpDropChance ( float Chance ) {: .copyable aria-label='Functions' }

___

### Set·Homing·Type () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetHomingType ( LaserHomingType Type ) {: .copyable aria-label='Functions' }

___

### Set·Max·Distance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetMaxDistance ( float Distance ) {: .copyable aria-label='Functions' }

___

### Set·Multidimensional·Touched () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetMultidimensionalTouched ( boolean Value ) {: .copyable aria-label='Functions' }

___

### Set·One·Hit () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetOneHit ( boolean Value ) {: .copyable aria-label='Functions' }

___

### Set·Timeout () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetTimeout ( int Value ) {: .copyable aria-label='Functions' }

___

<div class="rgon-extension" markdown="1">

### SetTimeout () {: aria-label='Functions' }
#### void SetTimeout ( int Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>

### Shoot·Angle () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### static [EntityLaser](EntityLaser.md) ShootAngle ( int Variant, [Vector](Vector.md) SourcePos, float AngleDegrees, int Timeout, [Vector](Vector.md) PosOffset, [Entity](Entity.md) Source ) {: .copyable aria-label='Functions' }
static helper to simplify spawning lasers
___
## Variables

### Angle {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Angle  {: .copyable aria-label='Variables' }

___

### Angle·Degrees {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float AngleDegrees  {: .copyable aria-label='Variables' }

___

### Black·Hp·Drop·Chance {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float BlackHpDropChance  {: .copyable aria-label='Variables' }
For maw of void.
___

### Bounce·Laser {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) BounceLaser  {: .copyable aria-label='Variables' data-altreturn='nil' }

___

### Curve·Strength {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float CurveStrength  {: .copyable aria-label='Variables' }
My Reflection.
___

### Disable·Follow·Parent {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean DisableFollowParent  {: .copyable aria-label='Variables' }
Set on children of other lasers, for instance Rubber Cement reflections. Disables m_ParentOffset.
___

### End·Point {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) EndPoint  {: .copyable aria-label='Variables' }
Will hold the endpoint so it will not need to be recalculated when accessed from extern.
___

### First·Update {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean FirstUpdate  {: .copyable aria-label='Variables' }

___

### Grid·Hit {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean GridHit  {: .copyable aria-label='Variables' }
`true` if laser can be clipped by grid entities and it was clipped at that frame.
___

### Homing·Laser {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### HomingLaser HomingLaser  {: .copyable aria-label='Variables' }

___

### Homing·Type {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### LaserHomingType HomingType  {: .copyable aria-label='Variables' }

___

<div class="rgon-extension" markdown="1">

### HomingType {: aria-label='Modified Variables' }
#### int HomingType [ ](#){: .rgonorplus .tooltip .badge }  {: .copyable aria-label='Modified Variables' }
Same as the default, but now returns a proper integer value instead of userdata.

___

## Functions

</div>

### Is·Active·Rotating {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsActiveRotating  {: .copyable aria-label='Variables' }

___

### Laser·Length {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float LaserLength  {: .copyable aria-label='Variables' }

___

### Last·Angle·Degrees {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float LastAngleDegrees  {: .copyable aria-label='Variables' }

___

### Max·Distance {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float MaxDistance  {: .copyable aria-label='Variables' }
Used to trim brimstone for Azazel (0 - off)
___

### One·Hit {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean OneHit  {: .copyable aria-label='Variables' }
Laser hits only once.
___

### Parent·Offset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) ParentOffset  {: .copyable aria-label='Variables' }

___

### Radius {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Radius  {: .copyable aria-label='Variables' }

___

### Rotation·Degrees {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float RotationDegrees  {: .copyable aria-label='Variables' }

___

### Rotation·Delay {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int RotationDelay  {: .copyable aria-label='Variables' }

___

### Rotation·Spd {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float RotationSpd  {: .copyable aria-label='Variables' }

___

### Sample·Laser {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean SampleLaser  {: .copyable aria-label='Variables' }

___

### Shrink {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean Shrink  {: .copyable aria-label='Variables' }

___

### Start·Angle·Degrees {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float StartAngleDegrees  {: .copyable aria-label='Variables' }
Some lasers have a bit of random variation in rotation so they need to remember their starting point.
___

### Tear·Flags {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [TearFlags](enums/TearFlags.md) TearFlags  {: .copyable aria-label='Variables' }
___

### Timeout {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Timeout  {: .copyable aria-label='Variables' }

___

<div class="rgon-only" markdown="1">

### FireSplitTear () {: aria-label='Functions' }
#### [EntityTear](EntityTear.md) FireSplitTear ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, float DamageMultiplier = 0.5, float SizeMultiplier = 0.6, int Variant = 0, [SplitTearType](enums/SplitTearType.md) splitType = SplitTearType.SPLIT_GENERIC ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Fire a new tear that inherits many attributes from this laser (flags, damage, size, color, etc).

This will also trigger the `MC_POST_FIRE_SPLIT_TEAR` callback. For custom effects, a string may be passed in place of the [SplitTearType](enums/SplitTearType.md).

___

### GetDamageMultiplier () {: aria-label='Functions' }
#### float GetDamageMultiplier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDisableFollowParent () {: aria-label='Functions' }
#### boolean GetDisableFollowParent ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetHitList () {: aria-label='Functions' }
#### int GetHitList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.

___

### GetOneHit () {: aria-label='Functions' }
#### boolean GetOneHit ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetScale () {: aria-label='Functions' }
#### float GetScale ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetShrink () {: aria-label='Functions' }
#### boolean GetShrink ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetTimeout () {: aria-label='Functions' }
#### int GetTimeout ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsMultidimensionalTouched () {: aria-label='Functions' }
#### boolean IsMultidimensionalTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns whether the laser was created through the Multi Dimensional Baby effect.

___

### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns whether the laser was created through the Angelic Prism effect.

___

### RecalculateSamplesNextUpdate () {: aria-label='Functions' }
#### void RecalculateSamplesNextUpdate ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Requests that the laser's shape be fully recalculated the next time it updates. This can force the laser to instantly change its MaxDistance/Radius instead of transitioning to the new value. Has no effect on OneHit or non-sample lasers.

___

### ResetSpriteScale () {: aria-label='Functions' }
#### void ResetSpriteScale ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### RotateToAngle () {: aria-label='Functions' }
#### void RotateToAngle ( float Angle, float Speed = 8.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetDamageMultiplier () {: aria-label='Functions' }
#### void SetDamageMultiplier ( float DamageMult ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetDisableFollowParent () {: aria-label='Functions' }
#### void SetDisableFollowParent ( boolean Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetPrismTouched () {: aria-label='Functions' }
#### void SetPrismTouched ( boolean IsTouched ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets whether the laser was created through the Angelic Prism effect.

___

### SetScale () {: aria-label='Functions' }
#### void SetScale ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetShrink () {: aria-label='Functions' }
#### void SetShrink ( boolean Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetNumChainedLasers () {: aria-label='Functions' }
#### int GetNumChainedLasers ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Related to the effect used by the Monstro's Lung + Technology synergy. If greater than 0, this may cause an additional laser to spawn at the endpoint of this laser, up to this many times.

___

### SetInitSound () {: aria-label='Functions' }
#### void SetInitSound ( [SoundEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/SoundEffect.html) Sound ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Set this after a laser is spawned but before it updates (for example, in [MC_POST_LASER_INIT](https://wofsauge.github.io/IsaacDocs/rep/enums/ModCallbacks.html#mc_post_laser_init)) to change the sound it makes. Set it to `SoundEffect.SOUND_NULL` to prevent any sound from playing.

___

### SetNumChainedLasers () {: aria-label='Functions' }
#### void SetNumChainedLasers ( int Value ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Controls the effect used by the Monstro's Lung + Technology synergy. If greater than 0, this may cause an additional laser to spawn at the endpoint of this laser, up to this many times. May not function for all laser variants.

___

</div>
