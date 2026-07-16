---
title: PathFinder
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 13
---

# PathFinder

## Summary

PathFinder 是用于控制非玩家角色（NPC）移动、路径规划和规避行为的工具类，提供了寻路、随机移动、逃避目标、路径检查等功能。

## Related Types

- [[Vector]]

## Key Methods

- [[#FindGridPath|FindGridPath]]
- [[#EvadeTarget|EvadeTarget]]
- [[#HasPathToPos|HasPathToPos]]
- [[#MoveRandomly|MoveRandomly]]
- [[#Reset|Reset]]

## Methods

### Functions

### EvadeTarget {#EvadeTarget}

```
void EvadeTarget ( Vector TargetPos )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

使实体远离指定目标位置，用于近距离回避，行为类似 Mulligoon。

**Use Cases:**

- 敌人感知到危险时进行规避
- 实现类似 Mulligoon 的后退躲闪机制

**See also:** 
[[#GetEvadeMovementCountdown|GetEvadeMovementCountdown]]


---

### FindGridPath {#FindGridPath}

```
void FindGridPath ( Vector Pos, float Speed, int PathMarker, boolean UseDirectPath )
```

*DLC: REP, REP+ | Modifiers: const*

引导实体以给定速度沿网格路径移向目标坐标，并可通过 PathMarker 设置所经过格子的寻路优先级。UseDirectPath 参数当前无效，实体总是沿轴对齐移动。

**Use Cases:**

- 敌人AI追踪玩家或逃向某点
- 自定义路径标记以影响后续寻路决策

**See also:** 
[[#Reset|Reset]], [[#ResetMovementTarget|ResetMovementTarget]], [[#HasDirectPath|HasDirectPath]], [[#UpdateGridIndex|UpdateGridIndex]]


---

### GetEvadeMovementCountdown {#GetEvadeMovementCountdown}

```
int GetEvadeMovementCountdown ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前逃避动作的剩余倒计时数值。

**Use Cases:**

- 检查逃避状态何时结束，以便切换回正常行为

**See also:** 
[[#EvadeTarget|EvadeTarget]]


---

### GetGridIndex {#GetGridIndex}

```
int GetGridIndex ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取实体当前所在位置的网格索引值。

**Use Cases:**

- 判断实体位于哪个格子，用于与 PathMarker 或网格实体交互

**See also:** 
[[#UpdateGridIndex|UpdateGridIndex]]


---

### HasDirectPath {#HasDirectPath}

```
boolean HasDirectPath ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检查实体是否拥有直达其目标的直接路径，仅当寻路器之前设置为直接路径模式时有效。

**Use Cases:**

- 判断是否可以直线冲向目标，无需绕路

**See also:** 
[[#FindGridPath|FindGridPath]]


---

### HasPathToPos {#HasPathToPos}

```
boolean HasPathToPos ( Vector Pos, boolean IgnorePoop )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

安全地检查给定位置是否可到达（不被岩石、坑等阻挡），不影响当前寻路器状态或成员变量。

Used for safe check if any NPC is behind rocks/pits, doesn't disturb class members.

**Use Cases:**

- 生成敌人前验证位置可达性
- 在不变更移动目标的前提下预判路径堵死情况

**See also:** 
[[#FindGridPath|FindGridPath]]


---

### MoveRandomly {#MoveRandomly}

```
boolean MoveRandomly ( boolean IgnoreStatusEffects )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

使实体全方向随机移动，行为类似 Gusher 敌人，返回是否成功开始移动。

**Use Cases:**

- 实现完全随机的漫游行为
- 制作不可预测的非追逐型敌人

**See also:** 
[[#MoveRandomlyBoss|MoveRandomlyBoss]], [[#MoveRandomlyAxisAligned|MoveRandomlyAxisAligned]]


---

### MoveRandomlyAxisAligned {#MoveRandomlyAxisAligned}

```
void MoveRandomlyAxisAligned ( float Speed, boolean IgnoreStatusEffects )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

使实体沿正交（轴对齐）方向随机移动，但由于已知Bug当前版本可能无实际效果。

**Use Cases:**

- 原本用于制作仅沿垂直/水平方向抖动的随机移动

**See also:** 
[[#MoveRandomly|MoveRandomly]]


---

### MoveRandomlyBoss {#MoveRandomlyBoss}

```
void MoveRandomlyBoss ( boolean IgnoreStatusEffects )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

使实体在随机游走的同时整体趋近玩家，模拟 Boss 的游走追击模式。

**Use Cases:**

- Boss 战中使用伪随机移动保持压迫感
- 让敌人看似无规律但逐步缩小距离

**See also:** 
[[#MoveRandomly|MoveRandomly]], [[#FindGridPath|FindGridPath]]


---

### Reset {#Reset}

```
void Reset ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

重置寻路器的内部状态，清空当前的路径数据与目标。

**Use Cases:**

- 在复用寻路器时清除旧配置
- 中断当前移动并准备新的寻路指令

**See also:** 
[[#ResetMovementTarget|ResetMovementTarget]], [[#FindGridPath|FindGridPath]]


---

### ResetMovementTarget {#ResetMovementTarget}

```
void ResetMovementTarget ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

清除当前设定的移动目标，使实体停止主动移动。

**Use Cases:**

- 立即取消寻路任务
- 准备接受新的目标点

**See also:** 
[[#Reset|Reset]], [[#FindGridPath|FindGridPath]]


---

### SetCanCrushRocks {#SetCanCrushRocks}

```
void SetCanCrushRocks ( boolean value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置实体是否能够压碎岩石的标记（当前版本无实际效果，既不改变实体行为也不影响 FindGridPath 的寻路判断）。

**Use Cases:**

- 为未来版本预留接口，意图允许敌人破坏障碍物

**See also:** 
[[#FindGridPath|FindGridPath]]


---

### UpdateGridIndex {#UpdateGridIndex}

```
void UpdateGridIndex ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 UpdateGridIndex 完成对应 API 操作

**See also:** 



---

## See Also

- [[Vector]]
