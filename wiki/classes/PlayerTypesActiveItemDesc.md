---
title: PlayerTypesActiveItemDesc
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 7
---

# PlayerTypesActiveItemDesc

## Summary

表示玩家所持主动道具的状态信息，记录充能、电池充能、物品类型及额外数据。

## Key Methods

- [[#Charge|Charge]]
- [[#Item|Item]]
- [[#PartialCharge|PartialCharge]]
- [[#VarData|VarData]]
- [[#BatteryCharge|BatteryCharge]]

## Methods

### Functions

### BatteryCharge {#BatteryCharge}

```
int BatteryCharge
```

*DLC: AB+, REP, REP+ | Modifiers: const*

表示从电池拾取中获得的额外充能值，独立于主充能计数。

**Use Cases:**

- 获取当前电池额外充能力度
- 修改电池补充量以自定义电池效果
- 计算道具总充能状态

**See also:** 
[[#Charge|Charge]], [[#PartialCharge|PartialCharge]], [[#Item|Item]]


---

### Charge {#Charge}

```
int Charge
```

*DLC: REP, REP+ | Modifiers: const*

表示主动道具的主充能次数，对罐子类道具也用于存储内含物数量。

For items like Jars this holds the number of flies/hearts.

**Use Cases:**

- 读取道具剩余使用次数
- 直接设置充能以修改道具行为
- 检查罐子类道具内收集的苍蝇或心数

**See also:** 
[[#Item|Item]], [[#PartialCharge|PartialCharge]], [[#VarData|VarData]]


---

### Item {#Item}

```
CollectibleType Item
```

*DLC: AB+, REP, REP+ | Modifiers: const*

表示当前所持主动道具的物品类型，用于识别具体道具。

**Use Cases:**

- 判断玩家当前装备的主动道具
- 基于道具类型编写条件逻辑
- 在主动道具切换后同步相关数据

**See also:** 
[[#Charge|Charge]], [[#VarData|VarData]]


---

### PartialCharge {#PartialCharge}

```
float PartialCharge
```

*DLC: AB+, REP, REP+ | Modifiers: const*

表示充能的分数进度（0-1），用于实现平滑充能显示和4.5伏特等效果。

How close the item is to gaining another charge (0-1 range, used by 4.5 Volt)

**Use Cases:**

- 实现自定义充能条动画
- 配合4.5伏特计算额外充能增量
- 控制部分充能的视觉反馈

**See also:** 
[[#Charge|Charge]], [[#TimedRechargeCooldown|TimedRechargeCooldown]]


---

### SubCharge {#SubCharge}

```
int SubCharge
```

*DLC: AB+, REP, REP+ | Modifiers: const*

表示某些道具使用的子充能计数，具体含义因道具而异。

**Use Cases:**

- 读取具有子充能系统的道具状态
- 修改子充能以实现多阶段道具行为
- 辅助复杂充能道具的数据管理

**See also:** 
[[#Charge|Charge]], [[#Item|Item]], [[#VarData|VarData]]


---

### TimedRechargeCooldown {#TimedRechargeCooldown}

```
int TimedRechargeCooldown
```

*DLC: AB+, REP, REP+ | Modifiers: static*

表示定时充能道具的当前冷却帧数，用于暂停充能（如Spin To Win完全消耗后）。

Number of frames before an item with a timed cooldown can recharge again (used by Spin To Win to pause its recharge after fully discharging it)

**Use Cases:**

- 获取或设置道具的充能冷却时间
- 实现类似Spin To Win的间歇充能机制
- 防止道具在冷却期间被重复使用

**See also:** 
[[#Charge|Charge]], [[#PartialCharge|PartialCharge]]


---

### VarData {#VarData}

```
int VarData
```

*DLC: AB+, REP, REP+ | Modifiers: const*

存储主动道具的额外自定义数据，如Jar of Wisps的剩余使用次数。

Holds extra information for some active items (such as the number of uses for Jar of Wisps)

**Use Cases:**

- 读取特定道具的额外状态信息
- 修改额外数据以扩展道具功能
- 实现类似精灵罐计数等自定义机制

**See also:** 
[[#Item|Item]], [[#Charge|Charge]], [[#SubCharge|SubCharge]]


---
