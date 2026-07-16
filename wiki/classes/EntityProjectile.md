---
title: EntityProjectile
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 22
---

# EntityProjectile

## Summary

表示游戏中的投射物实体，提供属性与标志的动态修改，支持超时触发状态切换。

## Inheritance

- Inherits from: [[Entity]]

## Key Methods

- [[#AddProjectileFlags|AddProjectileFlags]]
- [[#ChangeFlags|ChangeFlags]]
- [[#HasProjectileFlags|HasProjectileFlags]]

## Methods

### Functions

### AddChangeFlags {#AddChangeFlags}

```
void AddChangeFlags ( ProjectileFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

向ChangeFlags添加标志，定义超时后切换的状态属性。

**Use Cases:**

- 设置改变后的弹幕特性
- 动态组合多个标志

**See also:** 
[[#ChangeFlags|ChangeFlags]], [[#ChangeTimeout|ChangeTimeout]]


---

### AddFallingAccel {#AddFallingAccel}

```
void AddFallingAccel ( float Value )
```

*DLC: REP, REP+ | Modifiers: const*

增加投射物的下落加速度，影响高度变化。

**Use Cases:**

- 调整抛物线轨迹
- 重力效果微调

**See also:** 
[[#FallingAccel|FallingAccel]], [[#AddFallingSpeed|AddFallingSpeed]]


---

### AddFallingSpeed {#AddFallingSpeed}

```
void AddFallingSpeed ( float Value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

增加投射物的下落速度，改变垂直移动快慢。

**Use Cases:**

- 控制坠落节奏
- 修正垂直偏移

**See also:** 
[[#FallingSpeed|FallingSpeed]], [[#AddFallingAccel|AddFallingAccel]]


---

### AddHeight {#AddHeight}

```
void AddHeight ( float Value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

增加投射物的当前高度值。

**Use Cases:**

- 模拟跳跃上升
- 调整垂直打击点

**See also:** 
[[#Height|Height]], [[#FallingSpeed|FallingSpeed]]


---

### AddProjectileFlags {#AddProjectileFlags}

```
void AddProjectileFlags ( ProjectileFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加ProjectileFlags标志，赋予或叠加行为属性。

**Use Cases:**

- 动态赋予追踪或穿透
- 组合标志实现复杂子弹

**See also:** 
[[#ProjectileFlags|ProjectileFlags]], [[#ClearProjectileFlags|ClearProjectileFlags]]


---

### AddScale {#AddScale}

```
void AddScale ( float Value )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

增加投射物的视觉缩放比例。

**Use Cases:**

- 尺寸渐变效果
- 视觉比例调整

**See also:** 
[[#Scale|Scale]]


---

### ClearProjectileFlags {#ClearProjectileFlags}

```
void ClearProjectileFlags ( ProjectileFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

清除指定的ProjectileFlags标志。

**Use Cases:**

- 移除临时特性
- 重置默认行为

**See also:** 
[[#ProjectileFlags|ProjectileFlags]], [[#AddProjectileFlags|AddProjectileFlags]]


---

### HasProjectileFlags {#HasProjectileFlags}

```
boolean HasProjectileFlags ( ProjectileFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检查投射物是否拥有指定标志。

**Use Cases:**

- 条件判断分支
- 根据标志触发效果

**See also:** 
[[#ProjectileFlags|ProjectileFlags]], [[#AddProjectileFlags|AddProjectileFlags]]


---

### Acceleration {#Acceleration}

```
float Acceleration
```

*DLC: AB+, REP, REP+ | Modifiers: const*

投射物的加速度值，影响速度随时间变化。

**Use Cases:**

- 实现逐渐加速
- 设置恒定变速

**See also:** 



---

### ChangeFlags {#ChangeFlags}

```
ProjectileFlags ChangeFlags
```

*DLC: AB+, REP, REP+ | Modifiers: const*

超时后切换的标志集，定义改变后的属性。

**Use Cases:**

- 预置改变状态
- 配合ChangeTimeout切换模式

**See also:** 
[[#AddChangeFlags|AddChangeFlags]], [[#ChangeTimeout|ChangeTimeout]]


---

### ChangeTimeout {#ChangeTimeout}

```
int ChangeTimeout
```

*DLC: AB+, REP, REP+ | Modifiers: const*

从生成到状态改变所需的帧数。

**Use Cases:**

- 延迟弹幕变形
- 定时切换轨迹

**See also:** 
[[#ChangeFlags|ChangeFlags]], [[#ChangeVelocity|ChangeVelocity]]


---

### ChangeVelocity {#ChangeVelocity}

```
float ChangeVelocity
```

*DLC: AB+, REP, REP+ | Modifiers: const*

状态改变后应用的速度大小。

**Use Cases:**

- 改变后弹幕加速
- 统一化速度向量长度

**See also:** 
[[#ChangeTimeout|ChangeTimeout]], [[#ChangeFlags|ChangeFlags]]


---

### CurvingStrength {#CurvingStrength}

```
float CurvingStrength
```

*DLC: AB+, REP, REP+ | Modifiers: static*

曲线运动强度，影响弹道弯曲程度。

**Use Cases:**

- 实现弧形飞行
- 调整追踪前摇

**See also:** 



---

### Damage {#Damage}

```
float Damage
```

*DLC: AB+, REP, REP+ | Modifiers: const*

投射物造成的伤害数值。

**Use Cases:**

- 设置威胁等级
- 平衡弹幕威力

**See also:** 



---

### DepthOffset {#DepthOffset}

```
float DepthOffset
```

*DLC: AB+, REP, REP+ | Modifiers: static*

深度偏移，控制渲染层级。

**Use Cases:**

- 调整视觉前后顺序
- 伪3D效果

**See also:** 



---

### FallingAccel {#FallingAccel}

```
float FallingAccel
```

*DLC: AB+, REP, REP+ | Modifiers: const*

下落加速度变量，定义重力效果强度。

**Use Cases:**

- 创造不同重力环境
- 控制高度变化率

**See also:** 
[[#AddFallingAccel|AddFallingAccel]], [[#FallingSpeed|FallingSpeed]]


---

### FallingSpeed {#FallingSpeed}

```
float FallingSpeed
```

*DLC: AB+, REP, REP+*

下落速度变量，影响垂直移动速度。

**Use Cases:**

- 设定初始下落快慢
- 维持恒定坠落

**See also:** 
[[#AddFallingSpeed|AddFallingSpeed]], [[#FallingAccel|FallingAccel]]


---

### Height {#Height}

```
float Height
```

*DLC: AB+, REP, REP+ | Modifiers: const*

投射物当前高度，通常为负值。

**Use Cases:**

- 判断地面碰撞
- 实现跳跃动画

**See also:** 
[[#AddHeight|AddHeight]], [[#FallingSpeed|FallingSpeed]]


---

### HomingStrength {#HomingStrength}

```
float HomingStrength
```

*DLC: AB+, REP, REP+ | Modifiers: static*

追踪强度，控制向目标变向的程度。

**Use Cases:**

- 制作制导子弹
- 调整追踪灵敏度

**See also:** 



---

### ProjectileFlags {#ProjectileFlags}

```
ProjectileFlags ProjectileFlags
```

*DLC: AB+, REP, REP+ | Modifiers: static*

投射物的行为标志变量，可读写。

**Use Cases:**

- 读取当前标志状态
- 整体替换标志集

**See also:** 
[[#AddProjectileFlags|AddProjectileFlags]], [[#HasProjectileFlags|HasProjectileFlags]]


---

### Scale {#Scale}

```
float Scale
```

*DLC: AB+, REP, REP+ | Modifiers: const*

投射物的视觉缩放比例变量。

**Use Cases:**

- 动态改变大小
- 统一缩放引用

**See also:** 
[[#AddScale|AddScale]]


---

### WiggleFrameOffset {#WiggleFrameOffset}

```
int WiggleFrameOffset
```

*DLC: AB+, REP, REP+ | Modifiers: static*

摆动动画的起始帧偏移量。

**Use Cases:**

- 同步摆动相位
- 创造错落摆动效果

**See also:** 



---

## See Also

- [[Entity]]
