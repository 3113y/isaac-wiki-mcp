---
title: EntityLaser
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 44
---

# EntityLaser

## Summary

EntityLaser 表示游戏中的激光实体，包括硫磺火、科技激光、环形激光等，提供对激光路径、状态、行为和属性的完整控制，常通过 EntityPlayer 的 Fire 系方法获取。

## Inheritance

- Inherits from: [[Entity]]

## Related Types

- [[Vector]]
- [[VectorList]]

## Key Methods

- [[#ShootAngle|ShootAngle]]
- [[#GetSamples|GetSamples]]
- [[#GetEndPoint|GetEndPoint]]
- [[#SetMaxDistance|SetMaxDistance]]
- [[#IsCircleLaser|IsCircleLaser]]

## Methods

### Functions

### AddTearFlags {#AddTearFlags}

```
void AddTearFlags ( TearFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将指定的TearFlags添加到激光的泪弹标志中，影响激光的碰撞或行为属性。

**Use Cases:**

- 赋予激光穿透效果
- 设置激光的追踪属性
- 组合多种泪弹效果

**See also:** 
[[#HasTearFlags|HasTearFlags]], [[#ClearTearFlags|ClearTearFlags]], [[#TearFlags|TearFlags]]


---

### CalculateEndPoint {#CalculateEndPoint}

```
static Vector CalculateEndPoint ( Vector Start, Vector Dir, Vector PositionOffset, Entity Parent, float Margin )
```

*DLC: REP, REP+ | Modifiers: const*

根据起点、方向、偏移、父实体和边距计算激光的终点位置。

**Use Cases:**

- 预先确定激光路径
- 用于精确的碰撞预测
- 辅助自定义激光行为

**See also:** 
[[#GetEndPoint|GetEndPoint]], [[#ShootAngle|ShootAngle]]


---

### ClearTearFlags {#ClearTearFlags}

```
void ClearTearFlags ( TearFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

移除激光的指定TearFlags，以撤销之前添加的属性。

**Use Cases:**

- 移除追踪效果
- 重置激光特性
- 动态调整激光行为

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#HasTearFlags|HasTearFlags]], [[#TearFlags|TearFlags]]


---

### GetEndPoint {#GetEndPoint}

```
const Vector GetEndPoint ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回激光的终点向量，避免重复计算，可直接用于效果定位。

**Use Cases:**

- 获取激光末端位置
- 在终点生成特效
- 检测激光是否接触边界

**See also:** 
[[#CalculateEndPoint|CalculateEndPoint]], [[#EndPoint|EndPoint]]


---

### GetNonOptimizedSamples {#GetNonOptimizedSamples}

```
const VectorList GetNonOptimizedSamples ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回沿激光路径均匀分布的51个样本点，即使直线也返回全量点，适合需要密集路径信息的情况。

返回一个向量表（VectorList）用于表达激光的路径。通常会返回沿激光路径均匀分布的51个点，相对于[`GetSamples()`](#getsamples)只返回表示激光路径所需的最少点。

**Use Cases:**

- 绘制激光光柱特效
- 精细的碰撞检测
- 逐点处理路径事件

**See also:** 
[[#GetSamples|GetSamples]]


---

### GetRenderZ {#GetRenderZ}

```
int GetRenderZ ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回激光的渲染层级，用于控制绘制顺序。

**Use Cases:**

- 调试激光绘制遮挡
- 自定义特效渲染层级

**See also:** 



---

### GetSamples {#GetSamples}

```
const VectorList GetSamples ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回表示激光路径的最少样本点，直线时仅返回起点和终点，节省计算。

**Use Cases:**

- 高效绘制激光
- 简化碰撞判断
- 路径信息提取

**See also:** 
[[#GetNonOptimizedSamples|GetNonOptimizedSamples]]


---

### HasTearFlags {#HasTearFlags}

```
boolean HasTearFlags ( TearFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

测试激光当前的TearFlags是否包含给定的标志位组合。

**Use Cases:**

- 判断激光拥有哪些属性
- 条件逻辑分支

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#ClearTearFlags|ClearTearFlags]], [[#TearFlags|TearFlags]]


---

### IsCircleLaser {#IsCircleLaser}

```
boolean IsCircleLaser ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回激光是否为某种环形激光（如科技X、鲁多维科环），根据子类型区分类别。

**Use Cases:**

- 识别激光类型
- 针对环形激光应用特殊逻辑

**See also:** 
[[#SetActiveRotation|SetActiveRotation]], [[#RotationDegrees|RotationDegrees]]


---

### IsSampleLaser {#IsSampleLaser}

```
boolean IsSampleLaser ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回激光是否采用采样模式渲染。

**Use Cases:**

- 区分渲染方式
- 优化绘制策略

**See also:** 
[[#SampleLaser|SampleLaser]]


---

### SetActiveRotation {#SetActiveRotation}

```
void SetActiveRotation ( int Delay, float AngleDegrees, float RotationSpd, boolean TimeoutComplete )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

配置激光的延迟、角度、旋转速度和超时完成标志，让激光按设定动态旋转。

**Use Cases:**

- 创建旋转激光如科技零
- 控制虚空之喉转动

**See also:** 
[[#IsActiveRotating|IsActiveRotating]], [[#RotationDelay|RotationDelay]], [[#RotationSpd|RotationSpd]], [[#RotationDegrees|RotationDegrees]]


---

### SetBlackHpDropChance {#SetBlackHpDropChance}

```
void SetBlackHpDropChance ( float Chance )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设定激光击杀敌人掉落黑心的几率，主要用于虚空之喉。

**Use Cases:**

- 模仿虚空之喉效果
- 自定义掉落物逻辑

**See also:** 
[[#BlackHpDropChance|BlackHpDropChance]]


---

### SetHomingType {#SetHomingType}

```
void SetHomingType ( LaserHomingType Type )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

指定激光的追踪模式（如无追踪、追踪敌人等）。

**Use Cases:**

- 赋予激光追踪能力
- 改变追踪行为

**See also:** 
[[#HomingType|HomingType]], [[#HomingLaser|HomingLaser]]


---

### SetMaxDistance {#SetMaxDistance}

```
void SetMaxDistance ( float Distance )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

限制激光的长度，如用于缩短阿萨谢尔硫磺火的最大射程。

**Use Cases:**

- 裁剪激光距离
- 模拟短射程激光

**See also:** 
[[#MaxDistance|MaxDistance]], [[#LaserLength|LaserLength]]


---

### SetMultidimensionalTouched {#SetMultidimensionalTouched}

```
void SetMultidimensionalTouched ( boolean Value )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

标记激光是否被多维伤害触发过。

**Use Cases:**

- 管理多维效果交互
- 防止重复触发

**See also:** 



---

### SetOneHit {#SetOneHit}

```
void SetOneHit ( boolean Value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

使激光在命中后消失或只造成一次伤害。

**Use Cases:**

- 创建一次性激光
- 平衡高强度激光

**See also:** 
[[#OneHit|OneHit]]


---

### SetTimeout {#SetTimeout}

```
void SetTimeout ( int Value )
```

*DLC: AB+, REP, REP+*

设定激光的存活时间帧数，到期后自动移除。

**Use Cases:**

- 控制激光持续时间
- 防止无限持续时间

**See also:** 
[[#Timeout|Timeout]], [[#FirstUpdate|FirstUpdate]]


---

### ShootAngle {#ShootAngle}

```
static EntityLaser ShootAngle ( int Variant, Vector SourcePos, float AngleDegrees, int Timeout, Vector PosOffset, Entity Source )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

简便地创建激光实体，指定类型、起点、角度、超时等参数，返回生成的激光。

简单化静态助手以简化激光的生成

**Use Cases:**

- 快速生成自定义激光
- 替代冗长的生成逻辑

**See also:** 
[[#CalculateEndPoint|CalculateEndPoint]]


---

### Angle {#Angle}

```
float Angle
```

*DLC: AB+, REP, REP+ | Modifiers: static*

激光当前弧度角。

**Use Cases:**

- 读取或修改激光方向（弧度）
- 与角度制计算转换

**See also:** 
[[#AngleDegrees|AngleDegrees]], [[#SetActiveRotation|SetActiveRotation]]


---

### AngleDegrees {#AngleDegrees}

```
float AngleDegrees
```

*DLC: AB+, REP, REP+ | Modifiers: static*

激光当前角度（度），与Angle对应。

**Use Cases:**

- 获取角度制方向
- 设置旋转角度

**See also:** 
[[#Angle|Angle]], [[#SetActiveRotation|SetActiveRotation]]


---

### BlackHpDropChance {#BlackHpDropChance}

```
float BlackHpDropChance
```

*DLC: AB+, REP, REP+ | Modifiers: const*

激光击杀敌人掉落黑心的概率，主要用于虚空之喉。

For maw of void.

**Use Cases:**

- 获取或修改黑心掉落率
- 自定义虚空之喉行为

**See also:** 
[[#SetBlackHpDropChance|SetBlackHpDropChance]]


---

### BounceLaser {#BounceLaser}

```
Entity BounceLaser {: .copyable aria-label='Variables' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: static*

指向反弹激光实体的引用，用于橡胶胶水等效果。

**Use Cases:**

- 追踪激光反弹链
- 管理子激光

**See also:** 
[[#DisableFollowParent|DisableFollowParent]]


---

### CurveStrength {#CurveStrength}

```
float CurveStrength
```

*DLC: AB+, REP, REP+*

激光的弯曲强度，实现“我的倒影”效果。

My Reflection.

**Use Cases:**

- 制造弯曲激光
- 模拟反射效果

**See also:** 



---

### DisableFollowParent {#DisableFollowParent}

```
boolean DisableFollowParent
```

*DLC: AB+, REP, REP+ | Modifiers: const*

是否禁用跟随父对象偏移，在作为子激光时使用。

设置为其他激光的子项时使用，例如橡胶胶水的反弹。禁用 m_ParentOffset。

**Use Cases:**

- 管理反弹激光的跟随
- 解除父级依赖

**See also:** 
[[#ParentOffset|ParentOffset]], [[#BounceLaser|BounceLaser]]


---

### EndPoint {#EndPoint}

```
Vector EndPoint
```

*DLC: AB+, REP, REP+ | Modifiers: static*

缓存的激光终点向量，避免重复计算。

将会保存终点，以便在外部访问时不需要重新计算。

**Use Cases:**

- 快速获取终点
- 减少性能开销

**See also:** 
[[#GetEndPoint|GetEndPoint]], [[#CalculateEndPoint|CalculateEndPoint]]


---

### FirstUpdate {#FirstUpdate}

```
boolean FirstUpdate
```

*DLC: AB+, REP | Modifiers: const*

标记激光是否处于第一次更新状态。

**Use Cases:**

- 初始化特定行为
- 防止重复触发

**See also:** 
[[#SetTimeout|SetTimeout]]


---

### GridHit {#GridHit}

```
boolean GridHit
```

*DLC: AB+, REP, REP+ | Modifiers: static*

指示激光在当前帧是否被网格实体阻挡。

返回 `true` 如果激光可以被网格实体阻挡，并且在该帧被阻挡。

**Use Cases:**

- 环境碰撞检测
- 决定激光是否终止

**See also:** 
[[#CalculateEndPoint|CalculateEndPoint]]


---

### HomingLaser {#HomingLaser}

```
HomingLaser HomingLaser
```

*DLC: AB+, REP, REP+ | Modifiers: const*

与追踪相关的内部数据。

**Use Cases:**

- 高级追踪逻辑定制

**See also:** 
[[#SetHomingType|SetHomingType]], [[#HomingType|HomingType]]


---

### HomingType {#HomingType}

```
LaserHomingType HomingType
```

*DLC: REP, REP+ | Modifiers: const*

当前激光的追踪类型枚举值。

**Use Cases:**

- 判断追踪模式
- 读取追踪设置

**See also:** 
[[#SetHomingType|SetHomingType]], [[#HomingLaser|HomingLaser]]


---

### IsActiveRotating {#IsActiveRotating}

```
boolean IsActiveRotating
```

*DLC: AB+, REP, REP+*

激光是否正在进行主动旋转。

**Use Cases:**

- 检查旋转状态
- 控制逻辑分支

**See also:** 
[[#SetActiveRotation|SetActiveRotation]]


---

### LaserLength {#LaserLength}

```
float LaserLength
```

*DLC: AB+, REP, REP+*

激光的实际长度。

**Use Cases:**

- 获取或调整激光长度
- 与最大距离对比

**See also:** 
[[#SetMaxDistance|SetMaxDistance]], [[#MaxDistance|MaxDistance]]


---

### LastAngleDegrees {#LastAngleDegrees}

```
float LastAngleDegrees
```

*DLC: AB+, REP, REP+*

上一帧的角度（度），用于计算角度变化。

**Use Cases:**

- 跟踪旋转增量
- 防抖处理

**See also:** 
[[#AngleDegrees|AngleDegrees]], [[#SetActiveRotation|SetActiveRotation]]


---

### MaxDistance {#MaxDistance}

```
float MaxDistance
```

*DLC: AB+, REP, REP+*

激光的最大延伸距离，0 表示无限制。

Used to trim brimstone for Azazel (0 - off)

**Use Cases:**

- 限制硫磺火射程
- 动态调整距离

**See also:** 
[[#SetMaxDistance|SetMaxDistance]], [[#LaserLength|LaserLength]]


---

### OneHit {#OneHit}

```
boolean OneHit
```

*DLC: AB+, REP, REP+*

激光是否只命中一次。

Laser hits only once.

**Use Cases:**

- 设计一次性效果
- 避免多重伤害

**See also:** 
[[#SetOneHit|SetOneHit]]


---

### ParentOffset {#ParentOffset}

```
Vector ParentOffset
```

*DLC: AB+, REP, REP+*

相对于父实体的偏移向量。

**Use Cases:**

- 设定子激光位置
- 跟随父实体

**See also:** 
[[#DisableFollowParent|DisableFollowParent]], [[#BounceLaser|BounceLaser]]


---

### Radius {#Radius}

```
float Radius
```

*DLC: AB+, REP, REP+*

激光的碰撞半径。

**Use Cases:**

- 调整激光粗细
- 修改碰撞检测范围

**See also:** 



---

### RotationDegrees {#RotationDegrees}

```
float RotationDegrees
```

*DLC: AB+, REP, REP+*

当前旋转角度（度）。

**Use Cases:**

- 读取或修改旋转角度
- 生成旋转动画

**See also:** 
[[#SetActiveRotation|SetActiveRotation]], [[#RotationSpd|RotationSpd]]


---

### RotationDelay {#RotationDelay}

```
int RotationDelay
```

*DLC: AB+, REP, REP+*

旋转开始前的延迟帧数。

**Use Cases:**

- 控制旋转启动时间
- 实现延迟旋转效果

**See also:** 
[[#SetActiveRotation|SetActiveRotation]]


---

### RotationSpd {#RotationSpd}

```
float RotationSpd
```

*DLC: AB+, REP, REP+*

旋转速度。

**Use Cases:**

- 调整旋转快慢
- 设置动态旋转

**See also:** 
[[#SetActiveRotation|SetActiveRotation]], [[#RotationDegrees|RotationDegrees]]


---

### SampleLaser {#SampleLaser}

```
boolean SampleLaser
```

*DLC: AB+, REP, REP+*

标识是否为采样渲染模式激光。

**Use Cases:**

- 判断渲染方式
- 优化绘制

**See also:** 
[[#IsSampleLaser|IsSampleLaser]]


---

### Shrink {#Shrink}

```
boolean Shrink
```

*DLC: AB+, REP, REP+*

激光是否正在收缩消失。

**Use Cases:**

- 检测生命周期末期
- 播放收缩特效

**See also:** 



---

### StartAngleDegrees {#StartAngleDegrees}

```
float StartAngleDegrees
```

*DLC: AB+, REP, REP+*

旋转起始角度，用于随机旋转的起始参考。

**Use Cases:**

- 记录起始角度
- 计算旋转偏移

**See also:** 
[[#SetActiveRotation|SetActiveRotation]]


---

### TearFlags {#TearFlags}

```
TearFlags TearFlags
```

*DLC: AB+, REP, REP+*

激光当前的泪弹标志集合。

___

**Use Cases:**

- 读取或覆盖完整泪弹标志
- 调试激光属性

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#ClearTearFlags|ClearTearFlags]], [[#HasTearFlags|HasTearFlags]]


---

### Timeout {#Timeout}

```
int Timeout
```

*DLC: AB+, REP, REP+*

激光剩余存活帧数。

**Use Cases:**

- 获取剩余时间
- 控制消失时机

**See also:** 
[[#SetTimeout|SetTimeout]]


---

## See Also

- [[Entity]]
- [[EntityLaser]]
- [[Vector]]
- [[VectorList]]
