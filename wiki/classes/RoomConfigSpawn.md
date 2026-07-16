---
title: RoomConfigSpawn
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 6
---

# RoomConfigSpawn

## Summary

代表房间配置中的一个生成点，包含多个可能的生成条目及其权重，并可根据权重随机选取一个条目。

## Related Types

- [[Room]]
- [[RoomConfigEntries]]

## Key Methods

- [[#PickEntry|PickEntry]]
- [[#Entries|Entries]]
- [[#SumWeights|SumWeights]]

## Methods

### Functions

### PickEntry {#PickEntry}

```
const RoomConfig Entry PickEntry ( float r )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

根据介于0和1之间的随机值r，基于权重随机选取一个房间配置条目，返回对应的RoomConfig Entry。

r is a value between 0 and 1

**Use Cases:**

- 根据随机种子确定生成物
- 实现基于权重的生成逻辑

**See also:** 
[[#Entries|Entries]], [[#SumWeights|SumWeights]]


---

### Entries {#Entries}

```
RoomConfigEntries Entries
```

*DLC: REP, REP+ | Modifiers: const*

获取此生成点下的所有房间配置条目数组。

**Use Cases:**

- 遍历所有可能的生成条目
- 获取特定索引的条目

**See also:** 
[[#PickEntry|PickEntry]]


---

### EntryCount {#EntryCount}

```
int EntryCount
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回此生成点包含的条目数量。

**Use Cases:**

- 判断是否有条目
- 用于循环遍历

**See also:** 
[[#Entries|Entries]]


---

### SumWeights {#SumWeights}

```
float SumWeights
```

*DLC: AB+, REP, REP+ | Modifiers: const*

所有条目权重的总和，用于权重归一化。

**Use Cases:**

- 计算归一化随机值
- 判断生成点是否无条目（和为0）

**See also:** 
[[#PickEntry|PickEntry]]


---

### X {#X}

```
int X
```

*DLC: AB+, REP, REP+ | Modifiers: const*

生成点在房间内的X坐标。

**Use Cases:**

- 定位生成位置
- 配合房间布局

**See also:** 
[[#Y|Y]]


---

### Y {#Y}

```
int Y
```

*DLC: AB+, REP, REP+ | Modifiers: static*

生成点在房间内的Y坐标。

**Use Cases:**

- 定位生成位置
- 配合房间布局

**See also:** 
[[#X|X]]


---

## See Also

- [[Room]]
- [[RoomConfigEntries]]
