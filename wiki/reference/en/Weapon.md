---
tags:
  - Class
---
# Class "Weapon"

???+ info
    You can access this class through the following function:

    * [EntityPlayer:GetWeapon()](EntityPlayer.md#getweapon)

    ???+ example "Example Code"
        ```lua
        local weapon = Isaac.GetPlayer(0):GetWeapon(1)
        ```

## Functions

<div class="rgon-only" markdown="1">

### ClearItemAnim () {: aria-label='Functions' }
#### void ClearItemAnim ( int ItemID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCharge () {: aria-label='Functions' }
#### float GetCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDirection () {: aria-label='Functions' }
#### [Vector](Vector.md) GetDirection ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetFireDelay () {: aria-label='Functions' }
#### float GetFireDelay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMainEntity () {: aria-label='Functions' }
#### [Entity](Entity.md) GetMainEntity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the active entity used by the weapon (for example, EntityLaser for Brimstone or EntityKnife for Mom's Knife).

Returns `nil` if no active entity can be found.

___

### GetMaxFireDelay () {: aria-label='Functions' }
#### float GetMaxFireDelay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetModifiers () {: aria-label='Functions' }
#### [WeaponModifier](enums/WeaponModifier.md) GetModifiers ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetNumFired () {: aria-label='Functions' }
#### int GetNumFired ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetOwner () {: aria-label='Functions' }
#### [Entity](Entity.md) GetOwner ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetWeaponType () {: aria-label='Functions' }
#### [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) GetWeaponType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsAxisAligned () {: aria-label='Functions' }
#### boolean IsAxisAligned ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsItemAnimFinished () {: aria-label='Functions' }
#### boolean IsItemAnimFinished ( int ItemID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### PlayItemAnim () {: aria-label='Functions' }
#### void PlayItemAnim ( int ItemID, int AnimId, [Vector](Vector.md) Direction, float unk ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetCharge () {: aria-label='Functions' }
#### void SetCharge ( float Charge ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetFireDelay () {: aria-label='Functions' }
#### void SetFireDelay ( float Delay ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetHeadLockTime () {: aria-label='Functions' }
#### void SetHeadLockTime ( int Time ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetModifiers () {: aria-label='Functions' }
#### void SetModifiers ( [WeaponModifier](enums/WeaponModifier.md) modifiers ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMaxCharge () {: aria-label='Functions' }
#### float GetMaxCharge ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
