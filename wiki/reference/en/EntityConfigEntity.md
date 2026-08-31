---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "EntityConfigEntity"

???+ info
    You can obtain this class through the following function:

    * [EntityConfig.GetEntity()](EntityConfig.md#getentity)

    ???+ example "Example Code"
        ```lua
        local gaperConfig = EntityConfig.GetEntity(EntityType.ENTITY_GAPER)
        ```
        
## Functions

<div class="rgon-only" markdown="1">

### CanBeChampion () {: aria-label='Functions' }
#### boolean CanBeChampion ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CanBeRerolledInto () {: aria-label='Functions' }
#### boolean CanBeRerolledInto ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CanShutDoors () {: aria-label='Functions' }
#### boolean CanShutDoors ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetAnm2Path () {: aria-label='Functions' }
#### string GetAnm2Path ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBaseHP () {: aria-label='Functions' }
#### float GetBaseHP ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBestiaryAnimation () {: aria-label='Functions' }
#### string GetBestiaryAnimation ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBestiaryAnm2Path () {: aria-label='Functions' }
#### string GetBestiaryAnm2Path ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBestiaryFloorAlt () {: aria-label='Functions' }
#### string GetBestiaryFloorAlt ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBestiaryOffset () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetBestiaryOffset ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBestiaryOverlay () {: aria-label='Functions' }
#### string GetBestiaryOverlay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBestiaryScale () {: aria-label='Functions' }
#### float GetBestiaryScale ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBossID () {: aria-label='Functions' }
#### [BossType](enums/BossType.md) GetBossID ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollisionDamage () {: aria-label='Functions' }
#### float GetCollisionDamage ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollisionInterval () {: aria-label='Functions' }
#### int GetCollisionInterval ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollisionRadius () {: aria-label='Functions' }
#### float GetCollisionRadius ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Also known as “Size”.

___

### GetCollisionRadiusMultiplier () {: aria-label='Functions' }
#### [const Vector](Vector.md) GetCollisionRadiusMultiplier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Also known as “SizeMulti”.

___

### GetCustomTags () {: aria-label='Functions' }
#### table GetCustomTags ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table containing all strings specified in the entity's `customtags` attribute in [entities2.xml](xml/entities.md). Tags are always returned in lowercase. See [entities2.xml](xml/entities.md) for more information about `customtags`.

___

### GetDevolvedEntity () {: aria-label='Functions' }
#### [EntityConfigEntity](EntityConfigEntity.md) GetDevolvedEntity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the [EntityConfigEntity](EntityConfigEntity.md) that this entity would "devolve" into when D10 is used.

Returns nil if the entity has no devolution and would die instead.

___

### GetEntityTags () {: aria-label='Functions' }
#### int GetEntityTags ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the bitmask of [EntityTag](enums/EntityTag.md)s for this entity.

___

### GetFriction () {: aria-label='Functions' }
#### float GetFriction ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetGibFlags () {: aria-label='Functions' }
#### int GetGibFlags ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the bitmask of [GibFlag](enums/GibFlag.md)s for this entity.

___

### GetGibsAmount () {: aria-label='Functions' }
#### int GetGibsAmount ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetGridCollisionPoints () {: aria-label='Functions' }
#### int GetGridCollisionPoints ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMass () {: aria-label='Functions' }
#### float GetMass ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetModName () {: aria-label='Functions' }
#### string GetModName ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the name of the mod that the entity comes from. Returns nil for vanilla entities.

___

### GetName () {: aria-label='Functions' }
#### string GetName ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPortraitID () {: aria-label='Functions' }
#### int GetPortraitID ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetShadowSize () {: aria-label='Functions' }
#### float GetShadowSize ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Note that this value is the `shadowSize` specified in the XML, divided by 100.

___

### GetShieldStrength () {: aria-label='Functions' }
#### float GetShieldStrength ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the amount of armor the entity has.

___

### GetStageHP () {: aria-label='Functions' }
#### float GetStageHP ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSubType () {: aria-label='Functions' }
#### int GetSubType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetType () {: aria-label='Functions' }
#### int GetType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetVariant () {: aria-label='Functions' }
#### int GetVariant ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### HasCustomTag () {: aria-label='Functions' }
#### boolean HasCustomTag ( string tag ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if the entity's `customtags` attribute in [entities2.xml](xml/entities.md) contains the provided string. The check is case-insensitive. See [entities2.xml](xml/entities.md) for more information about `customtags`.

___

### HasEntityTags () {: aria-label='Functions' }
#### boolean HasEntityTags ( int Tags ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if the entity has all [EntityTag](enums/EntityTag.md) values specified in the provided bitset.

___

### HasFloorAlts () {: aria-label='Functions' }
#### boolean HasFloorAlts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### HasGibFlags () {: aria-label='Functions' }
#### boolean HasGibFlags ( int Flags ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if the entity has all [GibFlag](enums/GibFlag.md) values specified in the provided bitset.

___

### IsBoss () {: aria-label='Functions' }
#### boolean IsBoss ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
