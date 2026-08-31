---
tags:
  - Class
---
# Class "RoomConfigStage"

???+ info
    你可以通过以下函数获取此类:

    - [RoomConfig.GetStage()](RoomConfig.md#getstage)
    
    ???+ example "Example Code"
        ```lua
        local roomConfigStage = RoomConfig.GetStage(StbType.BASEMENT)
        ```

## Functions

<div class="rgon-only" markdown="1">

### GetBackdrop () {: aria-label='Functions' }
#### [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html?h=backdrop) GetBackdrop ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回该舞台默认房间使用的 `BackdropType`。

### GetBossSpot () {: aria-label='Functions' }
#### string GetBossSpot ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回 Boss 开场动画中使用的 Boss 位置精灵路径。

### GetDisplayName () {: aria-label='Functions' }
#### string GetDisplayName ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回舞台名称。

___

### GetXMLName () {: aria-label='Functions' }
#### string GetXMLName ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsLoaded () {: aria-label='Functions' }
#### boolean IsLoaded ( int mode = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBackdrop () {: aria-label='Functions' }
#### void SetBackdrop ( [BackdropType](https://wofsauge.github.io/IsaacDocs/rep/enums/BackdropType.html?h=backdrop) Backdrop ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置该舞台默认房间使用的 `BackdropType`。

### SetBossSpot () {: aria-label='Functions' }
#### void SetBossSpot ( string PngFilename ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置 Boss 开场动画中使用的 Boss 位置精灵路径。

### SetDisplayName () {: aria-label='Functions' }
#### void SetDisplayName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置舞台名称。

### SetMusic () {: aria-label='Functions' }
#### void SetMusic ( [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html?h=music) Music ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置该舞台默认房间使用的 `Music`。

### SetPlayerSpot () {: aria-label='Functions' }
#### void SetPlayerSpot ( string PngFilename ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置 Boss 开场动画和梦魇过渡中使用的玩家位置精灵路径。

### SetSuffix () {: aria-label='Functions' }
#### void SetSuffix ( string Suffix ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置该舞台用于舞台专属精灵的后缀，例如 Boss/玩家位置精灵以及敌人的专属变体。

___

### SetXMLName () {: aria-label='Functions' }
#### void SetXMLName ( string name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### Unload () {: aria-label='Functions' }
#### void Unload ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetID () {: aria-label='Functions' }
#### int GetID ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMusic () {: aria-label='Functions' }
#### [Music](https://wofsauge.github.io/IsaacDocs/rep/enums/Music.html?h=music) GetMusic ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the `Music` used by default rooms on the stage.

___

### GetPlayerSpot () {: aria-label='Functions' }
#### string GetPlayerSpot ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the sprite path for the player spot used in the boss intro and nightmare transition.

___

### GetRoomSet () {: aria-label='Functions' }
#### [RoomConfigSet](CcpContainer_RoomConfigSet.md) GetRoomSet ( int Mode ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a [RoomConfigSet](CcpContainer_RoomConfigSet.md) containing every [RoomConfigRoom](https://wofsauge.github.io/IsaacDocs/rep/RoomConfig_Room.html) in the stage.

`Mode` is `0` for Normal Mode and `1` for Greed Mode.
___

### GetSuffix () {: aria-label='Functions' }
#### string GetSuffix ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the suffix used by the stage for stage-specific sprites, such as the boss/player spot and unique enemy variants.

___

</div>
