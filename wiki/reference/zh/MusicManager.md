---
tags:
  - Globals
  - Class
---
# Class "MusicManager"

???+ info
    This class can be accessed by using its constructor:

    ???+ example "Example Code"
        ```lua
        local musicManager = MusicManager()
        ```

## Constructors

### Music·Manager () {: aria-label='Constructors' }
[ ](#){: .alldlc .tooltip .badge }
#### [MusicManager](MusicManager.md) MusicManager ( ) {: .copyable aria-label='Constructors' }

Returns a [MusicManager](MusicManager.md) object.

???- example "Example Code"
    Example usage:
    ```lua
    MusicManager():Disable()

    ```
___
## Functions

### Crossfade () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void Crossfade ( [Music](enums/Music.md) ID, float FadeRate = 0.08 ) {: .copyable aria-label='Functions' }
???+ bug "Bug"
    If the ID parameter is negative or falls out of the allowed range of music IDs, this function will crash the game.

___

<div class="rgon-extension" markdown="1">

### Crossfade () {: aria-label='Modified Functions' }
#### void Crossfade ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) MusicId, float FadeRate = 0.08 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
现在会验证音乐 ID，以避免崩溃。

</div>

### Disable () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Disable ( ) {: .copyable aria-label='Functions' }

___

### Disable·Layer () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void DisableLayer ( int LayerId = 0 ) {: .copyable aria-label='Functions' }

___

### Enable () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Enable ( ) {: .copyable aria-label='Functions' }

___

### Enable·Layer () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void EnableLayer ( int LayerId = 0, boolean Instant = false ) {: .copyable aria-label='Functions' }

___

### Fadein () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void Fadein ( [Music](enums/Music.md) ID, float Volume = 1, float FadeRate = 0.08 ) {: .copyable aria-label='Functions' }

___

<div class="rgon-extension" markdown="1">

### Fadein () {: aria-label='Modified Functions' }
#### void Fadein ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) MusicId, float Volume = 1, float Volume = 0.08 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
现在会验证音乐 ID，以避免崩溃。

</div>

### Fadeout () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void Fadeout ( float FadeRate = 0.08 ) {: .copyable aria-label='Functions' }

___

### Get·Current·Music·ID () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Music](enums/Music.md) GetCurrentMusicID ( ) {: .copyable aria-label='Functions' }

___

### Get·Queued·Music·ID () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Music](enums/Music.md) GetQueuedMusicID ( ) {: .copyable aria-label='Functions' }
if nothing is queued, return the current music id
___

### Is·Enabled () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsEnabled ( ) {: .copyable aria-label='Functions' }

___

### Is·Layer·Enabled () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean IsLayerEnabled ( int LayerId = 0 ) {: .copyable aria-label='Functions' }

___

### Pause () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Pause ( ) {: .copyable aria-label='Functions' }

___

### Pitch·Slide () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PitchSlide ( float TargetPitch ) {: .copyable aria-label='Functions' }

___

### Play () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Play ( [Music](enums/Music.md) ID, float Volume = 1 ) {: .copyable aria-label='Functions' }
???+ bug "Bug"
    If the ID parameter is negative or falls out of the allowed range of music IDs, this function will crash the game.

___

<div class="rgon-extension" markdown="1">

### Play () {: aria-label='Modified Functions' }
#### void Play ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) MusicId, int Volume = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
现在会验证音乐 ID，以避免崩溃。

</div>

### Queue () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Queue ( [Music](enums/Music.md) ID ) {: .copyable aria-label='Functions' }

___

### Reset·Pitch () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ResetPitch ( ) {: .copyable aria-label='Functions' }

___

### Resume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Resume ( ) {: .copyable aria-label='Functions' }

___

### Update·Volume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void UpdateVolume ( ) {: .copyable aria-label='Functions' }

This function sets the music volume to the volume defined in the options menu.
___

### Volume·Slide () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void VolumeSlide ( float TargetVolume, float FadeRate = 0.08 ) {: .copyable aria-label='Functions' }

___

<div class="rgon-only" markdown="1">

### GetCurrentPitch () {: aria-label='Functions' }
#### float GetCurrentPitch ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### PlayJingle () {: aria-label='Functions' }
#### void PlayJingle ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) MusicId, int Duration = 140 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetCurrentPitch () {: aria-label='Functions' }
#### void SetCurrentPitch ( float Pitch ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### StopJingle () {: aria-label='Functions' }
#### void StopJingle ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCurrentJingleID () {: aria-label='Functions' }
#### [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html) GetCurrentJingleID ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the ID of the currently playing jingle, or 0 if no jingle is playing or the current jingle is fading out.

___

</div>
