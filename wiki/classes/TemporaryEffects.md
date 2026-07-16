---
title: TemporaryEffects
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 17
---

# TemporaryEffects

## Summary

管理玩家身上的临时效果，包括道具效果(CollectibleEffect)、空物品效果(NullEffect)和饰品效果(TrinketEffect)。这些效果主要用于追踪物品内部状态（如神圣屏障层数）而非提供完整的物品能力。

## Related Types

- [[EffectList]]
- [[TemporaryEffect]]

## Key Methods

- [[#AddCollectibleEffect|AddCollectibleEffect]]
- [[#RemoveCollectibleEffect|RemoveCollectibleEffect]]
- [[#HasCollectibleEffect|HasCollectibleEffect]]
- [[#GetCollectibleEffect|GetCollectibleEffect]]
- [[#ClearEffects|ClearEffects]]

## Methods

### Functions

### AddCollectibleEffect {#AddCollectibleEffect}

```
void AddCollectibleEffect ( CollectibleType CollectibleType, boolean AddCostume = true, int Count = 1 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加指定道具的CollectibleEffect，可附加角色服装，并遵循物品的冷却或持久标记。

Adds the CollectibleEffect associated with a given item. If the passed item's CollectibleEffect is marked to have a cooldown or be persistent in items.xml, this will be respected.

**Use Cases:**

- 赋予玩家神圣屏障的充能层数
- 触发需要物品状态支持的效果而不实际获得道具
- 为特定道具显示其装饰服装

**See also:** 
[[#GetCollectibleEffect|GetCollectibleEffect]], [[#HasCollectibleEffect|HasCollectibleEffect]], [[#RemoveCollectibleEffect|RemoveCollectibleEffect]]


---

### AddNullEffect {#AddNullEffect}

```
void AddNullEffect ( NullItemID NullId, boolean AddCostume = true, int Count = 1 )
```

*DLC: REP, REP+ | Modifiers: const*

添加指定空物品的NullEffect，可附加服装和设置叠加数量。

**Use Cases:**

- 给予空卡片或符文等效果
- 叠加空物品的装饰状态

**See also:** 
[[#GetNullEffect|GetNullEffect]], [[#HasNullEffect|HasNullEffect]], [[#RemoveNullEffect|RemoveNullEffect]]


---

### AddTrinketEffect {#AddTrinketEffect}

```
void AddTrinketEffect ( TrinketType TrinketType, boolean AddCostume = true, int Count = 1 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加指定饰品的TrinketEffect，可附加服装和设置叠加数量。

**Use Cases:**

- 临时赋予饰品效果及其服装
- 测试饰品相关状态

**See also:** 
[[#GetTrinketEffect|GetTrinketEffect]], [[#HasTrinketEffect|HasTrinketEffect]], [[#RemoveTrinketEffect|RemoveTrinketEffect]]


---

### ClearEffects {#ClearEffects}

```
void ClearEffects ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

移除玩家当前所有的临时效果，包括道具效果、空物品效果和饰品效果。

**Use Cases:**

- 重置所有临时赋予的状态
- 清理不需要的效果时使用

**See also:** 
[[#RemoveCollectibleEffect|RemoveCollectibleEffect]], [[#RemoveNullEffect|RemoveNullEffect]], [[#RemoveTrinketEffect|RemoveTrinketEffect]]


---

### GetCollectibleEffect {#GetCollectibleEffect}

```
const TemporaryEffect GetCollectibleEffect ( CollectibleType CollectibleType )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取指定道具类型的TemporaryEffect对象，用于读取该效果的详细状态。

**Use Cases:**

- 查询特定道具效果的内部数据
- 判断效果是否处于激活或冷却状态

**See also:** 
[[#GetCollectibleEffectNum|GetCollectibleEffectNum]], [[#HasCollectibleEffect|HasCollectibleEffect]]


---

### GetCollectibleEffectNum {#GetCollectibleEffectNum}

```
int GetCollectibleEffectNum ( CollectibleType CollectibleType )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取指定道具效果的当前叠加层数。

**Use Cases:**

- 了解某一效果被叠加的次数
- 监控效果强度

**See also:** 
[[#GetCollectibleEffect|GetCollectibleEffect]]


---

### GetEffectsList {#GetEffectsList}

```
const EffectList GetEffectsList ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回包含所有当前临时效果的列表，可遍历每个效果项。

**Use Cases:**

- 遍历玩家所有临时效果进行统一处理
- 调试输出当前效果清单

**See also:** 



---

### GetNullEffect {#GetNullEffect}

```
const TemporaryEffect GetNullEffect ( ItemConfigNullItemID NullId )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取指定空物品类型的TemporaryEffect对象，用于查询其内部状态。

**Use Cases:**

- 检查某空物品效果的详细属性

**See also:** 
[[#GetNullEffectNum|GetNullEffectNum]], [[#HasNullEffect|HasNullEffect]]


---

### GetNullEffectNum {#GetNullEffectNum}

```
int GetNullEffectNum ( ItemConfigNullItemID NullId )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取指定空物品效果的当前叠加层数。

**Use Cases:**

- 了解空物品效果叠加次数

**See also:** 
[[#GetNullEffect|GetNullEffect]]


---

### GetTrinketEffect {#GetTrinketEffect}

```
const TemporaryEffect GetTrinketEffect ( TrinketType TrinketType )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取指定饰品类型的TemporaryEffect对象，用于读取其状态。

**Use Cases:**

- 检查饰品临时效果的详细数据

**See also:** 
[[#GetTrinketEffectNum|GetTrinketEffectNum]], [[#HasTrinketEffect|HasTrinketEffect]]


---

### GetTrinketEffectNum {#GetTrinketEffectNum}

```
int GetTrinketEffectNum ( TrinketType TrinketType )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取指定饰品效果的当前叠加层数。

**Use Cases:**

- 了解饰品效果叠加的次数

**See also:** 
[[#GetTrinketEffect|GetTrinketEffect]]


---

### HasCollectibleEffect {#HasCollectibleEffect}

```
boolean HasCollectibleEffect ( CollectibleType CollectibleType )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检测玩家是否拥有指定的道具效果。

**Use Cases:**

- 条件判断是否已施加某种效果
- 避免重复添加相同效果

**See also:** 
[[#GetCollectibleEffect|GetCollectibleEffect]], [[#AddCollectibleEffect|AddCollectibleEffect]]


---

### HasNullEffect {#HasNullEffect}

```
boolean HasNullEffect ( ItemConfigNullItemID NullId )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

检测玩家是否拥有指定的空物品效果。

**Use Cases:**

- 判断空物品是否生效

**See also:** 
[[#GetNullEffect|GetNullEffect]], [[#AddNullEffect|AddNullEffect]]


---

### HasTrinketEffect {#HasTrinketEffect}

```
boolean HasTrinketEffect ( TrinketType TrinketType )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检测玩家是否拥有指定的饰品效果。

**Use Cases:**

- 判断饰品效果是否已存在

**See also:** 
[[#GetTrinketEffect|GetTrinketEffect]], [[#AddTrinketEffect|AddTrinketEffect]]


---

### RemoveCollectibleEffect {#RemoveCollectibleEffect}

```
void RemoveCollectibleEffect ( CollectibleType CollectibleType, int Count = 1 )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

移除指定道具效果，可指定移除数量，传入-1移除所有该效果实例。

Count = -1 removes all instances of the effect

**Use Cases:**

- 减少或完全消除道具效果
- 控制效果堆叠上限

**See also:** 
[[#AddCollectibleEffect|AddCollectibleEffect]], [[#HasCollectibleEffect|HasCollectibleEffect]]


---

### RemoveNullEffect {#RemoveNullEffect}

```
void RemoveNullEffect ( ItemConfigNullItemID NullId, int Count = 1 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

移除指定空物品效果，可指定数量，-1则全部移除。

Count = -1 removes all instances of the effect

**Use Cases:**

- 撤销空物品效果

**See also:** 
[[#AddNullEffect|AddNullEffect]], [[#HasNullEffect|HasNullEffect]]


---

### RemoveTrinketEffect {#RemoveTrinketEffect}

```
void RemoveTrinketEffect ( TrinketType TrinketType, int Count = 1 )
```

*DLC: AB+, REP, REP+*

移除指定饰品效果，可指定数量，-1则全部移除。

Count = -1 removes all instances of the effect

**Use Cases:**

- 撤销饰品临时效果

**See also:** 
[[#AddTrinketEffect|AddTrinketEffect]], [[#HasTrinketEffect|HasTrinketEffect]]


---

## See Also

- [[EffectList]]
- [[TemporaryEffect]]
