---
title: RoomConfigEntry
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 4
---

# RoomConfigEntry

## Summary

表示房间配置中一个实体生成条目的数据容器，记录了可能生成的实体类型、变体、子类型及其权重。

## Related Types

- [[Entity]]

## Key Methods

- [[#Type|Type]]
- [[#Variant|Variant]]
- [[#Subtype|Subtype]]
- [[#Weight|Weight]]

## Methods

### Functions

### Subtype {#Subtype}

```
int Subtype
```

*DLC: AB+, REP, REP+ | Modifiers: const*

该条目的实体子类型，用于区分同一类型和变体下的不同具体形态（如特定种类的心或硬币）。

**Use Cases:**

- 获取子类型以确定生成实体的精细变种
- 对子类型进行过滤或修改来改变房间内容

**See also:** 
[[#Type|Type]], [[#Variant|Variant]]


---

### Type {#Type}

```
EntityType Type
```

*DLC: REP, REP+ | Modifiers: const*

该条目生成的实体类型，对应 EntityType 枚举，决定实体大类（如怪物、掉落物、障碍物）。

**Use Cases:**

- 判断该条目对应的是何种实体类别
- 改变类型以完全替换房间中可能出现的实体

**See also:** 
[[#Variant|Variant]], [[#Subtype|Subtype]]


---

### Variant {#Variant}

```
int Variant
```

*DLC: AB+, REP, REP+ | Modifiers: const*

该条目的实体变体，在 EntityType 基础上进一步细分实体形态（如不同种类的敌人）。

**Use Cases:**

- 获取具体实体变体用于精确控制生成
- 修改变体以创建自定义房间配置

**See also:** 
[[#Type|Type]], [[#Subtype|Subtype]]


---

### Weight {#Weight}

```
float Weight
```

*DLC: AB+, REP, REP+ | Modifiers: const*

该条目的生成权重，数值越高被选中生成的概率越大，用于房间配置的随机抽取。

**Use Cases:**

- 调整或读取实体出现的概率
- 基于权重自行实现自定义挑选逻辑

**See also:** 
[[#Type|Type]], [[#Variant|Variant]]


---

## See Also

- [[Entity]]
