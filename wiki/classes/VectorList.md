---
title: VectorList
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# VectorList

## Summary

激光采样点的向量列表，用于存储 EntityLaser 的路径样本坐标。

## Related Types

- [[Vector]]

## Key Methods

- [[#__len|__len]]
- [[#Get|Get]]
- [[#Size|Size]]

## Methods

### Operators

### __len {#__len}

```
int __len ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回列表中的向量数量，支持 # 操作符，效果等同于 Size 属性。

**Use Cases:**

- 获取激光样本总数
- 循环遍历所有样本时的循环上限

**See also:** 
[[#Size|Size]], [[#Get|Get]]


---

### Functions

### Get {#Get}

```
Vector Get ( int idx )
```

*DLC: REP, REP+ | Modifiers: const*

根据索引获取激光路径上的一个采样点向量，用于扩展或分析激光轨迹。

**Use Cases:**

- 提取激光某个特定位置坐标
- 计算两点之间的方向或距离
- 绘制激光特效或障碍物检测

**See also:** 
[[#__len|__len]], [[#Size|Size]]


---

### Size {#Size}

```
const int Size
```

*DLC: AB+, REP, REP+ | Modifiers: const*

只读属性，返回列表中的向量元素数量，等效于 __len()。

**Use Cases:**

- 快速获取样本数量
- 判断激光样本是否为空

**See also:** 
[[#__len|__len]], [[#Get|Get]]


---

## See Also

- [[Vector]]
