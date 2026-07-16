---
title: ItemConfigItem
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 36
---

# ItemConfigItem

## Summary

Represents configuration data for a single item (collectible, trinket, or null item), providing access to its properties such as costs, hearts added, tags, quality, and unlock status.

## Key Methods

- [[#HasTags|HasTags]]
- [[#IsAvailable|IsAvailable]]
- [[#ID|ID]]
- [[#Name|Name]]
- [[#Type|Type]]

## Methods

### Functions

### HasTags {#HasTags}

```
boolean HasTags ( int Tags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Checks whether the item has a specific tag or set of tags, typically used for transformation or category filtering.

**Use Cases:**

- Verifying if an item contributes to a transformation (e.g., Bob transformation)
- Filtering items by tag for custom pools or logic

**See also:** 
[[#Tags|Tags]]


---

### IsAvailable {#IsAvailable}

```
boolean IsAvailable ( )
```

*DLC: REP, REP+ | Modifiers: const*

Returns true if the item is unlocked and not blocked by tags, otherwise false.

**Use Cases:**

- Determining if an item can appear in the current run
- Filtering item lists to only available items

**See also:** 
[[#AchievementID|AchievementID]], [[#Hidden|Hidden]]


---

### IsCollectible {#IsCollectible}

```
boolean IsCollectible ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns true if the item is a collectible (active or passive).

**Use Cases:**

- Type-checking before applying collectible-specific logic
- Differentiating between collectibles, trinkets, and null items

**See also:** 
[[#IsTrinket|IsTrinket]], [[#IsNull|IsNull]], [[#Type|Type]]


---

### IsNull {#IsNull}

```
boolean IsNull ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns true if the item is a null item (i.e., not a valid collectible or trinket).

**Use Cases:**

- Validating that an obtained ItemConfigItem reference corresponds to a real item

**See also:** 
[[#IsCollectible|IsCollectible]], [[#IsTrinket|IsTrinket]]


---

### IsTrinket {#IsTrinket}

```
boolean IsTrinket ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns true if the item is a trinket.

**Use Cases:**

- Distinguishing trinkets from collectibles when handling item data
- Building trinket‑only UI or logic

**See also:** 
[[#IsCollectible|IsCollectible]], [[#IsNull|IsNull]]


---

### AchievementID {#AchievementID}

```
int AchievementID
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns the achievement ID required to unlock the item, or -1 if unlocked by default.

**Use Cases:**

- Checking which achievement unlocks an item
- Displaying unlock requirements in custom menus

**See also:** 
[[#IsAvailable|IsAvailable]]


---

### AddBlackHearts {#AddBlackHearts}

```
int AddBlackHearts
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the number of black hearts (half‑heart units) the item grants on pickup.

**Use Cases:**

- Calculating total health gain from an item
- Balancing custom items or showing pickup previews

**See also:** 
[[#AddSoulHearts|AddSoulHearts]], [[#AddHearts|AddHearts]], [[#AddMaxHearts|AddMaxHearts]]


---

### AddBombs {#AddBombs}

```
int AddBombs
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the number of bombs the item adds to the player.

**Use Cases:**

- Determining bomb‑related bonuses
- Simulating item pickup effects

**See also:** 
[[#AddKeys|AddKeys]], [[#AddCoins|AddCoins]]


---

### AddCoins {#AddCoins}

```
int AddCoins
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the number of coins the item adds to the player.

**Use Cases:**

- Evaluating coin gain from an item
- Custom shop or economy modding

**See also:** 
[[#AddBombs|AddBombs]], [[#AddKeys|AddKeys]]


---

### AddCostumeOnPickup {#AddCostumeOnPickup}

```
boolean AddCostumeOnPickup
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Indicates whether the item adds its associated costume when picked up.

**Use Cases:**

- Controlling visual appearance changes
- Preventing costume application in certain mods

**See also:** 
[[#Costume|Costume]]


---

### AddHearts {#AddHearts}

```
int AddHearts
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the number of red hearts (half‑heart units) the item heals.

**Use Cases:**

- Calculating health restoration from an item
- Item stat display for mods

**See also:** 
[[#AddSoulHearts|AddSoulHearts]], [[#AddBlackHearts|AddBlackHearts]], [[#AddMaxHearts|AddMaxHearts]]


---

### AddKeys {#AddKeys}

```
int AddKeys
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the number of keys the item adds to the player.

**Use Cases:**

- Determining resource gain from items
- Custom pickup effects

**See also:** 
[[#AddBombs|AddBombs]], [[#AddCoins|AddCoins]]


---

### AddMaxHearts {#AddMaxHearts}

```
int AddMaxHearts
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns the number of empty heart containers (half‑heart units) the item grants, increasing maximum health.

**Use Cases:**

- Calculating max‑HP changes from an item
- Previewing health capacity before pickup

**See also:** 
[[#AddHearts|AddHearts]], [[#AddSoulHearts|AddSoulHearts]]


---

### AddSoulHearts {#AddSoulHearts}

```
int AddSoulHearts
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the number of soul hearts (half‑heart units) the item adds to the player.

**Use Cases:**

- Checking soul heart gains from an item
- Adjusting item balance

**See also:** 
[[#AddBlackHearts|AddBlackHearts]], [[#AddHearts|AddHearts]]


---

### CacheFlags {#CacheFlags}

```
int CacheFlags
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns the CacheFlag bitmask that specifies which player stats the item modifies.

**Use Cases:**

- Understanding stat‑change triggers for passive items
- Building systems that react to cache evaluations

**See also:** 
[[#PassiveCache|PassiveCache]]


---

### ChargeType {#ChargeType}

```
int ChargeType
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the charge type (0: Normal, 1: Timed, 2: Special) for active items.

**Use Cases:**

- Classifying active item behavior
- Implementing custom charge mechanics

**See also:** 
[[#MaxCharges|MaxCharges]], [[#InitCharge|InitCharge]]


---

### ClearEffectsOnRemove {#ClearEffectsOnRemove}

```
boolean ClearEffectsOnRemove
```

*DLC: AB+, REP, REP+*

Returns whether the item's effects should be cleared when the item is removed from the player.

**Use Cases:**

- Handling item removal logic in mods
- Understanding persistent vs temporary effects

**See also:** 
[[#PersistentEffect|PersistentEffect]]


---

### Costume {#Costume}

```
const Costume Costume
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the Costume object that the item provides, describing its visual appearance changes.

**Use Cases:**

- Retrieving costume data for custom rendering
- Checking if an item has a visual effect

**See also:** 
[[#AddCostumeOnPickup|AddCostumeOnPickup]]


---

### CraftingQuality {#CraftingQuality}

```
int CraftingQuality
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns the quality used for the Bag of Crafting algorithm; -1 means the item cannot be crafted.

**Use Cases:**

- Adjusting crafting recipes
- Displaying crafting potential in UI

**See also:** 
[[#Quality|Quality]]


---

### Description {#Description}

```
string Description
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns the item description string, which in Repentance is a placeholder key (e.g., '#THE_SAD_ONION_DESCRIPTION').

**Use Cases:**

- Retrieving description for custom mod tooltips
- Localization or string replacement

**See also:** 
[[#Name|Name]]


---

### DevilPrice {#DevilPrice}

```
int DevilPrice
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the heart cost (full red heart units) for purchasing the item in a devil deal.

**Use Cases:**

- Calculating devil deal prices
- Displaying cost previews in custom shops

**See also:** 
[[#ShopPrice|ShopPrice]]


---

### Discharged {#Discharged}

```
boolean Discharged
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Removed attribute from Repentance; previously indicated a discharged state. No functional use in current version.

This attribute got removed with Repentance.

**Use Cases:**

- 调用 Discharged 完成对应 API 操作

**See also:** 



---

### GfxFileName {#GfxFileName}

```
string GfxFileName
```

*DLC: AB+, REP, REP+*

Returns the file path to the item's graphics file (GFX).

**Use Cases:**

- Loading custom sprites for mods
- Referencing item animations

**See also:** 
[[#ID|ID]]


---

### Hidden {#Hidden}

```
boolean Hidden
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns true if the item should not appear in the Death Certificate area.

**Use Cases:**

- Item pool manipulation
- Hiding certain items from Death Certificate in mods

**See also:** 
[[#IsAvailable|IsAvailable]]


---

### ID {#ID}

```
int ID
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns the numeric CollectibleType/TrinketType ID of the item.

**Use Cases:**

- Using the ID for item spawning or logic branching
- Mapping ID to item name or data

**See also:** 
[[#Name|Name]], [[#Type|Type]]


---

### InitCharge {#InitCharge}

```
int InitCharge
```

*DLC: AB+, REP | Modifiers: const*

Returns the initial charge amount an active item has when first picked up; -1 means fully charged.

**Use Cases:**

- Setting up active item charge on acquisition
- Balancing new active items

**See also:** 
[[#MaxCharges|MaxCharges]], [[#ChargeType|ChargeType]]


---

### MaxCharges {#MaxCharges}

```
int MaxCharges
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns the maximum charge capacity of an active item.

**Use Cases:**

- Charge bar calculations
- Active item balance testing

**See also:** 
[[#InitCharge|InitCharge]], [[#ChargeType|ChargeType]]


---

### MaxCooldown {#MaxCooldown}

```
int MaxCooldown
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the maximum cooldown (in frames) for an active item's effect.

**Use Cases:**

- Understanding active item duration
- Timing custom effects

**See also:** 
[[#MaxCharges|MaxCharges]]


---

### Name {#Name}

```
string Name
```

*DLC: REP, REP+ | Modifiers: const*

Returns the item name string, which in Repentance is a placeholder key (e.g., '#THE_SAD_ONION_NAME').

**Use Cases:**

- Displaying item names in custom UI
- Localization or string replacement

**See also:** 
[[#Description|Description]], [[#ID|ID]]


---

### PassiveCache {#PassiveCache}

```
boolean PassiveCache
```

*DLC: AB+, REP, REP+*

Indicates whether a cache evaluation is triggered when the item is picked up (relevant for items like Mom's Box).

**Use Cases:**

- Modifying passive item behavior
- Debugging stat update triggers

**See also:** 
[[#CacheFlags|CacheFlags]]


---

### PersistentEffect {#PersistentEffect}

```
boolean PersistentEffect
```

*DLC: AB+, REP, REP+*

Returns true if an active item's effect persists between rooms.

**Use Cases:**

- Designing items with room‑persistent effects
- Checking effect lifespan

**See also:** 
[[#ClearEffectsOnRemove|ClearEffectsOnRemove]]


---

### Quality {#Quality}

```
int Quality
```

*DLC: AB+, REP, REP+*

Returns the item quality value (0 to 4), representing general power level.

**Use Cases:**

- Evaluating item strength
- Quality‑based item sorting or filtering

**See also:** 
[[#CraftingQuality|CraftingQuality]]


---

### ShopPrice {#ShopPrice}

```
int ShopPrice
```

*DLC: AB+, REP, REP+*

Returns the shop price (in coins) for the item; defaults to 15 if not defined.

**Use Cases:**

- Calculating shop purchase costs
- Custom economy modding

**See also:** 
[[#DevilPrice|DevilPrice]]


---

### Special {#Special}

```
boolean Special
```

*DLC: AB+, REP, REP+*

Boolean flag for the deprecated special item reroll system; not used in Repentance.

**Use Cases:**

- 调用 Special 完成对应 API 操作

**See also:** 



---

### Tags {#Tags}

```
int Tags
```

*DLC: AB+, REP, REP+*

Returns the raw integer bitmask of tags assigned to the item.

**Use Cases:**

- Direct bitwise tag checks
- Storing or comparing tag data

**See also:** 
[[#HasTags|HasTags]]


---

### Type {#Type}

```
ItemType Type
```

*DLC: AB+, REP, REP+*

Returns the ItemType enum value (e.g., ACTIVE, PASSIVE, FAMILIAR, TRINKET) of the item.

**Use Cases:**

- Categorizing items by type
- Switching on item type for logic

**See also:** 
[[#ID|ID]], [[#IsCollectible|IsCollectible]], [[#IsTrinket|IsTrinket]], [[#IsNull|IsNull]]


---
