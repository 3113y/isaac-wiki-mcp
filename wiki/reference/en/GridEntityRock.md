---
tags:
  - Class
---
# Class "GridEntityRock"

???+ info
    You can get this class by using the following function:

    * [GridEntity.ToRock()](GridEntity.md#torock)

    ???+ example "Example Code"
        `Game():GetRoom():GetGridEntity(25):ToRock()`

## Class Diagram
--8<-- "en/snippets/GridEntityClassDiagram.md"
## Functions

### Get·Big·Rock·Frame () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetBigRockFrame ( ) {: .copyable aria-label='Functions' }

___

### Get·Rubble·Anim () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### string GetRubbleAnim ( ) {: .copyable aria-label='Functions' }

___

### Get·Sprite () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Sprite](Sprite.md) GetSprite ( ) {: .copyable aria-label='Functions' }
Same as the Repentance exclusive function [GetSprite()](GridEntity.md#getsprite).

___

### Set·Big·Rock·Frame () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetBigRockFrame ( int Frame ) {: .copyable aria-label='Functions' }

___

### Update·Anim·Frame () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void UpdateAnimFrame ( ) {: .copyable aria-label='Functions' }

___
## Variables

### Anim {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### string Anim  {: .copyable aria-label='Variables' }

___

### Frame·Cnt {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int FrameCnt  {: .copyable aria-label='Variables' }

___

### Rubble·Anim {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### string RubbleAnim  {: .copyable aria-label='Variables' }

___

<div class="rgon-only" markdown="1">

### GetAltRockType () {: aria-label='Functions' }
#### int GetAltRockType ( [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html) Backdrop = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### PlayBreakSound () {: aria-label='Functions' }
#### void PlayBreakSound ( [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type, [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html) Backdrop = 0 ) {: .copyable aria-label='Functions' }     [ ](#){: .rgonorplus .tooltip .badge }

___

### RegisterRockDestroyed () {: aria-label='Functions' }
#### void RegisterRockDestroyed ( [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### RenderTop () {: aria-label='Functions' }
#### void RenderTop ( [Vector](Vector.md) Offset ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SpawnDrops () {: aria-label='Functions' }
#### static void SpawnDrops ( [Vector](Vector.md) Position, [GridEntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/GridEntityType.html) Type, int GridVariant, int Seed, boolean Unknown, [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html) Backdrop = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### TrySpawnLadder () {: aria-label='Functions' }
#### void TrySpawnLadder ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### TrySpawnWorms () {: aria-label='Functions' }
#### void TrySpawnWorms ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### UpdateCollision () {: aria-label='Functions' }
#### void UpdateCollision ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### UpdateNeighbors () {: aria-label='Functions' }
#### void UpdateNeighbors ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
If the rock is currently "connected" to other rocks as part of a "big rock," this function breaks its connections to its neighbors. The neighboring rocks' graphics are updated appropriately, but this rock's graphics are not updated.

The game calls this function when a rock is destroyed or lifted. For the function to succeed, the rock must still have the appropriate Variant for a big rock (1000+).

___

</div>
