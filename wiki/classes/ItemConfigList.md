---
title: ItemConfigList
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# ItemConfigList

## Summary

代表由 ItemConfig 返回的物品配置列表（如空物品或饰品）。提供列表长度查询功能，但按索引获取元素的方法存在 Bug，无法返回有效数据。

## Key Methods

- [[#__len|__len]]
- [[#Size|Size]]

## Methods

### Operators

### __len {#__len}

```
int __len ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取列表中的物品数量，支持使用 # 号操作符。等效于读取 Size 变量。

**Use Cases:**

- 快速获取列表长度用于循环边界
- 判断列表是否为空

**See also:** 
[[#Size|Size]]


---

### Functions

### Get {#Get}

```
userdata Get ( int idx )
```

*DLC: REP, REP+ | Modifiers: const*

按索引获取列表中的物品配置 userdata，但根据已知 Bug 此方法不会返回可用的数据，实际上无法使用。

**Use Cases:**

- 理论上用于按索引访问物品配置

**See also:** 



---

### Size {#Size}

```
const int Size
```

*DLC: AB+, REP, REP+ | Modifiers: const*

只读变量，存储列表中的物品数量，功能与通过长度运算符获取的值相同。

**Use Cases:**

- 需要整数变量保存列表大小时使用
- 替代长度运算符进行长度检查

**See also:** 
[[#__len|__len]]


---
