---
title: QueueItemData
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# QueueItemData

## Summary

代表玩家排队中的道具数据，包含充能状态、道具配置信息和是否已触摸的标记。

## Related Types

- [[ItemConfig]]

## Key Methods

- [[#Charge|Charge]]
- [[#Item|Item]]
- [[#Touched|Touched]]

## Methods

### Functions

### Charge {#Charge}

```
int Charge
```

*DLC: AB+, REP, REP+ | Modifiers: const*

排队道具当前的充能数值，用于判断道具是否可用或显示充能状态。

**Use Cases:**

- 检查排队道具是否充满能量
- 在UI中绘制充能进度条

**See also:** 
[[#Item|Item]]


---

### Item {#Item}

```
ItemConfig Item Item
```

*DLC: REP, REP+ | Modifiers: const*

返回排队道具的 ItemConfig_Item 对象，提供该道具的完整配置信息。

**Use Cases:**

- 获取排队道具的ID或类型
- 显示排队道具的图标或名称

**See also:** 
[[#Charge|Charge]], [[#Touched|Touched]]


---

### Touched {#Touched}

```
boolean Touched
```

*DLC: AB+, REP, REP+ | Modifiers: const*

表示玩家是否已经触摸过该排队道具，通常用于决定是否触发拾取行为。

**Use Cases:**

- 判断是否可以自动拾取排队道具
- 控制排队道具的可交互状态

**See also:** 
[[#Item|Item]]


---

## See Also

- [[ItemConfig]]
