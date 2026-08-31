---
tags:
  - Class
---
> Documentation prose polished by a constrained language model; API facts and signatures retain their upstream source.

# Class "ColorParams"

???+ info
    This class can be accessed through its constructor:
    ???+ example "Example Code"
        ```lua
        local fiveSecondRedColor = ColorParams(Color(1,0,0,1),255,150,false,false)
        ```

## Constructors

<div class="rgon-only" markdown="1">

### ColorParams () {: aria-label='Constructors' }
#### [ColorParams](ColorParams.md) ColorParams ( [Color](Color.md) color, int priority, int duration1, int duration2, boolean fadeout, boolean shared ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constructors' }

___

## Functions

### GetColor () {: aria-label='Functions' }
#### [Color](Color.md) GetColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDuration () {: aria-label='Functions' }
#### int GetDuration ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Defines how long these parameters should last in update frames. This does not affect the number of frames remaining, but it does affect the fadeout speed (calculated as `Lifespan / Duration`) when `Fadeout` is enabled.

___

### GetFadeout () {: aria-label='Functions' }
#### boolean GetFadeout ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetLifespan () {: aria-label='Functions' }
#### int GetLifespan ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Defines how many update frames remain before these parameters expire. This value is decremented by `1` on each non-interpolation update, at a rate of `30` updates per second. Changing it directly affects how many frames remain before these parameters expire.

___

### GetPriority () {: aria-label='Functions' }
#### int GetPriority ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetShared () {: aria-label='Functions' }
#### boolean GetShared ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetColor () {: aria-label='Functions' }
#### void SetColor ( [Color](Color.md) Color ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetDuration () {: aria-label='Functions' }
#### void SetDuration ( int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetFadeout () {: aria-label='Functions' }
#### void SetFadeout ( boolean Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetLifespan () {: aria-label='Functions' }
#### void SetLifespan ( int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetPriority () {: aria-label='Functions' }
#### void SetPriority ( int Priority ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetShared () {: aria-label='Functions' }
#### void SetShared ( boolean Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>
