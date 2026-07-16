---
title: ItemConfig
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 12
---

# ItemConfig

## Summary

A central repository for retrieving game item configuration data, including collectibles, trinkets, cards, pills, and null items, with both individual ID lookups and (bugged) bulk lists. Also provides static validation and costume-checking utilities.

## Key Methods

- [[#GetCollectible|GetCollectible]]
- [[#GetTrinket|GetTrinket]]
- [[#GetCard|GetCard]]
- [[#GetPillEffect|GetPillEffect]]
- [[#IsValidCollectible|IsValidCollectible]]

## Methods

### Functions

### GetCard {#GetCard}

```
const ItemConfig Card GetCard ( Card ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Retrieves the ItemConfig_Card for the specified Card enum ID, returning nil if no configuration exists.

Returns `nil` if no itemconfig to the given ID can be found.

**Use Cases:**

- Look up card name or description
- Check if a card is supported by the game

**See also:** 
[[#GetCards|GetCards]], [[#GetCollectible|GetCollectible]], [[#GetTrinket|GetTrinket]], [[#GetPillEffect|GetPillEffect]]


---

### GetCards {#GetCards}

```
const CardList GetCards ( )
```

*DLC: REP, REP+ | Modifiers: const*

Returns a list of all card configurations (CardList), but note that calling Get() on the list is bugged and returns unusable userdata; Size is reliable.

**Use Cases:**

- Get the total count of available cards
- Potentially iterate card types via index if a workaround exists

**See also:** 
[[#GetCard|GetCard]], [[#GetCollectibles|GetCollectibles]], [[#GetTrinkets|GetTrinkets]], [[#GetPillEffects|GetPillEffects]]


---

### GetCollectible {#GetCollectible}

```
const ItemConfig Item GetCollectible ( CollectibleType ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Retrieves the ItemConfig_Item for the given CollectibleType, returning nil if not found.

**Use Cases:**

- Access properties like name, description, quality of a collectible
- Programmatically inspect collectible stats
- Obtain config to pass to ShouldAddCostumeOnPickup

**See also:** 
[[#GetTrinket|GetTrinket]], [[#GetCard|GetCard]], [[#GetPillEffect|GetPillEffect]], [[#GetNullItem|GetNullItem]]


---

### GetCollectibles {#GetCollectibles}

```
const userdata GetCollectibles ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns a list of all collectible item configs, but Get() is bugged; Size is usable to determine the highest ID + 1.

**Use Cases:**

- Calculate the maximum collectible ID (Size - 1)
- Count collectibles including modded ones

**See also:** 
[[#GetCollectible|GetCollectible]], [[#IsValidCollectible|IsValidCollectible]]


---

### GetNullItem {#GetNullItem}

```
const ItemConfig Item GetNullItem ( NullItemID ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Retrieves the ItemConfig_Item for the given NullItemID, returning nil if not found.

Returns `nil` if no itemconfig to the given ID can be found.

**Use Cases:**

- Look up configuration of a null item
- Verify null item existence

**See also:** 
[[#GetCollectible|GetCollectible]], [[#GetTrinket|GetTrinket]], [[#GetCard|GetCard]], [[#GetPillEffect|GetPillEffect]]


---

### GetNullItems {#GetNullItems}

```
const ItemList GetNullItems ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns a list of all null item configs, but Get() is bugged.

**Use Cases:**

- Get count of null items

**See also:** 
[[#GetNullItem|GetNullItem]]


---

### GetPillEffect {#GetPillEffect}

```
const ItemConfig PillEffect GetPillEffect ( PillEffect ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Retrieves the ItemConfig_PillEffect for the specified PillEffect ID, returning nil if not found.

Returns `nil` if no itemconfig to the given ID can be found.

**Use Cases:**

- Get pill name or color
- Check if a pill effect is registered

**See also:** 
[[#GetPillEffects|GetPillEffects]], [[#GetCard|GetCard]], [[#GetCollectible|GetCollectible]], [[#GetTrinket|GetTrinket]]


---

### GetPillEffects {#GetPillEffects}

```
const PillList GetPillEffects ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns a list of all pill effect configs, but Get() is bugged.

**Use Cases:**

- Get total number of pill effects

**See also:** 
[[#GetPillEffect|GetPillEffect]]


---

### GetTrinket {#GetTrinket}

```
const ItemConfig Item GetTrinket ( TrinketType ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Retrieves the ItemConfig_Item for the given TrinketType, returning nil if not found.

Returns `nil` if no itemconfig to the given ID can be found.

**Use Cases:**

- Access trinket properties like name, description
- Check trinket behavior details

**See also:** 



---

### GetTrinkets {#GetTrinkets}

```
const ItemList GetTrinkets ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetTrinkets 完成对应 API 操作

**See also:** 



---

### IsValidCollectible {#IsValidCollectible}

```
static boolean IsValidCollectible ( CollectibleType ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 IsValidCollectible 完成对应 API 操作

**See also:** 



---

### ShouldAddCostumeOnPickup {#ShouldAddCostumeOnPickup}

```
static boolean ShouldAddCostumeOnPickup ( ItemConfig Item Config )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns weather a given item config object should add a costume when picking up the associated item.

Returns weather a given item config object should add a costume when picking up the associated item.

**Use Cases:**

- 调用 ShouldAddCostumeOnPickup 完成对应 API 操作

**See also:** 



---

## See Also

- [[ItemConfig]]
