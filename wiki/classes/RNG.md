---
title: RNG
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 6
---

# RNG

## Summary

RNG 类提供基于 Xorshift 算法的确定性伪随机数生成。所有实例必须通过 SetSeed 设置非零种子和对应的 ShiftIdx 后才能用于随机数计算。广泛用于实体掉落、卡片、道具等需要种子的场景。

## Key Methods

- [[#SetSeed|SetSeed]]
- [[#RandomInt|RandomInt]]
- [[#RandomFloat|RandomFloat]]
- [[#Next|Next]]

## Methods

### Constructors

### RNG {#RNG}

```
RNG RNG ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

构造一个新的 RNG 对象，初始种子固定为 2853650767。必须随后调用 SetSeed 赋予有意义种子才能用于实际随机数生成。

**Use Cases:**

- 创建可配置的独立随机数序列
- 作为实体或房间 RNG 的初始容器

**See also:** 
[[#SetSeed|SetSeed]]


---

### Functions

### GetSeed {#GetSeed}

```
int GetSeed ( )
```

*DLC: REP, REP+ | Modifiers: const*

返回 RNG 当前内部种子值，可用于保存状态或诊断。

**Use Cases:**

- 保存随机状态以便日后还原
- 调试时检查当前种子

**See also:** 
[[#SetSeed|SetSeed]]


---

### Next {#Next}

```
int Next ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将 RNG 内部状态向前迭代一步，返回下一个伪随机整数，通常由 RandomInt / RandomFloat 自动调用。

**Use Cases:**

- 手动推进随机数序列
- 实现自定义随机逻辑

**See also:** 
[[#RandomInt|RandomInt]], [[#RandomFloat|RandomFloat]]


---

### RandomFloat {#RandomFloat}

```
float RandomFloat ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回 [0,1) 区间浮点随机数，会自动调用 Next，常用于概率比较。

返回一个 0 到 1 之间的数。包含下限 0，不包含上限 1。

**Use Cases:**

- 判断百分比触发事件
- 实现概率性行为

**See also:** 
[[#Next|Next]]


---

### RandomInt {#RandomInt}

```
int RandomInt ( int Max )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回 [0, Max) 区间整型随机数，会自动调用 Next，适用于索引或计数选择。

返回一个 0 到最大值之间的整数。包含下限 0，不包含上限 Max。

**Use Cases:**

- 随机选择数组元素
- 生成随机掉落数量

**See also:** 
[[#Next|Next]]


---

### SetSeed {#SetSeed}

```
void SetSeed ( int Seed, int ShiftIdx )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

设置 RNG 的种子及 ShiftIdx。Seed 必须为正整数且非零，ShiftIdx 范围 0-80。推荐使用 ShiftIdx=35。

设置指定 RNG 对象的种子。Seed 必须为正整数且**不能为 0**，否则会导致崩溃。ShiftIdx 必须在 0 到 80（含）之间，否则也会导致崩溃。

**Use Cases:**

- 初始化 RNG 以复现游戏内特定序列
- 从游戏种子衍生出各类子 RNG

**See also:** 
[[#RNG|RNG]], [[#GetSeed|GetSeed]], [[#RandomInt|RandomInt]], [[#RandomFloat|RandomFloat]]


---

## See Also

- [[RNG]]
