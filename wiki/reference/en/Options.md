---
tags:
  - Globals
  - Class
---
# Global Class "Options"

???+ info
    You can get this class by using the `Options` global table.

    The `Options` class represents the values contained within the user's `options.ini` file. For example, this is useful so that mods that add things to the HUD can properly account for the `HUDOffset`.

    Note that mods have free reign to modify these values, so it is possible for a mod to e.g. change the volume to max and play sound effects. Please use this class responsibly.

    The `Options` class is a singleton that is exposed as a global variable. Thus, you can directly get and set values in the class without having to do anything first:

    ???+ example "Example Code"
        ```lua
        local bulletVisibility = Options.BulletVisibility -- "bulletVisibility" is now set to true or false
        Options.ChargeBars = true -- Force charge bars to be on for the player
        ```

## Variables

### Announcer·Voice·Mode {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int AnnouncerVoiceMode  {: .copyable aria-label='Variables' }
0: random, 1: off, 2: always on

___

### Bullet·Visibility {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean BulletVisibility  {: .copyable aria-label='Variables' }

___

### Camera·Style {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int CameraStyle  {: .copyable aria-label='Variables' }
active cam 1: on, 2: off

___

### Charge·Bars {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean ChargeBars  {: .copyable aria-label='Variables' }

___

### Console·Font {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int ConsoleFont  {: .copyable aria-label='Variables' }
0: default, 1: small, 2: tiny

___

### Debug·Console·Enabled {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean DebugConsoleEnabled  {: .copyable aria-label='Variables' }

___

### Display·Popups {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean DisplayPopups  {: .copyable aria-label='Variables' }

___

### Extra·HUD·Style {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int ExtraHUDStyle  {: .copyable aria-label='Variables' }
0: off, 1: on, 2: mini

___

### Faded·Console·Display {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean FadedConsoleDisplay  {: .copyable aria-label='Variables' }

___

### Filter {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean Filter  {: .copyable aria-label='Variables' }

___

### Found·HUD {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean FoundHUD  {: .copyable aria-label='Variables' }

___

### Fullscreen {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean Fullscreen  {: .copyable aria-label='Variables' }

___

### Gamma {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### float Gamma  {: .copyable aria-label='Variables' }
0.5-1.5

___

### HUD·Offset {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### float HUDOffset  {: .copyable aria-label='Variables' }
0-1

Each notch in the options menu increments or decrements this by 0.1.

___

### JacobEsauControls {: aria-label='Variables' }
[ ](#){: .repplus .tooltip .badge }
#### string JacobEsauControls  {: .copyable aria-label='Variables' }
Added with Repentance+.

___

### Language {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### string Language  {: .copyable aria-label='Variables' }
Read only

___

### Map·Opacity {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### float MapOpacity  {: .copyable aria-label='Variables' }
0-1

___

### Max·Render·Scale {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int MaxRenderScale  {: .copyable aria-label='Variables' }
1-99

___

### Max·Scale {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int MaxScale  {: .copyable aria-label='Variables' }
1-99

___

### Mouse·Control {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean MouseControl  {: .copyable aria-label='Variables' }

___

### Music·Volume {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### float MusicVolume  {: .copyable aria-label='Variables' }
0-1

Attempting to set this to anything other than 0 or 1 will result in a bugged value. Thus, mods should never set this, lest they permanently blow away the end-user's previous setting.

___

### Pause·On·Focus·Lost {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean PauseOnFocusLost  {: .copyable aria-label='Variables' }

___

### Rumble·Enabled {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean RumbleEnabled  {: .copyable aria-label='Variables' }

___

### Save·Command·History {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean SaveCommandHistory  {: .copyable aria-label='Variables' }

___

### SFX·Volume {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### float SFXVolume  {: .copyable aria-label='Variables' }
0-1

Attempting to set this to anything other than 0 or 1 will result in a bugged value. Thus, mods should never set this, lest they permanently blow away the end-user's previous setting.

___

<div class="rgon-extension" markdown="1">

### SFXVolume {: aria-label='Modified Variables' }
#### float SFXVolume [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Variables' }
Can now be set correctly. New values are clamped to one decimal place so that adjusting the volume in the options menu does not produce invalid values.
___
## Variables

</div>

### Use·Borderless·Fullscreen {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean UseBorderlessFullscreen  {: .copyable aria-label='Variables' }
Only takes effect if Fullscreen is also true.

___

### VSync {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean VSync  {: .copyable aria-label='Variables' }

___

<div class="rgon-only" markdown="1">

### AimLockEnabled {: aria-label='Variables'}
#### boolean AimLockEnabled [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### AscentVoiceOver {: aria-label='Variables'}
#### boolean AscentVoiceOver [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### BetterVoidGeneration {: aria-label='Variables' }
#### boolean BetterVoidGeneration [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
If enabled, The Void draws from all unlocked floors, including floors on alternate paths.

___

### BossHPOnBottom {: aria-label='Variables'}
#### boolean BossHPOnBottom [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### Brightness {: aria-label='Variables'}
#### float Brightness [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### Contrast {: aria-label='Variables'}
#### float Contrast [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### Exposure {: aria-label='Variables'}
#### float Exposure [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### HushPanicStateFix {: aria-label='Variables' }
#### boolean HushPanicStateFix [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
Fixes a vanilla bug that causes Hush to have no attack cooldown below 50% health.

___

### KeyMasterDealChance {: aria-label='Variables' }
#### boolean KeyMasterDealChance [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
If enabled, killing Key Master bums also increases the chance of a deal.

___

### OnlineChatEnabled {: aria-label='Variables'}
#### boolean OnlineChatEnabled [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
(read-only)

___

### OnlineChatFilterEnabled {: aria-label='Variables'}
#### boolean OnlineChatFilterEnabled [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
(read-only)

___

### OnlineColorSet {: aria-label='Variables'}
#### int OnlineColorSet [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
(read-only)

___

### OnlineHUD {: aria-label='Variables'}
#### int OnlineHUD [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
(read-only)

___

### OnlineInputDelay {: aria-label='Variables'}
#### int OnlineInputDelay [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
(read-only)

___

### OnlinePlayerOpacity {: aria-label='Variables'}
#### int OnlinePlayerOpacity [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
(read-only)

___

### OnlinePlayerVolume {: aria-label='Variables'}
#### int OnlinePlayerVolume [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
(read-only)

___

### PreventModUpdates {: aria-label='Variables' }
#### boolean PreventModUpdates [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
(read-only)

___

### QuickRoomClear {: aria-label='Variables' }
#### boolean QuickRoomClear [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### StatHUDPlanetarium {: aria-label='Variables' }
#### boolean StatHUDPlanetarium [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
If enabled, natively displays the Planetarium chance on the HUD.

Note that this option has no effect if Planetariums are not unlocked. Therefore, checking this value alone is insufficient to determine whether the Planetarium HUD is being rendered.

___

### StreamerMode {: aria-label='Variables'}
#### boolean StreamerMode [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }
(read-only)

___

### TouchMode {: aria-label='Variables'}
#### int TouchMode [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### WindowHeight {: aria-label='Variables'}
#### int WindowHeight [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### WindowPosX {: aria-label='Variables'}
#### int WindowPosX [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### WindowPosY {: aria-label='Variables'}
#### int WindowPosY [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

### WindowWidth {: aria-label='Variables'}
#### int WindowWidth [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Variables' }

___

</div>
