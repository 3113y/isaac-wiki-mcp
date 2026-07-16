---
title: KColor
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 5
---

# KColor

## Summary

KColor 表示带透明度的 RGBA 颜色，主要用于 Font 类，提供构造函数、预定义颜色常量和分量读写变量。

## Related Types

- [[Color]]

## Key Methods

- [[#KColor|KColor]]
- [[#KColor.Black|KColor.Black]]
- [[#Red|Red]]
- [[#Green|Green]]
- [[#Blue|Blue]]

## Methods

### Constructors

### KColor {#KColor}

```
KColor KColor ( float red, float green, float blue, float alpha )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

KColor 构造函数，创建指定红、绿、蓝及不透明度分量的颜色对象。

**Use Cases:**

- 创建自定义颜色
- 动态调整颜色值

**See also:** 
[[#Red|Red]], [[#Green|Green]], [[#Blue|Blue]], [[#KColor.Black|KColor.Black]]


---

### Functions

### KColor.Black {#KColor.Black}

```
float Alpha
```

*DLC: REP, REP+ | Modifiers: const*

预定义黑色常量，等价于 KColor(0, 0, 0, 1)。

**Use Cases:**

- 快速获取黑色
- 用作默认描边或阴影

**See also:** 
[[#KColor|KColor]], [[#Red|Red]], [[#Green|Green]], [[#Blue|Blue]]


---

### Blue {#Blue}

```
float Blue
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取或设置颜色的蓝色分量。

**Use Cases:**

- 单独调整蓝色通道
- 读取已存颜色的蓝色值

**See also:** 
[[#KColor|KColor]], [[#Green|Green]], [[#Red|Red]]


---

### Green {#Green}

```
float Green
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取或设置颜色的绿色分量。

**Use Cases:**

- 单独调整绿色通道
- 读取已存颜色的绿色值

**See also:** 
[[#KColor|KColor]], [[#Blue|Blue]], [[#Red|Red]]


---

### Red {#Red}

```
float Red
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取或设置颜色的红色分量。

**Use Cases:**

- 单独调整红色通道
- 读取已存颜色的红色值

**See also:** 
[[#KColor|KColor]], [[#Green|Green]], [[#Blue|Blue]]


---

## See Also

- [[Color]]
- [[KColor]]
