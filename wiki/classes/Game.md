---
title: Game
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 87
---

# Game

## Summary

Game 类是游戏运行时的主要控制接口，提供对玩家、房间、关卡、画面特效、游戏状态（如恶魔交易计数、挑战完成、结局触发）的访问与修改能力。大部分与游戏进程相关的全局操作都通过该类的实例进行。

## Related Types

- [[Color]]
- [[Entity]]
- [[EntityNPC]]
- [[EntityPlayer]]
- [[Font]]
- [[HUD]]
- [[Isaac]]
- [[ItemPool]]
- [[Level]]
- [[Room]]
- [[Seeds]]
- [[Vector]]

## Key Methods

- [[#GetPlayer|GetPlayer]]
- [[#GetRoom|GetRoom]]
- [[#GetLevel|GetLevel]]
- [[#End|End]]
- [[#ChangeRoom|ChangeRoom]]

## Methods

### Constructors

### Game {#Game}

```
Game Game ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Game 类的构造函数，返回一个 Game 实例。是获取游戏全局对象的标准入口，后续所有 Game 方法调用都需基于该实例。

**Use Cases:**

- 初始化 Game 对象以访问游戏全局状态
- 调用 IsPaused 等需要先获取实例的方法

**See also:** 
[[#GetPlayer|GetPlayer]], [[#GetRoom|GetRoom]]


---

### Functions

### AddDevilRoomDeal {#AddDevilRoomDeal}

```
void AddDevilRoomDeal ( )
```

*DLC: REP, REP+ | Modifiers: const*

将已拿取的恶魔交易次数加 1。该操作会影响天使房的出现概率，模拟从恶魔房夺取道具的行为。

**Use Cases:**

- 手动增加恶魔交易计数以调整天使房概率
- 在自定义事件中模拟恶魔房交易

**See also:** 
[[#GetDevilRoomDeals|GetDevilRoomDeals]], [[#AddStageWithoutDamage|AddStageWithoutDamage]]


---

### AddEncounteredBoss {#AddEncounteredBoss}

```
void AddEncounteredBoss ( EntityType Boss, int Variant )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

标记指定的 Boss 已被遭遇。通常用于记录玩家是否见过某个 Boss，可能影响后续游戏逻辑或成就。

**Use Cases:**

- 记录 Boss 遭遇状态以供后续检查
- 在多周目或自定义模式下管理 Boss 出现

**See also:** 
[[#HasEncounteredBoss|HasEncounteredBoss]], [[#GetNumEncounteredBosses|GetNumEncounteredBosses]]


---

### AddPixelation {#AddPixelation}

```
void AddPixelation ( int Duration )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

触发“复古视觉”药丸效果，使屏幕产生像素化显示，持续指定的帧数。

**Use Cases:**

- 临时改变画面风格
- 实现自定义像素化效果

**See also:** 
[[#Darken|Darken]], [[#Fadein|Fadein]]


---

### AddStageWithoutDamage {#AddStageWithoutDamage}

```
void AddStageWithoutDamage ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

增加一个“未受伤害通过的层数”计数器。此计数用于恶魔房/天使房概率计算等隐藏机制。

**Use Cases:**

- 手动增加无伤层数以模拟无伤通过
- 调试或修改天使房/恶魔房概率

**See also:** 
[[#GetStagesWithoutDamage|GetStagesWithoutDamage]], [[#ClearStagesWithoutDamage|ClearStagesWithoutDamage]]


---

### AddStageWithoutHeartsPicked {#AddStageWithoutHeartsPicked}

```
void AddStageWithoutHeartsPicked ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

增加一个“未拾取红心通过的层数”计数器。与该计数相关的游戏机制（如某些成就或隐藏要求）可能会受影响。

**Use Cases:**

- 跟踪无拾心通过的状态
- 为自定义挑战统计相关数据

**See also:** 
[[#GetStagesWithoutHeartsPicked|GetStagesWithoutHeartsPicked]], [[#ClearStagesWithoutHeartsPicked|ClearStagesWithoutHeartsPicked]]


---

### AddTreasureRoomsVisited {#AddTreasureRoomsVisited}

```
void AddTreasureRoomsVisited ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

增加已访问宝箱房的数量计数。可能影响游戏内某些统计或成就。

**Use Cases:**

- 记录宝箱房访问次数
- 在自定义模组中触发与宝箱房相关的逻辑

**See also:** 
[[#GetTreasureRoomVisitCount|GetTreasureRoomVisitCount]]


---

### BombDamage {#BombDamage}

```
void BombDamage ( Vector Position, float Damage, float Radius, boolean LineCheck = true, Entity Source = nil, TearFlags TearFlags = TearFlags.TEAR_NORMAL, int DamageFlags = DamageFlags.DAMAGE_EXPLOSION, boolean DamageSource = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

在指定位置产生一次炸弹伤害，不包含视觉效果。仅计算伤害和碰撞检测，常用于需要自定义伤害逻辑的场合。

**Use Cases:**

- 模拟单纯的炸弹伤害而不附加特效
- 配合自定义爆炸效果使用

**See also:** 
[[#BombExplosionEffects|BombExplosionEffects]], [[#BombTearflagEffects|BombTearflagEffects]]


---

### BombExplosionEffects {#BombExplosionEffects}

```
void BombExplosionEffects ( Vector Position, float Damage, TearFlags TearFlags = TearFlags.TEAR_NORMAL, Color Color = Color.Default, Entity Source = nil, float RadiusMult = 1, boolean LineCheck = true, boolean DamageSource = false, int DamageFlags = DamageFlags.DAMAGE_EXPLOSION )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

完整的炸弹爆炸处理：施加伤害、生成爆炸视觉效果、并根据 TearFlags 应用状态效果。是触发标准爆炸的首选方法。

The complete bomb explosion package: Do damage, spawn boomgraphics, and apply tearflag-based effects.

**Use Cases:**

- 模拟标准炸弹爆炸
- 在自定义道具或效果中产生爆炸

**See also:** 
[[#BombDamage|BombDamage]], [[#BombTearflagEffects|BombTearflagEffects]]


---

### BombTearflagEffects {#BombTearflagEffects}

```
void BombTearflagEffects ( Vector Position, float Radius, TearFlags TearFlags, Entity Source = nil, float RadiusMult = 1)
```

*DLC: AB+, REP, REP+ | Modifiers: const*

仅执行炸弹爆炸时的特殊效果（如基于 TearFlags 的状态施加），不产生伤害和通用视觉效果。用于需要只施加特殊效果的场景。

Does bomb-exclusive special effects.

**Use Cases:**

- 仅触发爆炸关联的状态效果
- 精细控制爆炸的组成部分

**See also:** 
[[#BombExplosionEffects|BombExplosionEffects]], [[#BombDamage|BombDamage]]


---

### ButterBeanFart {#ButterBeanFart}

```
void ButterBeanFart ( Vector Position, float Radius, Entity Source, boolean ShowEffect, boolean DoSuperKnockback )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

模拟“黄油豆”（Butter Bean）道具的放屁效果，可击退敌人并产生视觉效果，支持超级击退模式。

**Use Cases:**

- 再现黄油豆效果
- 自定义击退类交互

**See also:** 
[[#Fart|Fart]], [[#CharmFart|CharmFart]]


---

### ChangeRoom {#ChangeRoom}

```
void ChangeRoom ( int RoomIndex, int Dimension = -1 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将玩家切换到指定索引的房间，并正确处理 FX 层，相比 Level.ChangeRoom 更为安全。支持指定维度。

**Use Cases:**

- 实现传送效果
- 在非主线维度间切换

**See also:** 
[[#GetRoom|GetRoom]], [[#GetLevel|GetLevel]]


---

### CharmFart {#CharmFart}

```
void CharmFart ( Vector Position, float Radius, Entity Source )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

产生一个魅惑效果的放屁，能够魅惑范围内的敌人。

**Use Cases:**

- 实现魅惑类型的放屁效果
- 与特定道具或敌人交互

**See also:** 
[[#Fart|Fart]], [[#ButterBeanFart|ButterBeanFart]]


---

### ClearDonationModAngel {#ClearDonationModAngel}

```
void ClearDonationModAngel ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

清空商店捐款机带来的天使房概率修正值（Angel Modifier），重置该加成。

**Use Cases:**

- 重置商店捐款对天使房的影响
- 用于调试或特殊模式

**See also:** 
[[#GetDonationModAngel|GetDonationModAngel]], [[#DonateAngel|DonateAngel]]


---

### ClearDonationModGreed {#ClearDonationModGreed}

```
void ClearDonationModGreed ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

清空贪婪模式下捐款机带来的修正值（Greed Modifier），重置相关加成。

**Use Cases:**

- 重置贪婪机修正
- 调试贪婪模式下的状态

**See also:** 
[[#GetDonationModGreed|GetDonationModGreed]], [[#DonateGreed|DonateGreed]]


---

### ClearStagesWithoutDamage {#ClearStagesWithoutDamage}

```
void ClearStagesWithoutDamage ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将无伤通关层数计数器归零。通常用于死亡或重置时清除该记录。

**Use Cases:**

- 玩家受到伤害时重置无伤计数
- 手动修改无伤挑战相关状态

**See also:** 
[[#AddStageWithoutDamage|AddStageWithoutDamage]], [[#GetStagesWithoutDamage|GetStagesWithoutDamage]]


---

### ClearStagesWithoutHeartsPicked {#ClearStagesWithoutHeartsPicked}

```
void ClearStagesWithoutHeartsPicked ( )
```

*DLC: AB+, REP, REP+*

将未拾取红心通过的层数计数器归零。

**Use Cases:**

- 重置无拾心限制的进度记录
- 用于挑战或成就系统的状态重置

**See also:** 
[[#AddStageWithoutHeartsPicked|AddStageWithoutHeartsPicked]], [[#GetStagesWithoutHeartsPicked|GetStagesWithoutHeartsPicked]]


---

### Darken {#Darken}

```
void Darken ( float Darkness, int Timeout )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

在指定时间内让房间按设定数值变暗，内部用于羔羊战斗或骰子房激活等情景。

**Use Cases:**

- 模拟房间变暗氛围
- 制作自定义视觉过渡

**See also:** 
[[#GetDarknessModifier|GetDarknessModifier]], [[#GetTargetDarkness|GetTargetDarkness]]


---

### DonateAngel {#DonateAngel}

```
void DonateAngel ( int Donate )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

模拟向商店捐款机捐款 10 枚硬币对天使房概率的提升效果，但不消耗实际硬币。

**Use Cases:**

- 调试天使房概率
- 在自定义内容中直接调整天使房概率

**See also:** 
[[#GetDonationModAngel|GetDonationModAngel]], [[#ClearDonationModAngel|ClearDonationModAngel]]


---

### DonateGreed {#DonateGreed}

```
void DonateGreed ( int Donate )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

模拟向贪婪捐款机捐款的效果，影响贪婪模式下的相关概率（如生成机遇等）。

**Use Cases:**

- 调整贪婪模式下的机器修正
- 调试贪婪相关机制

**See also:** 
[[#GetDonationModGreed|GetDonationModGreed]], [[#ClearDonationModGreed|ClearDonationModGreed]]


---

### End {#End}

```
void End ( Ending Ending )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

触发游戏结局，根据传入的 Ending 枚举值播放对应的结局动画、增加胜利连胜计数。传入无效值可人为增加连胜。

???+ note "Ending notes"

**Use Cases:**

- 完成自定义结局触发
- 调试连胜或结局相关逻辑

**See also:** 
[[#Fadeout|Fadeout]], [[#FinishChallenge|FinishChallenge]]


---

### Fadein {#Fadein}

```
void Fadein ( float Speed )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

以指定速度执行淡入效果（从黑色或指定颜色渐变至正常）。基本版本。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 场景过渡后恢复正常可视
- 配合 Fadeout 制作完整过场

**See also:** 
[[#Fadeout|Fadeout]], [[#Darken|Darken]]


---

### void Fadein ( float Speed, boolean ShowIcon = true, [KColor](KColor.md) Color = KColor.Black ) {#void Fadein ( float Speed, boolean ShowIcon = true, [KColor](KColor.md) Color = KColor.Black )}

```
void Fadeout ( float Speed, FadeoutTarget Target )
```

*DLC: AB+, REP, REP+*

Fadein 的增强版本，允许指定是否显示游戏图标以及自定义淡入颜色。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 控制淡入时是否显示UI图标
- 使用非黑色颜色进行自定义淡入

**See also:** 
[[#Fadein|Fadein]], [[#Fadeout|Fadeout]], [[#Darken|Darken]]


---

### void Fadeout ( float Speed, FadeoutTarget Target, [KColor](KColor.md) Color = KColor.Black ) {#void Fadeout ( float Speed, FadeoutTarget Target, [KColor](KColor.md) Color = KColor.Black )}

```
void Fart ( Vector Position, float Radius = 85, Entity Source = nil, float FartScale = 1, int FartSubType = 0, Color FartColor = Color.Default )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Fadeout 的完整版本，执行淡出效果并可指定目标菜单（如回到文件选择、标题、新游戏等），支持自定义颜色。

**Use Cases:**

- 在结束游戏或返回菜单时使用
- 制作自定义过渡效果

**See also:** 
[[#Fadeout|Fadeout]], [[#Fadein|Fadein]], [[#End|End]]


---

### FinishChallenge {#FinishChallenge}

```
void FinishChallenge ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

立即完成当前挑战（如挑战模式），触发挑战完成后的逻辑。

**Use Cases:**

- 测试挑战完成后的事件
- 跳过当前挑战

**See also:** 
[[#End|End]]


---

### GetAmbush {#GetAmbush}

```
Ambush GetAmbush ( )
```

*DLC: AB+, REP | Modifiers: const*

尝试获取当前伏击（Ambush）事件。由于返回 UserData，该函数目前无法正常使用，存在 bug。

???+ bug "Bug"

**Use Cases:**

- 调用 GetAmbush 完成对应 API 操作

**See also:** 



---

### GetDarknessModifier {#GetDarknessModifier}

```
float GetDarknessModifier ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取当前黑暗度修改器的值。该值影响房间实际渲染的黑暗程度，与 Darken 等方法相关。

**Use Cases:**

- 查询当前黑暗度
- 根据黑暗度动态调整特效

**See also:** 
[[#Darken|Darken]], [[#GetTargetDarkness|GetTargetDarkness]]


---

### GetDevilRoomDeals {#GetDevilRoomDeals}

```
int GetDevilRoomDeals ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取当前已获取的恶魔房间交易次数。

**Use Cases:**

- 检查恶魔交易计数以计算天使房概率
- 调试房间生成逻辑

**See also:** 
[[#AddDevilRoomDeal|AddDevilRoomDeal]]


---

### GetDonationModAngel {#GetDonationModAngel}

```
int GetDonationModAngel ( )
```

*DLC: REP, REP+ | Modifiers: const*

获取商店捐款机带来的天使房概率修正值。数值越高，天使房出现概率越大。

**Use Cases:**

- 判断当前天使房概率加成
- 根据捐款状态调整游戏逻辑

**See also:** 
[[#DonateAngel|DonateAngel]], [[#ClearDonationModAngel|ClearDonationModAngel]]


---

### GetDonationModGreed {#GetDonationModGreed}

```
int GetDonationModGreed ( )
```

*DLC: AB+, REP, REP+*

获取贪婪模式下捐款机带来的修正值，影响贪婪相关的事件概率。

**Use Cases:**

- 查询贪婪模式捐赠状态
- 调整贪婪相关掉落或生成

**See also:** 
[[#DonateGreed|DonateGreed]], [[#ClearDonationModGreed|ClearDonationModGreed]]


---

### GetFont {#GetFont}

```
Font GetFont ( )
```

*DLC: AB+, REP, REP+*

返回当前游戏使用的 Font 对象，用于文本渲染等操作。

**Use Cases:**

- 获取字体以进行自定义绘图
- 测量文本宽度等

**See also:** 
[[#GetHUD|GetHUD]]


---

### GetFrameCount {#GetFrameCount}

```
int GetFrameCount ( )
```

*DLC: AB+, REP, REP+*

返回游戏实际运行的帧数（暂停期间不计入），与 Isaac.GetFrameCount() 不同。60 帧为 1 秒（30帧制实现）。

**Use Cases:**

- 计算实时游戏时间
- 制作基于游戏运行时间的逻辑

**See also:** 



---

### GetGreedBossWaveNum {#GetGreedBossWaveNum}

```
int GetGreedBossWaveNum ( )
```

*DLC: AB+, REP, REP+*

返回贪婪模式下当前楼层的 Boss 波数。

**Use Cases:**

- 获取贪婪模式进度信息
- 控制 Boss 波生成时机

**See also:** 
[[#GetGreedWavesNum|GetGreedWavesNum]], [[#IsGreedMode|IsGreedMode]]


---

### GetGreedWavesNum {#GetGreedWavesNum}

```
int GetGreedWavesNum ( )
```

*DLC: AB+, REP, REP+*

返回贪婪模式当前层的总波数（包括小怪和Boss波）。

**Use Cases:**

- 获取贪婪模式完整波数配置
- 用于UI显示或生成逻辑

**See also:** 
[[#GetGreedBossWaveNum|GetGreedBossWaveNum]], [[#IsGreedMode|IsGreedMode]]


---

### GetHUD {#GetHUD}

```
HUD GetHUD ( )
```

*DLC: AB+, REP, REP+*

返回游戏 HUD 对象，可用于控制血量、道具、地图等 UI 元素的显示。

**Use Cases:**

- 操作或隐藏游戏界面
- 自定义 HUD 元素

**See also:** 
[[#GetPlayer|GetPlayer]], [[#GetRoom|GetRoom]]


---

### GetItemOverlay {#GetItemOverlay}

```
ItemOverlay GetItemOverlay ( )
```

*DLC: AB+, REP, REP+*

尝试获取物品覆盖层对象。由于返回 UserData，该函数目前被标记为有 bug 且无法使用。

???+ bug "Bug"

**Use Cases:**

- 调用 GetItemOverlay 完成对应 API 操作

**See also:** 



---

### GetItemPool {#GetItemPool}

```
ItemPool GetItemPool ( )
```

*DLC: AB+, REP, REP+*

获取当前游戏的物品池对象，用于查询和管理随机物品生成。

**Use Cases:**

- 手动控制物品生成概率
- 读取物品池状态

**See also:** 
[[#GetLevel|GetLevel]]


---

### GetLastDevilRoomStage {#GetLastDevilRoomStage}

```
LevelStage GetLastDevilRoomStage ( )
```

*DLC: AB+, REP, REP+*

尝试获取最近一次有恶魔房间的楼层阶段。由于返回 UserData，该函数存在 bug，可能无法正常工作。

**Use Cases:**

- 调用 GetLastDevilRoomStage 完成对应 API 操作

**See also:** 



---

### GetLastLevelWithDamage {#GetLastLevelWithDamage}

```
LevelStage GetLastLevelWithDamage ( )
```

*DLC: AB+, REP, REP+*

尝试获取最近一次受到伤害的楼层阶段。同样因返回 UserData 而可能有 bug。

**Use Cases:**

- 调用 GetLastLevelWithDamage 完成对应 API 操作

**See also:** 



---

### GetLastLevelWithoutHalfHp {#GetLastLevelWithoutHalfHp}

```
LevelStage GetLastLevelWithoutHalfHp ( )
```

*DLC: AB+, REP, REP+*

尝试获取最近一次以半颗心以下状态通过的楼层阶段。返回 UserData，可能存在 bug。

**Use Cases:**

- 调用 GetLastLevelWithoutHalfHp 完成对应 API 操作

**See also:** 



---

### GetLevel {#GetLevel}

```
Level GetLevel ( )
```

*DLC: AB+, REP, REP+*

返回当前关卡对象，用于访问关卡布局、种子和房间信息。

**Use Cases:**

- 获取当前关卡阶段类型
- 修改关卡房间布局
- 获取关卡种子

**See also:** 
[[#GetRoom|GetRoom]], [[#GetSeeds|GetSeeds]]


---

### GetNearestPlayer {#GetNearestPlayer}

```
EntityPlayer GetNearestPlayer ( Vector Pos )
```

*DLC: AB+, REP, REP+*

获取距离给定位置最近的玩家实体，常用于定位目标或施加效果。

**Use Cases:**

- 向最近玩家施放技能
- 检测玩家与位置的距离
- 合作模式中选择最近玩家

**See also:** 
[[#GetPlayer|GetPlayer]], [[#GetRandomPlayer|GetRandomPlayer]], [[#GetNumPlayers|GetNumPlayers]]


---

### GetNumEncounteredBosses {#GetNumEncounteredBosses}

```
int GetNumEncounteredBosses ( )
```

*DLC: AB+, REP, REP+*

返回已遭遇的 BOSS 种类数量，用于追踪进度或解锁相关条件。

**Use Cases:**

- 成就统计
- 判断是否遭遇过所有 BOSS

**See also:** 
[[#HasEncounteredBoss|HasEncounteredBoss]]


---

### GetNumPlayers {#GetNumPlayers}

```
int GetNumPlayers ( )
```

*DLC: AB+, REP, REP+*

返回当前游戏中的玩家数量（含合作角色），用于判断单人或多人模式。

**Use Cases:**

- 遍历所有玩家实体
- 根据玩家数量调整难度
- 合作模式特殊逻辑

**See also:** 
[[#GetPlayer|GetPlayer]], [[#GetNearestPlayer|GetNearestPlayer]]


---

### GetPlayer {#GetPlayer}

```
EntityPlayer GetPlayer ( int Index ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

根据索引获取对应的玩家实体，索引无效时返回 nil 或最后一名玩家。

Returns the [EntityPlayer](EntityPlayer.md) with the given index. This function can return `nil` if the function is called before any player is initialized. If an index is given, that is not used, it will return the last player in the list.

**Use Cases:**

- 获取特定编号的玩家
- 修改玩家属性或状态
- 传送玩家

**See also:** 
[[#GetNearestPlayer|GetNearestPlayer]], [[#GetRandomPlayer|GetRandomPlayer]], [[#GetNumPlayers|GetNumPlayers]]


---

### GetRandomPlayer {#GetRandomPlayer}

```
EntityPlayer GetRandomPlayer ( Vector Pos, float Radius )
```

*DLC: AB+, REP, REP+*

在给定位置和半径内随机选择一个玩家实体，用于需要随机目标的效果。

**Use Cases:**

- 随机选择目标施放诅咒
- 随机分配奖励

**See also:** 
[[#GetNearestPlayer|GetNearestPlayer]], [[#GetPlayer|GetPlayer]]


---

### GetRoom {#GetRoom}

```
Room GetRoom ( )
```

*DLC: REP, REP+*

返回当前房间对象，提供对房间内实体、门和布局的访问。

**Use Cases:**

- 获取房间类型与形状
- 修改房间内敌人或掉落物
- 检测房间是否清空

**See also:** 
[[#GetLevel|GetLevel]], [[#StartRoomTransition|StartRoomTransition]]


---

### GetScreenShakeCountdown {#GetScreenShakeCountdown}

```
int GetScreenShakeCountdown ( )
```

*DLC: REP, REP+ | Modifiers: const*

获取屏幕震动效果的剩余帧数，用于判断震动状态或持续时间。

**Use Cases:**

- 检测屏幕是否仍在震动
- 自定义震动结束后的逻辑

**See also:** 
[[#ShakeScreen|ShakeScreen]]


---

### GetSeeds {#GetSeeds}

```
Seeds GetSeeds ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回游戏种子对象，可用于获取当前运行的种子值或控制随机。

**Use Cases:**

- 获取关卡种子用于外部工具
- 手动设置随机种子

**See also:** 
[[#GetLevel|GetLevel]]


---

### GetStagesWithoutDamage {#GetStagesWithoutDamage}

```
int GetStagesWithoutDamage ( )
```

*DLC: AB+, REP, REP+*

返回当前连续无伤通关的房间层数，影响恶魔/天使房出现概率。

**Use Cases:**

- 检测无伤达成状态
- 定制房间开启条件

**See also:** 
[[#GetStagesWithoutHeartsPicked|GetStagesWithoutHeartsPicked]]


---

### GetStagesWithoutHeartsPicked {#GetStagesWithoutHeartsPicked}

```
int GetStagesWithoutHeartsPicked ( )
```

*DLC: AB+, REP, REP+*

返回当前连续不拾取红心通关的房间层数，用于成就或特殊效果。

**Use Cases:**

- 追踪不拾心挑战进度
- 解锁相关成就

**See also:** 
[[#GetStagesWithoutDamage|GetStagesWithoutDamage]]


---

### GetStateFlag {#GetStateFlag}

```
boolean GetStateFlag ( GameStateFlag GameStateFlag )
```

*DLC: AB+, REP, REP+*

获取指定游戏状态标志的开关状态（如 Boss Rush 是否激活）。

**Use Cases:**

- 检查特殊挑战模式
- 按状态触发事件

**See also:** 
[[#SetStateFlag|SetStateFlag]], [[#IsGreedMode|IsGreedMode]], [[#IsPaused|IsPaused]]


---

### GetTargetDarkness {#GetTargetDarkness}

```
float GetTargetDarkness ( )
```

*DLC: AB+, REP, REP+*

返回当前房间黑暗度的目标值，用于检测黑暗效果是否正在改变。

**Use Cases:**

- 判断房间变暗动画进程
- 黑暗相关特效

**See also:** 



---

### GetTreasureRoomVisitCount {#GetTreasureRoomVisitCount}

```
int GetTreasureRoomVisitCount ( )
```

*DLC: AB+, REP, REP+*

返回当前游戏已访问宝藏房间的次数，用于统计或解锁。

**Use Cases:**

- 检测宝藏房探索数量
- 触发相关成就

**See also:** 



---

### GetVictoryLap {#GetVictoryLap}

```
int GetVictoryLap ( )
```

*DLC: AB+, REP, REP+*

返回当前胜利圈数，用于循环难度调整和记录。

**Use Cases:**

- 检测是否在胜利圈
- 根据圈数调整敌人强度

**See also:** 
[[#NextVictoryLap|NextVictoryLap]]


---

### HasEncounteredBoss {#HasEncounteredBoss}

```
boolean HasEncounteredBoss ( EntityType Boss, int Variant )
```

*DLC: AB+, REP, REP+*

检查是否已遭遇指定的 BOSS 类型和变种，用于条件判断和进度。

**Use Cases:**

- 检查某种 BOSS 是否被打败
- 解锁条件判定

**See also:** 
[[#GetNumEncounteredBosses|GetNumEncounteredBosses]]


---

### HasHallucination {#HasHallucination}

```
boolean HasHallucination ( )
```

*DLC: AB+, REP, REP+*

返回当前是否正在播放 Delirium 的干扰动画（静态噪声叠加历史画面）。

Returns true if the Delirium animation (Static noise intersected with past gameplay fotage) is playing right now.

**Use Cases:**

- 在幻觉期间暂停玩家输入
- 自定义幻觉效果的表现

**See also:** 
[[#ShowHallucination|ShowHallucination]]


---

### IsGreedMode {#IsGreedMode}

```
boolean IsGreedMode ( )
```

*DLC: AB+, REP, REP+*

返回当前游戏模式是否为 Greed 或 Greedier 模式。

Returns true if the current gamemode is set to Greed or Greedier mode.

**Use Cases:**

- 切换贪婪特有逻辑
- 限制某些道具生效

**See also:** 
[[#GetStateFlag|GetStateFlag]]


---

### IsPaused {#IsPaused}

```
boolean IsPaused ( )
```

*DLC: REP, REP+*

返回游戏是否处于暂停状态，常用于在回调中判断是否执行逻辑。

**Use Cases:**

- 暂停期间暂停计时
- 跳过暂停时的更新

**See also:** 
[[#GetStateFlag|GetStateFlag]]


---

### MakeShockwave {#MakeShockwave}

```
void MakeShockwave ( Vector Position, float Amplitude, float Speed, int Duration )
```

*DLC: REP, REP+*

在指定位置创建屏幕冲击波效果，常用于 Boss 技能或大型爆炸。

???- info "Reference"

**Use Cases:**

- 制作自定义 Boss 攻击
- 为爆炸添加视觉冲击

**See also:** 
[[#ShakeScreen|ShakeScreen]], [[#SpawnParticles|SpawnParticles]]


---

### MoveToRandomRoom {#MoveToRandomRoom}

```
void MoveToRandomRoom ( boolean IAmErrorRoom, int Seed, EntityPlayer Player )
```

*DLC: REP, REP+*

将指定玩家传送至随机房间（可选 I Am Error 房间），基于种子选择。

**Use Cases:**

- 实现诅咒房间效果
- 随机传送类道具

**See also:** 
[[#StartRoomTransition|StartRoomTransition]]


---

### NextVictoryLap {#NextVictoryLap}

```
void NextVictoryLap ( )
```

*DLC: AB+, REP, REP+*

触发下一圈胜利循环，重置部分进度并提高难度。

**Use Cases:**

- 主动进入胜利圈
- 循环挑战管理

**See also:** 
[[#GetVictoryLap|GetVictoryLap]]


---

### Render {#Render}

```
void Render ( )
```

*DLC: AB+, REP, REP+*

执行一次游戏画面的手动渲染，通常配合 Update 用于自定义渲染顺序。

**Use Cases:**

- 在特定时机强制刷新画面
- 自定义 UI 后手动渲染

**See also:** 
[[#Update|Update]]


---

### RerollEnemy {#RerollEnemy}

```
boolean RerollEnemy ( Entity e )
```

*DLC: AB+, REP, REP+*

将指定敌人重骰为随机另一种敌人，成功返回 true。

**Use Cases:**

- D6 效果作用于敌人
- 随机化房间内敌人

**See also:** 
[[#Spawn|Spawn]]


---

### RerollLevelCollectibles {#RerollLevelCollectibles}

```
void RerollLevelCollectibles ( )
```

*DLC: AB+, REP, REP+*

重骰当前房间内的所有被动/主动收集品，类似骰子房效果。

**Use Cases:**

- 重置道具获取更好的物品
- 定制重置房间效果

**See also:** 
[[#RerollLevelPickups|RerollLevelPickups]], [[#Spawn|Spawn]]


---

### RerollLevelPickups {#RerollLevelPickups}

```
void RerollLevelPickups ( int Seed )
```

*DLC: REP, REP+*

重骰当前房间内所有掉落物（心、硬币、炸弹等）为随机其他拾取物。

**Use Cases:**

- 清理房间后改变掉落
- 特殊道具激活效果

**See also:** 
[[#RerollLevelCollectibles|RerollLevelCollectibles]], [[#Spawn|Spawn]]


---

### SetLastDevilRoomStage {#SetLastDevilRoomStage}

```
void SetLastDevilRoomStage ( LevelStage Stage )
```

*DLC: AB+, REP, REP+*

设置最后一次出现恶魔房的楼层阶段，用于影响后续恶魔/天使房概率。

**Use Cases:**

- 手动调整房间出现概率
- 重置恶魔房记录

**See also:** 



---

### SetLastLevelWithDamage {#SetLastLevelWithDamage}

```
void SetLastLevelWithDamage ( LevelStage Stage )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置最后一次受到伤害的楼层阶段，影响部分成就或房间概率。

**Use Cases:**

- 手动修改伤害记录
- 调试无伤相关概率

**See also:** 



---

### SetLastLevelWithoutHalfHp {#SetLastLevelWithoutHalfHp}

```
void SetLastLevelWithoutHalfHp ( LevelStage Stage )
```

*DLC: AB+, REP, REP+*

设置最后一次半血以下通关的楼层阶段，用于调整相关解锁条件。

**Use Cases:**

- 控制半血通关记录
- 调试成就逻辑

**See also:** 



---

### SetStateFlag {#SetStateFlag}

```
void SetStateFlag ( GameStateFlag GameStateFlag, boolean Val )
```

*DLC: AB+, REP, REP+*

设置或清除指定的游戏状态标志，例如激活 Boss Rush 或 Hush 入口。

**Use Cases:**

- 强制开启 Boss Rush 门
- 关闭或开启各种游戏状态

**See also:** 
[[#GetStateFlag|GetStateFlag]]


---

### ShakeScreen {#ShakeScreen}

```
void ShakeScreen ( int Timeout )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

使屏幕震动指定帧数，常用于炸弹爆炸或强力技能。

**Use Cases:**

- 为自定义爆炸添加震动
- 强化技能打击感

**See also:** 
[[#GetScreenShakeCountdown|GetScreenShakeCountdown]], [[#MakeShockwave|MakeShockwave]]


---

### ShowFortune {#ShowFortune}

```
void ShowFortune ( )
```

*DLC: AB+, REP, REP+*

在游戏中显示一条预言/命运信息，类似命运之轮的效果。

**Use Cases:**

- 显示自定义提示
- 制作命运卡片

**See also:** 



---

### ShowHallucination {#ShowHallucination}

```
void ShowHallucination ( int FrameCount, BackdropType Backdrop = BackdropType.NUM_BACKDROPS )
```

*DLC: AB+, REP, REP+*

播放 Delirium 幻觉动画，包括静态噪声和历史画面，并可更换背景。

Plays the Delirium animation (Static noise intersected with past gameplay fotage), which will also change the background of the current room.

**Use Cases:**

- 模拟 Delirium 战斗开场
- 制作幻觉类效果

**See also:** 
[[#HasHallucination|HasHallucination]]


---

### ShowRule {#ShowRule}

```
void ShowRule ( )
```

*DLC: AB+, REP, REP+*

在屏幕上显示游戏规则或提示文本。

**Use Cases:**

- 显示教程信息
- 自定义规则提示

**See also:** 



---

### Spawn {#Spawn}

```
Entity Spawn ( EntityType Type, int Variant, Vector Position, Vector Velocity, Entity Spawner, int SubType, int Seed )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

根据类型、变种、位置、速度等参数生成一个实体，返回生成的实体。

**Use Cases:**

- 生成敌人或 BOSS
- 掉落自定义物品
- 创建特效实体

**See also:** 
[[#SpawnEntityDesc|SpawnEntityDesc]], [[#RerollEnemy|RerollEnemy]]


---

### SpawnEntityDesc {#SpawnEntityDesc}

```
EntityNPC SpawnEntityDesc ( EntityDesc desc, Vector Position, Entity Spawner )
```

*DLC: REP, REP+ | Modifiers: const*

使用 EntityDesc 描述来生成 NPC 实体，提供更便捷的创建方式。

**Use Cases:**

- 批量生成预定义的敌人
- 通过描述表生成实体

**See also:** 
[[#Spawn|Spawn]]


---

### SpawnParticles {#SpawnParticles}

```
void SpawnParticles ( Vector Pos, EffectVariant ParticleType, int NumParticles, float Speed, Color Color = Color.Default, float Height = 100000, int SubType = 0 )
```

*DLC: AB+, REP, REP+*

在指定位置生成一组粒子效果，可设置类型、数量、速度和颜色。

**Use Cases:**

- 爆炸粒子
- 魔法特效
- 环境氛围

**See also:** 
[[#MakeShockwave|MakeShockwave]]


---

### StartRoomTransition {#StartRoomTransition}

```
void StartRoomTransition ( int RoomIndex, Direction Direction, RoomTransitionAnim Animation = RoomTransitionAnim.WALK, EntityPlayer Player = nil, int Dimension = -1 )
```

*DLC: AB+, REP, REP+*

播放房间过渡动画并切换到指定房间，支持方向、动画类型和维度。

**Use Cases:**

- 手动切换房间
- 实现传送门效果

**See also:** 
[[#StartStageTransition|StartStageTransition]], [[#MoveToRandomRoom|MoveToRandomRoom]]


---

### StartStageTransition {#StartStageTransition}

```
void StartStageTransition ( boolean SameStage, int TransitionOverride, EntityPlayer Player )
```

*DLC: AB+, REP, REP+*

播放楼层过渡动画并切换到下一层或指定层，常用于成就或通关。

**Use Cases:**

- 手动进入下一楼层
- 触发楼层更换

**See also:** 
[[#StartRoomTransition|StartRoomTransition]]


---

### Update {#Update}

```
void Update ( )
```

*DLC: AB+, REP, REP+*

执行一次游戏逻辑更新，通常与 Render 一起组成自定义游戏循环。

**Use Cases:**

- 手动控制游戏循环节奏
- 在特定时序执行更新

**See also:** 
[[#Render|Render]]


---

### UpdateStrangeAttractor {#UpdateStrangeAttractor}

```
void UpdateStrangeAttractor ( Vector Position, float Force = 10, float Radius = 250 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

在指定位置更新奇异吸引子效果，可自定义作用力和半径。通常用于实现类似「奇异吸引子」道具的物理行为。

**Use Cases:**

- 模拟奇异吸引子道具的吸引效果
- 自定义吸引范围与力度

**See also:** 



---

### BlueWombParTime {#BlueWombParTime}

```
int BlueWombParTime
```

*DLC: AB+, REP, REP+*

返回进入蓝子宫（Hush）所需的游戏帧数时限。用于判定是否满足时间条件。

**Use Cases:**

- 获取蓝子宫时间阈值
- 判断是否能在时限内到达蓝子宫

**See also:** 



---

### BossRushParTime {#BossRushParTime}

```
int BossRushParTime
```

*DLC: AB+, REP, REP+*

返回 Boss Rush 的限时帧数。该值代表游戏时间帧数，通常用于判定是否满足进入 Boss Rush 的条件。

Number of frames of game time.

**Use Cases:**

- 获取 Boss Rush 标准时限
- 时间相关的成就或触发逻辑

**See also:** 



---

### Challenge {#Challenge}

```
Challenge Challenge
```

*DLC: AB+, REP, REP+*

表示当前游戏的挑战模式（如红色钥匙、冲刺等），只读。

**Use Cases:**

- 检测当前运行的挑战模式
- 根据挑战类型调整游戏行为

**See also:** 



---

### Difficulty {#Difficulty}

```
const Difficulty Difficulty
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前游戏的难度设置（普通/困难），只读。

**Use Cases:**

- 区分普通与困难难度以改变游戏平衡
- 在 UI 或成就中展示难度

**See also:** 



---

### ScreenShakeOffset {#ScreenShakeOffset}

```
const Vector ScreenShakeOffset
```

*DLC: AB+, REP, REP+ | Modifiers: const*

提供当前屏幕震动偏移向量，只读。可用于补偿震动对 UI 或渲染的影响。

**Use Cases:**

- 定位 UI 元素时抵消屏幕震动
- 获取震动强度与方向

**See also:** 



---

### TimeCounter {#TimeCounter}

```
int TimeCounter
```

*DLC: AB+, REP, REP+*

可修改的游戏时间计数器，主要用于计时事件（如 Boss Rush、每日挑战），但不用于物理时间步进。

same as FrameCounter but can be modified, mostly used for timed events (bossrush, daily, ...) and not for timestepping

**Use Cases:**

- 创建自定义限时挑战
- 调整定时事件的触发时机

**See also:** 



---

## See Also

- [[Color]]
- [[Entity]]
- [[EntityNPC]]
- [[EntityPlayer]]
- [[Font]]
- [[HUD]]
- [[Isaac]]
- [[ItemPool]]
- [[Level]]
- [[Room]]
- [[Seeds]]
- [[Vector]]
