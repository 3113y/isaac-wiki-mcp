---
title: CostumeConfigList
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# CostumeConfigList

## Summary

表示一套服装配置的只读列表，但目前无法直接获取该类的实例；主要用于提供服装数量信息，但获取单个配置的方法因Bug无效。

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

返回列表中服装配置的数量，与变量 Size 功能相同。

**Use Cases:**

- 使用 # 操作符获取列表长度
- 循环遍历索引之前检查长度

**See also:** 
[[#Size|Size]]


---

### Functions

### Get {#Get}

```
userdata Get ( int idx )
```

*DLC: REP, REP+ | Modifiers: const*

尝试通过索引获取指定的服装配置数据，但已知存在Bug，返回的 userdata 不可用。

**Use Cases:**

- 本方法因Bug无法实际使用

**See also:** 



---

### Size {#Size}

```
const int Size
```

*DLC: AB+, REP, REP+ | Modifiers: const*

一个只读常量，表示列表中服装配置的数量，等价于 __len 的结果。

**Use Cases:**

- 直接读取服装配置数量
- 与其他长度比较

**See also:** 
[[#__len|__len]]


---
