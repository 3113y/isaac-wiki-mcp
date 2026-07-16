---
title: BitSet128
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 15
---

# BitSet128

## Summary

BitSet128 用于存储最大128位的标志位系统，解决64位整数标志数量限制，通过低64位(l)和高64位(h)组合实现，支持位运算与比较操作。

## Key Methods

- [[#Get|Get]]
- [[#Set|Set]]
- [[#__bor|__bor]]
- [[#__band|__band]]
- [[#__bxor|__bxor]]

## Methods

### Constructors

### BitSet128 {#BitSet128}

```
BitSet128 BitSet128 ( int Low = 0, int High = 0 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

构造函数，创建一个新的 BitSet128 对象，可指定低64位和高64位的初始整数值，默认均为0。

**Use Cases:**

- 创建包含特定标志的实例
- 从枚举值初始化标志集

**See also:** 
[[#Set|Set]], [[#Get|Get]], [[#h|h]], [[#l|l]]


---

### Operators

### __bnot {#__bnot}

```
BitSet128 __bnot ( )
```

*DLC: REP, REP+ | Modifiers: const*

按位取反操作 (~)，返回当前 BitSet128 所有位翻转后的新对象。

Defines the negation of a [BitSet128](BitSet128.md) object using the `~` operator.

**Use Cases:**

- 翻转所有标志位
- 创建互补标志集

**See also:** 
[[#__bor|__bor]], [[#__band|__band]], [[#__bxor|__bxor]]


---

### __bor {#__bor}

```
BitSet128 __bor ( BitSet128 Right )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

按位或操作 (|)，合并两个 BitSet128 的所有标志位，返回结果对象。

Defines the binary OR operation of two [BitSet128](BitSet128.md) objects using the `|` operator.

**Use Cases:**

- 组合多个标志
- 累积不同来源的效果

**See also:** 
[[#__band|__band]], [[#__bxor|__bxor]], [[#Get|Get]], [[#Set|Set]]


---

### __band {#__band}

```
BitSet128 __band ( BitSet128 Right )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

按位与操作 (&)，保留两个 BitSet128 都设置的标志位，返回结果对象。

Defines the binary AND operation of two [BitSet128](BitSet128.md) objects using the `&` operator.

**Use Cases:**

- 检查共享标志
- 过滤特定标志组

**See also:** 
[[#__bor|__bor]], [[#__bxor|__bxor]], [[#Get|Get]], [[#Set|Set]]


---

### __bxor {#__bxor}

```
BitSet128 __bxor ( BitSet128 Right )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

按位异或操作 (文档描述使用 ~，实际应为 ^)，保留两个 BitSet128 差异的标志位。

Defines the binary XOR operation of two [BitSet128](BitSet128.md) objects using the `~` operator.

**Use Cases:**

- 切换标志位状态
- 找出不同标志集

**See also:** 
[[#__bor|__bor]], [[#__band|__band]], [[#Get|Get]], [[#Set|Set]]


---

### __shl {#__shl}

```
BitSet128 __shl ( int Shift )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

左移操作 (<<)，将 BitSet128 的所有位向左移动指定位数。

Defines the left bit-shift operator of a [BitSet128](BitSet128.md) object using the `<<` operator.

**Use Cases:**

- 位操作构建
- 动态创建高位标志

**See also:** 
[[#__shr|__shr]], [[#Get|Get]], [[#Set|Set]]


---

### __shr {#__shr}

```
BitSet128 __shr ( int Shift )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

右移操作 (>>)，将 BitSet128 的所有位向右移动指定位数。

Defines the right bit-shift operator of a [BitSet128](BitSet128.md) object using the `>>` operator.

**Use Cases:**

- 位操作解析
- 提取低部分标志

**See also:** 
[[#__shl|__shl]], [[#Get|Get]], [[#Set|Set]]


---

### __eq {#__eq}

```
boolean __eq ( BitSet128 right )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

相等比较 (==)，判断两个 BitSet128 对象的低、高部分是否完全相同。

Defines the equality operation of two [BitSet128](BitSet128.md) objects using the `==` operator.

**Use Cases:**

- 精确匹配标志集
- 判断状态一致

**See also:** 
[[#__lt|__lt]], [[#__le|__le]], [[#Get|Get]]


---

### __lt {#__lt}

```
boolean __lt ( BitSet128 right )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

小于比较 (<)，按数值比较两个 BitSet128（先比较高64位，再比较低64位），隐含 > 运算符。

Defines the "smaller than"-Operation of two [BitSet128](BitSet128.md) objects using the `<` operator.

**Use Cases:**

- 排序标志集
- 区间判断

**See also:** 
[[#__le|__le]], [[#__eq|__eq]]


---

### __le {#__le}

```
boolean __le ( BitSet128 right )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

小于等于比较 (<=)，按数值比较两个 BitSet128，隐含 >= 运算符。

Defines the "smaller of equal" operation of two [BitSet128](BitSet128.md) objects using the `<=` operator.

**Use Cases:**

- 范围检查
- 非严格排序

**See also:** 
[[#__lt|__lt]], [[#__eq|__eq]]


---

### __tostring {#__tostring}

```
void __tostring ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

[BitSet128](BitSet128.md) objects can be cast to a string object, which returns information about this object in the following format:

[BitSet128](BitSet128.md) objects can be cast to a string object, which returns information about this object in the following format:

**Use Cases:**

- 调用 __tostring 完成对应 API 操作

**See also:** 



---

### Functions

### Get {#Get}

```
boolean Get ( int BitPosition )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取指定位置的布尔值，指示该标志是否被设置。

Gets the flags' value at the provided position.

**Use Cases:**

- 检查特定标志状态
- 条件分支判断

**See also:** 
[[#Set|Set]]


---

### Set {#Set}

```
void Set ( int BitPosition, boolean State )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Sets the bit at the given position to the given value.

Sets the bit at the given position to the given value.

**Use Cases:**

- 调用 Set 完成对应 API 操作

**See also:** 



---

### h {#h}

```
int h
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the number representing the "High" or "upper" 64-bit number of the 128bit [BitSet128](BitSet128.md) object.

Returns the number representing the "High" or "upper" 64-bit number of the 128bit [BitSet128](BitSet128.md) object.

**Use Cases:**

- 调用 h 完成对应 API 操作

**See also:** 



---

### l {#l}

```
int l
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns the number representing the "Low" or "lower" 64-bit number of the 128bit [BitSet128](BitSet128.md) object.

Returns the number representing the "Low" or "lower" 64-bit number of the 128bit [BitSet128](BitSet128.md) object.

**Use Cases:**

- 调用 l 完成对应 API 操作

**See also:** 



---

## See Also

- [[BitSet128]]
