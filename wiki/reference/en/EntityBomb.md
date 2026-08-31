---
tags:
  - Class
---
# Class "EntityBomb"

???+ info
    You can get this class by using the following function:

    * [Entity.ToBomb()](Entity.md#tobomb)
    * [EntityPlayer.FireBomb()](EntityPlayer.md#firebomb)

    ???+ example "Example Code"
        `local entity = Isaac.GetPlayer():FireBomb(Vector(0,0), Vector(1,1))`

## Class Diagram
--8<-- "en/snippets/EntityClassDiagram.md"

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

Uses [TearFlags](enums/TearFlags.md) to alter the behavior of the bomb.
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
Returns the target angle for rocket bombs. It affects both their movement and sprite orientation.

___

### GetRocketSpeed () {: aria-label='Functions' }
#### float GetRocketSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the target speed for rocket bombs. Under normal conditions, it increases by 1 every frame.

___

### GetScale () {: aria-label='Functions' }
#### float GetScale ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used to apply the animation set for the bomb costume.

___

### IsLoadingCostumes () {: aria-label='Functions' }
#### boolean IsLoadingCostumes ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns whether the bomb was created by the Angelic Prism effect.

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
Sets whether the bomb was created by the Angelic Prism effect.

___

### SetRocketAngle () {: aria-label='Functions' }
#### void SetRocketAngle ( float Angle ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the target angle for a rocket bomb. It affects both its movement and sprite orientation.

___

### SetRocketSpeed () {: aria-label='Functions' }
#### void SetRocketSpeed ( float Speed ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the target speed for a rocket bomb. Under normal conditions, it increases by 1 every frame.

___

### SetScale () {: aria-label='Functions' }
#### void SetScale ( float Scale ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Should be used with the [SetLoadCostumes](#setloadcostumes) method.

___

### UpdateDirtColor () {: aria-label='Functions' }
#### void UpdateDirtColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
