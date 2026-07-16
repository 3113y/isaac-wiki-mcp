---
title: ProjectileParams
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 24
---

# ProjectileParams

## Summary

ProjectileParams 是一个参数容器类，用于在发射投射物时传递自定义属性，如速度、颜色、碰撞、变化状态及扩散角度等，配合 EntityPlayer:FireProjectile 等函数使用。

## Related Types

- [[Color]]
- [[Vector]]

## Key Methods

- [[#ProjectileParams|ProjectileParams]]
- [[#ChangeFlags|ChangeFlags]]
- [[#Spread|Spread]]
- [[#BulletFlags|BulletFlags]]
- [[#HomingStrength|HomingStrength]]

## Methods

### Constructors

### ProjectileParams {#ProjectileParams}

```
ProjectileParams ProjectileParams ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

构造 ProjectileParams 实例，用于存放投射物的各项自定义参数，可通过链式赋值后传递给发射函数。

**Use Cases:**

- 创建空白参数对象以便按需设置属性
- 结合 Game():SpawnEntity() 或 FireProjectile 发射自定义投射物

**See also:** 
[[#Variant|Variant]], [[#Spread|Spread]], [[#VelocityMulti|VelocityMulti]], [[#Color|Color]]


---

### Functions

### Acceleration {#Acceleration}

```
float Acceleration
```

*DLC: REP, REP+ | Modifiers: const*

设置投射物的加速度值，影响其速度随时间的变化。

**Use Cases:**

- 模拟重力或加速效果
- 实现投射物速度曲线

**See also:** 
[[#FallingAccelModifier|FallingAccelModifier]], [[#VelocityMulti|VelocityMulti]]


---

### BulletFlags {#BulletFlags}

```
int BulletFlags
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置子弹的额外标志位（Bitmask），用于启用特定子弹行为（如穿透、跟踪等）。

**Use Cases:**

- 让子弹获得穿透或磁性效果
- 组合多种子弹特效

**See also:** 
[[#ChangeFlags|ChangeFlags]], [[#HomingStrength|HomingStrength]]


---

### ChangeFlags {#ChangeFlags}

```
ProjectileFlags ChangeFlags
```

*DLC: AB+, REP, REP+ | Modifiers: const*

指定投射物进入跟踪状态时的跟踪强度。

**Use Cases:**

- 让子弹具有追踪目标的能力
- 调整跟踪转向的灵敏度

**See also:** 
[[#HomingStrength|HomingStrength]]


---

### ChangeTimeout {#ChangeTimeout}

```
int ChangeTimeout
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 ChangeTimeout 完成对应 API 操作

**See also:** 



---

### ChangeVelocity {#ChangeVelocity}

```
float ChangeVelocity
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 ChangeVelocity 完成对应 API 操作

**See also:** 



---

### CircleAngle {#CircleAngle}

```
float CircleAngle
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Angle offset used by fire_projectiles PROJECTILES_CIRCLE type emitter. Random by default.

Angle offset used by fire_projectiles PROJECTILES_CIRCLE type emitter. Random by default.

**Use Cases:**

- 调用 CircleAngle 完成对应 API 操作

**See also:** 



---

### Color {#Color}

```
Color Color
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Color 完成对应 API 操作

**See also:** 



---

### CurvingStrength {#CurvingStrength}

```
float CurvingStrength
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Use very small values for curving like 0.005.

Use very small values for curving like 0.005.

**Use Cases:**

- 调用 CurvingStrength 完成对应 API 操作

**See also:** 



---

### DepthOffset {#DepthOffset}

```
float DepthOffset
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 DepthOffset 完成对应 API 操作

**See also:** 



---

### DotProductLimit {#DotProductLimit}

```
float DotProductLimit
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Direction bullets are being fired in Dot product of FireDirectionLimit, bullet direction must be &gt;= this value

Direction bullets are being fired in Dot product of FireDirectionLimit, bullet direction must be &gt;= this value

**Use Cases:**

- 调用 DotProductLimit 完成对应 API 操作

**See also:** 



---

### FallingAccelModifier {#FallingAccelModifier}

```
float FallingAccelModifier
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 FallingAccelModifier 完成对应 API 操作

**See also:** 



---

### FallingSpeedModifier {#FallingSpeedModifier}

```
float FallingSpeedModifier
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 FallingSpeedModifier 完成对应 API 操作

**See also:** 



---

### FireDirectionLimit {#FireDirectionLimit}

```
Vector FireDirectionLimit
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 FireDirectionLimit 完成对应 API 操作

**See also:** 



---

### GridCollision {#GridCollision}

```
boolean GridCollision
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 GridCollision 完成对应 API 操作

**See also:** 



---

### HeightModifier {#HeightModifier}

```
float HeightModifier
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 HeightModifier 完成对应 API 操作

**See also:** 



---

### HomingStrength {#HomingStrength}

```
float HomingStrength
```

*DLC: AB+, REP, REP+*

Multiplier on normal homing strength. Unused if SMART bullet flag is not set.

Multiplier on normal homing strength. Unused if SMART bullet flag is not set.

**Use Cases:**

- 调用 HomingStrength 完成对应 API 操作

**See also:** 



---

### PositionOffset {#PositionOffset}

```
Vector PositionOffset
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 PositionOffset 完成对应 API 操作

**See also:** 



---

### Scale {#Scale}

```
float Scale
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Scale 完成对应 API 操作

**See also:** 



---

### Spread {#Spread}

```
float Spread
```

*DLC: AB+, REP, REP+ | Modifiers: static*

For quad/quint/etc spread shots.

For quad/quint/etc spread shots.

**Use Cases:**

- 调用 Spread 完成对应 API 操作

**See also:** 



---

### TargetPosition {#TargetPosition}

```
Vector TargetPosition
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 TargetPosition 完成对应 API 操作

**See also:** 



---

### Variant {#Variant}

```
int Variant
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Variant 完成对应 API 操作

**See also:** 



---

### VelocityMulti {#VelocityMulti}

```
float VelocityMulti
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 VelocityMulti 完成对应 API 操作

**See also:** 



---

### WiggleFrameOffset {#WiggleFrameOffset}

```
int WiggleFrameOffset
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Used to offset the wiggle wave.

Used to offset the wiggle wave.

**Use Cases:**

- 调用 WiggleFrameOffset 完成对应 API 操作

**See also:** 



---

## See Also

- [[Color]]
- [[Vector]]
