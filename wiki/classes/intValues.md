---
title: intValues
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# intValues

## Summary

intValues 是一个整数列表类，提供对一系列整数的存储和索引访问能力，通常用于获取游戏内部生成的随机数值或预定义整数序列。

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

重载长度运算符，返回该整数列表的元素总数。

**Use Cases:**

- 快速判断列表是否为空
- 循环中获取迭代次数

**See also:** 
[[#Size|Size]]


---

### Functions

### Get {#Get}

```
userdata Get ( int idx )
```

*DLC: REP, REP+ | Modifiers: const*

根据给定的整数索引获取列表中的对应元素，索引从 0 开始。

**Use Cases:**

- 按位置读取指定整数
- 遍历所有元素值

**See also:** 
[[#Size|Size]]


---

### Size {#Size}

```
const int Size
```

*DLC: AB+, REP, REP+ | Modifiers: const*

只读变量，存储该整数列表的当前长度。

**Use Cases:**

- 获取列表大小而不触发运算符调用
- 判断列表是否已被修改

**See also:** 
[[#__len|__len]]


---
