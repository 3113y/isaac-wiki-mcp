---
title: EntityNPC
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 37
---

# EntityNPC

## Summary

EntityNPC 表示游戏中的所有非玩家实体，包括敌人、Boss、友方 NPC 以及特殊单位。提供控制动画、发射弹幕、形态转换、精英化、查询与寻路等丰富功能，是操作 NPC 行为的核心类。

## Inheritance

- Inherits from: [[Entity]]

## Related Types

- [[Color]]
- [[EntityEffect]]
- [[EntityList]]
- [[EntityProjectile]]
- [[EntityRef]]
- [[PathFinder]]
- [[ProjectileParams]]
- [[Vector]]

## Key Methods

- [[#Morph|Morph]]
- [[#FireBossProjectiles|FireBossProjectiles]]
- [[#FireProjectiles|FireProjectiles]]
- [[#GetPlayerTarget|GetPlayerTarget]]
- [[#QueryNPCsType|QueryNPCsType]]

## Methods

### Functions

### AnimWalkFrame {#AnimWalkFrame}

```
void AnimWalkFrame ( string HorizontalAnim, string VerticalAnim, float SpeedThreshold )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

根据水平移动方向 HorizontalAnim 和垂直移动方向 VerticalAnim 播放对应的行走动画帧，当移动速度超过 SpeedThreshold 时触发。

**Use Cases:**

- 为自定义 NPC 设置不同方向的行走动画
- 在速度变化时动态切换动画帧

**See also:** 



---

### CalcTargetPosition {#CalcTargetPosition}

```
Vector CalcTargetPosition ( float DistanceLimit )
```

*DLC: REP, REP+ | Modifiers: const*

计算并返回一个限制在 DistanceLimit 范围内的目标位置向量，常用于敌人 AI 的移动目标计算。

**Use Cases:**

- 限制敌人追击范围
- 生成随机巡逻点

**See also:** 
[[#ResetPathFinderTarget|ResetPathFinderTarget]]


---

### CanBeDamagedFromVelocity {#CanBeDamagedFromVelocity}

```
boolean CanBeDamagedFromVelocity ( Vector Velocity )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

判断该 NPC 是否可以被给定的速度造成的伤害杀死（例如踩踏或碰撞伤害）。

**Use Cases:**

- 实现玩家踩踏敌人时的伤害判定
- 防止某些 NPC 被误杀

**See also:** 



---

### CanReroll {#CanReroll}

```
boolean CanReroll ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检查该 NPC 是否可以被重置（如 D10 骰子效果）。

**Use Cases:**

- 配合重置道具的逻辑筛选目标
- 防止独特敌人被意外重骰

**See also:** 



---

### FireBossProjectiles {#FireBossProjectiles}

```
EntityProjectile FireBossProjectiles ( int NumProjectiles, Vector TargetPos, float TrajectoryModifier, ProjectileParams Params )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

向 TargetPos 发射一系列 Boss 弹幕，数量为 NumProjectiles，可通过 TrajectoryModifier 调整轨迹随机性，使用 FallingAccelModifier 可使弹幕加速下落。返回最后一个生成的弹幕指针。

发射一系列弹幕，目标可以是玩家，方向会随机化，或者在瞄准玩家时稍微随机化。可以使用 FallingAccelModifier 使弹幕更快落地。返回最后生成的弹幕指针（例如，当 NumProjectiles=1 时很有用）。

**Use Cases:**

- 制造 Boss 的弹幕攻击模式
- 实现从天而降的弹幕雨

**See also:** 
[[#FireProjectiles|FireProjectiles]]


---

### FireProjectiles {#FireProjectiles}

```
void FireProjectiles ( Vector Pos, Vector Velocity, ProjectilesMode Mode, ProjectileParams Params )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

从指定位置 Pos 以 Velocity 方向和速度发射指定 Mode（模式0~9）的弹幕组合，弹幕参数通过 Params 配置。

**Use Cases:**

- 实现多重弹幕攻击（扇形、圆形、十字形等）
- 自定义敌人弹幕散布

**See also:** 
[[#FireBossProjectiles|FireBossProjectiles]]


---

### GetAliveEnemyCount {#GetAliveEnemyCount}

```
int GetAliveEnemyCount ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前房间内存活敌人的数量，供友方 NPC 重新定向攻击目标时使用。

**Use Cases:**

- 友方 NPC 寻找剩余敌人
- 动态调整敌人生成逻辑

**See also:** 
[[#GetPlayerTarget|GetPlayerTarget]]


---

### GetBossColorIdx {#GetBossColorIdx}

```
int GetBossColorIdx ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取 Boss 的颜色索引，实际存储值比 bosscolors.xml 中定义的索引小1，使用时需加1。

**Use Cases:**

- 读取 Boss 当前颜色配置
- 联动精英系统进行视觉调整

**See also:** 
[[#GetChampionColorIdx|GetChampionColorIdx]]


---

### GetChampionColorIdx {#GetChampionColorIdx}

```
ChampionColorIdx GetChampionColorIdx ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回该 NPC 的精英颜色索引，若未成为精英怪则返回 -1。

**Use Cases:**

- 判断敌人是否为精英
- 根据精英类型调整掉落或行为

**See also:** 
[[#IsChampion|IsChampion]], [[#MakeChampion|MakeChampion]]


---

### GetPlayerTarget {#GetPlayerTarget}

```
Entity GetPlayerTarget ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取该 NPC 当前锁定的玩家目标实体，若无'最好的朋友'等修饰符则直接返回玩家。

如果没有修饰符（最好的朋友），这将返回玩家

**Use Cases:**

- 敌人 AI 追逐特定玩家
- 友方 NPC 选择跟随对象

**See also:** 
[[#ResetPathFinderTarget|ResetPathFinderTarget]]


---

### IsBoss {#IsBoss}

```
boolean IsBoss ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

判断该 NPC 是否为 Boss 实体。

**Use Cases:**

- 区分 Boss 与小怪以应用不同逻辑
- 血量条显示或特殊死亡处理

**See also:** 
[[#IsChampion|IsChampion]], [[#GetBossColorIdx|GetBossColorIdx]]


---

### IsChampion {#IsChampion}

```
boolean IsChampion ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

判断该 NPC 是否为精英怪。

**Use Cases:**

- 触发精英特有掉落或行为
- UI 上标记精英敌人

**See also:** 
[[#GetChampionColorIdx|GetChampionColorIdx]], [[#MakeChampion|MakeChampion]]


---

### KillUnique {#KillUnique}

```
void KillUnique ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

以特殊死亡动画杀死该 NPC，例如 Flush! 对粪便敌人的效果。

对于具有独特死亡动画的实体，例如 Flush! 与粪便敌人。

**Use Cases:**

- 实现道具秒杀效果并播放特定动画
- 处理特定敌人的非普通死亡

**See also:** 



---

### MakeChampion {#MakeChampion}

```
void MakeChampion ( int Seed, ChampionColor ChampionColorIdx = -1, boolean Init = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

强制将一个非精英 NPC 转变为精英怪（ChampionColorIdx 指定类型或随机），并重置其生命值为最大值。Init 参数用于初次生成时调用。

强制非精英怪成为精英怪，重置生命值为最大生命值。

**Use Cases:**

- 将普通敌人升级为精英
- 自定义刷新房间时生成精英怪

**See also:** 
[[#IsChampion|IsChampion]], [[#GetChampionColorIdx|GetChampionColorIdx]], [[#Morph|Morph]]


---

### MakeSplat {#MakeSplat}

```
EntityEffect MakeSplat ( float Size )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

生成一个指定 Size 的飞溅（血溅）特效 EntityEffect，通常用于受伤或死亡时。

**Use Cases:**

- 敌人死亡时产生血溅
- 自定义受伤特效

**See also:** 



---

### Morph {#Morph}

```
boolean Morph ( EntityType type, int Variant, int SubType, int ChampionColorIdx )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将当前 NPC 变形为另一种实体类型（包括精英），通过 EntityType、Variant、SubType 和 ChampionColorIdx 指定。返回是否变形成功。注意无法通过此方法将精英转为普通。

**Use Cases:**

- 动态切换敌人形态（如第二形态）
- 触发特定 Boss 的阶段转换

**See also:** 
[[#MakeChampion|MakeChampion]], [[#IsChampion|IsChampion]]


---

### PlaySound {#PlaySound}

```
void PlaySound ( SoundEffect ID, float Volume, int FrameDelay, boolean Loop, float Pitch )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 PlaySound 完成对应 API 操作

**See also:** 



---

### QueryNPCsGroup {#QueryNPCsGroup}

```
EntityList QueryNPCsGroup ( int GroupIdx )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 QueryNPCsGroup 完成对应 API 操作

**See also:** 



---

### QueryNPCsSpawnerType {#QueryNPCsSpawnerType}

```
EntityList QueryNPCsSpawnerType ( EntityType SpawnerType, EntityType Type, boolean OnlyEnemies )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 QueryNPCsSpawnerType 完成对应 API 操作

**See also:** 



---

### QueryNPCsType {#QueryNPCsType}

```
EntityList QueryNPCsType ( EntityType Type, int Variant )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 QueryNPCsType 完成对应 API 操作

**See also:** 



---

### ResetPathFinderTarget {#ResetPathFinderTarget}

```
void ResetPathFinderTarget ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 ResetPathFinderTarget 完成对应 API 操作

**See also:** 



---

### ThrowSpider {#ThrowSpider}

```
static const EntityNPC ThrowSpider ( Vector Position, Entity Spawner, Vector TargetPos, boolean Big, float YOffset )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 ThrowSpider 完成对应 API 操作

**See also:** 



---

### CanShutDoors {#CanShutDoors}

```
boolean CanShutDoors
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 CanShutDoors 完成对应 API 操作

**See also:** 



---

### ChildNPC {#ChildNPC}

```
const EntityNPC ChildNPC {: .copyable aria-label='Variables' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 ChildNPC 完成对应 API 操作

**See also:** 



---

### EntityRef {#EntityRef}

```
Entity EntityRef
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 EntityRef 完成对应 API 操作

**See also:** 



---

### GroupIdx {#GroupIdx}

```
int GroupIdx
```

*DLC: AB+, REP | Modifiers: const*

Used to identify multichunks groups.

Used to identify multichunks groups.

**Use Cases:**

- 调用 GroupIdx 完成对应 API 操作

**See also:** 



---

### I1 {#I1}

```
int I1
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 I1 完成对应 API 操作

**See also:** 



---

### I2 {#I2}

```
int I2
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 I2 完成对应 API 操作

**See also:** 



---

### ParentNPC {#ParentNPC}

```
const EntityNPC ParentNPC {: .copyable aria-label='Variables' data-altreturn='nil' }
```

*DLC: REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 ParentNPC 完成对应 API 操作

**See also:** 



---

### Pathfinder {#Pathfinder}

```
PathFinder Pathfinder
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Pathfinder 完成对应 API 操作

**See also:** 



---

### ProjectileCooldown {#ProjectileCooldown}

```
int ProjectileCooldown
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 ProjectileCooldown 完成对应 API 操作

**See also:** 



---

### ProjectileDelay {#ProjectileDelay}

```
int ProjectileDelay
```

*DLC: AB+, REP, REP+*

&gt;0: projectile will be fired in n frames

&gt;0: projectile will be fired in n frames

**Use Cases:**

- 调用 ProjectileDelay 完成对应 API 操作

**See also:** 



---

### Scale {#Scale}

```
float Scale
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Scale 完成对应 API 操作

**See also:** 



---

### State {#State}

```
NpcState State
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 State 完成对应 API 操作

**See also:** 



---

### StateFrame {#StateFrame}

```
int StateFrame
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 StateFrame 完成对应 API 操作

**See also:** 



---

### V1 {#V1}

```
Vector V1
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 V1 完成对应 API 操作

**See also:** 



---

### V2 {#V2}

```
Vector V2
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 V2 完成对应 API 操作

**See also:** 



---

## See Also

- [[Color]]
- [[Entity]]
- [[EntityEffect]]
- [[EntityList]]
- [[EntityNPC]]
- [[EntityProjectile]]
- [[EntityRef]]
- [[PathFinder]]
- [[ProjectileParams]]
- [[Vector]]
