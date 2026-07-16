---
title: GridEntitySpikes
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 1
---

# GridEntitySpikes

## Summary

GridEntitySpikes 代表游戏中的可伸缩尖刺网格实体，通过 Timeout 变量控制尖刺的伸出与收回状态切换。

## Inheritance

- Inherits from: [[GridEntity]]

## Key Methods

- [[#Timeout|Timeout]]

## Methods

### Functions

### Timeout {#Timeout}

```
int Timeout
```

*DLC: AB+, REP, REP+ | Modifiers: const*

控制尖刺伸出/收回状态切换的整数计时器，每次状态切换后重置倒计时，当值为 0 时触发下一次状态变化。

**Use Cases:**

- 延长或缩短尖刺伸出/收回的间隔时间
- 同步尖刺状态与其他实体行为

**See also:** 



---

## See Also

- [[GridEntity]]
