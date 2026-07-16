---
title: GridEntityTNT
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 1
---

# GridEntityTNT

## Summary

GridEntityTNT 代表可爆炸的 TNT 桶网格实体，通常通过 GridEntity.ToTNT() 获得，用于控制和检测 TNT 的状态。

## Inheritance

- Inherits from: [[GridEntity]]

## Key Methods

- [[#FrameCnt|FrameCnt]]

## Methods

### Functions

### FrameCnt {#FrameCnt}

```
int FrameCnt
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取或设置 TNT 实体的帧计数器，用于控制爆炸前的动画进度或计时。

**Use Cases:**

- 读取 TNT 剩余爆炸帧数
- 修改帧计数以加快或延迟爆炸

**See also:** 



---

## See Also

- [[GridEntity]]
