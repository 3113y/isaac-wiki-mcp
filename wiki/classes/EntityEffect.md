---
title: EntityEffect
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 18
---

# EntityEffect

## Summary

EntityEffect 是用于表示游戏中各种视觉特效的实体类，如冲击波、水迹、粒子等。提供跟随父实体、设置伤害来源、配置半径、控制持续时间和下落物理效果等功能。

## Inheritance

- Inherits from: [[Entity]]

## Related Types

- [[Sprite]]
- [[Vector]]

## Key Methods

- [[#SetTimeout|SetTimeout]]
- [[#SetRadii|SetRadii]]
- [[#FollowParent|FollowParent]]
- [[#IsPlayerCreep|IsPlayerCreep]]
- [[#SetDamageSource|SetDamageSource]]

## Methods

### Functions

### FollowParent {#FollowParent}

```
void FollowParent ( Entity Parent )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

使当前特效跟随指定的父实体，让效果附着在目标上移动。

**Use Cases:**

- 让粒子环绕玩家
- 将特效粘附在怪物上

**See also:** 
[[#IsFollowing|IsFollowing]], [[#ParentOffset|ParentOffset]]


---

### IsPlayerCreep {#IsPlayerCreep}

```
static boolean IsPlayerCreep ( EffectVariant Variant )
```

*DLC: REP, REP+ | Modifiers: const*

静态方法，检查给定的 EffectVariant 是否属于玩家留下的毒液（如妈踩后产生的液体）。

**Use Cases:**

- 判断地面液体是否为玩家来源
- 伤害结算时区分归属

**See also:** 



---

### SetDamageSource {#SetDamageSource}

```
void SetDamageSource ( EntityType DamageSource )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置该特效造成的伤害来源实体类型，用于归属判定。

**Use Cases:**

- 让爆炸伤害统计为玩家
- 标明环境伤害来源

**See also:** 
[[#DamageSource|DamageSource]]


---

### SetRadii {#SetRadii}

```
void SetRadii ( float min, float max )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置冲击波的内外半径，控制其影响范围。

用于冲击波（shockwaves）。

**Use Cases:**

- 动态调整爆炸冲击波大小
- 制作扩散环效果

**See also:** 
[[#MinRadius|MinRadius]], [[#MaxRadius|MaxRadius]]


---

### SetTimeout {#SetTimeout}

```
void SetTimeout ( int Timeout )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置特效的自动消失倒计时帧数。

**Use Cases:**

- 控制粒子存在时长
- 让临时特效到时自动清除

**See also:** 
[[#Timeout|Timeout]]


---

### DamageSource {#DamageSource}

```
int DamageSource
```

*DLC: AB+, REP, REP+ | Modifiers: static*

整数属性，存储该特效的伤害来源实体类型。

**Use Cases:**

- 读取伤害来源做统计
- 修改已存在的伤害归属

**See also:** 
[[#SetDamageSource|SetDamageSource]]


---

### FallingAcceleration {#FallingAcceleration}

```
float FallingAcceleration
```

*DLC: AB+, REP, REP+ | Modifiers: const*

下落加速度，模拟重力影响，用于掉落类特效。

**Use Cases:**

- 实现陨石加速坠落
- 制作越落越快的粒子

**See also:** 
[[#FallingSpeed|FallingSpeed]]


---

### FallingSpeed {#FallingSpeed}

```
float FallingSpeed
```

*DLC: AB+, REP, REP+ | Modifiers: const*

当前下落速度，与 FallingAcceleration 配合使用。

**Use Cases:**

- 读取当前坠落速度以调整动画
- 让掉落物弹跳

**See also:** 
[[#FallingAcceleration|FallingAcceleration]]


---

### IsFollowing {#IsFollowing}

```
boolean IsFollowing
```

*DLC: AB+, REP, REP+ | Modifiers: const*

布尔值，指示该特效当前是否正在跟随父实体。

**Use Cases:**

- 判断跟随状态以切换行为
- 解绑跟随前检查

**See also:** 
[[#FollowParent|FollowParent]]


---

### LifeSpan {#LifeSpan}

```
int LifeSpan
```

*DLC: AB+, REP, REP+ | Modifiers: const*

特效的总生命帧数，控制其最大存在时长。

**Use Cases:**

- 设置长粒子存在时间
- 获取剩余寿命比例

**See also:** 
[[#Timeout|Timeout]]


---

### m_Height {#m_Height}

```
float m_Height
```

*DLC: AB+, REP, REP+ | Modifiers: const*

特效高度值，直接影响渲染时粒子的 .dy 偏移，用于表现层次感。

用于粒子的 .dy

**Use Cases:**

- 制作漂浮粒子效果
- 实现立体感冲击波

**See also:** 



---

### MaxRadius {#MaxRadius}

```
float MaxRadius
```

*DLC: AB+, REP, REP+ | Modifiers: const*

冲击波的最大半径，与 SetRadii 配合控制外边界。

**Use Cases:**

- 读取冲击波当前最大范围
- 动态缩放冲击波大小

**See also:** 
[[#SetRadii|SetRadii]]


---

### MinRadius {#MinRadius}

```
float MinRadius
```

*DLC: AB+, REP, REP+ | Modifiers: static*

冲击波的最小半径，与 MaxRadius 一起定义中空区域。

用于冲击波（shockwaves）。

**Use Cases:**

- 制作中空冲击波
- 读取内径进行精确碰撞

**See also:** 
[[#SetRadii|SetRadii]]


---

### ParentOffset {#ParentOffset}

```
Vector ParentOffset
```

*DLC: AB+, REP, REP+ | Modifiers: const*

特效相对于跟随父实体的偏移向量，用于控制跟随时的相对位置。

可能很快就会被淘汰，取而代之的是 m_SpriteOffset

**Use Cases:**

- 调整特效在父实体上的附着点
- 实现偏移跟随效果

**See also:** 
[[#SetParentOffset|SetParentOffset]]


---

### Rotation {#Rotation}

```
float Rotation
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Rotation 完成对应 API 操作

**See also:** 



---

### Scale {#Scale}

```
float Scale
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Scale 完成对应 API 操作

**See also:** 



---

### State {#State}

```
int State
```

*DLC: AB+, REP, REP+*

状态变量，可在 Init() 中随意使用，初始化为 0

状态变量，可在 Init() 中随意使用，初始化为 0

**Use Cases:**

- 调用 State 完成对应 API 操作

**See also:** 



---

### Timeout {#Timeout}

```
int Timeout
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Timeout 完成对应 API 操作

**See also:** 



---

## See Also

- [[Entity]]
- [[Sprite]]
- [[Vector]]
