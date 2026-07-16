---
title: EntityTear
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 29
---

# EntityTear

## Summary

代表游戏中玩家或其他源发射的眼泪实体，用于控制眼泪的外观、行为、物理属性和特殊效果。

## Inheritance

- Inherits from: [[Entity]]

## Related Types

- [[Vector]]

## Key Methods

- [[#AddTearFlags|AddTearFlags]]
- [[#ChangeVariant|ChangeVariant]]
- [[#SetDeadEyeIntensity|SetDeadEyeIntensity]]

## Methods

### Functions

### AddTearFlags {#AddTearFlags}

```
void AddTearFlags ( TearFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为眼泪添加指定的 TearFlags，赋予特殊效果如穿透或寻的。

**Use Cases:**

- 使眼泪获得穿透敌人能力
- 添加光谱或追踪效果

**See also:** 
[[#HasTearFlags|HasTearFlags]], [[#ClearTearFlags|ClearTearFlags]]


---

### ChangeVariant {#ChangeVariant}

```
void ChangeVariant ( TearVariant NewVariant )
```

*DLC: REP, REP+ | Modifiers: const*

切换眼泪的变体类型，改变其外观和基础行为。

**Use Cases:**

- 将普通眼泪变为硫磺火激光
- 改为穿刺或爆炸泪

**See also:** 
[[#TearFlags|TearFlags]]


---

### ClearTearFlags {#ClearTearFlags}

```
void ClearTearFlags ( TearFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

从眼泪中移除指定的 TearFlags，撤销对应效果。

**Use Cases:**

- 移除临时赋予的追踪标志

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#HasTearFlags|HasTearFlags]]


---

### HasTearFlags {#HasTearFlags}

```
boolean HasTearFlags ( TearFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检查眼泪是否拥有指定的 TearFlags，用于条件逻辑。

**Use Cases:**

- 根据眼泪标志触发额外伤害

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#TearFlags|TearFlags]]


---

### ResetSpriteScale {#ResetSpriteScale}

```
void ResetSpriteScale ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

根据当前缩放值重置眼泪精灵动画，矫正因缩放导致的动画异常。

Resets the tear sprite animation depending on scale.

**Use Cases:**

- 改变眼泪大小后恢复正确动画

**See also:** 
[[#Scale|Scale]]


---

### SetDeadEyeIntensity {#SetDeadEyeIntensity}

```
void SetDeadEyeIntensity ( float Intensity )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

设置死亡之眼效果的强度，影响连击精准度增益。

**Use Cases:**

- 动态调整死亡之眼伤害加成

**See also:** 
[[#CanTriggerStreakEnd|CanTriggerStreakEnd]]


---

### SetKnockbackMultiplier {#SetKnockbackMultiplier}

```
void SetKnockbackMultiplier ( float Multiplier )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置眼泪的击退倍率，影响对敌人的击退力。

**Use Cases:**

- 增加或减少击退效果

**See also:** 
[[#KnockbackMultiplier|KnockbackMultiplier]]


---

### SetParentOffset {#SetParentOffset}

```
void SetParentOffset ( Vector Offset )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置眼泪相对于发射实体的偏移位置，调整生成点。

**Use Cases:**

- 偏移眼泪出现位置以匹配自定义动画

**See also:** 
[[#ParentOffset|ParentOffset]]


---

### SetWaitFrames {#SetWaitFrames}

```
void SetWaitFrames ( int Value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置眼泪在行动前的等待帧数，产生延时效果。

**Use Cases:**

- 实现蓄力或延时发射

**See also:** 
[[#WaitFrames|WaitFrames]]


---

### BaseDamage {#BaseDamage}

```
const float BaseDamage
```

*DLC: AB+, REP, REP+ | Modifiers: const*

只读变量，记录眼泪的基础伤害值，独立于伤害修改。

**Use Cases:**

- 读取原始伤害用于比例计算

**See also:** 



---

### BaseScale {#BaseScale}

```
const float BaseScale
```

*DLC: AB+, REP, REP+ | Modifiers: const*

只读变量，记录眼泪的基础缩放大小。

**Use Cases:**

- 获取默认尺寸以便恢复

**See also:** 



---

### Bounced {#Bounced}

```
boolean Bounced
```

*DLC: AB+, REP, REP+ | Modifiers: const*

指示眼泪是否发生了弹射（Repentance 中已移除）。

true if tear bounced off something.

**Use Cases:**

- 向后兼容判断反弹状态

**See also:** 



---

### CanTriggerStreakEnd {#CanTriggerStreakEnd}

```
boolean CanTriggerStreakEnd
```

*DLC: AB+, REP, REP+ | Modifiers: static*

控制眼泪能否触发连击中断条件，用于 Onan 及 Dead Eye。

For Onan's strak and Dead Eye.

**Use Cases:**

- 避免自定义泪影响连击计数

**See also:** 
[[#SetDeadEyeIntensity|SetDeadEyeIntensity]]


---

### ContinueVelocity {#ContinueVelocity}

```
Vector ContinueVelocity
```

*DLC: AB+, REP, REP+ | Modifiers: const*

存储泪的持续速度向量，影响轨迹惯性。

**Use Cases:**

- 调整曲线泪的飞行方向

**See also:** 



---

### FallingAcceleration {#FallingAcceleration}

```
float FallingAcceleration
```

*DLC: AB+, REP, REP+ | Modifiers: static*

控制眼泪下落过程中的加速度。

**Use Cases:**

- 模拟下落重力效果

**See also:** 



---

### FallingSpeed {#FallingSpeed}

```
float FallingSpeed
```

*DLC: AB+, REP, REP+ | Modifiers: const*

当前眼泪的下落速度。

**Use Cases:**

- 获取下落状态速度

**See also:** 



---

### Height {#Height}

```
float Height
```

*DLC: AB+, REP, REP+*

眼泪的离地高度，影响视觉和弹道高度。

**Use Cases:**

- 控制泪的垂直位置

**See also:** 



---

### HomingFriction {#HomingFriction}

```
float HomingFriction
```

*DLC: AB+, REP, REP+ | Modifiers: const*

寻的摩擦系数，影响跟踪转向平滑度。

**Use Cases:**

- 调整跟踪泪的灵活性

**See also:** 



---

### KnockbackMultiplier {#KnockbackMultiplier}

```
float KnockbackMultiplier
```

*DLC: AB+, REP, REP+ | Modifiers: static*

当前眼泪的击退强度倍率。

**Use Cases:**

- 读取击退值用于计算

**See also:** 
[[#SetKnockbackMultiplier|SetKnockbackMultiplier]]


---

### ParentOffset {#ParentOffset}

```
Vector ParentOffset
```

*DLC: AB+, REP, REP+ | Modifiers: static*

相对于发射者的位置偏移，用于调整实体位置而非渲染偏移。

Used for Position adjustment (vs PositionOffset which is a render offset)

**Use Cases:**

- 微调眼泪生成点
- 避免与发射者重叠

**See also:** 
[[#SetParentOffset|SetParentOffset]]


---

### PosDisplacement {#PosDisplacement}

```
const Vector PosDisplacement
```

*DLC: AB+, REP, REP+ | Modifiers: const*

只读位移向量，表示眼泪生成时的位置修正。

**Use Cases:**

- 获取预设位移值

**See also:** 



---

### Rotation {#Rotation}

```
float Rotation
```

*DLC: AB+, REP, REP+ | Modifiers: static*

眼泪精灵的旋转角度。

**Use Cases:**

- 旋转泪精灵以匹配方向

**See also:** 



---

### Scale {#Scale}

```
float Scale
```

*DLC: AB+, REP, REP+*

当前眼泪的缩放比例。

**Use Cases:**

- 动态改变眼泪大小

**See also:** 
[[#ResetSpriteScale|ResetSpriteScale]]


---

### StickDiff {#StickDiff}

```
Vector StickDiff
```

*DLC: AB+, REP, REP+ | Modifiers: const*

黏着在目标上的相对位置差异向量。

**Use Cases:**

- 控制黏附着时的偏移

**See also:** 



---

### StickTarget {#StickTarget}

```
Entity StickTarget {: .copyable aria-label='Variables' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: static*

眼泪粘附的目标实体，可能为 nil。

**Use Cases:**

- 获取附着目标进行额外操作

**See also:** 



---

### StickTimer {#StickTimer}

```
int StickTimer
```

*DLC: AB+, REP | Modifiers: const*

眼泪剩余粘附帧数。

**Use Cases:**

- 判断何时解除粘附

**See also:** 



---

### TearFlags {#TearFlags}

```
TearFlags TearFlags
```

*DLC: AB+, REP, REP+ | Modifiers: static*

眼泪当前拥有的所有 TearFlags 位掩码。

**Use Cases:**

- 检查或比较标志集合

**See also:** 
[[#AddTearFlags|AddTearFlags]]


---

### TearIndex {#TearIndex}

```
const int TearIndex
```

*DLC: AB+, REP, REP+ | Modifiers: const*

玩家本轮发射眼泪的全局序号，从0开始递增。

- In each run, the game keeps track of how many tears have been fired by the player in total.

**Use Cases:**

- 判断是否为第一颗泪
- 标记特定泪的ID

**See also:** 



---

### WaitFrames {#WaitFrames}

```
int WaitFrames
```

*DLC: REP, REP+ | Modifiers: const*

眼泪等待行动前的剩余帧数。

**Use Cases:**

- 控制延迟生效

**See also:** 
[[#SetWaitFrames|SetWaitFrames]]


---

## See Also

- [[Entity]]
- [[Vector]]
