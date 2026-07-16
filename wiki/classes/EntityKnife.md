---
title: EntityKnife
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 18
---

# EntityKnife

## Summary

EntityKnife 代表一把飞刀实体，通常由玩家发射（如妈妈的刀）或作为路径跟随刀（如科技零）存在。提供控制刀的行为、泪液标志、运动参数和渲染属性的方法，用于自定义刀的飞行、返回和视觉表现。

## Inheritance

- Inherits from: [[Entity]]

## Key Methods

- [[#AddTearFlags|AddTearFlags]]
- [[#Shoot|Shoot]]
- [[#Reset|Reset]]
- [[#GetKnifeDistance|GetKnifeDistance]]
- [[#SetPathFollowSpeed|SetPathFollowSpeed]]

## Methods

### Functions

### AddTearFlags {#AddTearFlags}

```
void AddTearFlags ( TearFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为刀添加指定的泪液标志，从而赋予特殊效果（如穿透、追踪、爆炸等）。

**Use Cases:**

- 制作有追踪效果的刀
- 临时赋予穿透特性
- 叠加多种泪液效果

**See also:** 
[[#HasTearFlags|HasTearFlags]], [[#ClearTearFlags|ClearTearFlags]], [[#TearFlags|TearFlags]]


---

### ClearTearFlags {#ClearTearFlags}

```
void ClearTearFlags ( TearFlags Flags )
```

*DLC: REP, REP+ | Modifiers: const*

移除刀的特定泪液标志，取消对应效果。

**Use Cases:**

- 某条件达成后移除追踪
- 还原刀的基础行为
- 状态切换时清理旧效果

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#HasTearFlags|HasTearFlags]]


---

### GetKnifeDistance {#GetKnifeDistance}

```
float GetKnifeDistance ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回刀与发射者（或关联实体）之间的距离。

**Use Cases:**

- 判断刀是否超出最大距离
- 实现距离衰减伤害
- 绘制环绕玩家视觉特效

**See also:** 
[[#MaxDistance|MaxDistance]], [[#Shoot|Shoot]]


---

### GetKnifeVelocity {#GetKnifeVelocity}

```
float GetKnifeVelocity ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取刀的当前速度标量，用于运动计算或特效强度。

**Use Cases:**

- 根据速度调整拖尾长度
- 碰撞后速度重置
- 伤害受速度影响

**See also:** 
[[#SetPathFollowSpeed|SetPathFollowSpeed]], [[#GetKnifeDistance|GetKnifeDistance]]


---

### GetRenderZ {#GetRenderZ}

```
int GetRenderZ ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取刀在渲染顺序中的 Z 值，用于控制绘制层级。

**Use Cases:**

- 确保刀渲染在玩家之上
- 多层刀特效层级排序
- 避免被其他实体遮挡

**See also:** 
[[#Scale|Scale]], [[#Rotation|Rotation]]


---

### HasTearFlags {#HasTearFlags}

```
boolean HasTearFlags ( TearFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

检查刀是否拥有指定的泪液标志。

**Use Cases:**

- 根据标志切换伤害类型
- 条件性移除效果
- 视觉反馈判定

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#ClearTearFlags|ClearTearFlags]], [[#TearFlags|TearFlags]]


---

### IsFlying {#IsFlying}

```
boolean IsFlying ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回刀是否处于飞行状态（无视障碍）。

**Use Cases:**

- 决定刀的碰撞判定模式
- 改变拖尾粒子效果
- 逻辑区分飞行刀与地面刀

**See also:** 
[[#GetKnifeVelocity|GetKnifeVelocity]], [[#AddTearFlags|AddTearFlags]]


---

### Reset {#Reset}

```
void Reset ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

使主刀强制返回玩家位置，常用于结束飞行或重置状态。

用于主刀（master knifes），以使其返回到玩家。

**Use Cases:**

- 主动道具冷却时回收刀
- 切换房间时重置位置
- 强制停止远程攻击

**See also:** 
[[#Shoot|Shoot]], [[#GetKnifeDistance|GetKnifeDistance]]


---

### SetPathFollowSpeed {#SetPathFollowSpeed}

```
void SetPathFollowSpeed ( float Speed )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置路径跟随刀沿路径移动的速度倍率。

**Use Cases:**

- 调整科技零风格的环绕速度
- 创建变速路径动画
- 配合 PathOffset 动态移动

**See also:** 
[[#PathFollowSpeed|PathFollowSpeed]], [[#PathOffset|PathOffset]]


---

### Shoot {#Shoot}

```
void Shoot ( float Charge, float Range )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

发射刀，由蓄力值和射程控制其飞行距离与速度。

**Use Cases:**

- 制造可蓄力投掷的刀
- 模拟妈妈的刀攻击
- 自定义技能的射程计算

**See also:** 
[[#Charge|Charge]], [[#MaxDistance|MaxDistance]], [[#Reset|Reset]]


---

### Charge {#Charge}

```
float Charge
```

*DLC: AB+, REP, REP+ | Modifiers: const*

刀的蓄力值，影响 Shoot 时的初始速度和/或射程。

**Use Cases:**

- 组合蓄力条显示
- 蓄力中断后重置为0
- 满蓄力自动发射

**See also:** 
[[#Shoot|Shoot]], [[#SetPathFollowSpeed|SetPathFollowSpeed]]


---

### MaxDistance {#MaxDistance}

```
float MaxDistance
```

*DLC: AB+, REP, REP+ | Modifiers: const*

刀的最大飞行距离，超过后可能消失或返回。

**Use Cases:**

- 自定义射程上限
- 缩短或延长刀存活时间
- 射程计数器

**See also:** 
[[#Shoot|Shoot]], [[#GetKnifeDistance|GetKnifeDistance]]


---

### PathFollowSpeed {#PathFollowSpeed}

```
float PathFollowSpeed
```

*DLC: AB+, REP, REP+ | Modifiers: static*

路径跟随刀的路径移动速度基础值，用于环绕或固定轨迹运动。

Unit speed of path moving knifes.

**Use Cases:**

- 创建慢速护航刀
- 调整科技零旋转速度
- 与 PathOffset 配合实现动态螺旋

**See also:** 
[[#SetPathFollowSpeed|SetPathFollowSpeed]], [[#PathOffset|PathOffset]]


---

### PathOffset {#PathOffset}

```
float PathOffset
```

*DLC: AB+, REP, REP+ | Modifiers: const*

刀沿设定路径的偏移量，改变其在路径上的初始或当前位置。

**Use Cases:**

- 多把刀均匀分布同一条路径
- 创建波状运动
- 动画循环偏移

**See also:** 
[[#PathFollowSpeed|PathFollowSpeed]], [[#SetPathFollowSpeed|SetPathFollowSpeed]]


---

### Rotation {#Rotation}

```
float Rotation
```

*DLC: AB+, REP, REP+ | Modifiers: static*

刀的当前旋转角度（弧度或度），影响朝向和视觉效果。

**Use Cases:**

- 随鼠标角度旋转刀
- 生成扇形刀阵
- 绘制旋转拖尾

**See also:** 
[[#RotationOffset|RotationOffset]], [[#Shoot|Shoot]]


---

### RotationOffset {#RotationOffset}

```
float RotationOffset
```

*DLC: AB+, REP, REP+ | Modifiers: const*

刀的基础旋转偏移量，叠加到 Rotation 上用于初始朝向。

**Use Cases:**

- 固定多把刀均匀分布
- 设置默认朝向
- 在不改变逻辑角度下调整外观

**See also:** 
[[#Rotation|Rotation]], [[#Scale|Scale]]


---

### Scale {#Scale}

```
float Scale
```

*DLC: AB+, REP, REP+*

刀的渲染缩放因子，改变视觉大小。

**Use Cases:**

- 制作小刀变成大刀的成长效果
- 蓄力时动态缩放
- 统一调整多把刀的大小

**See also:** 
[[#GetRenderZ|GetRenderZ]], [[#Rotation|Rotation]]


---

### TearFlags {#TearFlags}

```
TearFlags TearFlags
```

*DLC: AB+, REP, REP+ | Modifiers: const*

存储当前刀拥有的泪液标志组合，对应 Add/Clear/HasTearFlags。

**Use Cases:**

- 直接读取当前全部标志
- 用于条件判断或复制状态
- 配合位运算组合新效果

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#ClearTearFlags|ClearTearFlags]], [[#HasTearFlags|HasTearFlags]]


---

## See Also

- [[Entity]]
