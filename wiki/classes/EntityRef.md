---
title: EntityRef
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 9
---

# EntityRef

## Summary

EntityRef 用于封装和传递实体引用及其状态信息，常用于获取伤害来源、友好/魅惑状态等。

## Related Types

- [[Entity]]
- [[Vector]]

## Key Methods

- [[#Entity|Entity]]
- [[#IsFriendly|IsFriendly]]
- [[#IsCharmed|IsCharmed]]
- [[#Type|Type]]
- [[#Variant|Variant]]

## Methods

### Constructors

### EntityRef {#EntityRef}

```
EntityRef EntityRef ( Entity )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

构造函数，根据传入的 Entity 创建一个包含其状态快照的 EntityRef 对象。

**Use Cases:**

- 从任意实体创建引用
- 记录实体在某个时刻的状态

**See also:** 
[[#Entity|Entity]], [[#IsFriendly|IsFriendly]], [[#Type|Type]]


---

### Functions

### Entity {#Entity}

```
Entity Entity
```

*DLC: REP, REP+ | Modifiers: const*

获取该引用指向的实际 Entity 对象，可能为 nil。

optional

**Use Cases:**

- 获取实际实体进行操作
- 判断引用是否有效

**See also:** 
[[#IsFriendly|IsFriendly]], [[#IsCharmed|IsCharmed]]


---

### IsCharmed {#IsCharmed}

```
boolean IsCharmed
```

*DLC: AB+, REP, REP+ | Modifiers: const*

表示实体是否处于魅惑状态。

**Use Cases:**

- 判断实体是否被魅惑从而改变行为
- 配合友好判断进行更复杂的逻辑

**See also:** 
[[#IsFriendly|IsFriendly]]


---

### IsFriendly {#IsFriendly}

```
boolean IsFriendly
```

*DLC: AB+, REP, REP+ | Modifiers: const*

表示实体是否对玩家友好。

**Use Cases:**

- 判断实体是否盟友
- 决定是否攻击该实体

**See also:** 
[[#IsCharmed|IsCharmed]]


---

### Position {#Position}

```
Vector Position
```

*DLC: AB+, REP, REP+ | Modifiers: const*

记录实体在引用创建时的位置。

**Use Cases:**

- 获取伤害来源的位置
- 用于生成特效或计算距离

**See also:** 
[[#Entity|Entity]]


---

### SpawnerType {#SpawnerType}

```
EntityType SpawnerType
```

*DLC: AB+, REP, REP+ | Modifiers: static*

如果实体由生成者产生，则记录生成者的实体类型。

**Use Cases:**

- 追踪实体是由何种来源生成的
- 用于特殊逻辑判断生成者

**See also:** 
[[#SpawnerVariant|SpawnerVariant]], [[#Type|Type]]


---

### SpawnerVariant {#SpawnerVariant}

```
int SpawnerVariant
```

*DLC: AB+, REP, REP+ | Modifiers: const*

记录生成者的变种编号。

**Use Cases:**

- 进一步区分生成者种类
- 与 SpawnerType 配合使用

**See also:** 
[[#SpawnerType|SpawnerType]]


---

### Type {#Type}

```
EntityType Type
```

*DLC: AB+, REP, REP+ | Modifiers: const*

引用所代表实体的类型枚举。

**Use Cases:**

- 判断实体是哪种类型
- 用于条件判断或日志

**See also:** 
[[#Variant|Variant]]


---

### Variant {#Variant}

```
int Variant
```

*DLC: AB+, REP, REP+ | Modifiers: const*

引用所代表实体的变种编号。

**Use Cases:**

- 与 Type 配合确定具体实体
- 区分同一类型不同变种

**See also:** 
[[#Type|Type]]


---

## See Also

- [[Entity]]
- [[Vector]]
