---
tags:
  - Global
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Global Class "EntityConfig"

???+ info
    These functions are available through the `EntityConfig` global table.

    **Note that to call these functions, you must use a `.` (period) instead of a `:` (colon)!**

    ???+ example "Example Code"
        ```lua
        local gaperConfig = EntityConfig.GetEntity(EntityType.ENTITY_GAPER)
        ```
        
## Functions

<div class="rgon-only" markdown="1">

### GetBaby () {: aria-label='Functions' }
#### [EntityConfigBaby](EntityConfigBaby.md) GetBaby ( [BabySubType](https://wofsauge.github.io/IsaacDocs/rep/enums/BabySubType.html) Type ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns nil if no co-op baby exists with the specified ID.

___

### GetEntity () {: aria-label='Functions' }
#### [EntityConfigEntity](EntityConfigEntity.md) GetEntity ( [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, int Variant = -1, int SubType = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns nil if no entity exists with the specified type.

Providing Variant and/or SubType is optional. If a non-existent Variant/SubType is requested, the base version of that entity is returned.

___

### GetMaxBabyID () {: aria-label='Functions' }
#### int GetMaxBabyID ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the highest ID (corresponding to SubType) currently assigned to a valid co-op baby.

___

### GetMaxPlayerType () {: aria-label='Functions' }
#### int GetMaxPlayerType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the highest PlayerType currently assigned to a valid character.

___

### GetPlayer () {: aria-label='Functions' }
#### [EntityConfigPlayer](EntityConfigPlayer.md) GetPlayer ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) PlayerType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns nil if no character exists with the specified PlayerType.

___

</div>
