---
title: ItemPool
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 16
---

# ItemPool

## Summary

ItemPool 类用于管理游戏中的各种物品池，包括道具、卡牌、药丸、饰品等，提供获取、添加、移除、黑名单控制及药丸鉴定等功能。

## Related Types

- [[Color]]
- [[EntityPlayer]]
- [[Room]]

## Key Methods

- [[#GetCollectible|GetCollectible]]
- [[#GetCard|GetCard]]
- [[#GetPill|GetPill]]
- [[#AddRoomBlacklist|AddRoomBlacklist]]
- [[#RemoveCollectible|RemoveCollectible]]

## Methods

### Functions

### AddBibleUpgrade {#AddBibleUpgrade}

```
void AddBibleUpgrade ( int Add, ItemPoolType PoolType )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

增加指定道具池的圣经升级计数，可能影响后续道具行为。

**Use Cases:**

- 用于挑战或特殊模式中调整圣经相关效果

**See also:** 



---

### AddRoomBlacklist {#AddRoomBlacklist}

```
void AddRoomBlacklist ( CollectibleType Item )
```

*DLC: REP, REP+ | Modifiers: const*

将指定道具加入当前房间黑名单，使其在本房间内无法从道具池中生成，换房间时自动重置。

Adds a given item to the blacklist. This item can no longer be chosen from itempools while the player is inside the current room. This effectively prevents the item from appearing.

**Use Cases:**

- 防止特定道具在当前房间重复出现
- 临时禁用某些道具的生成

**See also:** 
[[#ResetRoomBlacklist|ResetRoomBlacklist]]


---

### ForceAddPillEffect {#ForceAddPillEffect}

```
PillColor ForceAddPillEffect ( PillEffect ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

强制将指定药丸效果添加到药丸池中，通常用于挑战或自定义条件，返回对应的药丸颜色。

Forces a pill effect to be in the pool, usually for challenges, returns PillColor for that effect.

**Use Cases:**

- 在挑战中确保某种药丸效果可用
- 手动扩充药丸池

**See also:** 
[[#GetPillEffect|GetPillEffect]], [[#GetPill|GetPill]]


---

### GetCard {#GetCard}

```
Card GetCard ( int Seed, boolean Playing, boolean Rune, boolean OnlyRunes )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

根据种子和布尔参数随机获取一张卡牌或符文，支持单独获取符文。

**Use Cases:**

- 生成卡牌或符文掉落
- 根据种子控制随机结果

**See also:** 



---

### GetCollectible {#GetCollectible}

```
CollectibleType GetCollectible ( ItemPoolType PoolType, boolean Decrease = false, int Seed = Random(), CollectibleType DefaultItem = CollectibleType.COLLECTIBLE_NULL )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

从指定道具池中随机获取一个道具，支持减少池内数量、设置种子和默认道具，已内置处理各种特殊效果如混沌、神圣球等。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 生成房间奖励或掉落道具

**See also:** 



---

### [CollectibleType](enums/CollectibleType.md) GetCollectible ( [ItemPoolType](enums/ItemPoolType.md) PoolType, boolean Decrease = false, int Seed = Random {#[CollectibleType](enums/CollectibleType.md) GetCollectible ( [ItemPoolType](enums/ItemPoolType.md) PoolType, boolean Decrease = false, int Seed = Random}

```
ItemPoolType GetLastPool ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 [CollectibleType](enums/CollectibleType.md) GetCollectible ( [ItemPoolType](enums/ItemPoolType.md) PoolType, boolean Decrease = false, int Seed = Random 完成对应 API 操作

**See also:** 



---

### GetPill {#GetPill}

```
PillColor GetPill ( int Seed )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetPill 完成对应 API 操作

**See also:** 



---

### GetPillEffect {#GetPillEffect}

```
PillEffect GetPillEffect ( PillColor PillColor, EntityPlayer Player = nil )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetPillEffect 完成对应 API 操作

**See also:** 



---

### GetPoolForRoom {#GetPoolForRoom}

```
ItemPoolType GetPoolForRoom ( RoomType RoomType, int Seed )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetPoolForRoom 完成对应 API 操作

**See also:** 



---

### GetTrinket {#GetTrinket}

```
TrinketType GetTrinket ( boolean DontAdvanceRNG = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetTrinket 完成对应 API 操作

**See also:** 



---

### IdentifyPill {#IdentifyPill}

```
void IdentifyPill ( PillColor PillColor )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 IdentifyPill 完成对应 API 操作

**See also:** 



---

### IsPillIdentified {#IsPillIdentified}

```
boolean IsPillIdentified ( PillColor PillColor )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 IsPillIdentified 完成对应 API 操作

**See also:** 



---

### RemoveCollectible {#RemoveCollectible}

```
boolean RemoveCollectible ( CollectibleType Collectible )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Removes a collectible from the itempool. Returns true if given item did exist in the pool before.

Removes a collectible from the itempool. Returns true if given item did exist in the pool before.

**Use Cases:**

- 调用 RemoveCollectible 完成对应 API 操作

**See also:** 



---

### RemoveTrinket {#RemoveTrinket}

```
boolean RemoveTrinket ( TrinketType Trinket )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 RemoveTrinket 完成对应 API 操作

**See also:** 



---

### ResetRoomBlacklist {#ResetRoomBlacklist}

```
void ResetRoomBlacklist ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Clears the current item black list.

Clears the current item black list.

**Use Cases:**

- 调用 ResetRoomBlacklist 完成对应 API 操作

**See also:** 



---

### ResetTrinkets {#ResetTrinkets}

```
void ResetTrinkets ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 ResetTrinkets 完成对应 API 操作

**See also:** 



---

## See Also

- [[Color]]
- [[EntityPlayer]]
- [[ItemPool]]
- [[Room]]
