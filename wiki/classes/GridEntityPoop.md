---
title: GridEntityPoop
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 6
---

# GridEntityPoop

## Summary

代表游戏中的粪便网格实体，提供管理粪便生成率、重生机制、状态动画以及与玩家交互判断的功能。

## Inheritance

- Inherits from: [[GridEntity]]

## Key Methods

- [[#ReduceSpawnRate|ReduceSpawnRate]]
- [[#RespawnRedPoop|RespawnRedPoop]]
- [[#ReviveTimer|ReviveTimer]]
- [[#StateAnimation|StateAnimation]]
- [[#UnderPlayer|UnderPlayer]]

## Methods

### Functions

### ReduceSpawnRate {#ReduceSpawnRate}

```
void ReduceSpawnRate ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

降低粪便的生成率，可能用于控制特殊粪便出现的频率或调整游戏难度。

**Use Cases:**

- 减少红色粪便大量涌现的概率
- 动态平衡游戏过程中粪便的产生速度

**See also:** 
[[#RespawnRedPoop|RespawnRedPoop]]


---

### RespawnRedPoop {#RespawnRedPoop}

```
void RespawnRedPoop ( )
```

*DLC: REP, REP+ | Modifiers: const*

重新生成红色粪便，通常配合计时器或其他条件实现粪便的重生机制。

**Use Cases:**

- 触发红大便的复活流程
- 在被破坏或变化后恢复粪便实体

**See also:** 
[[#ReviveTimer|ReviveTimer]], [[#ReduceSpawnRate|ReduceSpawnRate]]


---

### ReducedSpawnRate {#ReducedSpawnRate}

```
boolean ReducedSpawnRate
```

*DLC: AB+, REP, REP+ | Modifiers: const*

已移除的布尔属性，曾在 Repentance 之前用于标识生成率是否已被降低。

This attribute got removed with Repentance.

**Use Cases:**

- 在旧版本中检查粪便生成率降低状态

**See also:** 



---

### ReviveTimer {#ReviveTimer}

```
int ReviveTimer
```

*DLC: AB+, REP, REP+ | Modifiers: const*

整型计时器，用于控制红色粪便重生的倒计时，到达一定数值后触发重生。

**Use Cases:**

- 读取或设置复活前的等待时间
- 实现延迟重生逻辑

**See also:** 
[[#RespawnRedPoop|RespawnRedPoop]]


---

### StateAnimation {#StateAnimation}

```
string StateAnimation
```

*DLC: AB+, REP, REP+ | Modifiers: const*

字符串属性，表示当前粪便的动画状态名称，据此切换不同的视觉表现。

**Use Cases:**

- 同步粪便外观与行为状态（如正常、快要复活等）
- 根据游戏逻辑更换动画片段

**See also:** 
[[#RespawnRedPoop|RespawnRedPoop]]


---

### UnderPlayer {#UnderPlayer}

```
boolean UnderPlayer
```

*DLC: AB+, REP, REP+ | Modifiers: static*

布尔属性，指示玩家是否正站在该粪便上方，用于判断玩家离开的时刻。

Used to determine when player moves away from the poop.

**Use Cases:**

- 检测玩家离开后触发事件（如生成敌人）
- 实现需要玩家接触的特殊交互

**See also:** 
[[#RespawnRedPoop|RespawnRedPoop]]


---

## See Also

- [[GridEntity]]
