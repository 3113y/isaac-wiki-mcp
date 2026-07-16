---
title: GridEntity
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 28
---

# GridEntity

## Summary

表示房间内的网格实体（如岩石、尖刺、门、坑）。可获取类型、变种、状态，并可进行破坏、伤害、渲染、更新及类型转换等操作。

- Subclasses:
  - [[GridEntityDoor]]
  - [[GridEntityPit]]
  - [[GridEntityPoop]]
  - [[GridEntityPressurePlate]]
  - [[GridEntityRock]]
  - [[GridEntitySpikes]]
  - [[GridEntityTNT]]

## Related Types

- [[Entity]]
- [[EntityRef]]
- [[GridEntityDesc]]
- [[GridEntityDoor]]
- [[GridEntityPit]]
- [[GridEntityPoop]]
- [[GridEntityPressurePlate]]
- [[GridEntityRock]]
- [[GridEntitySpikes]]
- [[GridEntityTNT]]
- [[RNG]]
- [[Sprite]]
- [[Vector]]

## Key Methods

- [[#GetType|GetType]]
- [[#Destroy|Destroy]]
- [[#Hurt|Hurt]]
- [[#Update|Update]]
- [[#ToRock|ToRock]]

## Methods

### Functions

### Destroy {#Destroy}

```
boolean Destroy ( boolean Immediate )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

立即或按游戏流程销毁网格实体，返回是否成功。

**Use Cases:**

- 移除障碍物
- 清除爆炸物如TNT

**See also:** 
[[#DestroyWithSource|DestroyWithSource]], [[#Hurt|Hurt]]


---

### DestroyWithSource {#DestroyWithSource}

```
boolean DestroyWithSource ( boolean Immediate, EntityRef Source )
```

*DLC: REP, REP+ | Modifiers: const*

销毁网格实体并指定来源实体，用于触发死亡相关回调。

**Use Cases:**

- 追踪伤害来源
- 实现因特定实体触发破坏的逻辑

**See also:** 
[[#Destroy|Destroy]], [[#HurtWithSource|HurtWithSource]]


---

### GetGridIndex {#GetGridIndex}

```
int GetGridIndex ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回网格实体在房间网格中的唯一索引。

**Use Cases:**

- 定位实体在房间的位置
- 与Room方法配合操作

**See also:** 
[[#Position|Position]], [[#GetType|GetType]]


---

### GetRNG {#GetRNG}

```
RNG GetRNG ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取该网格实体的RNG对象，但警告全局网格实体共用相同种子，建议使用GridEntityDesc的种子字段。

**Use Cases:**

- 谨慎使用以获得随机数（不推荐）
- 学习随机种子机制

**See also:** 
[[#GetSaveState|GetSaveState]], [[#Init|Init]]


---

### GetSaveState {#GetSaveState}

```
GridEntityDesc GetSaveState ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回网格实体的保存状态描述对象，与Desc属性相同，官方建议用此方法。

**Use Cases:**

- 获取实体的持续数据
- 修改种子或变量数据

**See also:** 
[[#Desc|Desc]], [[#VarData|VarData]]


---

### GetSprite {#GetSprite}

```
Sprite GetSprite ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回网格实体的Sprite对象，用于自定义渲染或动画。

**Use Cases:**

- 修改实体外观
- 播放动画

**See also:** 
[[#Render|Render]], [[#Update|Update]]


---

### GetType {#GetType}

```
GridEntityType GetType ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回网格实体的类型枚举（如岩石、尖刺、坑洞）。

**Use Cases:**

- 判断实体类型以执行特定逻辑
- 条件性行为

**See also:** 
[[#SetType|SetType]], [[#GetVariant|GetVariant]]


---

### GetVariant {#GetVariant}

```
int GetVariant ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回网格实体的变体编号，与类型组合确定具体表现。

**Use Cases:**

- 区分同类型不同种类
- 配合SetVariant修改外观

**See also:** 
[[#SetVariant|SetVariant]], [[#GetType|GetType]]


---

### Hurt {#Hurt}

```
boolean Hurt ( int Damage )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

对网格实体造成伤害，返回是否成功。

**Use Cases:**

- 实现攻击破坏岩石或敌人
- 触发伤害效果

**See also:** 
[[#HurtWithSource|HurtWithSource]], [[#Destroy|Destroy]]


---

### HurtWithSource {#HurtWithSource}

```
boolean HurtWithSource ( int Damage, EntityRef Source )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

对网格实体造成伤害并指定来源，用于伤害回调逻辑。

**Use Cases:**

- 记录谁造成了伤害
- 实现友方误伤检测

**See also:** 
[[#Hurt|Hurt]], [[#DestroyWithSource|DestroyWithSource]]


---

### Init {#Init}

```
void Init ( int Seed )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

用指定种子初始化网格实体。

**Use Cases:**

- 重置网格实体状态
- 使用固定种子控制随机性

**See also:** 
[[#GetRNG|GetRNG]], [[#GetSaveState|GetSaveState]]


---

### PostInit {#PostInit}

```
void PostInit ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 PostInit 完成对应 API 操作

**See also:** 



---

### Render {#Render}

```
void Render ( Vector Offset )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Render 完成对应 API 操作

**See also:** 



---

### SetType {#SetType}

```
void SetType ( GridEntityType Type )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SetType 完成对应 API 操作

**See also:** 



---

### SetVariant {#SetVariant}

```
void SetVariant ( int Variant )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 SetVariant 完成对应 API 操作

**See also:** 



---

### ToDoor {#ToDoor}

```
GridEntityDoor ToDoor ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 ToDoor 完成对应 API 操作

**See also:** 



---

### ToPit {#ToPit}

```
GridEntityPit ToPit ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 ToPit 完成对应 API 操作

**See also:** 



---

### ToPoop {#ToPoop}

```
GridEntityPoop ToPoop ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 ToPoop 完成对应 API 操作

**See also:** 



---

### ToPressurePlate {#ToPressurePlate}

```
GridEntityPressurePlate ToPressurePlate ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 ToPressurePlate 完成对应 API 操作

**See also:** 



---

### ToRock {#ToRock}

```
GridEntityRock ToRock ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 ToRock 完成对应 API 操作

**See also:** 



---

### ToSpikes {#ToSpikes}

```
GridEntitySpikes ToSpikes ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 ToSpikes 完成对应 API 操作

**See also:** 



---

### ToTNT {#ToTNT}

```
GridEntityTNT ToTNT ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 ToTNT 完成对应 API 操作

**See also:** 



---

### Update {#Update}

```
void Update ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Update 完成对应 API 操作

**See also:** 



---

### CollisionClass {#CollisionClass}

```
GridCollisionClass CollisionClass
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 CollisionClass 完成对应 API 操作

**See also:** 



---

### Desc {#Desc}

```
GridEntityDesc Desc
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Desc 完成对应 API 操作

**See also:** 



---

### Position {#Position}

```
const Vector Position
```

*DLC: AB+, REP | Modifiers: const*

Returns the position of the grid cell's center point

Returns the position of the grid cell's center point

**Use Cases:**

- 调用 Position 完成对应 API 操作

**See also:** 



---

### State {#State}

```
int State
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Used for various different usecases.

Used for various different usecases.

**Use Cases:**

- 调用 State 完成对应 API 操作

**See also:** 



---

### VarData {#VarData}

```
int VarData
```

*DLC: AB+, REP, REP+ | Modifiers: const*

A Variable that stores some entity-specific data. The content can have completely different effects for different GridEntities.

A Variable that stores some entity-specific data. The content can have completely different effects for different GridEntities.

**Use Cases:**

- 调用 VarData 完成对应 API 操作

**See also:** 



---

## See Also

- [[Entity]]
- [[EntityRef]]
- [[GridEntity]]
- [[GridEntityDesc]]
- [[GridEntityDoor]]
- [[GridEntityPit]]
- [[GridEntityPoop]]
- [[GridEntityPressurePlate]]
- [[GridEntityRock]]
- [[GridEntitySpikes]]
- [[GridEntityTNT]]
- [[RNG]]
- [[Sprite]]
- [[Vector]]
