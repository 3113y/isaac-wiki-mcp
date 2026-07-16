---
title: PlayerTypesPosVel
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 2
---

# PlayerTypesPosVel

## Summary

存储多方向射击时单个方向的位置和速度数据，由 EntityPlayer:GetMultiShotPositionVelocity() 返回。

## Related Types

- [[Vector]]

## Key Methods

- [[#Position|Position]]
- [[#Velocity|Velocity]]

## Methods

### Functions

### Position {#Position}

```
Vector Position
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取多方向射击中该方向对应的起始位置向量。

**Use Cases:**

- 确定子弹生成点以进行自定义偏移
- 根据位置生成射弹前的特效

**See also:** 
[[#Velocity|Velocity]]


---

### Velocity {#Velocity}

```
Vector Velocity
```

*DLC: REP, REP+ | Modifiers: const*

获取多方向射击中该方向对应的初始速度向量。

**Use Cases:**

- 修改子弹的初始速度以实现弹幕效果
- 基于速度值预测飞行路径或绘制指示线

**See also:** 
[[#Position|Position]]


---

## See Also

- [[Vector]]
