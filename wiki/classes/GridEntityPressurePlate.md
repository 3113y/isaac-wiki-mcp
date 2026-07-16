---
title: GridEntityPressurePlate
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 4
---

# GridEntityPressurePlate

## Summary

GridEntityPressurePlate 代表游戏中的压力板网格实体，用于在被触碰或按下时触发奖励、事件或逻辑，并专门在贪婪模式下管理相关行为和视觉效果。

## Inheritance

- Inherits from: [[GridEntity]]

## Related Types

- [[RNG]]
- [[Sprite]]

## Key Methods

- [[#Reward|Reward]]
- [[#GreedModeRNG|GreedModeRNG]]
- [[#NextGreedAnimation|NextGreedAnimation]]
- [[#TimerPlate|TimerPlate]]

## Methods

### Functions

### Reward {#Reward}

```
void Reward ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

立即触发压力板的奖励生成效果，如同被按压，但不会改变按压状态。在贪婪模式下，该方法会根据当前波次状态生成随机奖励或直接激活一波敌人而不增加波数计数器。

Triggers the spawning of the reward as if the plate would be pressed, without actually pressing it.

**Use Cases:**

- 在脚本中模拟玩家踩下压力板获得奖励
- 在不触发压力板动画或物理碰撞的情况下生成掉落物
- 在贪婪模式中动态控制波次生成以调整难度

**See also:** 
[[#GreedModeRNG|GreedModeRNG]]


---

### GreedModeRNG {#GreedModeRNG}

```
RNG GreedModeRNG
```

*DLC: REP, REP+ | Modifiers: const*

获取用于控制贪婪模式所有随机行为的 RNG 对象，包括奖励生成和波次触发中的随机种子。

RNG object that determines the RNG of anything GreedMode related.

**Use Cases:**

- 读取或修改贪婪模式压力板的随机种子
- 在自定义逻辑中确保随机结果的可重现性
- 结合 Reward 方法实现特定奖励概率控制

**See also:** 
[[#Reward|Reward]]


---

### NextGreedAnimation {#NextGreedAnimation}

```
string NextGreedAnimation
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置或获取贪婪压力板下一次要播放的动画名称，仅影响视觉表现，不改变实际功能。动画名称必须来自 grid_pressureplate.anm2 文件，否则会导致游戏崩溃。

Defines the animation that the greed-mode pressureplate should play. This effect is only visual!

**Use Cases:**

- 在关键游戏时刻切换压力板动画以提供视觉反馈
- 根据波次或状态显示不同的装饰动画
- 在 Mod 中为压力板引入新动画状态

**See also:** 
[[#TimerPlate|TimerPlate]], [[#Reward|Reward]]


---

### TimerPlate {#TimerPlate}

```
Sprite TimerPlate {: .copyable aria-label='Variables' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回对贪婪模式压力板下方计时器板 Sprite 对象的引用，可用于直接操作其外观、动画或属性。

Reference to the Sprite of the Timerplate beneath the pressureplate in Greed mode.

**Use Cases:**

- 调整计时器板的透明度或颜色以匹配 Mod 主题
- 读取或设置计时器板的当前播放帧以同步视觉效果
- 在自定义逻辑中替换计时器板的整个 Sprite

**See also:** 
[[#NextGreedAnimation|NextGreedAnimation]], [[#Reward|Reward]]


---

## See Also

- [[GridEntity]]
- [[RNG]]
- [[Sprite]]
