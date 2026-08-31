---
tags:
  - Class
---
# Class "EntityNPC"

???+ info
    You can get this class by using the following function:

    * [Entity.ToNPC()](Entity.md#tonpc)
    * [Game.SpawnEntityDesc()](Game.md#spawnentitydesc)

    ???+ example "Example Code"
        `local entity = Isaac.GetRoomEntities()[1]:ToNPC()`

## Class Diagram
--8<-- "en/snippets/EntityClassDiagram.md"
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
fire a number of projectiles, optionally targeting the player direction is randomized, or slightly randomized when targeting the player FallingAccelModifier can be used to make projectiles fall faster to the ground returns a pointer to the projectile spawned last (useful e.g. when NumProjectiles=1)
___

### Fire·Projectiles () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void FireProjectiles ( [Vector](Vector.md) Pos, [Vector](Vector.md) Velocity, ProjectilesMode Mode, [ProjectileParams](ProjectileParams.md) Params ) {: .copyable aria-label='Functions' }

???- info "ProjectilesMode"
    * 0 : single projectile
    * 1 : two projectiles (uses params.Spread)
    * 2 : three projectiles (uses params.Spread)
    * 3 : three projectiles (uses params.Spread, more spread out?)
    * 4 : four projectiles (uses params.Spread)
    * 5 : five projectiles (uses params.Spread)
    * 6 : four projectiles in a + pattern (uses velocity.x as speed)
    * 7 : four projectiles in a x pattern (uses velocity.x as speed)
    * 8 : eight projectiles in a star pattern (uses velocity.x as speed)
    * 9 : N projectiles in a circle (velocity.x = speed, velocity.y = N, params.FireDirectionLimit and params.DotProductLimit to fire in an arc only)
___

### Get·Alive·Enemy·Count () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetAliveEnemyCount ( ) {: .copyable aria-label='Functions' }
Used to redirect close door enemies to any enemies for friendly npcs.
___

### Get·Boss·Color·Idx () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetBossColorIdx ( ) {: .copyable aria-label='Functions' }


???- note "Notes"
    This will return the boss color idx reduced by 1. To get the actual color as set in bosscolors.xml, add +1 to the result.
___

<div class="rgon-extension" markdown="1">

### GetBossColorIdx () {: aria-label='Functions' }
#### int GetBossColorIdx ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `bosscoloridx` (usually just the subtype), or `-1` if this is not a boss color or boss colors do not apply.

___

</div>

### Get·Champion·Color·Idx () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [ChampionColorIdx](enums/ChampionColor.md) GetChampionColorIdx ( ) {: .copyable aria-label='Functions' }

Returns the NPC's champion color index. Returns -1 if the NPC is not a champion.
___

### Get·Player·Target () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) GetPlayerTarget ( ) {: .copyable aria-label='Functions' }
if there are no modifiers (best friend) this will return the player
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
For entities with unique death animation, like Flush! vs poop enemies.
___

### Make·Champion () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void MakeChampion ( int Seed, ChampionColor ChampionColorIdx = -1, boolean Init = false ) {: .copyable aria-label='Functions' }
Forces a non champion to become a champion, resets hp to max hp.

**ChampionColorIdx**: The type of champion to turn this enemy into (-1 results in a random champion type)

**Init**: Set to true when called while initializing the enemy, false otherwise
___

### Make·Splat () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityEffect](EntityEffect.md) MakeSplat ( float Size ) {: .copyable aria-label='Functions' }

___

### Morph () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean Morph ( [EntityType](enums/EntityType.md) type, int Variant, int SubType, int ChampionColorIdx ) {: .copyable aria-label='Functions' }

Morph the current entity into another one. [ChampionColorIdx](https://bindingofisaacrebirth.gamepedia.com/Monsters#Champions) can be used to turn the entity into a champion. Use `:::lua -1` in order to not add a champion color.
A list of Champion colors can be found here : [ChampionColorIdx](https://bindingofisaacrebirth.gamepedia.com/Monsters#Champions)

???+ bug
    This function can not turn a champion NPC into a regular NPC! for that, use the following code:
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
All arguments besides `ID` are now optional.

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
General usage int for AI specific actions. The effect and usage is manually defined for each entity. It can also not be used at all for some.

**Example**: The Frail sets I2 to 1 when entering the second phase.
___

### I2 {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int I2  {: .copyable aria-label='Variables' }
General usage int for AI specific actions. The effect and usage is manually defined for each entity. It can also not be used at all for some.

**Example**: The Frail sets I2 to 1 when entering the second phase.
___

### Parent·NPC {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [EntityNPC](EntityNPC.md) ParentNPC  {: .copyable aria-label='Variables' data-altreturn='nil' }
parent entity, for multi-entity NPCs like Larry Jr.
___

### Pathfinder {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [PathFinder](PathFinder.md) Pathfinder  {: .copyable aria-label='Variables' }

___

### Projectile·Cooldown {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ProjectileCooldown  {: .copyable aria-label='Variables' }
projectiles can fire again when it reaches 0
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
General usage Vector for AI specific actions. Initialized to be Vector(0,0). The effect and usage is manually defined for each entity. It can also not be used at all for some.
___

<div class="rgon-extension" markdown="1">

### V1 {: aria-label='Variables' }
#### [Vector](Vector.md) V1 [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
Fix of original function that now correctly returns a pointer to the Vector.
___

</div>

### V2 {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) V2  {: .copyable aria-label='Variables' }
General usage Vector for AI specific actions. Initialized to be Vector(0,0). The effect and usage is manually defined for each entity. It can also not be used at all for some.
___

<div class="rgon-extension" markdown="1">

### V2 {: aria-label='Variables' }
#### [Vector](Vector.md) V2 [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
Fix of original function that now correctly returns a pointer to the Vector.
___

</div>

<div class="rgon-only" markdown="1">

### GetPathfinder () {: aria-label='Modified Functions' }
#### [Pathfinder](Pathfinder.md) GetPathfinder ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Returns a [Pathfinder](Pathfinder.md) class with fixed versions of its functions. This supersedes [EntityNPC.Pathfinder](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.html#pathfinder), which has been left as-is for compatibility with existing mods.

### ApplyTearflagEffects () {: aria-label='Functions' }
#### void ApplyTearflagEffects ( [Vector](Vector.md) Position, [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) TearFlags, [Entity](Entity.md) Source = nil, float Damage = 3.5 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Attempts to apply the on-hit effects of the provided [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) to this enemy, credited to the provided source [Entity](Entity.md), if any.

Will also trigger [MC_POST_APPLY_TEARFLAG_EFFECTS](enums/ModCallbacks.md#mc_post_apply_tearflag_effects) if successful.

___

### ClearFlyingOverride () {: aria-label='Functions' }
#### void ClearFlyingOverride ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Removes any value set by [SetFlyingOverride](EntityNPC.md#setflyingoverride)

___

### FireBossProjectilesEx () {: aria-label='Functions' }
#### [EntityProjectile](EntityProjectile.md)[] FireBossProjectilesEx ( int NumProjectiles, [Vector](Vector.md) TargetPos, float TrajectoryModifier, [ProjectileParams](https://wofsauge.github.io/IsaacDocs/rep/ProjectileParams.html) Params ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Same as [FireBossProjectiles](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.html#firebossprojectiles), but returns a table containing the list of spawned projectiles.

___

### FireGridEntity () {: aria-label='Functions' }
#### [EntityProjectile](EntityProjectile.md) FireGridEntity ( [Sprite](Sprite.md) GridEntitySprite, [GridEntityDesc](https://wofsauge.github.io/IsaacDocs/rep/GridEntityDesc.html) GridEntityDesc, [Vector](Vector.md) Velocity, [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html) Backdrop = BackdropType.BASEMENT ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### FireProjectilesEx () {: aria-label='Functions' }
#### [EntityProjectile](EntityProjectile.md)[] FireProjectilesEx ([Vector](Vector.md) Position, [Vector](Vector.md) Velocity, ProjectilesMode Mode, [ProjectileParams](https://wofsauge.github.io/IsaacDocs/rep/ProjectileParams.html) Params) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Same as [FireProjectiles](https://wofsauge.github.io/IsaacDocs/rep/EntityNPC.html#fireprojectiles), but returns a table containing the list of spawned projectiles.

___

### GetControllerId () {: aria-label='Functions' }
#### int GetControllerId ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the ControllerId for the NPC, which indicates which player is controlling it. Will return `-1` when not being controlled by any player.

___

### GetDarkRedChampionRegenTimer () {: aria-label='Functions' }
#### int GetDarkRedChampionRegenTimer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDirtColor () {: aria-label='Functions' }
#### [Color](Color.md) GetDirtColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the dynamic dirt color of the entity. This lets entities like Nightcrawler blend in to the environment.

___

### GetFireplaceLoot () {: aria-label='Functions' }
#### [LootList](LootList.md) GetFireplaceLoot ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the unique [LootList](LootList.md) used by Fireplaces.

___

### GetFlyingOverride () {: aria-label='Functions' }
#### boolean GetFlyingOverride ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetHitList () {: aria-label='Functions' }
#### int[] GetHitList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.

___

### GetShieldStrength () {: aria-label='Functions' }
#### float GetShieldStrength ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetShopkeeperLoot () {: aria-label='Functions' }
#### [LootList](LootList.md) GetShopkeeperLoot ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the unique [LootList](LootList.md) used by Shopkeepers.

___

### GetSirenPlayerEntity () {: aria-label='Functions' }
#### [EntityPlayer](EntityPlayer.md) GetSirenPlayerEntity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsBossColor () {: aria-label='Functions' }
#### boolean IsBossColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ReplaceSpritesheet () {: aria-label='Functions' }
#### boolean ReplaceSpritesheet ( int LayerId, string PngFilename, boolean LoadGraphics = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Similar to [Sprite.ReplaceSpritesheet()](https://wofsauge.github.io/IsaacDocs/rep/Sprite.html#replacespritesheet). Appends "_champion"/stage suffix to `PngFilename` if possible.

___

### SetControllerId () {: aria-label='Functions' }
#### int SetControllerId ( int ControllerId ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the ControllerId for the NPC, which indicates which player will control it. Set it to `-1` to remove player control and restore normal behavior.

___

### SetFlyingOverride () {: aria-label='Functions' }
#### void SetFlyingOverride ( boolean CanFly ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets an override to the return value of IsFlying, which is normally based on [EntityGridCollisionClass](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityGridCollisionClass.html). Can be used to make grounded enemies ignore creep, or flying enemies get hit by creep.

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
Used by Lost Fly to force this NPC to focus on a specific target.

___

### TrySplit () {: aria-label='Functions' }
#### boolean TrySplit ( float DefaultDamage, [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, boolean DoScreenEffects = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Will attempt to split the enemy in two like the Meat Cleaver collectible. Returns `false` if the enemy dies from the damage before they split, `true` otherwise.

___

### TryThrow () {: aria-label='Functions' }
#### boolean TryThrow ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, [Vector](Vector.md) Direction, float Force ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "Info"
    `Force` only applies to NPC poop (it's modified and then used as V1.y, with V1.x being -20.0) and may be incorrect. This needs further investigation.

___

### UpdateDirtColor () {: aria-label='Functions' }
#### void UpdateDirtColor ( boolean Immediate ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Instructs the entity to update its dirt color. This is generally done automatically on vanilla entities, but up until now, modded ones have been quite limited in this regard.

If `Immediate` is set, the dirt color will be set to exactly what is beneath the entity. Otherwise, it will be updated smoothly over the course of multiple frames.

___

## Variables

</div>
