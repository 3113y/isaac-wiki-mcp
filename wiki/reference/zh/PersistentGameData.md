---
tags:
  - Class
---
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

# Class "PersistentGameData"

???+ info
    你可以通过以下函数获取此类：

    * [Isaac.GetPersistentGameData()](Isaac.md#getpersistentgamedata)

    ???+ example "Example Code"
        ```lua
        local persistentGameData = Isaac.GetPersistentGameData()
        ```
???+ warning "Warning"
    在游戏完成初始化前，不要调用此类中的函数！请勿尝试在回调之外使用这些函数。
    
## Functions

<div class="rgon-only" markdown="1">

### AddBestiaryKill () {: aria-label='Functions' }
#### void AddBestiaryKill ( int Type, int Variant = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### AddBossKilled () {: aria-label='Functions' }
#### void AddBossKilled ( [BossType](enums/BossType.md) Boss) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Marks this boss as killed and unlocks its relevant alternate floor if conditions are met.

### GetBestiaryDeathCount () {: aria-label='Functions' }
#### int GetBestiaryDeathCount ( int Type, int Variant ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBestiaryEncounterCount () {: aria-label='Functions' }
#### int GetBestiaryEncounterCount ( int Type, int Variant ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBestiaryKillCount () {: aria-label='Functions' }
#### int GetBestiaryKillCount ( int Type, int Variant ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetEventCounter () {: aria-label='Functions' }
#### int GetEventCounter ( [EventCounter](enums/EventCounter.md) EventCounter ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IncreaseEventCounter () {: aria-label='Functions' }
#### void IncreaseEventCounter ( [EventCounter](enums/EventCounter.md) EventCounter, int Count ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsBossKilled () {: aria-label='Functions' }
#### boolean IsBossKilled ( [BossType](enums/BossType.md) Boss) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns whether this boss was marked as killed (for purposes of unlock tracking).

### IsChallengeCompleted () {: aria-label='Functions' }
#### boolean IsChallengeCompleted ( [Challenge](https://wofsauge.github.io/IsaacDocs/rep/enums/Challenge.html) ChallengeId ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Checks if a challenge is completed.

### IsItemInCollection () {: aria-label='Functions' }
#### boolean IsItemInCollection ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) CollectibleId ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Checks if an item is in the collection. Aka. its at least picked up once in any run.

### TryUnlock () {: aria-label='Functions' }
#### boolean TryUnlock ( [Achievement](enums/Achievement.md) Unlock, boolean BlockPaperPopup = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if successful, `false` if unlocking failed or the secret was already unlocked.
Setting `BlockPaperPopup` to `true` prevents popping up the achievement paper for modded achievements.

### Unlocked () {: aria-label='Functions' }
#### boolean Unlocked ( [Achievement](enums/Achievement.md) Unlock ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Checks if achievement is unlocked.

### Unlock () {: aria-label='Functions' }
#### boolean Unlock ( [Achievement](enums/Achievement.md) Unlock, boolean BlockPaperPopup = false ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns `true` if successful, or `false` if unlocking failed or the secret was already unlocked. It almost never fails, unlike `TryUnlock`, which fails if achievements are disabled.

Setting `BlockPaperPopup` to `true` prevents popping up the achievement paper for modded achievements.
___

</div>
