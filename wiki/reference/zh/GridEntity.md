---
tags:
  - Class
---
# Class "GridEntity"

???+ info
    You can get this class by using the following function:

    * [Isaac.GridSpawn()](Isaac.md#gridspawn)
    * [Room.GetGridEntity()](Room.md#getgridentity)
    * [Room.GetGridEntityFromPos()](Room.md#getgridentityfrompos)

    ???+ example "Example Code"
        `Game():GetRoom():GetGridEntity(25)`

## Class Diagram
--8<-- "zh/snippets/GridEntityClassDiagram.md"

## Functions

### Destroy () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean Destroy ( boolean Immediate ) {: .copyable aria-label='Functions' }

___

### Destroy·With·Source () {: aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### boolean DestroyWithSource ( boolean Immediate, [EntityRef](EntityRef.md) Source ) {: .copyable aria-label='Functions' }

___

### Get·Grid·Index () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetGridIndex ( ) {: .copyable aria-label='Functions' }

___

### Get·RNG () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [RNG](RNG.md) GetRNG ( ) {: .copyable aria-label='Functions' }

???- warning "Warning"
    This RNG is initialized with the same seed for all grid entities in the whole run. Instead, it's advised to create a custom data structure or use either the [SpawnSeed](GridEntityDesc.md#spawnseed) or [VariableSeed](GridEntityDesc.md#variableseed) fields from the [GridEntityDesc](GridEntityDesc.md) object.

___

### Get·Save·State () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntityDesc](GridEntityDesc.md) GetSaveState ( ) {: .copyable aria-label='Functions' }

???+ info "Info"
    Both the [Desc](#desc) property and the [GetSaveState()](#getsavestate) method return the exact same [GridEntityDesc](GridEntityDesc.md) object. The game devs advise to use [GetSaveState()](#getsavestate) instead of [Desc](#desc).
___

### Get·Sprite () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [Sprite](Sprite.md) GetSprite ( ) {: .copyable aria-label='Functions' }

___

### Get·Type () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntityType](enums/GridEntityType.md) GetType ( ) {: .copyable aria-label='Functions' }

___

### Get·Variant () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetVariant ( ) {: .copyable aria-label='Functions' }

___

### Hurt () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean Hurt ( int Damage ) {: .copyable aria-label='Functions' }

___

### Hurt·With·Source () {: aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### boolean HurtWithSource ( int Damage, [EntityRef](EntityRef.md) Source ) {: .copyable aria-label='Functions' }

___

### Init () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Init ( int Seed ) {: .copyable aria-label='Functions' }

___

### Post·Init () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PostInit ( ) {: .copyable aria-label='Functions' }

___

### Render () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Render ( [Vector](Vector.md) Offset ) {: .copyable aria-label='Functions' }

___

### Set·Type () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetType ( [GridEntityType](enums/GridEntityType.md) Type ) {: .copyable aria-label='Functions' }

___

### Set·Variant () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetVariant ( int Variant ) {: .copyable aria-label='Functions' }

___

### To·Door () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntityDoor](GridEntityDoor.md) ToDoor ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.
___

### To·Pit () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntityPit](GridEntityPit.md) ToPit ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.
___

### To·Poop () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntityPoop](GridEntityPoop.md) ToPoop ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.
___

### To·Pressure·Plate () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntityPressurePlate](GridEntityPressurePlate.md) ToPressurePlate ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.
___

### To·Rock () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntityRock](GridEntityRock.md) ToRock ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.
___

### To·Spikes () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntitySpikes](GridEntitySpikes.md) ToSpikes ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.
___

### To·TNT () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntityTNT](GridEntityTNT.md) ToTNT ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.
___

<div class="rgon-extension" markdown="1">

### ToTNT () {: aria-label='Modified Functions' }
#### [GridEntityTNT](https://wofsauge.github.io/IsaacDocs/rep/GridEntityTNT.html) ToTNT ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
修改函数以改善网格实体更新回调的行为。

___

</div>

### Update () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Update ( ) {: .copyable aria-label='Functions' }

___
## Variables

### Collision·Class {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridCollisionClass](enums/GridCollisionClass.md) CollisionClass  {: .copyable aria-label='Variables' }

___

### Desc {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntityDesc](GridEntityDesc.md) Desc  {: .copyable aria-label='Variables' }

???+ info "Info"
    Both the [Desc](#desc) property and the [GetSaveState()](#getsavestate) method return the exact same [GridEntityDesc](GridEntityDesc.md) object. The game devs advise to use [GetSaveState()](#getsavestate) instead of [Desc](#desc).

___

### Position {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) Position  {: .copyable aria-label='Variables' }
Returns the position of the grid cell's center point
___

### State {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int State  {: .copyable aria-label='Variables' }
Used for various different usecases.

???- example "Example States"
    ```
    Rocks with state = 2 are destroyed rocks (The rubble is the rock basically)
    ```
___

### Var·Data {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int VarData  {: .copyable aria-label='Variables' }
A Variable that stores some entity-specific data. The content can have completely different effects for different GridEntities.

???- example "Example Code"
    This code spawns a functioning Void Portal into the center of the room. This will teleport you to the floor "The Void" and will have the same appearance as the vanilla portal:
    ```lua
    -- From: https://github.com/IsaacScript/isaac-typescript-definitions/blob/main/typings/unofficial/enumsGridEntityVariants.d.ts
    local TrapdoorVariant = {
      NORMAL = 0,
      VOID_PORTAL = 1,
    }

    local game = Game();
    local room = game:GetRoom()
    local centerPos = room:GetCenterPos()

    -- By default, this will spawn a normal trapdoor, even though we specify the Void Portal variant
    local voidPortal = Isaac.GridSpawn(GridEntityType.GRID_TRAPDOOR, TrapdoorVariant.VOID_PORTAL, centerPos, true)

    -- Set the destination to The Void and apply the pulse effect shader
    voidPortal.VarData = 1

    -- Replace the spritesheet to make it look like a Void Portal
    local sprite = portalEntity:GetSprite()
    sprite:Load("gfx/grid/voidtrapdoor.anm2", true)
    ```

___

<div class="rgon-only" markdown="1">

### GetRenderPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetRenderPosition ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetWaterClipFlags () {: aria-label='Functions' }
#### [WaterClipFlag](enums/WaterClipFlag.md) GetWaterClipFlags ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
获取一个位集，用于指示此网格实体应渲染在水面上方还是下方。

可以使用 `ResetWaterClipFlags()` 恢复原版状态。

___

### HurtDamage () {: aria-label='Functions' }
#### void HurtDamage ( [Entity](Entity.md) Entity, int PlayerDamage, int DamageFlags, float Damage, boolean ignoreGridCollision ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsBreakableRock () {: aria-label='Functions' }
#### void IsBreakableRock ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ResetWaterClipFlags () {: aria-label='Functions' }
#### void ResetWaterClipFlags ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将水面渲染恢复为默认的原版状态。参见 `SetWaterClipFlags()`。

___

### SetWaterClipFlags () {: aria-label='Functions' }
#### void SetWaterClipFlags ( [WaterClipFlag](enums/WaterClipFlag.md) Flags ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
允许修改此网格实体应渲染在水面上方还是下方。

请注意，这也会禁用原版对这些标志的自动更改，例如便便被破坏后切换为在水面下方渲染。

可以使用 `ResetWaterClipFlags()` 恢复原版状态。

___

### ToDecoration () {: aria-label='Functions' }
#### [GridEntityDecoration](GridEntityDecoration.md) ToDecoration ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityDecoration](GridEntityDecoration.md)对象。
???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___

### ToFire () {: aria-label='Functions' }
#### [GridEntityFire](GridEntityFire.md) ToFire ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityFire](GridEntityFire.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___

### ToGravity () {: aria-label='Functions' }
#### [GridEntityGravity](GridEntityGravity.md) ToGravity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityGravity](GridEntityGravity.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___

### ToLock () {: aria-label='Functions' }
#### [GridEntityLock](GridEntityLock.md) ToLock ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityLock](GridEntityLock.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___

### ToStairs () {: aria-label='Functions' }
#### [GridEntityStairs](GridEntityStairs.md) ToStairs ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityStairs](GridEntityStairs.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___

### ToStatue () {: aria-label='Functions' }
#### [GridEntityStatue](GridEntityStatue.md) ToStatue ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityStatue](GridEntityStatue.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___

### ToTeleporter () {: aria-label='Functions' }
#### [GridEntityTeleporter](GridEntityTeleporter.md) ToTeleporter ( ) {: .copyable aria-label='Functions' }    [ ](#){: .rgonorplus .tooltip .badge }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityTeleporter](GridEntityTeleporter.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___

### ToTrapDoor () {: aria-label='Functions' }
#### [GridEntityTrapDoor](GridEntityTrapDoor.md) ToTrapDoor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityTrapDoor](GridEntityTrapDoor.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___

### ToWall () {: aria-label='Functions' }
#### [GridEntityWall](GridEntityWall.md) ToWall ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityWall](GridEntityWall.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___

### ToWeb () {: aria-label='Functions' }
#### [GridEntityWeb](GridEntityWeb.md) ToWeb ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于将一个[GridEntity](GridEntity.md)对象转换为一个[GridEntityWeb](GridEntityWeb.md)对象。

???+ note "返回行为"

    如果转换不成功，此函数返回`nil`。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

</div>
