---
tags:
  - Class
---
# Class "EntityNPC"

???+ info
    你可以通过以下函数获取此类：

    * [Entity.ToNPC()](Entity.md#tonpc)
    * [Game.SpawnEntityDesc()](Game.md#spawnentitydesc)

    ???+ example "Example Code"
        `local entity = Isaac.GetRoomEntities()[1]:ToNPC()`

## Class Diagram
--8<-- "zh/snippets/EntityClassDiagram.md"
## Functions

### Anim·Walk·Frame () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimWalkFrame ( string HorizontalAnim, string VerticalAnim, float SpeedThreshold ) {: .copyable aria-label='Functions' }

___

### Calc·Target·Position () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) CalcTargetPosition ( float DistanceLimit ) {: .copyable aria-label='Functions' }

___

### Can·Be·Damaged·From·Velocity () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanBeDamagedFromVelocity ( [Vector](Vector.md) Velocity ) {: .copyable aria-label='Functions' }

___

### Can·Reroll () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanReroll ( ) {: .copyable aria-label='Functions' }

___

### Fire·Boss·Projectiles () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityProjectile](EntityProjectile.md) FireBossProjectiles ( int NumProjectiles, [Vector](Vector.md) TargetPos, float TrajectoryModifier, [ProjectileParams](ProjectileParams.md) Params ) {: .copyable aria-label='Functions' }
发射一系列弹幕，目标可以是玩家，方向会随机化，或者在瞄准玩家时稍微随机化。可以使用 FallingAccelModifier 使弹幕更快落地。返回最后生成的弹幕指针（例如，当 NumProjectiles=1 时很有用）。
___

### Fire·Projectiles () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void FireProjectiles ( [Vector](Vector.md) Pos, [Vector](Vector.md) Velocity, ProjectilesMode Mode, [ProjectileParams](ProjectileParams.md) Params ) {: .copyable aria-label='Functions' }

???- info "ProjectilesMode"
    该参数控制发射弹幕的模式：
    * 0 : 单发弹幕
    * 1 : 双发弹幕（使用 params.Spread）
    * 2 : 三发弹幕（使用 params.Spread）
    * 3 : 三发弹幕（使用 params.Spread，分布更广？）
    * 4 : 四发弹幕（使用 params.Spread）
    * 5 : 五发弹幕（使用 params.Spread）
    * 6 : 四发弹幕（使用 velocity.x 作为速度，呈 + 形状）
    * 7 : 四发弹幕（使用 velocity.x 作为速度，呈 x 形状）
    * 8 : 八发弹幕（使用 velocity.x 作为速度，呈星形）
    * 9 : N 发弹幕（使用 velocity.x 作为速度，velocity.y = N，params.FireDirectionLimit 和 params.DotProductLimit 仅在弧形中发射）
___

### Get·Alive·Enemy·Count () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetAliveEnemyCount ( ) {: .copyable aria-label='Functions' }

用于将近战敌人重定向到任何敌人以供友方 NPC 使用。
___

### Get·Boss·Color·Idx () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetBossColorIdx ( ) {: .copyable aria-label='Functions' }


???- note "Notes"

    这将返回减少 1 的 boss color idx。要获取在 bosscolors.xml 中设置的实际颜色，请在结果上加 1。
___

<div class="rgon-extension" markdown="1">

### GetBossColorIdx () {: aria-label='Functions' }
#### int GetBossColorIdx ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回 `bosscoloridx`（通常就是子类型）；如果不是 boss color，或 boss color 不适用，则返回 `-1`。

___

</div>

### Get·Champion·Color·Idx () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [ChampionColorIdx](enums/ChampionColor.md) GetChampionColorIdx ( ) {: .copyable aria-label='Functions' }

返回 NPC 的精英颜色索引。如果 NPC 不是精英怪，则返回 -1。
___

### Get·Player·Target () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) GetPlayerTarget ( ) {: .copyable aria-label='Functions' }
如果没有修饰符（最好的朋友），这将返回玩家
___

### Is·Boss () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsBoss ( ) {: .copyable aria-label='Functions' }

___

### Is·Champion () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsChampion ( ) {: .copyable aria-label='Functions' }

___

### Kill·Unique () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void KillUnique ( ) {: .copyable aria-label='Functions' }
对于具有独特死亡动画的实体，例如 Flush! 与粪便敌人。
___

### Make·Champion () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void MakeChampion ( int Seed, ChampionColor ChampionColorIdx = -1, boolean Init = false ) {: .copyable aria-label='Functions' }
强制非精英怪成为精英怪，重置生命值为最大生命值。

**ChampionColorIdx**: 要将此敌人变为的精英类型（-1 将导致随机精英类型）

**Init**: 在初始化敌人时调用时设置为 true，否则为 false
___

### Make·Splat () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityEffect](EntityEffect.md) MakeSplat ( float Size ) {: .copyable aria-label='Functions' }

___

### Morph () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean Morph ( [EntityType](enums/EntityType.md) type, int Variant, int SubType, int ChampionColorIdx ) {: .copyable aria-label='Functions' }

修改当前实体为另一个实体。可以使用 [ChampionColorIdx](https://bindingofisaacrebirth.gamepedia.com/Monsters#Champions) 将实体变为精英怪。使用 `:::lua -1` 以不添加精英变体。

精英变体索引的列表可以在这里找到 : [ChampionColorIdx](https://bindingofisaacrebirth.gamepedia.com/Monsters#Champions)

???+ bug

    这个函数无法将精英 NPC 转换为普通 NPC！为此，请使用以下代码：

    ```lua
    local previousNPC = entity:ToNPC()
    -- spawn the same entity at the same location as the old one
    Isaac.Spawn(previousNPC.Type, previousNPC.Variant, previousNPC.SubType, previousNPC.Position, previousNPC.Velocity, previousNPC.Parent)
    -- remove old entity
    previousNPC:Remove()
    ```

???- example "Example Code"

    This code turns an entity into a gaper.

    ```lua
    entity:ToNPC():Morph(EntityType.ENTITY_GAPER, 0, 0, -1)
    ```
___

### Play·Sound () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PlaySound ( [SoundEffect](enums/SoundEffect.md) ID, float Volume, int FrameDelay, boolean Loop, float Pitch ) {: .copyable aria-label='Functions' }

___

<div class="rgon-extension" markdown="1">

### PlaySound () {: aria-label='Modified Functions' }
#### void PlaySound ( int ID, float Volume = 1.0, int FrameDelay = 2, boolean Loop = true, float Pitch = 1.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
除 `ID` 外，所有参数现在均为可选参数。

___

## Functions

</div>

### Query·NPCs·Group () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityList](CppContainer_EntityList.md) QueryNPCsGroup ( int GroupIdx ) {: .copyable aria-label='Functions' }

___

### Query·NPCs·Spawner·Type () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityList](CppContainer_EntityList.md) QueryNPCsSpawnerType ( [EntityType](enums/EntityType.md) SpawnerType, [EntityType](enums/EntityType.md) Type, boolean OnlyEnemies ) {: .copyable aria-label='Functions' }

___

### Query·NPCs·Type () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityList](CppContainer_EntityList.md) QueryNPCsType ( [EntityType](enums/EntityType.md) Type, int Variant ) {: .copyable aria-label='Functions' }

___

### Reset·Path·Finder·Target () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ResetPathFinderTarget ( ) {: .copyable aria-label='Functions' }

___

### Throw·Spider () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### static const [EntityNPC](EntityNPC.md) ThrowSpider ( [Vector](Vector.md) Position, [Entity](Entity.md) Spawner, [Vector](Vector.md) TargetPos, boolean Big, float YOffset ) {: .copyable aria-label='Functions' }

___
## Variables

### Can·Shut·Doors {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanShutDoors  {: .copyable aria-label='Variables' }

___

### Child·NPC {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [EntityNPC](EntityNPC.md) ChildNPC  {: .copyable aria-label='Variables' data-altreturn='nil' }

___

### Entity·Ref {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) EntityRef {: .copyable aria-label='Variables' }

___

### Group·Idx {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int GroupIdx  {: .copyable aria-label='Variables' }
Used to identify multichunks groups.
___

### I1 {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int I1  {: .copyable aria-label='Variables' }

通常用于 AI 特定操作的通用用法 int。每个实体的效果和用法是手动定义的。对于某些实体，它也可能根本无法使用。

**Example**: 脆皮虫进入第二阶段时将 I2 设置为 1。
___

### I2 {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int I2  {: .copyable aria-label='Variables' }

通常用于 AI 特定操作的通用用法 int。每个实体的效果和用法是手动定义的。对于某些实体，它也可能根本无法使用。

**Example**: 脆皮虫进入第二阶段时将 I2 设置为 1。
___

### Parent·NPC {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [EntityNPC](EntityNPC.md) ParentNPC  {: .copyable aria-label='Variables' data-altreturn='nil' }

父实体，用于像 Larry Jr. 这样的多实体 NPC。
___

### Pathfinder {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [PathFinder](PathFinder.md) Pathfinder  {: .copyable aria-label='Variables' }

___

### Projectile·Cooldown {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ProjectileCooldown  {: .copyable aria-label='Variables' }

当 projectileCooldown 达到 0 时，弹幕可以再次发射
___

### Projectile·Delay {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ProjectileDelay  {: .copyable aria-label='Variables' }
&gt;0: projectile will be fired in n frames
___

### Scale {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Scale  {: .copyable aria-label='Variables' }

___

### State {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [NpcState](enums/NpcState.md) State  {: .copyable aria-label='Variables' }

___

### State·Frame {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int StateFrame  {: .copyable aria-label='Variables' }

___

### V1 {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) V1  {: .copyable aria-label='Variables' }

通常用于 AI 特定操作的通用用法 Vector。初始化为 Vector(0,0)。每个实体的效果和用法是手动定义的。对于某些实体，它也可能根本无法使用。
___

<div class="rgon-extension" markdown="1">

### V1 {: aria-label='Variables' }
#### [Vector](Vector.md) V1 [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
修复后的原函数现在能正确返回一个指向向量（Vector）的指针。

___

</div>

### V2 {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) V2  {: .copyable aria-label='Variables' }

通常用于 AI 特定操作的通用用法 Vector。初始化为 Vector(0,0)。每个实体的效果和用法是手动定义的。对于某些实体，它也可能根本无法使用。
___

<div class="rgon-extension" markdown="1">

### V2 {: aria-label='Variables' }
#### [Vector](Vector.md) V2 [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
修复后的原函数现在能正确返回一个指向向量（Vector）的指针。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

</div>

<div class="rgon-only" markdown="1">

### GetPathfinder () {: aria-label='Modified Functions' }
#### [Pathfinder](Pathfinder.md) GetPathfinder ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Returns a [Pathfinder](Pathfinder.md) class with fixed versions of its functions. This supersedes [EntityNPC.Pathfinder](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.html#pathfinder), which has been left as-is for compatibility with existing mods.

### ApplyTearflagEffects () {: aria-label='Functions' }
#### void ApplyTearflagEffects ( [Vector](Vector.md) Position, [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) TearFlags, [Entity](Entity.md) Source = nil, float Damage = 3.5 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
尝试将所提供 [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) 的命中效果应用于此敌人；如果提供了来源 [Entity](Entity.md)，效果将归因于该实体。

如果成功，还会触发 [MC_POST_APPLY_TEARFLAG_EFFECTS](enums/ModCallbacks.md#mc_post_apply_tearflag_effects)。

___

### ClearFlyingOverride () {: aria-label='Functions' }
#### void ClearFlyingOverride ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
移除 [SetFlyingOverride](EntityNPC.md#setflyingoverride) 设置的值。

___

### FireBossProjectilesEx () {: aria-label='Functions' }
#### [EntityProjectile](EntityProjectile.md)[] FireBossProjectilesEx ( int NumProjectiles, [Vector](Vector.md) TargetPos, float TrajectoryModifier, [ProjectileParams](https://wofsauge.github.io/IsaacDocs/rep/ProjectileParams.html) Params ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
与 [FireBossProjectiles](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.html#firebossprojectiles) 相同，但会返回包含已生成弹幕列表的表。

___

### FireGridEntity () {: aria-label='Functions' }
#### [EntityProjectile](EntityProjectile.md) FireGridEntity ( [Sprite](Sprite.md) GridEntitySprite, [GridEntityDesc](https://wofsauge.github.io/IsaacDocs/rep/GridEntityDesc.html) GridEntityDesc, [Vector](Vector.md) Velocity, [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html) Backdrop = BackdropType.BASEMENT ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### FireProjectilesEx () {: aria-label='Functions' }
#### [EntityProjectile](EntityProjectile.md)[] FireProjectilesEx ([Vector](Vector.md) Position, [Vector](Vector.md) Velocity, ProjectilesMode Mode, [ProjectileParams](https://wofsauge.github.io/IsaacDocs/rep/ProjectileParams.html) Params) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
与 [FireProjectiles](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.html#fireprojectiles) 相同，但会返回包含已生成弹幕列表的表。

___

### GetControllerId () {: aria-label='Functions' }
#### int GetControllerId ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回 NPC 的控制器 ID，表示当前由哪个玩家控制。未由任何玩家控制时返回 `-1`。

___

### GetDarkRedChampionRegenTimer () {: aria-label='Functions' }
#### int GetDarkRedChampionRegenTimer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDirtColor () {: aria-label='Functions' }
#### [Color](Color.md) GetDirtColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回实体的动态泥土颜色。这可以让像夜行者这样的实体融入环境。

___

### GetFireplaceLoot () {: aria-label='Functions' }
#### [LootList](LootList.md) GetFireplaceLoot ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回壁炉使用的唯一 [LootList](LootList.md)。

___

### GetFlyingOverride () {: aria-label='Functions' }
#### boolean GetFlyingOverride ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetHitList () {: aria-label='Functions' }
#### int[] GetHitList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回命中实体的数组，数组元素使用实体的 [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) 字段表示。

___

### GetShieldStrength () {: aria-label='Functions' }
#### float GetShieldStrength ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetShopkeeperLoot () {: aria-label='Functions' }
#### [LootList](LootList.md) GetShopkeeperLoot ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回店主使用的唯一 [LootList](LootList.md)。

___

### GetSirenPlayerEntity () {: aria-label='Functions' }
#### [EntityPlayer](EntityPlayer.md) GetSirenPlayerEntity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsBossColor () {: aria-label='Functions' }
#### boolean IsBossColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ReplaceSpritesheet () {: aria-label='Functions' }
#### boolean ReplaceSpritesheet ( int LayerId, string PngFilename, boolean LoadGraphics = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
类似于 [Sprite.ReplaceSpritesheet()](https://wofsauge.github.io/IsaacDocs/rep/Sprite.html#replacespritesheet)。如果可能的话，会在 `PngFilename` 后面追加 "_champion"/阶段后缀。

___

### SetControllerId () {: aria-label='Functions' }
#### int SetControllerId ( int ControllerId ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置 NPC 的控制器 ID，表示将由哪个玩家控制它。设为 `-1` 表示取消玩家控制并恢复正常行为。

___

### SetFlyingOverride () {: aria-label='Functions' }
#### void SetFlyingOverride ( boolean CanFly ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置对 IsFlying 返回值的覆盖；IsFlying 通常基于 [EntityGridCollisionClass](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityGridCollisionClass.html)。可用于让地面敌人忽略水迹，或让飞行敌人受到水迹影响。

___

### SetShieldStrength () {: aria-label='Functions' }
#### void SetShieldStrength ( float Strength ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ShootMaggotProjectile () {: aria-label='Functions' }
#### static const [EntityNPC](EntityNPC.md) ShootMaggotProjectile ( [Vector](Vector.md) Position, [Vector](Vector.md) Target, float FallingSpeed = -8.0, float YOffset = -24.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SpawnBloodCloud () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) SpawnBloodCloud ( [Vector](Vector.md) Position, [Color](Color.md) Color ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SpawnBloodSplash () {: aria-label='Functions' }
#### void SpawnBloodSplash ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ThrowLeech () {: aria-label='Functions' }
#### static const [EntityNPC](EntityNPC.md) ThrowLeech ( [Vector](Vector.md) Position, [Entity](Entity.md) Source, [Vector](Vector.md) Target, float YPosOffset = -10.0, boolean Big = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ThrowMaggot () {: aria-label='Functions' }
#### static const [EntityNPC](EntityNPC.md) ThrowMaggot ( [Vector](Vector.md) Origin, [Vector](Vector.md) Velocity, float YOffset = -10.0, float FallSpeed = -8.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ThrowMaggotAtPos () {: aria-label='Functions' }
#### static const [EntityNPC](EntityNPC.md) ThrowMaggotAtPos ( [Vector](Vector.md) Origin, [Vector](Vector.md) Target, float YOffset = -8.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ThrowRockSpider () {: aria-label='Functions' }
#### static const [EntityNPC](EntityNPC.md) ThrowRockSpider ( [Vector](Vector.md) Position, [Entity](Entity.md) Source, [Vector](Vector.md) Velocity, int Variant = 0, float YPosOffset = -10.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ThrowStrider () {: aria-label='Functions' }
#### static const [EntityNPC](EntityNPC.md) ThrowStrider ( [Vector](Vector.md) Position, [Entity](Entity.md) Source, [Vector](Vector.md) Target ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### TryForceTarget () {: aria-label='Functions' }
#### boolean TryForceTarget ( [Entity](Entity.md) Target, int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
由迷失苍蝇使用，用于强制该 NPC 专注于特定目标。

___

### TrySplit () {: aria-label='Functions' }
#### boolean TrySplit ( float DefaultDamage, [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, boolean DoScreenEffects = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将尝试像肉斧道具那样将敌人分裂成两个。如果敌人在分裂前因伤害死亡则返回 `false`，否则返回 `true`。

___

### TryThrow () {: aria-label='Functions' }
#### boolean TryThrow ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, [Vector](Vector.md) Direction, float Force ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Info"

    `Force` 仅适用于 NPC 便便（它会被修改，然后用作 V1.y，V1.x 为 -20.0），可能不准确。这需要进一步研究。

___

### UpdateDirtColor () {: aria-label='Functions' }
#### void UpdateDirtColor ( boolean Immediate ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
指示实体更新其泥土颜色。在原版实体中，这通常是自动完成的，但到目前为止，模组实体在这方面一直相当受限。
如果设置了 `Immediate`，泥土颜色将被设置为实体下方的确切颜色。否则，它将在多帧的过程中平滑更新。

___

</div>
