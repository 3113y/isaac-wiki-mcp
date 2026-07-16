---
title: RoomConfigEntries
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# RoomConfigEntries

## Summary

一个只读的 RoomConfigEntry 列表，表示某个房间生成点配置中的所有特定条目或变体。

## Related Types

- [[Room]]
- [[RoomConfigEntry]]

## Key Methods

- [[#Get|Get]]
- [[#Size|Size]]
- [[#__len|__len]]

## Methods

### Operators

### __len {#__len}

```
int __len ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回此条目列表中的元素总数，通常与 Size 变量值相同，支持 Lua 的 # 操作符。

**Use Cases:**

- 在 for 循环中配合 Get 使用以遍历所有条目
- 检查列表是否为空

**See also:** 
[[#Get|Get]], [[#Size|Size]]


---

### Functions

### Get {#Get}

```
RoomConfig Entry Get ( int idx )
```

*DLC: REP, REP+ | Modifiers: const*

根据给定的零基索引从列表中取出一个 RoomConfigEntry 实例，用于获取该条目的具体配置数据。

**Use Cases:**

- 获取指定位置的房间配置条目
- 动态查询某一生成项的类型和权重

**See also:** 
[[#__len|__len]], [[#Size|Size]]


---

### Size {#Size}

```
const int Size
```

*DLC: AB+, REP, REP+ | Modifiers: const*

常量属性，表示此条目列表的当前元素数量，与 __len 返回的值相同。

**Use Cases:**

- 在没有触发元方法的情况下获取列表长度
- 作为循环上限或边界检查

**See also:** 
[[#__len|__len]], [[#Get|Get]]


---

## See Also

- [[Room]]
- [[RoomConfigEntry]]
