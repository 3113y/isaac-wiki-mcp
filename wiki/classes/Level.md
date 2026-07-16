---
title: Level
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 64
---

# Level

## Summary

Level 类是当前楼层的核心接口，管理楼层阶段、房间布局、诅咒状态、地图效果以及恶魔/天使房概率等全局属性。

## Related Types

- [[Game]]
- [[RNG]]
- [[Room]]
- [[RoomDescriptor]]
- [[Vector]]

## Key Methods

- [[#GetCurrentRoomDesc|GetCurrentRoomDesc]]
- [[#GetStage|GetStage]]
- [[#GetAngelRoomChance|GetAngelRoomChance]]
- [[#AddCurse|AddCurse]]
- [[#InitializeDevilAngelRoom|InitializeDevilAngelRoom]]

## Methods

### Functions

### AddAngelRoomChance {#AddAngelRoomChance}

```
void AddAngelRoomChance ( float Chance )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

增加天使房概率修正值，直接累加指定数值到当前楼层的天使房出现几率调整项。

Adds `Chance` to the Angel deal modifier. See [GetAngelRoomChance](Level.md#getangelroomchance) for more information.

**Use Cases:**

- 提高特定楼层出现天使房的概率
- 配合惩罚机制动态调整房间类型偏向

**See also:** 
[[#GetAngelRoomChance|GetAngelRoomChance]], [[#InitializeDevilAngelRoom|InitializeDevilAngelRoom]]


---

### AddCurse {#AddCurse}

```
void AddCurse ( LevelCurse Curse, boolean ShowName )
```

*DLC: REP, REP+ | Modifiers: const*

向当前楼层添加指定类型的诅咒，并可选显示诅咒名称提示。

**Use Cases:**

- 触发自定义楼层诅咒效果
- 叠加多种诅咒以增加挑战难度

**See also:** 
[[#RemoveCurses|RemoveCurses]], [[#GetCurses|GetCurses]]


---

### ApplyBlueMapEffect {#ApplyBlueMapEffect}

```
void ApplyBlueMapEffect ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

激活蓝地图效果，揭示秘密房间位置，类似道具 X-Ray 效果。

**Use Cases:**

- 临时显示所有隐藏房间入口
- 制作自定义地图揭示效果

**See also:** 
[[#ApplyMapEffect|ApplyMapEffect]], [[#ApplyCompassEffect|ApplyCompassEffect]]


---

### ApplyCompassEffect {#ApplyCompassEffect}

```
void ApplyCompassEffect ( boolean Persistent )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

激活罗盘效果，在迷你地图上标记所有普通房间，可设置是否持久。

**Use Cases:**

- 模拟 Compass 道具效果
- 楼层开局自动揭示房间布局

**See also:** 
[[#RemoveCompassEffect|RemoveCompassEffect]], [[#ApplyMapEffect|ApplyMapEffect]]


---

### ApplyMapEffect {#ApplyMapEffect}

```
void ApplyMapEffect ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

激活全地图效果，揭示整个楼层的房间布局（不含隐藏房间），类似 Treasure Map 道具。

**Use Cases:**

- 一次性展示楼层全貌
- 组合其他地图效果达到完全可见

**See also:** 
[[#ApplyBlueMapEffect|ApplyBlueMapEffect]], [[#ApplyCompassEffect|ApplyCompassEffect]]


---

### CanOpenChallengeRoom {#CanOpenChallengeRoom}

```
boolean CanOpenChallengeRoom ( int RoomIndex )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

判断指定房间索引的挑战房门是否处于开启状态，只与楼层网格索引有关。

Returns whether or not a Challenge Room door will be open. You must pass this method a valid grid index on the floor. It does not matter if the grid index is actually attached to the Challenge Room or not. This method will always return `false` if an invalid or a negative grid index is passed.

**Use Cases:**

- 检测玩家是否满足进入挑战房的条件
- 自定义房间入口逻辑

**See also:** 
[[#GetCurrentRoomIndex|GetCurrentRoomIndex]], [[#GetRoomByIdx|GetRoomByIdx]]


---

### CanSpawnDevilRoom {#CanSpawnDevilRoom}

```
boolean CanSpawnDevilRoom ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检查当前楼层是否有生成恶魔房的条件。

**Use Cases:**

- 判断打完首领后是否会出现恶魔房
- 动态调整房间生成前条件

**See also:** 
[[#DisableDevilRoom|DisableDevilRoom]], [[#InitializeDevilAngelRoom|InitializeDevilAngelRoom]]


---

### CanStageHaveCurseOfLabyrinth {#CanStageHaveCurseOfLabyrinth}

```
boolean CanStageHaveCurseOfLabyrinth ( LevelStage Stage )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

判断指定阶段是否可以附带迷宫诅咒（Curse of Labyrinth）。

**Use Cases:**

- 验证特定楼层能否被诅咒扭转结构
- 避免在不适用场景施加迷宫诅咒

**See also:** 
[[#AddCurse|AddCurse]], [[#GetStage|GetStage]]


---

### ChangeRoom {#ChangeRoom}

```
void ChangeRoom ( int RoomIndex, int Dimension = -1 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

强制将玩家切换至指定房间索引和维度，但存在特效层更新问题，推荐使用 Game.ChangeRoom。

**Use Cases:**

- 快速传送至目标房间
- 实现非标准房间转移（不推荐）

**See also:** 
[[#GetCurrentRoomIndex|GetCurrentRoomIndex]]


---

### DisableDevilRoom {#DisableDevilRoom}

```
void DisableDevilRoom ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

禁用当前楼层恶魔房的生成。

**Use Cases:**

- 强制取消已满足的恶魔房出现
- 锁定楼层为天使房专用

**See also:** 
[[#CanSpawnDevilRoom|CanSpawnDevilRoom]], [[#InitializeDevilAngelRoom|InitializeDevilAngelRoom]]


---

### ForceHorsemanBoss {#ForceHorsemanBoss}

```
boolean ForceHorsemanBoss ( int Seed )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

根据提供的种子强制将首领替换为天启骑士类型，成功返回 true。

Returns `true` on success.

**Use Cases:**

- 固定楼层首领为指定骑士
- 打造基于种子的首领挑战

**See also:** 
[[#GetDungeonPlacementSeed|GetDungeonPlacementSeed]]


---

### GetAbsoluteStage {#GetAbsoluteStage}

```
LevelStage GetAbsoluteStage ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取绝对楼层阶段，贪婪模式下会映射为对应的普通楼层阶段。

In non-Greed Mode, returns the same thing as the `GetStage()` method. In Greed Mode, returns the adjusted stage similar to what it would be in non-Greed Mode.

**Use Cases:**

- 统一处理贪婪与非贪婪模式下的楼层逻辑
- 计算近似进度或难度

**See also:** 
[[#GetStage|GetStage]], [[#GetStageType|GetStageType]]


---

### GetAngelRoomChance {#GetAngelRoomChance}

```
float GetAngelRoomChance ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取当前楼层天使房概率修正值，实际天使房概率为 50% + 该值。

Gets the modifier value of the chance for this floor's deal to be an Angel room. Specifically, the actual effective chance for a deal to be an Angel room is 50% plus this value.

**Use Cases:**

- 读取当前天使房出现几率
- 确定是否需要干预房间生成

**See also:** 
[[#AddAngelRoomChance|AddAngelRoomChance]], [[#InitializeDevilAngelRoom|InitializeDevilAngelRoom]]


---

### GetCanSeeEverything {#GetCanSeeEverything}

```
boolean GetCanSeeEverything ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回楼层是否处于全图可见状态（通常由星象道具等提供）。

**Use Cases:**

- 检查玩家是否拥有永久全图效果
- 根据可见性调整UI或逻辑

**See also:** 
[[#SetCanSeeEverything|SetCanSeeEverything]], [[#ApplyMapEffect|ApplyMapEffect]]


---

### GetCurrentRoom {#GetCurrentRoom}

```
Room GetCurrentRoom ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取当前房间的 Room 对象。

**Use Cases:**

- 直接操作当前房间的实体和网格
- 读取房间类型与生成细节

**See also:** 
[[#GetCurrentRoomDesc|GetCurrentRoomDesc]], [[#GetRoomByIdx|GetRoomByIdx]]


---

### GetCurrentRoomDesc {#GetCurrentRoomDesc}

```
const RoomDescriptor GetCurrentRoomDesc ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取当前房间的只读 RoomDescriptor，若需修改请使用 GetRoomByIdx 与当前索引配合。

This functions returns a read only version of the [RoomDescriptor](RoomDescriptor.md) of the current room. If you want to edit the [RoomDescriptor](RoomDescriptor.md), use `GetRoomByIdx()` with `GetCurrentRoomIndex()` instead.

**Use Cases:**

- 安全地读取当前房间属性
- 防止误修改导致结构破坏

**See also:** 
[[#GetRoomByIdx|GetRoomByIdx]], [[#GetCurrentRoomIndex|GetCurrentRoomIndex]]


---

### GetCurrentRoomIndex {#GetCurrentRoomIndex}

```
int GetCurrentRoomIndex ( )
```

*DLC: AB+, REP, REP+*

返回当前房间在楼层网格上的索引（进入此房间时的位置）。

**Use Cases:**

- 定位当前房间坐标
- 配合房间列表进行遍历

**See also:** 
[[#GetCurrentRoomDesc|GetCurrentRoomDesc]], [[#GetRoomByIdx|GetRoomByIdx]]


---

### GetCurseName {#GetCurseName}

```
string GetCurseName ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取当前楼层活动诅咒的名称字符串。

**Use Cases:**

- 显示当前诅咒提示
- 日志记录或UI展示

**See also:** 
[[#GetCurses|GetCurses]], [[#AddCurse|AddCurse]]


---

### GetCurses {#GetCurses}

```
LevelCurse GetCurses ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取当前楼层所有激活的诅咒位掩码。

**Use Cases:**

- 检测是否有特定诅咒
- 基于诅咒组合编写逻辑

**See also:** 
[[#AddCurse|AddCurse]], [[#RemoveCurses|RemoveCurses]]


---

### GetDevilAngelRoomRNG {#GetDevilAngelRoomRNG}

```
RNG GetDevilAngelRoomRNG ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

提供恶魔/天使房生成所需的专用 RNG 对象。

**Use Cases:**

- 保存后重现代替原生成流程
- 自定义房间类型选择算法

**See also:** 
[[#InitializeDevilAngelRoom|InitializeDevilAngelRoom]], [[#CanSpawnDevilRoom|CanSpawnDevilRoom]]


---

### GetDungeonPlacementSeed {#GetDungeonPlacementSeed}

```
int GetDungeonPlacementSeed ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回决定地牢房间布局的随机种子。

**Use Cases:**

- 复现或分析楼层结构生成
- 联动种子进行自定义房间放置

**See also:** 
[[#GetRandomRoomIndex|GetRandomRoomIndex]], [[#GetStartingRoomIndex|GetStartingRoomIndex]]


---

### GetEnterPosition {#GetEnterPosition}

```
Vector GetEnterPosition ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取玩家进入本楼层时的初始位置坐标。

**Use Cases:**

- 放置初始传送点
- 重置玩家位置到楼层起点

**See also:** 
[[#GetStartingRoomIndex|GetStartingRoomIndex]], [[#GetCurrentRoom|GetCurrentRoom]]


---

### GetHeartPicked {#GetHeartPicked}

```
boolean GetHeartPicked ( )
```

*DLC: AB+, REP, REP+*

返回玩家是否已经在本楼层拾取了红心（用于某些成就或条件判断）。

**Use Cases:**

- 跟踪无伤成就条件
- 触发特定的事件逻辑

**See also:** 
[[#SetHeartPicked|SetHeartPicked]]


---

### GetLastBossRoomListIndex {#GetLastBossRoomListIndex}

```
int GetLastBossRoomListIndex ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回上一个首领房间在房间列表中的索引。

**Use Cases:**

- 定位前一个首领房位置
- 连续性首领挑战设计

**See also:** 
[[#GetRooms|GetRooms]], [[#GetCurrentRoomIndex|GetCurrentRoomIndex]]


---

### GetLastRoomDesc {#GetLastRoomDesc}

```
const RoomDescriptor GetLastRoomDesc ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取上一离开房间的只读 RoomDescriptor。

**Use Cases:**

- 回溯玩家来源房间属性
- 门类型逻辑判断

**See also:** 
[[#GetPreviousRoomIndex|GetPreviousRoomIndex]], [[#GetCurrentRoomDesc|GetCurrentRoomDesc]]


---

### GetName {#GetName}

```
string GetName ( )
```

*DLC: AB+, REP | Modifiers: const*

返回当前楼层的名称字符串。

**Use Cases:**

- UI 标题显示
- 根据名称定制效果

**See also:** 
[[#GetStage|GetStage]], [[#GetStageType|GetStageType]]


---

### GetNonCompleteRoomIndex {#GetNonCompleteRoomIndex}

```
int GetNonCompleteRoomIndex ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取楼层中尚未完成（点亮）的房间网格索引。

**Use Cases:**

- 寻找未探索房间用于回溯
- 自动化道具捕获路径

**See also:** 
[[#GetRoomCount|GetRoomCount]], [[#GetRooms|GetRooms]]


---

### GetPlanetariumChance {#GetPlanetariumChance}

```
float GetPlanetariumChance ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前楼层生成星象房的概率（0-1范围）。

Returns the probability of getting a Planetarium (in the 0-1 range)

**Use Cases:**

- 检测星象房开启可能性
- 调整奖励房间生成逻辑

**See also:** 
[[#GetAngelRoomChance|GetAngelRoomChance]], [[#CanSpawnDevilRoom|CanSpawnDevilRoom]]


---

### GetPreviousRoomIndex {#GetPreviousRoomIndex}

```
int GetPreviousRoomIndex ( )
```

*DLC: REP, REP+ | Modifiers: const*

返回玩家上一个所在房间的网格索引。

**Use Cases:**

- 快速实现按原路返回功能
- 追踪玩家路径

**See also:** 
[[#GetLastRoomDesc|GetLastRoomDesc]], [[#GetCurrentRoomIndex|GetCurrentRoomIndex]]


---

### GetRandomRoomIndex {#GetRandomRoomIndex}

```
int GetRandomRoomIndex ( boolean IAmErrorRoom, int Seed )
```

*DLC: AB+, REP, REP+*

返回一个随机房间索引，可指定是否为错误房并提供种子。

**Use Cases:**

- 随机传送或生成奖励房入口
- 配合特定种子生成固定随机结果

**See also:** 
[[#GetDungeonPlacementSeed|GetDungeonPlacementSeed]], [[#GetRoomByIdx|GetRoomByIdx]]


---

### GetRoomByIdx {#GetRoomByIdx}

```
RoomDescriptor GetRoomByIdx ( int RoomIdx, int Dimension = -1 )
```

*DLC: AB+, REP, REP+*

根据索引及维度获取可修改的 RoomDescriptor，务必检查返回值有效性。

**Use Cases:**

- 直接编辑房间属性（如清除标记）
- 跨维度访问死亡证明等特殊区域

**See also:** 
[[#GetCurrentRoomDesc|GetCurrentRoomDesc]], [[#GetRooms|GetRooms]]


---

### GetRoomCount {#GetRoomCount}

```
int GetRoomCount ( )
```

*DLC: AB+, REP, REP+*

返回当前楼层已生成房间的总数量。

**Use Cases:**

- 遍历全部房间时设定循环上限
- 统计楼层规模

**See also:** 
[[#GetRooms|GetRooms]], [[#GetNonCompleteRoomIndex|GetNonCompleteRoomIndex]]


---

### GetRooms {#GetRooms}

```
RoomDescriptor List GetRooms ( )
```

*DLC: AB+, REP, REP+*

返回当前楼层所有 RoomDescriptor 的列表容器。

**Use Cases:**

- 批量处理房间状态
- 搜索特定类型房间

**See also:** 
[[#GetRoomByIdx|GetRoomByIdx]], [[#GetRoomCount|GetRoomCount]]


---

### GetStage {#GetStage}

```
LevelStage GetStage ( )
```

*DLC: AB+, REP, REP+*

获取当前楼层的阶段（如 Basement=1, Caves=2 等）。

**Use Cases:**

- 依据阶段调整掉落或敌人强度
- 确定楼层进度

**See also:** 
[[#GetAbsoluteStage|GetAbsoluteStage]], [[#GetStageType|GetStageType]]


---

### GetStageType {#GetStageType}

```
StageType GetStageType ( )
```

*DLC: AB+, REP, REP+*

获取当前楼层的变体类型（如 Basement=0, Cellar=1, Burning Basement=2 等）。

The [StageType](enums/StageType.md) describes the variant of the current stage.

**Use Cases:**

- 区分楼层主题风格
- 为不同变体定制特殊事件

**See also:** 
[[#IsAltStage|IsAltStage]], [[#GetStage|GetStage]]


---

### GetStartingRoomIndex {#GetStartingRoomIndex}

```
int GetStartingRoomIndex ( )
```

*DLC: AB+, REP, REP+*

返回当前楼层起始房间的网格索引。

Returns the gridindex of the starting room of the current level.

**Use Cases:**

- 传送回出生房间
- 初始化玩家位置

**See also:** 
[[#GetEnterPosition|GetEnterPosition]], [[#GetCurrentRoomIndex|GetCurrentRoomIndex]]


---

### GetStateFlag {#GetStateFlag}

```
boolean GetStateFlag ( LevelStateFlag LevelStateFlag)
```

*DLC: AB+, REP, REP+*

根据传入的 LevelStateFlag 枚举查询对应的楼层状态是否启用。

**Use Cases:**

- 检查楼层特定全局标志（如商店已生成等）
- 条件性触发事件

**See also:** 
[[#HasBossChallenge|HasBossChallenge]]


---

### HasBossChallenge {#HasBossChallenge}

```
boolean HasBossChallenge ( )
```

*DLC: AB+, REP, REP+*

返回当前楼层是否存在首领挑战（Boss Rush）。

**Use Cases:**

- 检测是否在限定时间内到达
- 控制Boss Rush门的显示

**See also:** 
[[#CanOpenChallengeRoom|CanOpenChallengeRoom]], [[#GetStateFlag|GetStateFlag]]


---

### InitializeDevilAngelRoom {#InitializeDevilAngelRoom}

```
void InitializeDevilAngelRoom ( boolean ForceAngel, boolean ForceDevil )
```

*DLC: AB+, REP, REP+*

锁定本楼层恶魔/天使房间类型选择，此后无法变更，除非清除相关房间数据。

By calling this function, it "locks in" the choice between a Devil Room and an Angel Room for the current floor.

**Use Cases:**

- 强制触发天使房或恶魔房
- 在击败首领前固定房间类型

**See also:** 
[[#GetAngelRoomChance|GetAngelRoomChance]], [[#DisableDevilRoom|DisableDevilRoom]]


---

### IsAltStage {#IsAltStage}

```
boolean IsAltStage ( )
```

*DLC: AB+, REP, REP+*

判断当前楼层是否为替代楼层（如 Downpour, Mausoleum 等非原始变体）。

Returns `true` if the level's [StageType](enums/StageType.md) is not `StageType.STAGE_ORIGINAL`.

**Use Cases:**

- 区分原始路线与回溯路线
- 应用不同的掉落表或敌人配置

**See also:** 
[[#GetStageType|GetStageType]], [[#IsAscent|IsAscent]]


---

### IsAscent {#IsAscent}

```
boolean IsAscent ( )
```

*DLC: AB+, REP, REP+*

Returns true if the player is currently in the Ascent (after defeating Mom).

Returns `true` if the player is in the Ascent.

**Use Cases:**

- Modifying behavior after the Mom fight
- Unlocking achievements tied to the Ascent
- Conditional logic for ascension-specific events

**See also:** 
[[#IsPreAscent|IsPreAscent]], [[#GetStage|GetStage]], [[#IsNextStageAvailable|IsNextStageAvailable]]


---

### IsDevilRoomDisabled {#IsDevilRoomDisabled}

```
boolean IsDevilRoomDisabled ( )
```

*DLC: AB+, REP, REP+*

Checks whether the Devil Room is disabled for the current floor.

**Use Cases:**

- Determining if a Devil/Angel room can spawn
- Conditional rewards or challenges

**See also:** 
[[#DisableDevilRoom|DisableDevilRoom]], [[#CanSpawnDevilRoom|CanSpawnDevilRoom]], [[#InitializeDevilAngelRoom|InitializeDevilAngelRoom]]


---

### IsNextStageAvailable {#IsNextStageAvailable}

```
boolean IsNextStageAvailable ( )
```

*DLC: AB+, REP, REP+*

Returns false if on a final floor (e.g., Chest, Dark Room, The Void, Home), otherwise true.

Returns `false` if on a final floor (Chest/Dark Room, The Void, Home). Returns `true` otherwise, including cases where the next stage is technically not available such as not having the Polaroid or Negative when entering its respective Big Chest or beating Hush for the first time.

**Use Cases:**

- Preventing progression on final floors
- Checking if a next stage exists for custom transitions
- Controlling when a run should end

**See also:** 
[[#GetStage|GetStage]], [[#SetNextStage|SetNextStage]], [[#IsAscent|IsAscent]]


---

### IsPreAscent {#IsPreAscent}

```
boolean IsPreAscent ( )
```

*DLC: AB+, REP, REP+*

Returns true if the player is in the special Mausoleum/Gehenna II stage that leads to the Ascent.

Returns `true` if the player is in the version of Mausoleum/Gehenna II leading to the Ascent.

**Use Cases:**

- Preparing for The Beast encounter
- Custom door/event triggers before final ascent

**See also:** 
[[#IsAscent|IsAscent]], [[#GetStage|GetStage]], [[#GetStageType|GetStageType]]


---

### MakeRedRoomDoor {#MakeRedRoomDoor}

```
boolean MakeRedRoomDoor ( int CurrentRoomIdx, DoorSlot Slot )
```

*DLC: AB+, REP, REP+*

Attempts to create a red room door at the specified room index and door slot, returning true on success.

Attempts to create a red room door in the given room at the given door slot. Returns `true` on success.

**Use Cases:**

- Generating extra red rooms connected or disconnected
- Custom floor expansion mechanics

**See also:** 
[[#GetRoomByIdx|GetRoomByIdx]], [[#GetCurrentRoomIndex|GetCurrentRoomIndex]], [[#QueryRoomTypeIndex|QueryRoomTypeIndex]]


---

### QueryRoomTypeIndex {#QueryRoomTypeIndex}

```
int QueryRoomTypeIndex ( RoomType RoomType, boolean Visited, RNG rng, boolean IgnoreGroup = false )
```

*DLC: AB+, REP, REP+*

Queries a room layout index for a given RoomType, using visited status, an RNG, and an optional group ignore flag.

IgnoreGroup: If set to `true`, includes rooms that do not have the same group ID as the current room (currently unused)

**Use Cases:**

- Procedural room generation
- Finding specific room variants

**See also:** 
[[#GetRoomByIdx|GetRoomByIdx]], [[#MakeRedRoomDoor|MakeRedRoomDoor]]


---

### RemoveCompassEffect {#RemoveCompassEffect}

```
void RemoveCompassEffect ( )
```

*DLC: REP, REP+*

Removes the Compass map effect, hiding special room icons from the map.

**Use Cases:**

- Resetting map effects
- Custom map reveal items

**See also:** 
[[#ApplyCompassEffect|ApplyCompassEffect]], [[#ShowMap|ShowMap]], [[#ApplyMapEffect|ApplyMapEffect]]


---

### RemoveCurses {#RemoveCurses}

```
void RemoveCurses ( LevelCurse Curses )
```

*DLC: REP, REP+ | Modifiers: const*

Removes one or more curses from the current floor using a LevelCurse bitmask.

Curses: A bitmask of LevelCurse that indicates which curses will be removed

**Use Cases:**

- Curse removal by items or pills
- Debugging curse effects

**See also:** 
[[#AddCurse|AddCurse]], [[#GetCurses|GetCurses]], [[#GetCurseName|GetCurseName]]


---

### SetCanSeeEverything {#SetCanSeeEverything}

```
void SetCanSeeEverything ( boolean Value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Sets whether the player can see the entire map (all rooms visible).

**Use Cases:**

- Full map reveal items (e.g., The World)
- Debugging and testing

**See also:** 
[[#GetCanSeeEverything|GetCanSeeEverything]], [[#ApplyMapEffect|ApplyMapEffect]], [[#ShowMap|ShowMap]]


---

### SetHeartPicked {#SetHeartPicked}

```
void SetHeartPicked ( )
```

*DLC: AB+, REP, REP+*

Marks that the floor's heart drop has been picked up, preventing further heart drops.

**Use Cases:**

- Controlling heart drop mechanics
- Tracking player progress on a floor

**See also:** 
[[#GetHeartPicked|GetHeartPicked]]


---

### SetNextStage {#SetNextStage}

```
void SetNextStage ( )
```

*DLC: AB+, REP, REP+*

Advances to the next stage without applying full floor changes; use reseed or StartStageTransition to complete.

This function puts you in the next stage without applying any of the floor changes. For the changes to fully apply, either use the `reseed` [console command](tutorials/DebugConsole.md#reseed), or [Game.StartStageTransition](Game.md#startstagetransition).

**Use Cases:**

- Fast floor skipping
- Debugging stage progression

**See also:** 
[[#SetStage|SetStage]], [[#IsNextStageAvailable|IsNextStageAvailable]]


---

### SetRedHeartDamage {#SetRedHeartDamage}

```
void SetRedHeartDamage ( )
```

*DLC: AB+, REP, REP+*

Marks that red heart damage has been taken on this floor, affecting Devil Room chance.

**Use Cases:**

- Manipulating devil/angel room spawn conditions
- Custom penalty systems

**See also:** 
[[#CanSpawnDevilRoom|CanSpawnDevilRoom]]


---

### SetStage {#SetStage}

```
void SetStage ( int StageOffset, int StageTypeOffset )
```

*DLC: AB+, REP, REP+*

Changes the current floor and stage type using numeric offsets.

This function changes the current floor, and it's stage. For the changes to fully apply, either use the `reseed` [console command](tutorials/DebugConsole.md#reseed), or [Game.StartStageTransition](Game.md#startstagetransition).

**Use Cases:**

- Warping to different floors
- Custom level generation

**See also:** 
[[#GetStage|GetStage]], [[#GetStageType|GetStageType]], [[#SetNextStage|SetNextStage]]


---

### SetStateFlag {#SetStateFlag}

```
void SetStateFlag ( LevelStateFlag LevelStateFlag, boolean Val )
```

*DLC: AB+, REP, REP+*

Sets a LevelStateFlag to the given boolean value for the current level.

**Use Cases:**

- Managing floor-specific states (e.g., Boss Rush, red rooms)
- Activating or deactivating special room conditions

**See also:** 
[[#GetStateFlag|GetStateFlag]], [[#MakeRedRoomDoor|MakeRedRoomDoor]]


---

### ShowMap {#ShowMap}

```
void ShowMap ( )
```

*DLC: AB+, REP, REP+*

Reveals all rooms on the map except the top secret room, similar to a World card effect.

Show's all map (world/sun card effect) except the top secret room.

**Use Cases:**

- Map reveal items
- Debugging map layout

**See also:** 
[[#ApplyMapEffect|ApplyMapEffect]], [[#SetCanSeeEverything|SetCanSeeEverything]], [[#UpdateVisibility|UpdateVisibility]]


---

### ShowName {#ShowName}

```
void ShowName ( boolean Sticky )
```

*DLC: AB+, REP, REP+*

Displays the floor name banner, optionally sticky (persistent).

**Use Cases:**

- Custom floor introductions
- Cutscenes or modded floor naming

**See also:** 
[[#GetName|GetName]]


---

### UncoverHiddenDoor {#UncoverHiddenDoor}

```
void UncoverHiddenDoor ( int CurrentRoomIdx, DoorSlot Slot )
```

*DLC: AB+, REP, REP+*

Uncovers a hidden door (e.g., secret room door) between two rooms by modifying grid entities.

Uncovers the door on both sides by modifying the saved grid entities for neighboring room.

**Use Cases:**

- Mods that reveal secret rooms automatically
- Puzzle room mechanics

**See also:** 
[[#MakeRedRoomDoor|MakeRedRoomDoor]], [[#GetRoomByIdx|GetRoomByIdx]], [[#GetCurrentRoomIndex|GetCurrentRoomIndex]]


---

### Update {#Update}

```
void Update ( )
```

*DLC: AB+, REP, REP+*

Updates the Level state each frame; normally called internally.

**Use Cases:**

- Rarely called manually; engine internal

**See also:** 
[[#UpdateVisibility|UpdateVisibility]]


---

### UpdateVisibility {#UpdateVisibility}

```
void UpdateVisibility ( )
```

*DLC: REP, REP+*

Recalculates room visibility based on player position and current map effects.

**Use Cases:**

- Refreshing the map after changes
- Ensuring fog of war updates correctly

**See also:** 
[[#Update|Update]], [[#SetCanSeeEverything|SetCanSeeEverything]]


---

### DungeonReturnPosition {#DungeonReturnPosition}

```
Vector DungeonReturnPosition
```

*DLC: REP, REP+*

Stores the Vector position on the main floor from which the player entered a sub-dungeon.

**Use Cases:**

- Returning from a minigame or alternate dimension
- Teleporting back after a dungeon exit

**See also:** 
[[#DungeonReturnRoomIndex|DungeonReturnRoomIndex]]


---

### DungeonReturnRoomIndex {#DungeonReturnRoomIndex}

```
int DungeonReturnRoomIndex
```

*DLC: REP, REP+*

Stores the room index on the main floor to return to after a sub-dungeon.

**Use Cases:**

- Paired with DungeonReturnPosition for clean returns
- Mods that create custom dungeons

**See also:** 
[[#DungeonReturnPosition|DungeonReturnPosition]]


---

### EnterDoor {#EnterDoor}

```
int EnterDoor
```

*DLC: AB+, REP, REP+*

Indicates the door slot used to enter the current room.

**Use Cases:**

- Determining which direction the player came from
- Custom entry effects

**See also:** 
[[#LeaveDoor|LeaveDoor]], [[#GetCurrentRoomIndex|GetCurrentRoomIndex]]


---

### GreedModeWave {#GreedModeWave}

```
int GreedModeWave
```

*DLC: AB+, REP, REP+*

The current wave number in Greed Mode.

**Use Cases:**

- Tracking wave progression
- Spawning enemies or items per wave

**See also:** 
[[#GetStage|GetStage]]


---

### LeaveDoor {#LeaveDoor}

```
int LeaveDoor
```

*DLC: AB+, REP, REP+*

Indicates the door slot used when leaving the previous room.

**Use Cases:**

- Backtracking logic
- Room transition animations

**See also:** 
[[#EnterDoor|EnterDoor]], [[#GetPreviousRoomIndex|GetPreviousRoomIndex]]


---

## See Also

- [[Game]]
- [[Level]]
- [[RNG]]
- [[Room]]
- [[RoomDescriptor]]
- [[Vector]]
