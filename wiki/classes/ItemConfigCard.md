---
title: ItemConfigCard
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 14
---

# ItemConfigCard

## Summary

ItemConfigCard 封装卡牌/符文的配置数据，包括名称、描述、解锁状态、类型标识及动画等元信息。

## Key Methods

- [[#IsCard|IsCard]]
- [[#IsRune|IsRune]]
- [[#IsAvailable|IsAvailable]]
- [[#Name|Name]]
- [[#ID|ID]]

## Methods

### Functions

### IsAvailable {#IsAvailable}

```
boolean IsAvailable ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回布尔值，判断该卡牌整体是否可用（例如已解锁或满足出现条件）。

**Use Cases:**

- 在生成掉落前过滤不可用卡牌
- 决定某些成就或解锁机制是否触发

**See also:** 
[[#AchievementID|AchievementID]], [[#GreedModeAllowed|GreedModeAllowed]], [[#ID|ID]]


---

### IsCard {#IsCard}

```
boolean IsCard ( )
```

*DLC: REP, REP+ | Modifiers: const*

返回布尔值，表示该卡牌是否为普通卡牌（而非符文或其它类型）。

**Use Cases:**

- 区分卡牌属类以应用不同效果
- 在UI中按类别分组显示

**See also:** 
[[#IsRune|IsRune]], [[#CardType|CardType]], [[#ID|ID]]


---

### IsRune {#IsRune}

```
boolean IsRune ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回布尔值，表示该卡牌是否为符文。

**Use Cases:**

- 单独处理符文类物品的逻辑
- 在成就追踪时区分符文与普通卡牌

**See also:** 
[[#IsCard|IsCard]], [[#CardType|CardType]], [[#Name|Name]]


---

### AchievementID {#AchievementID}

```
int AchievementID
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回解锁此卡牌所需成就的ID，若默认可用则返回 -1。

Returns the ID of the achievement that unlocks the card. Returns ``:::lua -1`` if the card is unlocked by default.

**Use Cases:**

- 检查卡牌是否通过成就解锁
- 决定商店或掉落表是否需要成就前置

**See also:** 
[[#IsAvailable|IsAvailable]], [[#ID|ID]], [[#Name|Name]]


---

### AnnouncerDelay {#AnnouncerDelay}

```
int AnnouncerDelay
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取播报员播放卡牌名称的延迟时间（整数）。

**Use Cases:**

- 调节自定义播报音效的时机

**See also:** 
[[#AnnouncerVoice|AnnouncerVoice]], [[#Name|Name]]


---

### AnnouncerVoice {#AnnouncerVoice}

```
int AnnouncerVoice
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取与卡牌关联的播报员语音ID。

**Use Cases:**

- 播放特定语音响应卡牌使用或获得

**See also:** 
[[#AnnouncerDelay|AnnouncerDelay]], [[#Name|Name]]


---

### CardType {#CardType}

```
int CardType
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回表示卡牌类型的整数值（例如普通卡牌、符文等）。

**Use Cases:**

- 在不依赖布尔方法时进行分类型逻辑
- 存储或比较不同类型的卡牌

**See also:** 
[[#IsCard|IsCard]], [[#IsRune|IsRune]], [[#ID|ID]]


---

### Description {#Description}

```
string Description
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回卡牌的描述文本。在 Repentance 中返回的是本地化键名（如 #[CARD_NAME]_DESCRIPTION）。

**Use Cases:**

- 在UI中显示卡牌描述
- 通过键名进行本地化翻译

**See also:** 
[[#Name|Name]], [[#ID|ID]], [[#HudAnim|HudAnim]]


---

### GreedModeAllowed {#GreedModeAllowed}

```
boolean GreedModeAllowed
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回布尔值，指示该卡牌是否允许在贪婪/超级贪婪模式中出现。

**Use Cases:**

- 生成贪婪模式专属掉落表
- 过滤不适用的卡牌避免错误出现

**See also:** 
[[#IsAvailable|IsAvailable]], [[#ID|ID]]


---

### HudAnim {#HudAnim}

```
string HudAnim
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回卡片正面动画的名称（在 ui_cardfronts.anm2 中）。对标准卡牌返回空字符串，仅在模组卡牌上有效。

**Use Cases:**

- 加载自定义卡牌动画
- 在HUD上渲染特殊卡面效果

**See also:** 
[[#Name|Name]], [[#Description|Description]]


---

### ID {#ID}

```
int ID
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回该卡牌的唯一整数ID。

**Use Cases:**

- 比对不同卡牌
- 通过ID获取对应配置进行批量处理

**See also:** 
[[#Name|Name]], [[#IsCard|IsCard]], [[#IsRune|IsRune]]


---

### MimicCharge {#MimicCharge}

```
int MimicCharge
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回模仿（Mimic）相关充能数，具体含义视上下文而定。

**Use Cases:**

- 控制模仿效果或类似机制的充能消耗

**See also:** 
[[#IsCard|IsCard]], [[#CardType|CardType]]


---

### Name {#Name}

```
string Name
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回卡牌的名称。在 Repentance 中返回的是本地化键名（如 #[CARD_NAME]_NAME）。

**Use Cases:**

- 获取用于显示的卡牌名称
- 通过键名实现多语言支持

**See also:** 
[[#Description|Description]], [[#ID|ID]], [[#HudAnim|HudAnim]]


---

### PickupSubtype {#PickupSubtype}

```
int PickupSubtype
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回拾取物的子类型，可能与卡牌效果或生成基类对应。

**Use Cases:**

- 确定生成掉落时的拾取物类型
- 在拾取时触发特定子类型逻辑

**See also:** 
[[#CardType|CardType]], [[#ID|ID]]


---
