---
title: EntityBomb
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 8
---

# EntityBomb

## Summary

EntityBomb代表游戏中的炸弹实体，可由玩家发射或生成，提供修改炸弹属性、爆炸倒计时和眼泪标志等功能的接口。

## Inheritance

- Inherits from: [[Entity]]

## Key Methods

- [[#AddTearFlags|AddTearFlags]]
- [[#ClearTearFlags|ClearTearFlags]]
- [[#HasTearFlags|HasTearFlags]]
- [[#SetExplosionCountdown|SetExplosionCountdown]]

## Methods

### Functions

### AddTearFlags {#AddTearFlags}

```
void AddTearFlags ( TearFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为炸弹添加指定的泪弹效果标志，从而影响其爆炸行为或特殊功能。

**Use Cases:**

- 给炸弹添加毒气、燃烧或穿透等效果
- 组合多个标志创造复合爆炸特性

**See also:** 
[[#ClearTearFlags|ClearTearFlags]], [[#HasTearFlags|HasTearFlags]]


---

### ClearTearFlags {#ClearTearFlags}

```
void ClearTearFlags ( TearFlags Flags )
```

*DLC: REP, REP+ | Modifiers: const*

移除炸弹已拥有的指定泪弹效果标志，恢复默认爆炸行为。

**Use Cases:**

- 取消之前添加的毒气或追踪标志
- 动态调整炸弹的特性

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#HasTearFlags|HasTearFlags]]


---

### HasTearFlags {#HasTearFlags}

```
boolean HasTearFlags ( TearFlags Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检查炸弹当前是否包含特定的泪弹效果标志，返回布尔值。

**Use Cases:**

- 判断炸弹是否具有某种特殊效果以执行分支逻辑
- 在设置标志前进行状态检测

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#ClearTearFlags|ClearTearFlags]]


---

### SetExplosionCountdown {#SetExplosionCountdown}

```
void SetExplosionCountdown ( int Countdown )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置炸弹爆炸的倒计时（单位：帧），控制引爆时刻。

**Use Cases:**

- 立即引爆炸弹（Countdown设为0）
- 延长爆炸等待时间制作延时炸弹

**See also:** 



---

### ExplosionDamage {#ExplosionDamage}

```
float ExplosionDamage
```

*DLC: AB+, REP, REP+ | Modifiers: const*

炸弹爆炸时造成的伤害值，可读写以调整爆炸伤害。

**Use Cases:**

- 动态修改炸弹伤害以匹配玩家属性
- 创建高伤害或低伤害的特殊炸弹

**See also:** 
[[#SetExplosionCountdown|SetExplosionCountdown]]


---

### Flags {#Flags}

```
TearFlags Flags
```

*DLC: AB+, REP, REP+ | Modifiers: static*

直接表示炸弹当前拥有的所有泪弹效果标志，可整体读取或写入。

**Use Cases:**

- 一次性覆盖炸弹的全部标志
- 读取当前标志值用于逻辑判断

**See also:** 
[[#AddTearFlags|AddTearFlags]], [[#ClearTearFlags|ClearTearFlags]], [[#HasTearFlags|HasTearFlags]]


---

### IsFetus {#IsFetus}

```
boolean IsFetus
```

*DLC: AB+, REP, REP+ | Modifiers: const*

指示该炸弹是否源自Dr. Fetus道具或类似效果（胎儿炸弹）。

**Use Cases:**

- 识别炸弹生成来源以便应用特殊行为
- 限制某些操作仅对胎儿炸弹生效

**See also:** 



---

### RadiusMultiplier {#RadiusMultiplier}

```
float RadiusMultiplier
```

*DLC: AB+, REP, REP+ | Modifiers: const*

爆炸半径的乘数，影响最终爆炸作用范围。

**Use Cases:**

- 扩大炸弹的杀伤范围
- 制作缩小范围但集中伤害的炸弹

**See also:** 



---

## See Also

- [[Entity]]
