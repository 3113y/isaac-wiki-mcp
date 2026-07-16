---
title: PillConfigList
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# PillConfigList

## Summary

存储药丸效果列表的容器，提供数量获取和索引访问功能，但索引访问因Bug无法正常使用。

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

返回药丸效果列表的长度，支持#运算符直接调用。

**Use Cases:**

- 使用 # 运算符快速获取效果数量
- 在循环中作为最大索引边界

**See also:** 
[[#Size|Size]]


---

### Functions

### Get {#Get}

```
userdata Get ( int idx )
```

*DLC: REP, REP+ | Modifiers: const*

根据索引返回药丸效果数据，但实际存在Bug，无法获得可用对象，功能等同于无效。

**Use Cases:**

- 尝试按序号访问单个药丸效果（不可用）

**See also:** 



---

### Size {#Size}

```
const int Size
```

*DLC: AB+, REP, REP+ | Modifiers: const*

整数常量，表示列表中包含的药丸效果总数，与 __len 返回值一致。

**Use Cases:**

- 直接读取列表大小而无需使用运算符
- 在条件判断或循环设置中作为上限值

**See also:** 
[[#__len|__len]]


---
