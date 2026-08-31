---
tags:
  - Class
---
# Class "EntityEffect"

???+ info
    You can get this class by using the following function:

    * [Entity.ToEffect()](Entity.md#toeffect)
    * [EntityNPC.MakeSplat()](EntityNPC.md#makesplat)

    ???+ example "Example Code"
        `local entity = Isaac.GetRoomEntities()[1]:ToEffect()`

## Class Diagram
--8<-- "en/snippets/EntityClassDiagram.md"
## Functions

### Follow·Parent () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void FollowParent ( [Entity](Entity.md) Parent ) {: .copyable aria-label='Functions' }

___

### Is·Player·Creep () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### static boolean IsPlayerCreep ( [EffectVariant](enums/EffectVariant.md) Variant ) {: .copyable aria-label='Functions' }

___

### Set·Damage·Source () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetDamageSource ( [EntityType](enums/EntityType.md) DamageSource ) {: .copyable aria-label='Functions' }

___

### Set·Radii () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetRadii ( float min, float max ) {: .copyable aria-label='Functions' }
For shockwaves.
___

### Set·Timeout () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetTimeout ( int Timeout ) {: .copyable aria-label='Functions' }

___
## Variables

### Damage·Source {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int DamageSource  {: .copyable aria-label='Variables' }

___

### Falling·Acceleration {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float FallingAcceleration  {: .copyable aria-label='Variables' }

___

### Falling·Speed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float FallingSpeed  {: .copyable aria-label='Variables' }

___

### Is·Following {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsFollowing  {: .copyable aria-label='Variables' }

___

### Life·Span {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int LifeSpan  {: .copyable aria-label='Variables' }

___

### m_Height {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float m_Height  {: .copyable aria-label='Variables' }
for particles .dy
___

### Max·Radius {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float MaxRadius  {: .copyable aria-label='Variables' }

___

### Min·Radius {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float MinRadius  {: .copyable aria-label='Variables' }
For shockwaves.
___

### Parent·Offset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) ParentOffset  {: .copyable aria-label='Variables' }
probably obsolete soon, in favor of m_SpriteOffset
___

### Rotation {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Rotation  {: .copyable aria-label='Variables' }

___

### Scale {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Scale  {: .copyable aria-label='Variables' }

___

### State {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int State  {: .copyable aria-label='Variables' }
state var, may be used ad lib initialized to 0 in Init()
___

### Timeout {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Timeout  {: .copyable aria-label='Variables' }

This is decremented on every frame, even for custom effects. Custom effects have this value initialized to -1.
___

<div class="rgon-only" markdown="1">

### CreateLight () {: aria-label='Functions' }
#### static [EntityEffect](EntityEffect.md) CreateLight ( [Vector](Vector.md) Position, float Scale = RandomFloat[0.0-1.0], int Lifespan = -1, int State = 6, [Color](Color.md) Color = Default) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ warning "Warning"
    This static function must be called via `EntityEffect.CreateLight`.

___

### CreateLootPreview () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) CreateLootPreview ( [Vector](Vector.md) Position, [EntityPickup](EntityPickup.md) Owner, [EntityEffect](EntityEffect.md) Effect ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### AddTearFlags () {: aria-label='Functions' }
#### void AddTearFlags ( [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Applicable effects only"
	Works only for `EffectVariant.PLAYER_CREEP_HOLYWATER_TRAIL`, `EffectVariant.BRIMSTONE_BALL`, `EffectVariant.TECH_DOT`, and `EffectVariant.CHAIN_LIGHTNING`.

___

### ClearTearFlags () {: aria-label='Functions' }
#### void ClearTearFlags ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Applicable effects only"
	Works only for `EffectVariant.PLAYER_CREEP_HOLYWATER_TRAIL`, `EffectVariant.BRIMSTONE_BALL`, `EffectVariant.TECH_DOT`, and `EffectVariant.CHAIN_LIGHTNING`.

___

### GetGridEntityDesc () {: aria-label='Functions' }
#### [GridEntityDesc](https://wofsauge.github.io/IsaacDocs/rep/GridEntityDesc.html) GetGridEntityDesc ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Applicable effects only"
	Works only for `EffectVariant.GRID_ENTITY_PROJECTILE_HELPER`.

___

### GetTearFlags () {: aria-label='Functions' }
#### [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) GetTearFlags ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Applicable effects only"
	Works only for `EffectVariant.PLAYER_CREEP_HOLYWATER_TRAIL`, `EffectVariant.BRIMSTONE_BALL`, `EffectVariant.TECH_DOT`, and `EffectVariant.CHAIN_LIGHTNING`.

___

### HasTearFlags () {: aria-label='Functions' }
#### boolean HasTearFlags ( [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Applicable effects only"
	Works only for `EffectVariant.PLAYER_CREEP_HOLYWATER_TRAIL`, `EffectVariant.BRIMSTONE_BALL`, `EffectVariant.TECH_DOT`, and `EffectVariant.CHAIN_LIGHTNING`.

___

### SetTearFlags () {: aria-label='Functions' }
#### void SetTearFlags ( [TearFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/TearFlags.html) ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Applicable effects only"
	Works only for `EffectVariant.PLAYER_CREEP_HOLYWATER_TRAIL`, `EffectVariant.BRIMSTONE_BALL`, `EffectVariant.TECH_DOT`, and `EffectVariant.CHAIN_LIGHTNING`.

___

</div>
