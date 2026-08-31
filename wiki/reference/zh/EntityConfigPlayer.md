---
tags:
  - Class
---
# Class "EntityConfigPlayer"

???+ info

    可以通过以下函数获取此类：

    * [EntityConfig.GetPlayer()](EntityConfig.md#getplayer)

    ???+ example "Example Code"

        ```lua
        local cainConfig = EntityConfig.GetPlayer(PlayerType.PLAYER_CAIN)
        ```
        
## Functions

<div class="rgon-only" markdown="1">

### CanShoot () {: aria-label='Functions' }
#### boolean CanShoot ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetAchievementID () {: aria-label='Functions' }
#### [Achievement](enums/Achievement.md) GetAchievementID ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果角色未受原版成就锁定，则返回 -1；如果是“隐藏”的原版角色，则返回 -2。

___

### GetBirthrightDescription () {: aria-label='Functions' }
#### string GetBirthrightDescription ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBlackHearts () {: aria-label='Functions' }
#### int GetBlackHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBombs () {: aria-label='Functions' }
#### int GetBombs ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBrokenHearts () {: aria-label='Functions' }
#### int GetBrokenHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCard () {: aria-label='Functions' }
#### [Card](https://wofsauge.github.io/IsaacDocs/rep/enums/Card.html) GetCard ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
不包括通过解锁获得的起始卡牌；

也不包括模组添加的卡牌。

如果角色没有任何原版起始卡牌，则返回 0。

___

### GetCoins () {: aria-label='Functions' }
#### int GetCoins ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollectibles () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)[] GetCollectibles ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个包含角色起始物品的表，其中元素类型为 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)。

___

### GetCostumeID () {: aria-label='Functions' }
#### int GetCostumeID ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果角色没有通过 XML 定义的起始服装（如玛吉的头发），则返回 -1。

___

### GetCostumeSuffix () {: aria-label='Functions' }
#### string GetCostumeSuffix ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于角色特定服装精灵图的目录后缀。

___

### GetExtraPortraitPath () {: aria-label='Functions' }
#### string GetExtraPortraitPath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
指向一个 `.anm2` 文件的路径，该文件显示在角色的关卡过渡和 Boss 对战屏幕肖像之上。

___

### GetKeys () {: aria-label='Functions' }
#### int GetKeys ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetModdedControlsSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedControlsSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回用于模组角色起始房间控制界面的精灵图。

请注意，此精灵图由同一模组中的其他角色共享——其中存在一个与该角色同名的动画。

对于原版角色或没有相应动画的角色，返回 nil。

___

### GetModdedCoopMenuSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedCoopMenuSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回用于模组角色在合作角色选择轮中的图标的精灵图。

请注意，此精灵图由同一模组中的其他角色共享——其中存在一个与该角色同名的动画。

对于原版角色或没有相应动画的角色，返回 nil。

___

### GetModdedGameOverSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedGameOverSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回用于模组角色游戏结束屏幕（即其名字）的精灵图。

请注意，此精灵图由同一模组中的其他角色共享——其中存在一个与该角色同名的动画。

对于原版角色或没有相应动画的角色，返回 nil。

___

### GetModdedMenuBackgroundSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedMenuBackgroundSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回用于模组角色角色选择屏幕的精灵图。

请注意，此精灵图由同一模组中的其他角色共享——其中存在一个与该角色同名的动画。

对于原版角色或没有相应动画的角色，返回 nil。

___

### GetModdedMenuPortraitSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetModdedMenuPortraitSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回用于模组角色角色选择肖像的精灵图。

请注意，此精灵图由同一模组中的其他角色共享——其中存在一个与该角色同名的动画。

对于原版角色或没有相应动画的角色，返回 nil。

___

### GetName () {: aria-label='Functions' }
#### string GetName ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetNameImagePath () {: aria-label='Functions' }
#### string GetNameImagePath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
指向用于 Boss 对战屏幕上角色名字的 PNG 文件的路径。

___

### GetPill () {: aria-label='Functions' }
#### [PillColor](https://wofsauge.github.io/IsaacDocs/rep/enums/PillColor.html) GetPill ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
不包括通过解锁获得的起始药丸。

___

### GetPlayerType () {: aria-label='Functions' }
#### int GetPlayerType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPocketActive () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetPocketActive ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
不包括模组添加的物品。

___

### GetPortraitPath () {: aria-label='Functions' }
#### string GetPortraitPath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
指向用于角色主要关卡过渡和 Boss 对战屏幕肖像的 PNG 文件的路径。

___

### GetRedHearts () {: aria-label='Functions' }
#### int GetRedHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSkinColor () {: aria-label='Functions' }
#### [SkinColor](https://wofsauge.github.io/IsaacDocs/rep/enums/SkinColor.html) GetSkinColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSkinPath () {: aria-label='Functions' }
#### string GetSkinPath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
指向角色主要精灵图所用 PNG 文件的路径。

___

### GetSoulHearts () {: aria-label='Functions' }
#### int GetSoulHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetTaintedCounterpart () {: aria-label='Functions' }
#### [EntityConfigPlayer](EntityConfigPlayer.md) GetTaintedCounterpart ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
对于非堕化角色，返回其堕化对应角色；如果没有，则返回 nil。

对于堕化角色，返回其非堕化对应角色。

___

### GetTrinket () {: aria-label='Functions' }
#### [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) GetTrinket ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
不包括通过解锁获得的起始饰品。

不包括模组添加的饰品。

___

### IsHidden () {: aria-label='Functions' }
#### boolean IsHidden ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果角色在角色选择屏幕上不可见或不可选，则返回 true。

不包括那些只有在解锁前才隐藏的角色。

___

### IsTainted () {: aria-label='Functions' }
#### boolean IsTainted ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

</div>
