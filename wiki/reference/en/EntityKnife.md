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
Used for master knifes, to get back to player.
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
For a "hitbox" [EntityKnife](EntityKnife.md) ([KnifeSubType.CLUB_HITBOX](enums/KnifeSubType.md)) created by a melee weapon's "swing" (Bone Club, Spirit Sword, etc.), this function returns that weapon's "main" [EntityKnife](EntityKnife.md). It returns `nil` otherwise, including for hitbox entities spawned by other means.

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
Returns whether the knife was created through the Multi Dimensional Baby effect.

___

### IsPrismTouched () {: aria-label='Functions' }
#### boolean IsPrismTouched ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns whether the knife was created through the Angelic Prism effect.

___

### SetHitboxParentKnife () {: aria-label='Functions' }
#### void SetHitboxParentKnife ( [EntityKnife](EntityKnife.md) Knife ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Allows setting a custom value for `GetHitboxParentKnife`, which is intended to only be used for a "hitbox" [EntityKnife](EntityKnife.md) ([KnifeSubType.CLUB_HITBOX](enums/KnifeSubType.md)) to refer to the "main" [EntityKnife](EntityKnife.md) of a melee weapon (Bone Club, Spirit Sword, etc).

Note that setting this has no influence on any vanilla logic - this reference is only for the convenience of modders. Please use appropriately.

___

### SetIsSpinAttack () {: aria-label='Functions' }
#### void SetIsSpinAttack ( boolean isSpinAttack ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetIsSwinging () {: aria-label='Functions' }
#### void SetIsSwinging ( boolean isSwinging ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetMultidimensionalTouched () {: aria-label='Functions' }
#### void SetMultidimensionalTouched ( boolean IsTouched ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets whether the knife was created through the Multi Dimensional Baby effect.

___

### SetPrismTouched () {: aria-label='Functions' }
#### void SetPrismTouched ( boolean IsTouched ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets if the knife was created through the Angelic Prism effect.

___

### SetKnifeDistance () {: aria-label='Functions' }
#### void SetKnifeDistance ( float Distance ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetKnifeVelocity () {: aria-label='Functions' }
#### void SetKnifeVelocity ( float Velocity ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
