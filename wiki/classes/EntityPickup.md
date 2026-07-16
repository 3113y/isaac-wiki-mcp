---
title: EntityPickup
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 17
---

# EntityPickup

## Summary

EntityPickup 表示游戏中的可拾取物品实体，如硬币、心、炸弹、钥匙、宝箱、道具等。可通过 Entity:ToPickup() 将实体转换为拾取物操作接口，提供变形、价格控制、拾取行为、音效、箱子开启等功能。

## Inheritance

- Inherits from: [[Entity]]

## Related Types

- [[EntityPlayer]]
- [[Options]]
- [[RNG]]

## Key Methods

- [[#Morph|Morph]]
- [[#TryOpenChest|TryOpenChest]]
- [[#AppearFast|AppearFast]]
- [[#CanReroll|CanReroll]]
- [[#IsShopItem|IsShopItem]]

## Methods

### Functions

### AppearFast {#AppearFast}

```
void AppearFast ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

使拾取物立即以快速动画出现（跳过正常渐现过程）。

**Use Cases:**

- 动态生成拾取物时使玩家能立即看见并拾取
- 修复因延迟出现导致的奇怪显示问题

**See also:** 
[[#Morph|Morph]], [[#Wait|Wait]], [[#Timeout|Timeout]]


---

### CanReroll {#CanReroll}

```
boolean CanReroll ( )
```

*DLC: REP, REP+ | Modifiers: const*

查询该拾取物是否可以被重掷（如被 D6 等道具影响）。

**Use Cases:**

- 判断拾取物是否受重掷效果影响，用于自定义重掷逻辑
- 在重掷前过滤出不可重掷的拾取物以避免错误

**See also:** 
[[#Morph|Morph]], [[#ShopItemId|ShopItemId]]


---

### GetCoinValue {#GetCoinValue}

```
int GetCoinValue ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

若当前拾取物为硬币，返回其面值；否则返回 0。

If this is a coin, return its face value, else zero.

**Use Cases:**

- 获取硬币的金额以用于金钱统计或自定义交易
- 区分不同硬币面值实现特定机制

**See also:** 
[[#Morph|Morph]], [[#Price|Price]]


---

### IsShopItem {#IsShopItem}

```
boolean IsShopItem ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回该拾取物是否为商店中待售的物品。

**Use Cases:**

- 检测拾取物是否属于商店布局，以便修改价格或行为
- 在商店重掷时区分普通掉落和商店物品

**See also:** 
[[#ShopItemId|ShopItemId]], [[#Price|Price]], [[#AutoUpdatePrice|AutoUpdatePrice]]


---

### Morph {#Morph}

```
void Morph ( EntityType Type, int Variant, int SubType, boolean KeepPrice = false, boolean KeepSeed = false, boolean IgnoreModifiers = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将当前拾取物变形为指定的实体类型、变体和子类型，可选择保留价格、保留 RNG 种子或忽略外在修改效果（如堕化以撒的额外选择）。常用于生成自定义拾取物或纠正被全局效果扭曲的拾取物。

**Use Cases:**

- 动态改变拾取物类型，如将普通硬币变成幸运硬币
- 生成任务关键道具时防止被角色被动效果改变
- 保留价格实现商店物品类型替换而不重置价格
- 使用 KeepSeed 保持随机性一致，适用于伪随机环境

**See also:** 
[[#AppearFast|AppearFast]], [[#CanReroll|CanReroll]], [[#AutoUpdatePrice|AutoUpdatePrice]], [[#ShopItemId|ShopItemId]]


---

### PlayDropSound {#PlayDropSound}

```
void PlayDropSound ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

播放拾取物掉落时的音效。

**Use Cases:**

- 在自定义生成拾取物时模拟自然掉落声音
- 结合 Morph 等操作保持视听一致性

**See also:** 
[[#PlayPickupSound|PlayPickupSound]], [[#AppearFast|AppearFast]]


---

### PlayPickupSound {#PlayPickupSound}

```
void PlayPickupSound ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

播放拾取物被捡起时的音效。

**Use Cases:**

- 手动触发拾取时播放对应音效，提升反馈感
- 实现特殊拾取事件而不触发默认的自动拾取逻辑

**See also:** 
[[#PlayDropSound|PlayDropSound]]


---

### TryOpenChest {#TryOpenChest}

```
boolean TryOpenChest ( EntityPlayer Player = nil )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

尝试使用指定玩家打开此拾取物宝箱。若成功返回 true，通常用于触发宝箱内容物生成。

**Player**: The player that opened this chest

**Use Cases:**

- 自定义宝箱开启逻辑（如需要钥匙判定、动画）
- 通过玩家参考实现多人模式下正确的宝箱归属

**See also:** 
[[#Morph|Morph]], [[#State|State]]


---

### AutoUpdatePrice {#AutoUpdatePrice}

```
boolean AutoUpdatePrice
```

*DLC: AB+, REP, REP+ | Modifiers: const*

布尔变量，控制是否自动根据游戏规则更新拾取物价格（例如堕化店长的价格修正）。默认开启。

**Use Cases:**

- 关闭自动价格更新以实现自定义定价
- 在生成商店物品后立即手动设定价格并防止被覆盖

**See also:** 
[[#Price|Price]], [[#ShopItemId|ShopItemId]]


---

### Charge {#Charge}

```
int Charge
```

*DLC: AB+, REP, REP+ | Modifiers: const*

整数变量，记录携带电池的充能数（通常用于电池类拾取物）。

**Use Cases:**

- 设置或获取电池拾取物的充能值
- 使自定义电池物品提供特定的充能量

**See also:** 
[[#Morph|Morph]]


---

### OptionsPickupIndex {#OptionsPickupIndex}

```
int OptionsPickupIndex
```

*DLC: AB+, REP, REP+ | Modifiers: const*

非零整数值，使该拾取物与相同 OptionsPickupIndex 的其它拾取物形成选项组。当一个被拾取时，同组其它物品消失。

**Use Cases:**

- 创建二选一或多选一的拾取物组，类似游戏内选项道具
- 实现自定义房间机制时强制互斥拾取

**See also:** 
[[#Touched|Touched]]


---

### Price {#Price}

```
int Price
```

*DLC: AB+, REP, REP+ | Modifiers: const*

该拾取物在商店中的价格（整数）。仅当拾取物位于商店摊位时生效，配合 AutoUpdatePrice 可被自动修正。

该物品在商店中的价格。

**Use Cases:**

- 设置或修改商店物品的售价
- 动态定价或折扣机制

**See also:** 
[[#AutoUpdatePrice|AutoUpdatePrice]], [[#ShopItemId|ShopItemId]], [[#IsShopItem|IsShopItem]]


---

### ShopItemId {#ShopItemId}

```
int ShopItemId
```

*DLC: AB+, REP, REP+ | Modifiers: static*

商店物品槽 ID，用于标识该拾取物属于商店的哪个货架位置，并影响重置行为。设为 -1 可避免被 D6 重置为红心，-2 则采用恶魔交易价格自动定价。

**Use Cases:**

- 修复 Lua 生成商店物品被错误重置的问题
- 设定恶魔交易价格风格（设定为 -2）

**See also:** 
[[#Price|Price]], [[#AutoUpdatePrice|AutoUpdatePrice]], [[#IsShopItem|IsShopItem]]


---

### State {#State}

```
int State
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 State 完成对应 API 操作

**See also:** 



---

### Timeout {#Timeout}

```
int Timeout
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Timeout 完成对应 API 操作

**See also:** 



---

### Touched {#Touched}

```
boolean Touched
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Touched 完成对应 API 操作

**See also:** 



---

### Wait {#Wait}

```
int Wait
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Wait 完成对应 API 操作

**See also:** 



---

## See Also

- [[Entity]]
- [[EntityPlayer]]
- [[Options]]
- [[RNG]]
