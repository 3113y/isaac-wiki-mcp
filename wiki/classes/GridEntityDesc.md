---
title: GridEntityDesc
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 8
---

# GridEntityDesc

## Summary

GridEntityDesc用于保存网格实体的持久化状态信息，记录实体类型、变体、当前状态、生成计数、种子等数据，常通过GridEntity:GetSaveState()获取。

## Related Types

- [[Entity]]
- [[GridEntity]]

## Key Methods

- [[#Initialized|Initialized]]
- [[#SpawnCount|SpawnCount]]
- [[#SpawnSeed|SpawnSeed]]
- [[#State|State]]
- [[#Type|Type]]

## Methods

### Functions

### Initialized {#Initialized}

```
boolean Initialized
```

*DLC: AB+, REP, REP+ | Modifiers: const*

指示该网格实体描述是否已完成初始化，首次创建时值为false。

this is will be false when its first created

**Use Cases:**

- 检查实体是否处于初始创建状态
- 用于判断是否需要执行初始化逻辑

**See also:** 



---

### SpawnCount {#SpawnCount}

```
int SpawnCount
```

*DLC: REP, REP+ | Modifiers: const*

记录该实体被生成的次数。

how often this entity has been spawned

**Use Cases:**

- 判断是否为首次生成
- 根据生成次数调整实体行为

**See also:** 



---

### SpawnSeed {#SpawnSeed}

```
int SpawnSeed
```

*DLC: AB+, REP, REP+ | Modifiers: const*

生成时使用的种子值，用于确定实体属性或变体。

**Use Cases:**

- 复制或重建相同属性的实体
- 计算基于种子的随机行为

**See also:** 



---

### State {#State}

```
int State
```

*DLC: AB+, REP, REP+ | Modifiers: const*

表示实体的当前状态值，用于区分实体在生命周期中的不同阶段。

**Use Cases:**

- 根据状态驱动实体动画或行为
- 保存和恢复实体进度

**See also:** 



---

### Type {#Type}

```
GridEntityType Type
```

*DLC: AB+, REP, REP+ | Modifiers: const*

指示网格实体的类型，对应GridEntityType枚举值，决定实体的基础类别。

**Use Cases:**

- 识别实体是岩石、罐子、蘑菇等
- 过滤或统计特定类型的网格实体

**See also:** 



---

### VarData {#VarData}

```
int VarData
```

*DLC: AB+, REP, REP+ | Modifiers: static*

附加存储数据，当State不足以表达复杂状态时使用。

Additional data to be stored, when State is not enought.

**Use Cases:**

- 存储实体的自定义数值
- 扩展状态信息以支持多样行为

**See also:** 



---

### VariableSeed {#VariableSeed}

```
int VariableSeed
```

*DLC: AB+, REP, REP+ | Modifiers: const*

可变种子，会根据某些事件动态改变，影响实体行为。

this seed is will be changed based on some events

**Use Cases:**

- 在实体交互或更新时生成动态随机结果
- 追踪受事件影响的种子变化

**See also:** 



---

### Variant {#Variant}

```
int Variant
```

*DLC: AB+, REP, REP+ | Modifiers: const*

变体编号，用于细分同一类型下的不同外观或特性。

**Use Cases:**

- 区分同类型的子种类
- 根据变体设置实体外观和掉落物

**See also:** 



---

## See Also

- [[Entity]]
- [[GridEntity]]
