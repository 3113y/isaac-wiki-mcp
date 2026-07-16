---
title: RoomDescriptor
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 25
---

# RoomDescriptor

## Summary

RoomDescriptor 存储一个房间的元数据和状态信息，包括房间类型、清理状态、生成种子、网格索引和商店相关数据等。

## Related Types

- [[Room]]
- [[RoomConfigRoom]]

## Key Methods

- [[#Data|Data]]
- [[#Flags|Flags]]
- [[#GridIndex|GridIndex]]
- [[#Clear|Clear]]
- [[#ShopItemDiscountIdx|ShopItemDiscountIdx]]

## Methods

### Functions

### AllowedDoors {#AllowedDoors}

```
DoorSet AllowedDoors
```

*DLC: AB+, REP, REP+ | Modifiers: const*

存储房间允许的门数据，在加载时使用（如小Boss事件），但包含用户数据无法直接使用。

Contains data swapped just on load (in cases like minibosses, or other such events)

**Use Cases:**

- 调用 AllowedDoors 完成对应 API 操作

**See also:** 



---

### AwardSeed {#AwardSeed}

```
int AwardSeed
```

*DLC: REP, REP+ | Modifiers: const*

用于生成通关奖励（普通、小Boss、Boss房）和初始化商店物品（商店、恶魔房）的种子。

used to spawn clear awards (normal, miniboss, boss rooms) and initialize shop items (shop, devil rooms)

**Use Cases:**

- 生成房间奖励
- 初始化商店物品

**See also:** 
[[#SpawnSeed|SpawnSeed]]


---

### ChallengeDone {#ChallengeDone}

```
boolean ChallengeDone
```

*DLC: AB+, REP, REP+ | Modifiers: const*

标记房间是否已完成挑战。

**Use Cases:**

- 检查挑战是否完成

**See also:** 
[[#Clear|Clear]]


---

### Clear {#Clear}

```
boolean Clear
```

*DLC: AB+, REP, REP+ | Modifiers: const*

标记房间是否已清理。

**Use Cases:**

- 判断房间是否清空敌人

**See also:** 
[[#ClearCount|ClearCount]]


---

### ClearCount {#ClearCount}

```
int ClearCount
```

*DLC: AB+, REP, REP+ | Modifiers: const*

房间被清理的次数，用于判断是否已经清除敌人而不再次生成。

room is clear, don't spawn enemies when visiting

**Use Cases:**

- 防止重新访问时生成敌人

**See also:** 
[[#Clear|Clear]]


---

### Data {#Data}

```
RoomConfigRoom Data
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回房间的配置数据（RoomConfigRoom）。

**Use Cases:**

- 获取房间类型和布局信息

**See also:** 
[[#OverrideData|OverrideData]]


---

### DecorationSeed {#DecorationSeed}

```
int DecorationSeed
```

*DLC: AB+, REP, REP+ | Modifiers: const*

用于装饰元素的种子，如背景、房间装饰、店主皮肤等。

used for cosmetic stuff like backdrops, room decorations, shopkeeper skins

**Use Cases:**

- 生成随机装饰

**See also:** 



---

### DeliriumDistance {#DeliriumDistance}

```
int DeliriumDistance
```

*DLC: AB+, REP, REP+ | Modifiers: const*

在虚空层中记录当前房间距离百变怪Boss的步数。

Helper for The Void stage, holds the distance to the Delirium boss in room nr.

**Use Cases:**

- 虚空层导航提示

**See also:** 



---

### DisplayFlags {#DisplayFlags}

```
int DisplayFlags
```

*DLC: AB+, REP, REP+ | Modifiers: const*

控制小地图上该房间的可见性和图标显示，使用位标志。

**Use Cases:**

- 设置或读取房间在小地图上的展示状态

**See also:** 



---

### Flags {#Flags}

```
RoomDescriptor Flags
```

*DLC: AB+, REP, REP+ | Modifiers: const*

房间描述符的标志位，表示房间的全局属性。

The RoomDescriptor flags for the room.

**Use Cases:**

- 判断房间是否为特殊类型

**See also:** 
[[#Data|Data]]


---

### GridIndex {#GridIndex}

```
int GridIndex
```

*DLC: AB+, REP, REP+ | Modifiers: const*

房间在 13x13 网格中的索引，参照左上象限，对于特殊形状可能指向空洞位置。

**Use Cases:**

- 定位房间在关卡中的位置

**See also:** 
[[#SafeGridIndex|SafeGridIndex]], [[#ListIndex|ListIndex]]


---

### HasWater {#HasWater}

```
boolean HasWater
```

*DLC: AB+, REP, REP+ | Modifiers: const*

表示房间内是否有水。

**Use Cases:**

- 判定水坑等环境要素

**See also:** 



---

### ListIndex {#ListIndex}

```
int ListIndex
```

*DLC: AB+, REP, REP+ | Modifiers: static*

房间在生成顺序中的唯一索引，适合用作数据结构的键值。

**Use Cases:**

- 作为房间数据存储的标识

**See also:** 
[[#GridIndex|GridIndex]]


---

### NoReward {#NoReward}

```
boolean NoReward
```

*DLC: AB+, REP, REP+ | Modifiers: const*

标记房间是否不提供通关奖励。

**Use Cases:**

- 禁用特定房间的奖励

**See also:** 
[[#AwardSeed|AwardSeed]]


---

### OverrideData {#OverrideData}

```
RoomConfigRoom OverrideData
```

*DLC: AB+, REP, REP+ | Modifiers: static*

保存覆盖的房间数据，用于小Boss替换等场景。

The room variant is in Data. Because Room::Init uses a mix of data, one from level layout and one from replacement data like minibosses, we need to hold the new room data somewhere.

**Use Cases:**

- 实现房间类型动态替换

**See also:** 
[[#Data|Data]]


---

### PitsCount {#PitsCount}

```
int PitsCount
```

*DLC: AB+, REP, REP+ | Modifiers: const*

房间内坑的数量。

**Use Cases:**

- 了解房间危险程度

**See also:** 



---

### PoopCount {#PoopCount}

```
int PoopCount
```

*DLC: AB+, REP, REP+*

房间内粪堆的数量。

**Use Cases:**

- 计算特定实体数量

**See also:** 



---

### PressurePlatesTriggered {#PressurePlatesTriggered}

```
boolean PressurePlatesTriggered
```

*DLC: AB+, REP, REP+ | Modifiers: const*

表示压力板是否已被触发。

**Use Cases:**

- 判断机关状态

**See also:** 



---

### SacrificeDone {#SacrificeDone}

```
boolean SacrificeDone
```

*DLC: AB+, REP, REP+ | Modifiers: static*

标记献祭是否完成。

**Use Cases:**

- 控制献祭事件进度

**See also:** 
[[#ChallengeDone|ChallengeDone]]


---

### SafeGridIndex {#SafeGridIndex}

```
int SafeGridIndex
```

*DLC: AB+, REP, REP+ | Modifiers: static*

安全的网格索引，总是返回房间实际所占的左上象限，即使形状特殊也返回安全坐标。

**Use Cases:**

- 确保获取有效的房间坐标

**See also:** 
[[#GridIndex|GridIndex]]


---

### ShopItemDiscountIdx {#ShopItemDiscountIdx}

```
int ShopItemDiscountIdx
```

*DLC: AB+, REP, REP+ | Modifiers: const*

指定哪个ShopItemId的商品享受折扣，-1表示无折扣。

- The index that denotes which shop item(s) will be discounted.

**Use Cases:**

- 实现商店打折逻辑
- 修改打折物品

**See also:** 
[[#ShopItemIdx|ShopItemIdx]]


---

### ShopItemIdx {#ShopItemIdx}

```
int ShopItemIdx
```

*DLC: AB+, REP, REP+ | Modifiers: static*

下一个要添加的商店物品的ShopItemId，或表示当前总物品数模8的值。

- The ShopItemId value of the next shop item to add to the room.

**Use Cases:**

- 管理商店物品生成顺序
- 确定物品ID重复周期

**See also:** 
[[#ShopItemDiscountIdx|ShopItemDiscountIdx]]


---

### SpawnSeed {#SpawnSeed}

```
int SpawnSeed
```

*DLC: AB+, REP, REP+*

用于生成房间内实体和敌人掉落种子的种子值。

used to spawn entities at room load and initialize enemy drop seeds

**Use Cases:**

- 控制实体生成和掉落

**See also:** 
[[#AwardSeed|AwardSeed]]


---

### SurpriseMiniboss {#SurpriseMiniboss}

```
boolean SurpriseMiniboss
```

*DLC: AB+, REP, REP+ | Modifiers: const*

标记该房间是否有一个突袭小Boss。

___

**Use Cases:**

- 判断触发的战斗类型

**See also:** 



---

### VisitedCount {#VisitedCount}

```
int VisitedCount
```

*DLC: AB+, REP, REP+ | Modifiers: static*

记录该房间被访问过的次数。

how often the room has been visited

**Use Cases:**

- 追踪重复访问情况

**See also:** 



---

## See Also

- [[Room]]
- [[RoomConfigRoom]]
- [[RoomDescriptor]]
