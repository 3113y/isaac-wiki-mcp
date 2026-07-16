---
title: TearParams
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 7
---

# TearParams

## Summary

存储泪弹击中参数的数据结构，包含泪弹伤害、颜色、标记、变种、炸弹类型、高度和大小等属性，用于在回调中获取和传递泪弹状态。

## Related Types

- [[Color]]

## Key Methods

- [[#TearDamage|TearDamage]]
- [[#TearFlags|TearFlags]]
- [[#TearVariant|TearVariant]]
- [[#TearColor|TearColor]]
- [[#BombVariant|BombVariant]]

## Methods

### Functions

### BombVariant {#BombVariant}

```
int BombVariant
```

*DLC: AB+, REP, REP+ | Modifiers: const*

泪弹的炸弹变种枚举值，表示泪弹是否会转化为炸弹以及炸弹的具体类型。

**Use Cases:**

- 判断泪弹是否为炸弹泪弹
- 获取炸弹变种以生成对应爆炸效果

**See also:** 



---

### TearColor {#TearColor}

```
Color TearColor
```

*DLC: REP, REP+ | Modifiers: const*

泪弹的颜色，使用 Color 类表示，影响泪弹的视觉外观。

**Use Cases:**

- 改变泪弹颜色以实现视觉效果
- 根据颜色判断泪弹来源或效果类型

**See also:** 



---

### TearDamage {#TearDamage}

```
float TearDamage
```

*DLC: AB+, REP, REP+ | Modifiers: const*

泪弹的伤害数值，浮点数，用于计算泪弹造成的实际伤害。

**Use Cases:**

- 获取泪弹伤害以进行伤害计算
- 根据伤害值决定额外效果强度

**See also:** 



---

### TearFlags {#TearFlags}

```
TearFlags TearFlags
```

*DLC: AB+, REP, REP+ | Modifiers: const*

泪弹的效果标记位组合，使用 TearFlags 枚举，表示泪弹具有的特殊属性（如穿透、追踪等）。

**Use Cases:**

- 检查泪弹是否具有特定效果
- 组合标记以构造新泪弹参数

**See also:** 



---

### TearHeight {#TearHeight}

```
float TearHeight
```

*DLC: AB+, REP, REP+ | Modifiers: const*

泪弹的飞行高度，浮点值，影响泪弹的 Y 轴偏移，用于模拟 3D 效果。

**Use Cases:**

- 调整泪弹高度以越过多层障碍
- 判断泪弹能否命中飞行敌人

**See also:** 



---

### TearScale {#TearScale}

```
float TearScale
```

*DLC: AB+, REP, REP+ | Modifiers: static*

泪弹的大小缩放因子，浮点值，控制泪弹的显示尺寸。

**Use Cases:**

- 放大或缩小泪弹视觉
- 根据大小调整碰撞检测范围

**See also:** 



---

### TearVariant {#TearVariant}

```
int TearVariant
```

*DLC: AB+, REP, REP+ | Modifiers: const*

泪弹的变种类型，使用 TearVariant 枚举，决定泪弹的特殊行为（如普通泪弹、硫磺火等）。

**Use Cases:**

- 识别泪弹类型以执行不同逻辑
- 设置变种以生成特定武器效果

**See also:** 



---

## See Also

- [[Color]]
