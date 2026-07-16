---
title: CardConfigList
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# CardConfigList

## Summary

代表游戏中所有卡片配置的列表，通过 ItemConfig:GetCards() 获取，主要用于遍历和统计卡片数量。Get 方法由于 bug 暂时无法使用。

## Key Methods

- [[#Size|Size]]
- [[#__len|__len]]
- [[#Get|Get]]

## Methods

### Operators

### __len {#__len}

```
int __len ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

实现取长度运算符 #，返回列表中的卡片数量，与 Size 变量等效。

**Use Cases:**

- 快速获取列表长度
- 配合循环遍历卡片

**See also:** 
[[#Size|Size]], [[#Get|Get]]


---

### Functions

### Get {#Get}

```
userdata Get ( int idx )
```

*DLC: REP, REP+ | Modifiers: const*

尝试按索引获取卡片配置，但由于 bug 返回无效的 userdata，目前无法正常使用。

**Use Cases:**

- 本意是获取指定卡片配置，但当前无效

**See also:** 
[[#__len|__len]], [[#Size|Size]]


---

### Size {#Size}

```
const int Size
```

*DLC: AB+, REP, REP+ | Modifiers: const*

只读常量，存储列表中的卡片数量，功能与 __len 完全相同。

**Use Cases:**

- 直接读取卡片数量
- 替代 # 操作符使用

**See also:** 
[[#__len|__len]], [[#Get|Get]]


---
