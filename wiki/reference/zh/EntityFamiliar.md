---
tags:
  - Class
---
# Class "EntityFamiliar"

???+ info
    You can get this class by using the following function:

    * [Entity.ToFamiliar()](Entity.md#tofamiliar)
    * [EntityPlayer.AddItemWisp()](EntityPlayer.md#additemwisp)
    * [EntityPlayer.AddMinisaac()](EntityPlayer.md#addminisaac)
    * [EntityPlayer.AddSwarmFlyOrbital()](EntityPlayer.md#addswarmflyorbital)
    * [EntityPlayer.AddWisp()](EntityPlayer.md#addwisp)
    * [EntityPlayer.ThrowFriendlyDip()](EntityPlayer.md#throwfriendlydip)

    ???+ example "Example Code"
        `local familiarEntity = Isaac.GetPlayer():AddMinisaac(Vector(0,0))`

## Class Diagram
--8<-- "zh/snippets/EntityClassDiagram.md"
## Functions

### Add·Coins () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCoins ( int Value ) {: .copyable aria-label='Functions' }

___

### Add·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddHearts ( int Hearts ) {: .copyable aria-label='Functions' }

___

### Add·Keys () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddKeys ( int Keys ) {: .copyable aria-label='Functions' }

___

### Add·To·Delayed () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddToDelayed ( ) {: .copyable aria-label='Functions' }
Adds to delayed. This doesn't remove other flags!
___

### Add·To·Followers () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddToFollowers ( ) {: .copyable aria-label='Functions' }
Adds to followers. This doesn't remove other flags!
___

### Add·To·Orbit () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddToOrbit ( int Layer ) {: .copyable aria-label='Functions' }
Adds to orbitals. This doesn't remove other flags!
___

### Fire·Projectile () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityTear](EntityTear.md) FireProjectile ( [Vector](Vector.md) Dir ) {: .copyable aria-label='Functions' }

Shoots a projectile from the center of the familiar in the direction you defined.
If used on a familiar that shoots multiple projectiles (example: harlequin baby), this function will only return the left most projectile based on the direction. If used on familiars with special tears (example: Lil Brimstone,...), this will just shoot a regular tear.
This function will not play the shoot animation of the familiar.
___

### Follow·Parent () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void FollowParent ( ) {: .copyable aria-label='Functions' }

___

### Follow·Position () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void FollowPosition ( [Vector](Vector.md) Pos ) {: .copyable aria-label='Functions' }

___

### Get·Orbit·Distance () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### static [Vector](Vector.md) GetOrbitDistance ( int Layer ) {: .copyable aria-label='Functions' }

___

### Get·Orbit·Position () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetOrbitPosition ( [Vector](Vector.md) Pos ) {: .copyable aria-label='Functions' }

Returns the position of an orbiting familiar relative to the player's position. Returns `:::lua Vector(0,0) if its a normal familiar.`
The "pos" argument is used as an offset.
___

### Move·Delayed () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void MoveDelayed ( int NumFrames ) {: .copyable aria-label='Functions' }

___

### Move·Diagonally () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void MoveDiagonally ( float Speed ) {: .copyable aria-label='Functions' }

___

### Pick·Enemy·Target () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void PickEnemyTarget ( float MaxDistance, int FrameInterval = 13, int Flags = 0, [Vector](Vector.md) ConeDir = Vector.Zero, float ConeAngle = 15 ) {: .copyable aria-label='Functions' }
**Flags**: A combination of the following flags (none of these are set by default)

    * 1: Allow switching to a better target even if we already have one
    * 2: Don't prioritize enemies that are close to our owner
    * 4: Prioritize enemies with higher HP
    * 8: Prioritize enemies with lower HP
    * 16: Give lower priority to our current target (this makes us more likely to switch between targets)

**ConeDir**: If ~= Vector.Zero, searches for targets in a cone pointing in this direction

**ConeAngle**: If ConeDir ~= Vector.Zero, sets the half angle of the search cone in degrees (45 results in a search angle of 90 degrees)
___

### Play·Charge·Anim () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PlayChargeAnim ( [Direction](enums/Direction.md) Dir ) {: .copyable aria-label='Functions' }

___

### Play·Float·Anim () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PlayFloatAnim ( [Direction](enums/Direction.md) Dir ) {: .copyable aria-label='Functions' }

___

### Play·Shoot·Anim () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PlayShootAnim ( [Direction](enums/Direction.md) Dir ) {: .copyable aria-label='Functions' }

___

### Recalculate·Orbit·Offset () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int RecalculateOrbitOffset ( int Layer, boolean Add ) {: .copyable aria-label='Functions' }
Returns the number of familiars in that layer.
___

### Remove·From·Delayed () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveFromDelayed ( ) {: .copyable aria-label='Functions' }

___

### Remove·From·Followers () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveFromFollowers ( ) {: .copyable aria-label='Functions' }

___

### Remove·From·Orbit () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveFromOrbit ( ) {: .copyable aria-label='Functions' }

___

### Shoot () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Shoot ( ) {: .copyable aria-label='Functions' }
When called in POST_FAMILIAR_UPDATE on a custom familiar, appears to handle everything for a basic shooting familiar. This includes handling animations, firing tears, and synergies.

## Variables

### Coins {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Coins  {: .copyable aria-label='Variables' }

___

### Fire·Cooldown {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int FireCooldown  {: .copyable aria-label='Variables' }

___

### Head·Frame·Delay {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int HeadFrameDelay  {: .copyable aria-label='Variables' }

___

### Hearts {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Hearts  {: .copyable aria-label='Variables' }

___

### Is·Delayed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsDelayed {: .copyable aria-label='Variables' }

___

### Is·Follower {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsFollower {: .copyable aria-label='Variables' }

___

### Keys {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Keys  {: .copyable aria-label='Variables' }

___

### Last·Direction {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Direction](enums/Direction.md) LastDirection  {: .copyable aria-label='Variables' }

___

### Move·Direction {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Direction](enums/Direction.md) MoveDirection  {: .copyable aria-label='Variables' }

___

### Orbit·Angle·Offset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float OrbitAngleOffset  {: .copyable aria-label='Variables' }

Can be used to override the angular position of the familiar on its orbit based on the initial starting position of the orbit.

???- example "Example Code"
    This code will make all of your orbitals move as a tight wall around you.

    ```lua
    for i,v in ipairs(Isaac.GetRoomEntities()) do
        if v.Type==3 then
            v:ToFamiliar().OrbitAngleOffset = 0.25*i
        end
    end
    ```

    Result: ![angle offset](images/example_familiar_angleOffset.png)
___

### Orbit·Distance {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) OrbitDistance  {: .copyable aria-label='Variables' }

Defines the orbit of the familiar, if its an orbital. The Vector is interpreted as the dimensions of the circle/oval orbit. Example: `:::lua Vector(110,90)` is the orbital of "Forever alone".
___

### Orbit·Layer {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int OrbitLayer  {: .copyable aria-label='Variables' }

This value is `-1` by default, and changes to whichever value is defined by `EntityFamiliar:AddToOrbit()`.
___

### Orbit·Speed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float OrbitSpeed  {: .copyable aria-label='Variables' }

___

### Player {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityPlayer](EntityPlayer.md) Player  {: .copyable aria-label='Variables' }

___

### Room·Clear·Count {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int RoomClearCount  {: .copyable aria-label='Variables' }

___

### Shoot·Direction {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Direction](enums/Direction.md) ShootDirection  {: .copyable aria-label='Variables' }

___

### State {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int State  {: .copyable aria-label='Variables' }

___

<div class="rgon-only" markdown="1">

### CanBeDamagedByEnemies () {: aria-label='Functions' }
#### boolean CanBeDamagedByEnemies ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CanBeDamagedByLasers () {: aria-label='Functions' }
#### boolean CanBeDamagedByLasers ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CanBeDamagedByProjectiles () {: aria-label='Functions' }
#### boolean CanBeDamagedByProjectiles ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CanBlockProjectiles () {: aria-label='Functions' }
#### boolean CanBlockProjectiles ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CanCharm () {: aria-label='Functions' }
#### boolean CanCharm ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetActiveWeaponEntity () {: aria-label='Functions' }
#### [Entity](Entity.md) GetActiveWeaponEntity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the Entity associated with the familiar's active [Weapon](Weapon.md).

Returns `nil` if it cannot be found.

___

### GetActiveWeaponNumFired () {: aria-label='Functions' }
#### int GetActiveWeaponNumFired ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the amount of times the familiar's active [Weapon](Weapon.md) has been fired.

___

### GetDirtColor () {: aria-label='Functions' }
#### [Color](Color.md) GetDirtColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetFollowerPriority () {: aria-label='Functions' }
#### [FollowerPriority](enums/FollowerPriority.md) GetFollowerPriority ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetItemConfig () {: aria-label='Functions' }
#### [ItemConfigItem](ItemConfig_Item.md) GetItemConfig ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回赋予此跟班的道具所对应的 ItemConfigItem 对象。

如果跟班不是由道具生成的，则返回 nil。

___

### GetMoveDelayNum () {: aria-label='Functions' }
#### int GetMoveDelayNum ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回跟班相对于玩家移动的延迟帧数。30 帧 = 1 秒。

___

### GetMultiplier () {: aria-label='Functions' }
#### float GetMultiplier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回跟班的“乘数”；该值会受到 **BFFS!** 或 **Hive Mind** 等效果的影响，通常用于乘算跟班伤害等属性。

???- info "乘数"

    - **堕化拉撒路长子权**：x0.25
    - **BFFS!** 和 **Hive Mind**：x2.0
    - **堕化伯大尼**：x0.75

___

### GetPathfinder () {: aria-label='Functions' }
#### [PathFinder](https://wofsauge.github.io/IsaacDocs/rep/PathFinder.html) GetPathfinder ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRandomWisp () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetRandomWisp ( [RNG](RNG.md) RNG ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ warning "Warning"
    This is a static function and must be called via `EntityFamiliar.GetRandomWisp(RNG)`.

___

### GetWeapon () {: aria-label='Functions' }
#### [Weapon](Weapon.md) GetWeapon ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
对于不模仿玩家攻击的跟班（如魅魔等），返回 `nil`。

___

### InvalidateCachedMultiplier () {: aria-label='Functions' }
#### void InvalidateCachedMultiplier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
当下一次调用 [GetMultiplier](EntityFamiliar.md#getmultiplier) 时，触发 [MC_EVALUATE_FAMILIAR_MULTIPLIER](enums/ModCallbacks.md#mc_evaluate_familiar_multiplier) 来重新计算/允许修改乘数。

___

### IsCharmed () {: aria-label='Functions' }
#### boolean IsCharmed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsLilDelirium () {: aria-label='Functions' }
#### boolean IsLilDelirium ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### RemoveFromPlayer () {: aria-label='Functions' }
#### void RemoveFromPlayer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetLilDelirium () {: aria-label='Functions' }
#### void SetLilDelirium ( boolean isLilDelirium ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetMoveDelayNum () {: aria-label='Functions' }
#### void SetMoveDelayNum ( int Delay ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置跟班相对于玩家移动的延迟帧数。30 帧 = 1 秒。

___

### TriggerRoomClear () {: aria-label='Functions' }
#### void TriggerRoomClear ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### TryAimAtMarkedTarget () {: aria-label='Functions' }
#### [Vector](Vector.md) TryAimAtMarkedTarget ( [Vector](Vector.md) AimDirection, [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html) Direction = Direction.NO_DIRECTION ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
#### boolean, table TryAimAtMarkedTarget ( [Vector](Vector.md) AimDirection = nil, [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html) Direction = Direction.NO_DIRECTION, [Vector](Vector.md) TargetPos = nil ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果存在来自 Marked 或 Eye of the Occult/Gello 目标的玩家标记，则返回 `true`，否则返回 `false`。
返回包含修改后 AimDirection、Direction 和 TargetPos 的表。

旧版本会返回修改后的 TargetPos；如果失败，则返回 `nil`。

___

### UpdateDirtColor () {: aria-label='Functions' }
#### void UpdateDirtColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

</div>
