---
title: EntityList
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# EntityList

## Summary

EntityList 是实体的列表容器，通过特定查询函数获得，提供长度获取和按索引访问实体。

## Related Types

- [[Entity]]

## Key Methods

- [[#Get|Get]]
- [[#__len|__len]]
- [[#Size|Size]]

## Methods

### Operators

### __len {#__len}

```
int __len ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回列表中实体的数量，支持使用#操作符获取长度。

**Use Cases:**

- 统计实体数量
- 遍历实体时使用长度作为循环上限

**See also:** 
[[#Size|Size]], [[#Get|Get]]


---

### Functions

### Get {#Get}

```
Entity Get ( int idx )
```

*DLC: REP, REP+ | Modifiers: const*

根据索引获取列表中对应位置的实体。

**Use Cases:**

- 遍历实体列表访问每个实体
- 获取特定索引的实体进行修改

**See also:** 
[[#__len|__len]], [[#Size|Size]]


---

### Size {#Size}

```
const int Size
```

*DLC: AB+, REP, REP+ | Modifiers: const*

常量，表示列表中实体的数量，功能与__len操作符相同。

**Use Cases:**

- 获取实体数量
- 用于循环条件

**See also:** 
[[#__len|__len]], [[#Get|Get]]


---

## See Also

- [[Entity]]
