---
title: TemporaryEffect
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# TemporaryEffect

## Summary

TemporaryEffect 表示一个临时的道具或饰品效果实例，包含其冷却时间、叠加层数以及对应的物品配置数据。

## Related Types

- [[ItemConfig]]

## Key Methods

- [[#Cooldown|Cooldown]]
- [[#Count|Count]]
- [[#Item|Item]]

## Methods

### Functions

### Cooldown {#Cooldown}

```
int Cooldown
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取该临时效果的当前冷却时间（帧数）。

**Use Cases:**

- 检查临时效果是否仍处于冷却中
- 实现基于冷却时间的 UI 指示器

**See also:** 
[[#Count|Count]], [[#Item|Item]]


---

### Count {#Count}

```
int Count
```

*DLC: REP, REP+ | Modifiers: const*

获取该临时效果的当前叠加层数。

**Use Cases:**

- 判断临时效果的强度等级
- 控制效果叠加时的行为变化

**See also:** 
[[#Cooldown|Cooldown]], [[#Item|Item]]


---

### Item {#Item}

```
ItemConfig Item Item
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取与该临时效果关联的物品配置项（ItemConfig Item）。

**Use Cases:**

- 检索效果来源的完整物品数据
- 区分不同道具生成的同类临时效果

**See also:** 
[[#Cooldown|Cooldown]], [[#Count|Count]]


---

## See Also

- [[ItemConfig]]
