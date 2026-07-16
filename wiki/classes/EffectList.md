---
title: EffectList
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# EffectList

## Summary

EffectList 是一个临时效果列表容器，用于管理角色当前所有激活的 TemporaryEffect。可通过 TemporaryEffects:GetEffectsList() 获取。

## Related Types

- [[TemporaryEffect]]

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

长度运算符，返回 EffectList 中 TemporaryEffect 的总数量。

**Use Cases:**

- 使用 # 操作符快速获取效果数量
- 作为循环遍历的上限

**See also:** 
[[#Size|Size]], [[#Get|Get]]


---

### Functions

### Get {#Get}

```
TemporaryEffect Get ( int idx )
```

*DLC: REP, REP+ | Modifiers: const*

根据给定的整数索引获取 EffectList 中对应位置的 TemporaryEffect 对象。

**Use Cases:**

- 遍历列表处理每个临时效果
- 配合索引检查特定效果的状态

**See also:** 
[[#__len|__len]], [[#Size|Size]]


---

### Size {#Size}

```
const int Size
```

*DLC: AB+, REP, REP+ | Modifiers: const*

只读常量，记录 EffectList 中 TemporaryEffect 的数量，等价于 # 操作符的结果。

**Use Cases:**

- 直接读取列表大小
- 作为 for 循环的边界值

**See also:** 
[[#__len|__len]], [[#Get|Get]]


---

## See Also

- [[EffectList]]
- [[TemporaryEffect]]
