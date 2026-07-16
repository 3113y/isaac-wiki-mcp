---
title: RoomConfigSpawns
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# RoomConfigSpawns

## Summary

管理房间配置中所有可生成物（Spawn）的列表，提供数量查询和按索引获取具体生成物对象的功能。

## Related Types

- [[Room]]
- [[RoomConfigSpawn]]

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

获取列表中可生成物的总数，对应于长度操作符（#），返回值与 Size 变量相同。

**Use Cases:**

- 在循环开始前获取总数量
- 快速判断列表是否为空

**See also:** 
[[#Get|Get]], [[#Size|Size]]


---

### Functions

### Get {#Get}

```
RoomConfig Spawn Get ( int idx )
```

*DLC: REP, REP+ | Modifiers: const*

根据提供的整数索引从列表中返回一个 RoomConfigSpawn 对象，用于获取该生成物的详细配置数据。

**Use Cases:**

- 遍历所有生成物并获取每个生成物的具体信息
- 按索引访问特定的生成物点

**See also:** 
[[#__len|__len]], [[#Size|Size]]


---

### Size {#Size}

```
const int Size
```

*DLC: AB+, REP, REP+ | Modifiers: const*

常量整数属性，表示列表中可生成物的数量，功能等同于 __len 运算符的返回值。

**Use Cases:**

- 直接读取生成物总数而不调用运算符
- 作为只读值存储或比较

**See also:** 
[[#__len|__len]], [[#Get|Get]]


---

## See Also

- [[Room]]
- [[RoomConfigSpawn]]
