---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "AnimationData"

Cached data for one animation from a loaded ANM2 file. It is shared by all Sprites that use the same ANM2 and cannot be modified.

Can be obtained via [Sprite:GetAnimationData()](Sprite.md#getanimationdata), [Sprite:GetCurrentAnimationData()](Sprite.md#getanimationdata) or [Sprite:GetOverlayAnimationData()](Sprite.md#getanimationdata).

## Functions

<div class="rgon-only" markdown="1">

### GetAllLayers () {: aria-label='Functions' }
#### [AnimationLayer](AnimationLayer.md)[] GetAllLayers ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of AnimationLayers ordered from bottom to top (not by layer ID).

___

### GetLayer () {: aria-label='Functions' }
#### [AnimationLayer](AnimationLayer.md) GetLayer ( int LayerId ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets an AnimationLayer by its layer ID.

___

### GetLength () {: aria-label='Functions' }
#### int GetLength ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Length of this animation in frames.

___

### IsLoopingAnimation () {: aria-label='Functions' }
#### boolean IsLoopingAnimation ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetName () {: aria-label='Functions' }
#### string GetName ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
