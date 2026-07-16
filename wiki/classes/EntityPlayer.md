---
title: EntityPlayer
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 276
---

# EntityPlayer

## Summary

EntityPlayer 类代表玩家实体，提供大量方法用于操作玩家状态，包括生命值、消耗品、道具、攻击、动画、属性等，是 Mod 开发中最核心的玩家交互接口。

## Inheritance

- Inherits from: [[Entity]]

## Related Types

- [[Color]]
- [[EntityBomb]]
- [[EntityFamiliar]]
- [[EntityKnife]]
- [[EntityLaser]]
- [[EntityRef]]
- [[EntityTear]]
- [[GridEntity]]
- [[Input]]
- [[ItemConfig]]
- [[ItemConfigItem]]
- [[QueueItemData]]
- [[RNG]]
- [[Room]]
- [[Sprite]]
- [[TearParams]]
- [[TemporaryEffect]]
- [[TemporaryEffects]]
- [[Vector]]

## Key Methods

- [[#AddCollectible|AddCollectible]]
- [[#RemoveCollectible|RemoveCollectible]]
- [[#AddHearts|AddHearts]]
- [[#FireTear|FireTear]]
- [[#GetPlayerType|GetPlayerType]]

## Methods

### Functions

### AddBlackHearts {#AddBlackHearts}

```
void AddBlackHearts ( int BlackHearts )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加或移除黑心（每单位半颗心）。

**Use Cases:**

- 增加黑心数量
- 扣除黑心

**See also:** 
[[#AddSoulHearts|AddSoulHearts]], [[#AddHearts|AddHearts]]


---

### AddBloodCharge {#AddBloodCharge}

```
void AddBloodCharge ( int Amount )
```

*DLC: REP, REP+ | Modifiers: const*

添加血量充能，仅对堕化伯大妮有效。

**Use Cases:**

- 增加伯大妮的血量充能

**See also:** 
[[#AddSoulCharge|AddSoulCharge]], [[#GetBloodCharge|GetBloodCharge]]


---

### AddBlueFlies {#AddBlueFlies}

```
Entity AddBlueFlies ( int Amount, Vector Position, Entity Target )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

生成蓝苍蝇攻击敌人，数量受饰品鱼尾影响。

???- info "Amount"

**Use Cases:**

- 制造额外攻击随从

**See also:** 
[[#AddBlueSpider|AddBlueSpider]], [[#AddFriendlyDip|AddFriendlyDip]]


---

### AddBlueSpider {#AddBlueSpider}

```
Entity AddBlueSpider ( Vector Position )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

在指定位置生成一只蓝蜘蛛。

**Use Cases:**

- 创建爪机攻击单位

**See also:** 
[[#AddBlueFlies|AddBlueFlies]], [[#ThrowBlueSpider|ThrowBlueSpider]]


---

### AddBombs {#AddBombs}

```
void AddBombs ( int Amount )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加或移除炸弹数量。

**Use Cases:**

- 增加炸弹上限
- 减少炸弹数

**See also:** 
[[#GetNumBombs|GetNumBombs]], [[#AddKeys|AddKeys]]


---

### AddBoneHearts {#AddBoneHearts}

```
void AddBoneHearts ( int Hearts )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

添加或移除骨心（每个单位一颗骨心）。

**Use Cases:**

- 增加骨心容器

**See also:** 
[[#AddGoldenHearts|AddGoldenHearts]], [[#AddSoulHearts|AddSoulHearts]]


---

### AddBrokenHearts {#AddBrokenHearts}

```
void AddBrokenHearts ( int BrokenHearts )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加或移除碎心。

**Use Cases:**

- 增加碎心数量

**See also:** 
[[#GetBrokenHearts|GetBrokenHearts]], [[#AddHearts|AddHearts]]


---

### AddCacheFlags {#AddCacheFlags}

```
void AddCacheFlags ( CacheFlag CacheFlag )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

标记指定的缓存标签，下次缓存重算时将更新相应属性。

**Use Cases:**

- 刷新伤害、射速等统计

**See also:** 
[[#EvaluateItems|EvaluateItems]], [[#GetEffects|GetEffects]]


---

### AddCard {#AddCard}

```
void AddCard ( Card ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

给予一张卡牌。

**Use Cases:**

- 直接获得指定卡牌

**See also:** 
[[#GetCard|GetCard]], [[#SetCard|SetCard]]


---

### AddCoins {#AddCoins}

```
void AddCoins ( int Amount )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加或移除金币。

**Use Cases:**

- 增加金币
- 减少金币

**See also:** 
[[#GetNumCoins|GetNumCoins]], [[#AddBombs|AddBombs]]


---

### AddCollectible {#AddCollectible}

```
void AddCollectible ( CollectibleType Type, int Charge = 0, boolean FirstTimePickingUp = true, ActiveSlot Slot = ActiveSlot.SLOT_PRIMARY, int VarData = 0)
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加道具，支持设置充能、首次拾取、主动槽位和VarData。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 给予玩家道具
- 模拟首次拾取

**See also:** 
[[#RemoveCollectible|RemoveCollectible]], [[#HasCollectible|HasCollectible]]


---

### void AddCollectible ( [CollectibleType](enums/CollectibleType.md) Type, int Charge = 0, boolean FirstTimePickingUp = true, [ActiveSlot](enums/ActiveSlot.md) Slot = ActiveSlot.SLOT_PRIMARY, int VarData = 0, [ItemPoolType](enums/ItemPoolType.md) PoolType ) {#void AddCollectible ( [CollectibleType](enums/CollectibleType.md) Type, int Charge = 0, boolean FirstTimePickingUp = true, [ActiveSlot](enums/ActiveSlot.md) Slot = ActiveSlot.SLOT_PRIMARY, int VarData = 0, [ItemPoolType](enums/ItemPoolType.md) PoolType )}

```
void AddControlsCooldown ( int Cooldown )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加道具（重载），额外指定道具池类型。

**Use Cases:**

- 指定道具池的道具获取

**See also:** 
[[#AddCollectible|AddCollectible]], [[#CanAddCollectible|CanAddCollectible]], [[#GetCollectibleRNG|GetCollectibleRNG]]


---

### AddCostume {#AddCostume}

```
void AddCostume ( ItemConfigItem Item, boolean ItemStateOnly )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

添加基于ItemConfigItem的装扮。

**Use Cases:**

- 动态更换角色外观

**See also:** 
[[#RemoveCostume|RemoveCostume]], [[#ClearCostumes|ClearCostumes]]


---

### AddCurseMistEffect {#AddCurseMistEffect}

```
void AddCurseMistEffect ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加诅咒迷雾效果。

**Use Cases:**

- 触发迷雾视觉效果

**See also:** 
[[#RemoveCurseMistEffect|RemoveCurseMistEffect]], [[#HasCurseMistEffect|HasCurseMistEffect]]


---

### AddDeadEyeCharge {#AddDeadEyeCharge}

```
void AddDeadEyeCharge ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

增加精准射手充能层数。

**Use Cases:**

- 提升精准射手伤害加成

**See also:** 
[[#ClearDeadEyeCharge|ClearDeadEyeCharge]], [[#FireTear|FireTear]]


---

### AddDollarBillEffect {#AddDollarBillEffect}

```
void AddDollarBillEffect ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加3美元钞票的随机效果。

**Use Cases:**

- 随机获得短暂道具效果

**See also:** 
[[#GetEffects|GetEffects]], [[#AddCacheFlags|AddCacheFlags]]


---

### AddEternalHearts {#AddEternalHearts}

```
void AddEternalHearts ( int EternalHearts )
```

*DLC: AB+, REP, REP+*

添加或移除永恒之心（每单位半颗心）。

**Use Cases:**

- 增加永恒之心

**See also:** 
[[#GetEternalHearts|GetEternalHearts]], [[#AddHearts|AddHearts]]


---

### AddFriendlyDip {#AddFriendlyDip}

```
void AddFriendlyDip ( int Subtype, Vector Position )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

生成一个友好的小屎角色。

**Use Cases:**

- 召唤Dip随从

**See also:** 
[[#ThrowFriendlyDip|ThrowFriendlyDip]], [[#AddBlueFlies|AddBlueFlies]]


---

### AddGigaBombs {#AddGigaBombs}

```
void AddGigaBombs ( int GigaBombs )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

添加巨型炸弹数量，需提前增加普通炸弹。

**Use Cases:**

- 增加巨型炸弹

**See also:** 
[[#GetNumGigaBombs|GetNumGigaBombs]], [[#AddBombs|AddBombs]]


---

### AddGoldenBomb {#AddGoldenBomb}

```
void AddGoldenBomb ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

添加一个金炸弹效果。

**Use Cases:**

- 获得无限炸弹效果

**See also:** 
[[#RemoveGoldenBomb|RemoveGoldenBomb]], [[#HasGoldenBomb|HasGoldenBomb]]


---

### AddGoldenHearts {#AddGoldenHearts}

```
void AddGoldenHearts ( int Hearts )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加或移除金心（每个单位一颗金心）。

**Use Cases:**

- 增加金心容器

**See also:** 
[[#GetGoldenHearts|GetGoldenHearts]], [[#AddBoneHearts|AddBoneHearts]]


---

### AddGoldenKey {#AddGoldenKey}

```
void AddGoldenKey ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

添加一个金钥匙效果。

**Use Cases:**

- 获得无限钥匙效果

**See also:** 
[[#RemoveGoldenKey|RemoveGoldenKey]], [[#HasGoldenKey|HasGoldenKey]]


---

### AddHearts {#AddHearts}

```
void AddHearts ( int Hearts )
```

*DLC: AB+, REP, REP+*

添加或移除红心（每单位半颗心），填充心容器。

**Use Cases:**

- 恢复红心
- 扣除生命值

**See also:** 
[[#GetHearts|GetHearts]], [[#AddMaxHearts|AddMaxHearts]]


---

### AddItemWisp {#AddItemWisp}

```
EntityFamiliar AddItemWisp ( CollectibleType Collectible, Vector Position, boolean AdjustOrbitLayer = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

添加魂火（来自美德之书），可指定道具类型。

**Use Cases:**

- 召唤特殊魂火环绕物

**See also:** 
[[#AddWisp|AddWisp]], [[#TriggerBookOfVirtues|TriggerBookOfVirtues]]


---

### AddJarFlies {#AddJarFlies}

```
void AddJarFlies ( int Flies )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

添加苍蝇罐子中的苍蝇数量。

**Use Cases:**

- 增加苍蝇罐子存量

**See also:** 
[[#GetJarFlies|GetJarFlies]], [[#AddJarHearts|AddJarHearts]]


---

### AddJarHearts {#AddJarHearts}

```
void AddJarHearts ( int Hearts )
```

*DLC: AB+, REP | Modifiers: const*

添加心罐子中的生命储存量。

**Use Cases:**

- 增加心形罐子储存

**See also:** 
[[#GetJarHearts|GetJarHearts]], [[#AddJarFlies|AddJarFlies]]


---

### AddKeys {#AddKeys}

```
void AddKeys ( int Amount )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 AddKeys 完成对应 API 操作

**See also:** 



---

### AddMaxHearts {#AddMaxHearts}

```
void AddMaxHearts ( int MaxHearts, boolean IgnoreKeeper )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 AddMaxHearts 完成对应 API 操作

**See also:** 



---

### AddMinisaac {#AddMinisaac}

```
EntityFamiliar AddMinisaac ( Vector Position, boolean PlayAnim = true )
```

*DLC: REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 AddMinisaac 完成对应 API 操作

**See also:** 



---

### AddNullCostume {#AddNullCostume}

```
void AddNullCostume ( NullItemID NullId )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddNullCostume 完成对应 API 操作

**See also:** 



---

### AddPill {#AddPill}

```
void AddPill ( PillColor Pill )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddPill 完成对应 API 操作

**See also:** 



---

### AddPlayerFormCostume {#AddPlayerFormCostume}

```
void AddPlayerFormCostume ( PlayerForm Form )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddPlayerFormCostume 完成对应 API 操作

**See also:** 



---

### AddPoopMana {#AddPoopMana}

```
void AddPoopMana ( int Num )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddPoopMana 完成对应 API 操作

**See also:** 



---

### AddPrettyFly {#AddPrettyFly}

```
void AddPrettyFly ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddPrettyFly 完成对应 API 操作

**See also:** 



---

### AddRottenHearts {#AddRottenHearts}

```
void AddRottenHearts ( int RottenHearts )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddRottenHearts 完成对应 API 操作

**See also:** 



---

### AddSoulCharge {#AddSoulCharge}

```
void AddSoulCharge ( int Amount )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddSoulCharge 完成对应 API 操作

**See also:** 



---

### AddSoulHearts {#AddSoulHearts}

```
void AddSoulHearts ( int SoulHearts )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddSoulHearts 完成对应 API 操作

**See also:** 



---

### AddSwarmFlyOrbital {#AddSwarmFlyOrbital}

```
EntityFamiliar AddSwarmFlyOrbital ( Vector Position )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddSwarmFlyOrbital 完成对应 API 操作

**See also:** 



---

### AddTrinket {#AddTrinket}

```
void AddTrinket ( TrinketType Type, boolean FirstTimePickingUp = true )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddTrinket 完成对应 API 操作

**See also:** 



---

### AddWisp {#AddWisp}

```
EntityFamiliar AddWisp ( CollectibleType Collectible, Vector Position, boolean AdjustOrbitLayer = false, boolean DontUpdate = false )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AddWisp 完成对应 API 操作

**See also:** 



---

### AnimateAppear {#AnimateAppear}

```
void AnimateAppear ( )
```

*DLC: AB+, REP, REP+*

播放在关卡开始时通常播放的动画。

播放在关卡开始时通常播放的动画。

**Use Cases:**

- 调用 AnimateAppear 完成对应 API 操作

**See also:** 



---

### AnimateCard {#AnimateCard}

```
void AnimateCard ( Card ID, string AnimName = "Pickup" )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AnimateCard 完成对应 API 操作

**See also:** 



---

### AnimateCollectible {#AnimateCollectible}

```
void AnimateCollectible ( CollectibleType Collectible, string AnimName = "Pickup", string SpriteAnimName = "PlayerPickupSparkle" )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AnimateCollectible 完成对应 API 操作

**See also:** 



---

### AnimateHappy {#AnimateHappy}

```
void AnimateHappy ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AnimateHappy 完成对应 API 操作

**See also:** 



---

### AnimateLightTravel {#AnimateLightTravel}

```
void AnimateLightTravel ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AnimateLightTravel 完成对应 API 操作

**See also:** 



---

### AnimatePickup {#AnimatePickup}

```
void AnimatePickup ( Sprite sprite, boolean HideShadow = false, string AnimName = "Pickup" )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AnimatePickup 完成对应 API 操作

**See also:** 



---

### AnimatePill {#AnimatePill}

```
void AnimatePill ( PillColor Pill, string AnimName = "Pickup" )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 AnimatePill 完成对应 API 操作

**See also:** 



---

### AnimatePitfallIn {#AnimatePitfallIn}

```
void AnimatePitfallIn ( )
```

*DLC: REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 AnimatePitfallIn 完成对应 API 操作

**See also:** 



---

### AnimatePitfallOut {#AnimatePitfallOut}

```
void AnimatePitfallOut ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 AnimatePitfallOut 完成对应 API 操作

**See also:** 



---

### AnimateSad {#AnimateSad}

```
void AnimateSad ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AnimateSad 完成对应 API 操作

**See also:** 



---

### AnimateTeleport {#AnimateTeleport}

```
void AnimateTeleport ( boolean Up )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AnimateTeleport 完成对应 API 操作

**See also:** 



---

### AnimateTrapdoor {#AnimateTrapdoor}

```
void AnimateTrapdoor ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AnimateTrapdoor 完成对应 API 操作

**See also:** 



---

### AnimateTrinket {#AnimateTrinket}

```
void AnimateTrinket ( TrinketType Trinket, string AnimName = "Pickup", string SpriteAnimName = "PlayerPickupSparkle" )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AnimateTrinket 完成对应 API 操作

**See also:** 



---

### AreControlsEnabled {#AreControlsEnabled}

```
boolean AreControlsEnabled ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AreControlsEnabled 完成对应 API 操作

**See also:** 



---

### AreOpposingShootDirectionsPressed {#AreOpposingShootDirectionsPressed}

```
boolean AreOpposingShootDirectionsPressed ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 AreOpposingShootDirectionsPressed 完成对应 API 操作

**See also:** 



---

### CanAddCollectible {#CanAddCollectible}

```
boolean CanAddCollectible ( CollectibleType Type = CollectibleType.COLLECTIBLE_NULL )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 CanAddCollectible 完成对应 API 操作

**See also:** 



---

### CanPickBlackHearts {#CanPickBlackHearts}

```
boolean CanPickBlackHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 CanPickBlackHearts 完成对应 API 操作

**See also:** 



---

### CanPickBoneHearts {#CanPickBoneHearts}

```
boolean CanPickBoneHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 CanPickBoneHearts 完成对应 API 操作

**See also:** 



---

### CanPickGoldenHearts {#CanPickGoldenHearts}

```
boolean CanPickGoldenHearts ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 CanPickGoldenHearts 完成对应 API 操作

**See also:** 



---

### CanPickRedHearts {#CanPickRedHearts}

```
boolean CanPickRedHearts ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 CanPickRedHearts 完成对应 API 操作

**See also:** 



---

### CanPickRottenHearts {#CanPickRottenHearts}

```
boolean CanPickRottenHearts ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 CanPickRottenHearts 完成对应 API 操作

**See also:** 



---

### CanPickSoulHearts {#CanPickSoulHearts}

```
boolean CanPickSoulHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 CanPickSoulHearts 完成对应 API 操作

**See also:** 



---

### CanPickupItem {#CanPickupItem}

```
boolean CanPickupItem ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 CanPickupItem 完成对应 API 操作

**See also:** 



---

### CanShoot {#CanShoot}

```
boolean CanShoot ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 CanShoot 完成对应 API 操作

**See also:** 



---

### CanTurnHead {#CanTurnHead}

```
boolean CanTurnHead ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 CanTurnHead 完成对应 API 操作

**See also:** 



---

### ChangePlayerType {#ChangePlayerType}

```
void ChangePlayerType ( PlayerType PlayerType )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 ChangePlayerType 完成对应 API 操作

**See also:** 



---

### CheckFamiliar {#CheckFamiliar}

```
void CheckFamiliar ( FamiliarVariant FamiliarVariant, int TargetCount, RNG rng, ItemConfigItem SourceItemConfigItem = nil, int FamiliarSubType = -1 )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 CheckFamiliar 完成对应 API 操作

**See also:** 



---

### ClearCostumes {#ClearCostumes}

```
void ClearCostumes ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 ClearCostumes 完成对应 API 操作

**See also:** 



---

### ClearDeadEyeCharge {#ClearDeadEyeCharge}

```
void ClearDeadEyeCharge ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 ClearDeadEyeCharge 完成对应 API 操作

**See also:** 



---

### ClearTemporaryEffects {#ClearTemporaryEffects}

```
void ClearTemporaryEffects ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 ClearTemporaryEffects 完成对应 API 操作

**See also:** 



---

### DischargeActiveItem {#DischargeActiveItem}

```
void DischargeActiveItem ( ActiveSlot ActiveSlot = ActiveSlot.SLOT_PRIMARY )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 DischargeActiveItem 完成对应 API 操作

**See also:** 



---

### DonateLuck {#DonateLuck}

```
void DonateLuck ( int Luck )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 DonateLuck 完成对应 API 操作

**See also:** 



---

### DoZitEffect {#DoZitEffect}

```
void DoZitEffect ( Vector Direction )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 DoZitEffect 完成对应 API 操作

**See also:** 



---

### DropPocketItem {#DropPocketItem}

```
void DropPocketItem ( int PocketNum, Vector Pos )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 DropPocketItem 完成对应 API 操作

**See also:** 



---

### DropTrinket {#DropTrinket}

```
void DropTrinket ( Vector DropPos, boolean ReplaceTick )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 DropTrinket 完成对应 API 操作

**See also:** 



---

### EvaluateItems {#EvaluateItems}

```
void EvaluateItems ( )
```

*DLC: REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 EvaluateItems 完成对应 API 操作

**See also:** 



---

### FireBomb {#FireBomb}

```
EntityBomb FireBomb ( Vector Position, Vector Velocity, Entity Source = nil )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 FireBomb 完成对应 API 操作

**See also:** 



---

### FireBrimstone {#FireBrimstone}

```
EntityLaser FireBrimstone ( Vector Direction, Entity Source = nil, float DamageMultiplier = 1 )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 FireBrimstone 完成对应 API 操作

**See also:** 



---

### FireDelayedBrimstone {#FireDelayedBrimstone}

```
EntityLaser FireDelayedBrimstone ( float Angle, Entity Parent )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 FireDelayedBrimstone 完成对应 API 操作

**See also:** 



---

### FireKnife {#FireKnife}

```
EntityKnife FireKnife ( Entity Parent, float RotationOffset = 0, boolean CantOverwrite = false, int SubType = 0, int Variant = 0 )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 FireKnife 完成对应 API 操作

**See also:** 



---

### FireTear {#FireTear}

```
EntityTear FireTear ( Vector Position, Vector Velocity, boolean CanBeEye = true, boolean NoTractorBeam = false, boolean CanTriggerStreakEnd = true, Entity Source = nil, float DamageMultiplier = 1 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 FireTear 完成对应 API 操作

**See also:** 



---

### FireTechLaser {#FireTechLaser}

```
EntityLaser FireTechLaser ( Vector Position, LaserOffset OffsetID, Vector Direction, boolean LeftEye, boolean OneHit = false, Entity Source = nil, float DamageMultiplier = 1 )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 FireTechLaser 完成对应 API 操作

**See also:** 



---

### FireTechXLaser {#FireTechXLaser}

```
EntityLaser FireTechXLaser ( Vector Position, Vector Direction, float Radius, Entity Source = nil, float DamageMultiplier = 1 )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 FireTechXLaser 完成对应 API 操作

**See also:** 



---

### FlushQueueItem {#FlushQueueItem}

```
boolean FlushQueueItem ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 FlushQueueItem 完成对应 API 操作

**See also:** 



---

### FullCharge {#FullCharge}

```
boolean FullCharge ( ActiveSlot ActiveSlot = ActiveSlot.SLOT_PRIMARY, int Force = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 FullCharge 完成对应 API 操作

**See also:** 



---

### GetActiveCharge {#GetActiveCharge}

```
int GetActiveCharge ( ActiveSlot ActiveSlot = ActiveSlot.SLOT_PRIMARY )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetActiveCharge 完成对应 API 操作

**See also:** 



---

### GetActiveItem {#GetActiveItem}

```
CollectibleType GetActiveItem ( ActiveSlot ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' data-altreturn='0' }
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetActiveItem 完成对应 API 操作

**See also:** 



---

### GetActiveSubCharge {#GetActiveSubCharge}

```
int GetActiveSubCharge ( ActiveSlot ActiveSlot = ActiveSlot.SLOT_PRIMARY )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetActiveSubCharge 完成对应 API 操作

**See also:** 



---

### GetActiveWeaponEntity {#GetActiveWeaponEntity}

```
Entity GetActiveWeaponEntity ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetActiveWeaponEntity 完成对应 API 操作

**See also:** 



---

### GetAimDirection {#GetAimDirection}

```
const Vector GetAimDirection ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetAimDirection 完成对应 API 操作

**See also:** 



---

### GetBabySkin {#GetBabySkin}

```
BabySubType GetBabySkin ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetBabySkin 完成对应 API 操作

**See also:** 



---

### GetBatteryCharge {#GetBatteryCharge}

```
int GetBatteryCharge ( ActiveSlot ActiveSlot = ActiveSlot.SLOT_PRIMARY )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetBatteryCharge 完成对应 API 操作

**See also:** 



---

### GetBlackHearts {#GetBlackHearts}

```
int GetBlackHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetBlackHearts 完成对应 API 操作

**See also:** 



---

### GetBloodCharge {#GetBloodCharge}

```
int GetBloodCharge ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetBloodCharge 完成对应 API 操作

**See also:** 



---

### GetBodyColor {#GetBodyColor}

```
SkinColor GetBodyColor ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetBodyColor 完成对应 API 操作

**See also:** 



---

### GetBombFlags {#GetBombFlags}

```
int GetBombFlags ( )
```

*DLC: AB+, REP, REP+*

[ ](#){: .reporplus .tooltip .badge }

[ ](#){: .reporplus .tooltip .badge }

**Use Cases:**

- 调用 GetBombFlags 完成对应 API 操作

**See also:** 



---

### int GetBombFlags ( boolean IsFetus = false ) {#int GetBombFlags ( boolean IsFetus = false )}

```
BombVariant GetBombVariant ( TearFlags TearFlags, boolean ForceSmallBomb )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 int GetBombFlags ( boolean IsFetus = false ) 完成对应 API 操作

**See also:** 



---

### GetBoneHearts {#GetBoneHearts}

```
int GetBoneHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetBoneHearts 完成对应 API 操作

**See also:** 



---

### GetBrokenHearts {#GetBrokenHearts}

```
int GetBrokenHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetBrokenHearts 完成对应 API 操作

**See also:** 



---

### GetCard {#GetCard}

```
Card GetCard ( int SlotId ) {: .copyable aria-label='Functions' data-altreturn='0' }
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetCard 完成对应 API 操作

**See also:** 



---

### GetCardRNG {#GetCardRNG}

```
RNG GetCardRNG ( Card ID )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetCardRNG 完成对应 API 操作

**See also:** 



---

### GetCollectibleCount {#GetCollectibleCount}

```
int GetCollectibleCount ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetCollectibleCount 完成对应 API 操作

**See also:** 



---

### GetCollectibleNum {#GetCollectibleNum}

```
int GetCollectibleNum ( CollectibleType Type, boolean OnlyCountTrueItems = false )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetCollectibleNum 完成对应 API 操作

**See also:** 



---

### GetCollectibleRNG {#GetCollectibleRNG}

```
RNG GetCollectibleRNG ( CollectibleType ID )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetCollectibleRNG 完成对应 API 操作

**See also:** 



---

### GetCostumeNullPos {#GetCostumeNullPos}

```
Vector GetCostumeNullPos ( string NullFrameName, boolean HeadScale, Vector Direction )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetCostumeNullPos 完成对应 API 操作

**See also:** 



---

### GetDamageCooldown {#GetDamageCooldown}

```
int GetDamageCooldown ( )
```

*DLC: AB+*

**Use Cases:**

- 调用 GetDamageCooldown 完成对应 API 操作

**See also:** 



---

### GetEffectiveBloodCharge {#GetEffectiveBloodCharge}

```
int GetEffectiveBloodCharge ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetEffectiveBloodCharge 完成对应 API 操作

**See also:** 



---

### GetEffectiveMaxHearts {#GetEffectiveMaxHearts}

```
int GetEffectiveMaxHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetEffectiveMaxHearts 完成对应 API 操作

**See also:** 



---

### GetEffectiveSoulCharge {#GetEffectiveSoulCharge}

```
int GetEffectiveSoulCharge ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetEffectiveSoulCharge 完成对应 API 操作

**See also:** 



---

### GetEffects {#GetEffects}

```
TemporaryEffects GetEffects ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetEffects 完成对应 API 操作

**See also:** 



---

### GetEternalHearts {#GetEternalHearts}

```
int GetEternalHearts ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetEternalHearts 完成对应 API 操作

**See also:** 



---

### GetExtraLives {#GetExtraLives}

```
int GetExtraLives ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetExtraLives 完成对应 API 操作

**See also:** 



---

### GetFireDirection {#GetFireDirection}

```
Direction GetFireDirection ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetFireDirection 完成对应 API 操作

**See also:** 



---

### GetFlyingOffset {#GetFlyingOffset}

```
Vector GetFlyingOffset ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetFlyingOffset 完成对应 API 操作

**See also:** 



---

### GetGoldenHearts {#GetGoldenHearts}

```
int GetGoldenHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetGoldenHearts 完成对应 API 操作

**See also:** 



---

### GetGreedDonationBreakChance {#GetGreedDonationBreakChance}

```
float GetGreedDonationBreakChance ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetGreedDonationBreakChance 完成对应 API 操作

**See also:** 



---

### GetHeadColor {#GetHeadColor}

```
SkinColor GetHeadColor ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetHeadColor 完成对应 API 操作

**See also:** 



---

### GetHeadDirection {#GetHeadDirection}

```
Direction GetHeadDirection ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetHeadDirection 完成对应 API 操作

**See also:** 



---

### GetHeartLimit {#GetHeartLimit}

```
int GetHeartLimit ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetHeartLimit 完成对应 API 操作

**See also:** 



---

### GetHearts {#GetHearts}

```
int GetHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetHearts 完成对应 API 操作

**See also:** 



---

### GetItemState {#GetItemState}

```
CollectibleType GetItemState ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetItemState 完成对应 API 操作

**See also:** 



---

### GetJarFlies {#GetJarFlies}

```
int GetJarFlies ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetJarFlies 完成对应 API 操作

**See also:** 



---

### GetJarHearts {#GetJarHearts}

```
int GetJarHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetJarHearts 完成对应 API 操作

**See also:** 



---

### GetLaserOffset {#GetLaserOffset}

```
Vector GetLaserOffset ( LaserOffset ID, Vector Direction )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetLaserOffset 完成对应 API 操作

**See also:** 



---

### GetLastActionTriggers {#GetLastActionTriggers}

```
int GetLastActionTriggers ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetLastActionTriggers 完成对应 API 操作

**See also:** 



---

### GetLastDamageFlags {#GetLastDamageFlags}

```
int GetLastDamageFlags ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetLastDamageFlags 完成对应 API 操作

**See also:** 



---

### GetLastDamageSource {#GetLastDamageSource}

```
const EntityRef GetLastDamageSource ( )
```

*Modifiers: const*

**Use Cases:**

- 调用 GetLastDamageSource 完成对应 API 操作

**See also:** 



---

### GetLastDirection {#GetLastDirection}

```
const Vector GetLastDirection ( )
```

*Modifiers: const*

**Use Cases:**

- 调用 GetLastDirection 完成对应 API 操作

**See also:** 



---

### GetMainTwin {#GetMainTwin}

```
EntityPlayer GetMainTwin ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetMainTwin 完成对应 API 操作

**See also:** 



---

### GetMaxHearts {#GetMaxHearts}

```
int GetMaxHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetMaxHearts 完成对应 API 操作

**See also:** 



---

### GetMaxPocketItems {#GetMaxPocketItems}

```
int GetMaxPocketItems ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetMaxPocketItems 完成对应 API 操作

**See also:** 



---

### GetMaxPoopMana {#GetMaxPoopMana}

```
int GetMaxPoopMana ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetMaxPoopMana 完成对应 API 操作

**See also:** 



---

### GetMaxTrinkets {#GetMaxTrinkets}

```
int GetMaxTrinkets ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetMaxTrinkets 完成对应 API 操作

**See also:** 



---

### GetModelingClayEffect {#GetModelingClayEffect}

```
CollectibleType GetModelingClayEffect ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetModelingClayEffect 完成对应 API 操作

**See also:** 



---

### GetMovementDirection {#GetMovementDirection}

```
Direction GetMovementDirection ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetMovementDirection 完成对应 API 操作

**See also:** 



---

### GetMovementInput {#GetMovementInput}

```
const Vector GetMovementInput ( )
```

*Modifiers: const*

**Use Cases:**

- 调用 GetMovementInput 完成对应 API 操作

**See also:** 



---

### GetMovementJoystick {#GetMovementJoystick}

```
Vector GetMovementJoystick ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetMovementJoystick 完成对应 API 操作

**See also:** 



---

### GetMovementVector {#GetMovementVector}

```
Vector GetMovementVector ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetMovementVector 完成对应 API 操作

**See also:** 



---

### GetMultiShotParams {#GetMultiShotParams}

```
MultiShotParams GetMultiShotParams ( WeaponType WeaponType = WeaponType.WEAPON_TEARS )
```

*DLC: REP*

**Use Cases:**

- 调用 GetMultiShotParams 完成对应 API 操作

**See also:** 



---

### GetMultiShotPositionVelocity {#GetMultiShotPositionVelocity}

```
PosVel GetMultiShotPositionVelocity ( int LoopIndex, WeaponType Weapon, Vector ShotDirection, float ShotSpeed, MultiShotParams params )
```

*DLC: AB+, REP*

**Use Cases:**

- 调用 GetMultiShotPositionVelocity 完成对应 API 操作

**See also:** 



---

### GetName {#GetName}

```
string GetName ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetName 完成对应 API 操作

**See also:** 



---

### GetNPCTarget {#GetNPCTarget}

```
Entity GetNPCTarget ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetNPCTarget 完成对应 API 操作

**See also:** 



---

### GetNumBlueFlies {#GetNumBlueFlies}

```
int GetNumBlueFlies ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetNumBlueFlies 完成对应 API 操作

**See also:** 



---

### GetNumBlueSpiders {#GetNumBlueSpiders}

```
int GetNumBlueSpiders ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetNumBlueSpiders 完成对应 API 操作

**See also:** 



---

### GetNumBombs {#GetNumBombs}

```
int GetNumBombs ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetNumBombs 完成对应 API 操作

**See also:** 



---

### GetNumCoins {#GetNumCoins}

```
int GetNumCoins ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetNumCoins 完成对应 API 操作

**See also:** 



---

### GetNumGigaBombs {#GetNumGigaBombs}

```
int GetNumGigaBombs ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetNumGigaBombs 完成对应 API 操作

**See also:** 



---

### GetNumKeys {#GetNumKeys}

```
int GetNumKeys ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetNumKeys 完成对应 API 操作

**See also:** 



---

### GetOtherTwin {#GetOtherTwin}

```
EntityPlayer GetOtherTwin ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetOtherTwin 完成对应 API 操作

**See also:** 



---

### GetPill {#GetPill}

```
PillColor GetPill ( int SlotId ) {: .copyable aria-label='Functions' data-altreturn='0' }
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetPill 完成对应 API 操作

**See also:** 



---

### GetPillRNG {#GetPillRNG}

```
RNG GetPillRNG ( PillEffect ID )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetPillRNG 完成对应 API 操作

**See also:** 



---

### GetPlayerType {#GetPlayerType}

```
PlayerType GetPlayerType ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetPlayerType 完成对应 API 操作

**See also:** 



---

### GetPocketItem {#GetPocketItem}

```
const PlayerPocketItem GetPocketItem ( int SlotId )
```

*Modifiers: const*

**Use Cases:**

- 调用 GetPocketItem 完成对应 API 操作

**See also:** 



---

### GetPoopMana {#GetPoopMana}

```
int GetPoopMana ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetPoopMana 完成对应 API 操作

**See also:** 



---

### GetPoopSpell {#GetPoopSpell}

```
PoopSpellType GetPoopSpell ( int Position )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetPoopSpell 完成对应 API 操作

**See also:** 



---

### GetRecentMovementVector {#GetRecentMovementVector}

```
const Vector GetRecentMovementVector ( )
```

*Modifiers: const*

**Use Cases:**

- 调用 GetRecentMovementVector 完成对应 API 操作

**See also:** 



---

### GetRottenHearts {#GetRottenHearts}

```
int GetRottenHearts ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetRottenHearts 完成对应 API 操作

**See also:** 



---

### GetShootingInput {#GetShootingInput}

```
Vector GetShootingInput ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetShootingInput 完成对应 API 操作

**See also:** 



---

### GetShootingJoystick {#GetShootingJoystick}

```
Vector GetShootingJoystick ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetShootingJoystick 完成对应 API 操作

**See also:** 



---

### GetSmoothBodyRotation {#GetSmoothBodyRotation}

```
float GetSmoothBodyRotation ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetSmoothBodyRotation 完成对应 API 操作

**See also:** 



---

### GetSoulCharge {#GetSoulCharge}

```
int GetSoulCharge ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetSoulCharge 完成对应 API 操作

**See also:** 



---

### GetSoulHearts {#GetSoulHearts}

```
int GetSoulHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetSoulHearts 完成对应 API 操作

**See also:** 



---

### GetSubPlayer {#GetSubPlayer}

```
EntityPlayer GetSubPlayer ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetSubPlayer 完成对应 API 操作

**See also:** 



---

### GetTearHitParams {#GetTearHitParams}

```
TearParams GetTearHitParams ( WeaponType WeaponType, float DamageScale = 1, int TearDisplacement = 1, Entity Source = nil )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 GetTearHitParams 完成对应 API 操作

**See also:** 



---

### GetTearMovementInheritance {#GetTearMovementInheritance}

```
Vector GetTearMovementInheritance ( Vector ShotDirection )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetTearMovementInheritance 完成对应 API 操作

**See also:** 



---

### GetTearPoisonDamage {#GetTearPoisonDamage}

```
float GetTearPoisonDamage ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetTearPoisonDamage 完成对应 API 操作

**See also:** 



---

### GetTearRangeModifier {#GetTearRangeModifier}

```
int GetTearRangeModifier ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetTearRangeModifier 完成对应 API 操作

**See also:** 



---

### GetTotalDamageTaken {#GetTotalDamageTaken}

```
int GetTotalDamageTaken ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetTotalDamageTaken 完成对应 API 操作

**See also:** 



---

### GetTractorBeam {#GetTractorBeam}

```
Entity GetTractorBeam ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetTractorBeam 完成对应 API 操作

**See also:** 



---

### GetTrinket {#GetTrinket}

```
TrinketType GetTrinket ( int TrinketIndex ) {: .copyable aria-label='Functions' data-altreturn='0' }
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetTrinket 完成对应 API 操作

**See also:** 



---

### GetTrinketMultiplier {#GetTrinketMultiplier}

```
int GetTrinketMultiplier ( TrinketType TrinketID )
```

*DLC: AB+, REP, REP+*

Gets the multiplier of a given Trinket effect. This is analog to the number of times the trinket effect is applied.

Gets the multiplier of a given Trinket effect. This is analog to the number of times the trinket effect is applied.

**Use Cases:**

- 调用 GetTrinketMultiplier 完成对应 API 操作

**See also:** 



---

### GetTrinketRNG {#GetTrinketRNG}

```
RNG GetTrinketRNG ( TrinketType TrinketID )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetTrinketRNG 完成对应 API 操作

**See also:** 



---

### GetVelocityBeforeUpdate {#GetVelocityBeforeUpdate}

```
const Vector GetVelocityBeforeUpdate ( )
```

*Modifiers: const*

**Use Cases:**

- 调用 GetVelocityBeforeUpdate 完成对应 API 操作

**See also:** 



---

### GetZodiacEffect {#GetZodiacEffect}

```
CollectibleType GetZodiacEffect ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetZodiacEffect 完成对应 API 操作

**See also:** 



---

### HasCollectible {#HasCollectible}

```
boolean HasCollectible ( CollectibleType Type, boolean IgnoreModifiers = false )
```

*DLC: REP, REP+*

**IgnoreModifiers**: If set to true, only counts collectibles the player actually owns and ignores effects granted by items like Zodiac, 3 Dollar Bill and Lemegeton

**IgnoreModifiers**: If set to true, only counts collectibles the player actually owns and ignores effects granted by items like Zodiac, 3 Dollar Bill and Lemegeton

**Use Cases:**

- 调用 HasCollectible 完成对应 API 操作

**See also:** 



---

### HasCurseMistEffect {#HasCurseMistEffect}

```
boolean HasCurseMistEffect ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 HasCurseMistEffect 完成对应 API 操作

**See also:** 



---

### HasFullHearts {#HasFullHearts}

```
boolean HasFullHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 HasFullHearts 完成对应 API 操作

**See also:** 



---

### HasFullHeartsAndSoulHearts {#HasFullHeartsAndSoulHearts}

```
boolean HasFullHeartsAndSoulHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 HasFullHeartsAndSoulHearts 完成对应 API 操作

**See also:** 



---

### HasGoldenBomb {#HasGoldenBomb}

```
boolean HasGoldenBomb ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 HasGoldenBomb 完成对应 API 操作

**See also:** 



---

### HasGoldenKey {#HasGoldenKey}

```
boolean HasGoldenKey ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 HasGoldenKey 完成对应 API 操作

**See also:** 



---

### HasInvincibility {#HasInvincibility}

```
boolean HasInvincibility ( DamageFlag Flags = 0 )
```

*DLC: REP, REP+*

returns true when player is in an invincibility state

returns true when player is in an invincibility state

**Use Cases:**

- 调用 HasInvincibility 完成对应 API 操作

**See also:** 



---

### HasPlayerForm {#HasPlayerForm}

```
boolean HasPlayerForm ( PlayerForm Form )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 HasPlayerForm 完成对应 API 操作

**See also:** 



---

### HasTimedItem {#HasTimedItem}

```
boolean HasTimedItem ( )
```

*DLC: AB+, REP, REP+*

Returns true if you have a timed active item *(such as Brown Nugget)* in the first active slot

Returns true if you have a timed active item *(such as Brown Nugget)* in the first active slot

**Use Cases:**

- 调用 HasTimedItem 完成对应 API 操作

**See also:** 



---

### HasTrinket {#HasTrinket}

```
boolean HasTrinket ( TrinketType Type, boolean IgnoreModifiers = false )
```

*DLC: REP, REP+*

**IgnoreModifiers**: If set to true, only counts trinkets the player actually holds and ignores effects granted by other items

**IgnoreModifiers**: If set to true, only counts trinkets the player actually holds and ignores effects granted by other items

**Use Cases:**

- 调用 HasTrinket 完成对应 API 操作

**See also:** 



---

### HasWeaponType {#HasWeaponType}

```
boolean HasWeaponType ( WeaponType WeaponType )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 HasWeaponType 完成对应 API 操作

**See also:** 



---

### InitBabySkin {#InitBabySkin}

```
void InitBabySkin ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 InitBabySkin 完成对应 API 操作

**See also:** 



---

### IsBlackHeart {#IsBlackHeart}

```
boolean IsBlackHeart ( int Heart )
```

*DLC: AB+, REP, REP+*

This can be used instead of GetBlackHearts to figure out which soul hearts are black hearts.

This can be used instead of GetBlackHearts to figure out which soul hearts are black hearts.

**Use Cases:**

- 调用 IsBlackHeart 完成对应 API 操作

**See also:** 



---

### IsBoneHeart {#IsBoneHeart}

```
boolean IsBoneHeart ( int heart )
```

*DLC: AB+, REP, REP+*

This can be used to figure out the ordering of bone hearts amongst soul/black hearts.

This can be used to figure out the ordering of bone hearts amongst soul/black hearts.

**Use Cases:**

- 调用 IsBoneHeart 完成对应 API 操作

**See also:** 



---

### IsCoopGhost {#IsCoopGhost}

```
boolean IsCoopGhost ( )
```

*DLC: REP, REP+*

In a multiplayer game, if a player dies, they will return as a tiny ghost. This method returns true if the player is a co-op ghost.

In a multiplayer game, if a player dies, they will return as a tiny ghost. This method returns true if the player is a co-op ghost.

**Use Cases:**

- 调用 IsCoopGhost 完成对应 API 操作

**See also:** 



---

### IsExtraAnimationFinished {#IsExtraAnimationFinished}

```
boolean IsExtraAnimationFinished ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 IsExtraAnimationFinished 完成对应 API 操作

**See also:** 



---

### IsFullSpriteRendering {#IsFullSpriteRendering}

```
boolean IsFullSpriteRendering ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 IsFullSpriteRendering 完成对应 API 操作

**See also:** 



---

### IsHeldItemVisible {#IsHeldItemVisible}

```
boolean IsHeldItemVisible ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 IsHeldItemVisible 完成对应 API 操作

**See also:** 



---

### IsHoldingItem {#IsHoldingItem}

```
boolean IsHoldingItem ( )
```

*DLC: AB+, REP, REP+*

Is Player holding up an item (card/collectible/etc)

Is Player holding up an item (card/collectible/etc)

**Use Cases:**

- 调用 IsHoldingItem 完成对应 API 操作

**See also:** 



---

### IsItemQueueEmpty {#IsItemQueueEmpty}

```
boolean IsItemQueueEmpty ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 IsItemQueueEmpty 完成对应 API 操作

**See also:** 



---

### IsP2Appearing {#IsP2Appearing}

```
boolean IsP2Appearing ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 IsP2Appearing 完成对应 API 操作

**See also:** 



---

### IsPosInSpotLight {#IsPosInSpotLight}

```
boolean IsPosInSpotLight ( Vector Position )
```

*DLC: AB+, REP, REP+*

Returns true if the `position` is in the AOE of the **Night Light** item.

Returns true if the `position` is in the AOE of the **Night Light** item.

**Use Cases:**

- 调用 IsPosInSpotLight 完成对应 API 操作

**See also:** 



---

### IsSubPlayer {#IsSubPlayer}

```
boolean IsSubPlayer ( )
```

*DLC: AB+, REP, REP+*

Returns true if the player object was returned from the `EntityPlayer.GetSubPlayer` method. (This method is not related to multiplayer.)

Returns true if the player object was returned from the `EntityPlayer.GetSubPlayer` method. (This method is not related to multiplayer.)

**Use Cases:**

- 调用 IsSubPlayer 完成对应 API 操作

**See also:** 



---

### NeedsCharge {#NeedsCharge}

```
boolean NeedsCharge ( ActiveSlot ActiveSlot = ActiveSlot.SLOT_PRIMARY )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 NeedsCharge 完成对应 API 操作

**See also:** 



---

### PlayExtraAnimation {#PlayExtraAnimation}

```
void PlayExtraAnimation ( string Animation )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 PlayExtraAnimation 完成对应 API 操作

**See also:** 



---

### QueueExtraAnimation {#QueueExtraAnimation}

```
void QueueExtraAnimation ( string Animation )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 QueueExtraAnimation 完成对应 API 操作

**See also:** 



---

### QueueItem {#QueueItem}

```
void QueueItem ( ItemConfigItem Item, int Charge = 0, boolean Touched = false, boolean Golden = false, int VarData = 0 )
```

*DLC: REP, REP+*

When the player touches a collectible or trinket, they are not granted it immediately. Instead, the item is queued for the duration of the animation where the player holds the item above their head. When the animation is finished, the item in the queue will be granted. This method adds a new item to the item queue. If the player is not currently playing an animation, then the queued item will simply be awarded instantly.

When the player touches a collectible or trinket, they are not granted it immediately. Instead, the item is queued for the duration of the animation where the player holds the item above their head. When the animation is finished, the item in the queue will be granted. This method adds a new item to the item queue. If the player is not currently playing an animation, then the queued item will simply be awarded instantly.

**Use Cases:**

- 调用 QueueItem 完成对应 API 操作

**See also:** 



---

### RemoveBlackHeart {#RemoveBlackHeart}

```
void RemoveBlackHeart ( int BlackHeart )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RemoveBlackHeart 完成对应 API 操作

**See also:** 



---

### RemoveBlueFly {#RemoveBlueFly}

```
void RemoveBlueFly ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RemoveBlueFly 完成对应 API 操作

**See also:** 



---

### RemoveBlueSpider {#RemoveBlueSpider}

```
void RemoveBlueSpider ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RemoveBlueSpider 完成对应 API 操作

**See also:** 



---

### RemoveCollectible {#RemoveCollectible}

```
void RemoveCollectible ( CollectibleType Type, boolean IgnoreModifiers = false, ActiveSlot ActiveSlot = ActiveSlot.SLOT_PRIMARY, boolean RemoveFromPlayerForm = true )
```

*DLC: REP, REP+*

**IgnoreModifiers**: Ignores collectible effects granted by other items (i.e. Void)

**IgnoreModifiers**: Ignores collectible effects granted by other items (i.e. Void)

**Use Cases:**

- 调用 RemoveCollectible 完成对应 API 操作

**See also:** 



---

### RemoveCostume {#RemoveCostume}

```
void RemoveCostume ( ItemConfigItem Item )
```

*DLC: AB+, REP, REP+*

Removes a given costume based on its item config entry.

Removes a given costume based on its item config entry.

**Use Cases:**

- 调用 RemoveCostume 完成对应 API 操作

**See also:** 



---

### RemoveCurseMistEffect {#RemoveCurseMistEffect}

```
void RemoveCurseMistEffect ( )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 RemoveCurseMistEffect 完成对应 API 操作

**See also:** 



---

### RemoveGoldenBomb {#RemoveGoldenBomb}

```
void RemoveGoldenBomb ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RemoveGoldenBomb 完成对应 API 操作

**See also:** 



---

### RemoveGoldenKey {#RemoveGoldenKey}

```
void RemoveGoldenKey ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RemoveGoldenKey 完成对应 API 操作

**See also:** 



---

### RemoveSkinCostume {#RemoveSkinCostume}

```
void RemoveSkinCostume ( )
```

*DLC: AB+, REP, REP+*

Removes player-specific costumes like Magdalene's hair or Cain's eyepatch.

Removes player-specific costumes like Magdalene's hair or Cain's eyepatch.

**Use Cases:**

- 调用 RemoveSkinCostume 完成对应 API 操作

**See also:** 



---

### RenderBody {#RenderBody}

```
void RenderBody ( Vector position )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RenderBody 完成对应 API 操作

**See also:** 



---

### RenderGlow {#RenderGlow}

```
void RenderGlow ( Vector position )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RenderGlow 完成对应 API 操作

**See also:** 



---

### RenderHead {#RenderHead}

```
void RenderHead ( Vector position )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RenderHead 完成对应 API 操作

**See also:** 



---

### RenderTop {#RenderTop}

```
void RenderTop ( Vector position )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RenderTop 完成对应 API 操作

**See also:** 



---

### ReplaceCostumeSprite {#ReplaceCostumeSprite}

```
void ReplaceCostumeSprite ( ItemConfigItem Item, string SpritePath, int SpriteId )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 ReplaceCostumeSprite 完成对应 API 操作

**See also:** 



---

### ResetDamageCooldown {#ResetDamageCooldown}

```
void ResetDamageCooldown ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 ResetDamageCooldown 完成对应 API 操作

**See also:** 



---

### ResetItemState {#ResetItemState}

```
void ResetItemState ( )
```

*DLC: AB+, REP, REP+*

[Room](Room.md) transitions call this to prevent lock ups.

[Room](Room.md) transitions call this to prevent lock ups.

**Use Cases:**

- 调用 ResetItemState 完成对应 API 操作

**See also:** 



---

### RespawnFamiliars {#RespawnFamiliars}

```
void RespawnFamiliars ( )
```

*DLC: AB+, REP, REP+*

Respawns all familiars associated to the player.

Respawns all familiars associated to the player.

**Use Cases:**

- 调用 RespawnFamiliars 完成对应 API 操作

**See also:** 



---

### Revive {#Revive}

```
void Revive ( )
```

*DLC: AB+, REP, REP+*

Revives the player.

Revives the player.

**Use Cases:**

- 调用 Revive 完成对应 API 操作

**See also:** 



---

### SetActiveCharge {#SetActiveCharge}

```
void SetActiveCharge ( int Charge, ActiveSlot ActiveSlot = ActiveSlot.SLOT_PRIMARY )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 SetActiveCharge 完成对应 API 操作

**See also:** 



---

### SetBloodCharge {#SetBloodCharge}

```
void SetBloodCharge ( int Amount )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 SetBloodCharge 完成对应 API 操作

**See also:** 



---

### SetCard {#SetCard}

```
void SetCard ( int SlotId, Card ID )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SetCard 完成对应 API 操作

**See also:** 



---

### SetFullHearts {#SetFullHearts}

```
void SetFullHearts ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SetFullHearts 完成对应 API 操作

**See also:** 



---

### SetMinDamageCooldown {#SetMinDamageCooldown}

```
void SetMinDamageCooldown ( int DamageCooldown )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SetMinDamageCooldown 完成对应 API 操作

**See also:** 



---

### SetPill {#SetPill}

```
void SetPill ( int SlotId, PillColor Pill )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SetPill 完成对应 API 操作

**See also:** 



---

### SetPocketActiveItem {#SetPocketActiveItem}

```
void SetPocketActiveItem ( CollectibleType Type, ActiveSlot Slot, boolean KeepInPools )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 SetPocketActiveItem 完成对应 API 操作

**See also:** 



---

### SetShootingCooldown {#SetShootingCooldown}

```
void SetShootingCooldown ( int Cooldown )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SetShootingCooldown 完成对应 API 操作

**See also:** 



---

### SetSoulCharge {#SetSoulCharge}

```
void SetSoulCharge ( int Amount )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 SetSoulCharge 完成对应 API 操作

**See also:** 



---

### SetTargetTrapDoor {#SetTargetTrapDoor}

```
void SetTargetTrapDoor ( GridEntity TrapDoor )
```

*DLC: AB+*

**Use Cases:**

- 调用 SetTargetTrapDoor 完成对应 API 操作

**See also:** 



---

### ShootRedCandle {#ShootRedCandle}

```
void ShootRedCandle ( Vector Direction )
```

*DLC: AB+, REP, REP+*

for ghost pepper item + poop and farts

for ghost pepper item + poop and farts

**Use Cases:**

- 调用 ShootRedCandle 完成对应 API 操作

**See also:** 



---

### SpawnMawOfVoid {#SpawnMawOfVoid}

```
EntityLaser SpawnMawOfVoid ( int Timeout )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SpawnMawOfVoid 完成对应 API 操作

**See also:** 



---

### StopExtraAnimation {#StopExtraAnimation}

```
void StopExtraAnimation ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 StopExtraAnimation 完成对应 API 操作

**See also:** 



---

### SwapActiveItems {#SwapActiveItems}

```
void SwapActiveItems ( )
```

*DLC: AB+, REP, REP+*

Swaps active items in the **Schoolbag** activeslot

Swaps active items in the **Schoolbag** activeslot

**Use Cases:**

- 调用 SwapActiveItems 完成对应 API 操作

**See also:** 



---

### ThrowBlueSpider {#ThrowBlueSpider}

```
Entity ThrowBlueSpider ( Vector Position, Vector Target )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 ThrowBlueSpider 完成对应 API 操作

**See also:** 



---

### ThrowFriendlyDip {#ThrowFriendlyDip}

```
EntityFamiliar ThrowFriendlyDip ( int Subtype, Vector Position, Vector Target )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 ThrowFriendlyDip 完成对应 API 操作

**See also:** 



---

### ThrowHeldEntity {#ThrowHeldEntity}

```
Entity ThrowHeldEntity ( Vector Velocity )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 ThrowHeldEntity 完成对应 API 操作

**See also:** 



---

### TriggerBookOfVirtues {#TriggerBookOfVirtues}

```
void TriggerBookOfVirtues ( CollectibleType Type = CollectibleType.COLLECTIBLE_NULL, int Charge = 0 )
```

*DLC: REP, REP+*

Works only if the player has the **Book of Virtues** item, otherwise does nothing

Works only if the player has the **Book of Virtues** item, otherwise does nothing

**Use Cases:**

- 调用 TriggerBookOfVirtues 完成对应 API 操作

**See also:** 



---

### TryHoldEntity {#TryHoldEntity}

```
boolean TryHoldEntity ( Entity Entity )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 TryHoldEntity 完成对应 API 操作

**See also:** 



---

### TryHoldTrinket {#TryHoldTrinket}

```
boolean TryHoldTrinket ( TrinketType Type )
```

*DLC: AB+, REP, REP+*

Returns true if an active item pickup cooldown is over. returns true if trinket can be added, else false

Returns true if an active item pickup cooldown is over. returns true if trinket can be added, else false

**Use Cases:**

- 调用 TryHoldTrinket 完成对应 API 操作

**See also:** 



---

### TryRemoveCollectibleCostume {#TryRemoveCollectibleCostume}

```
void TryRemoveCollectibleCostume ( CollectibleType Collectible, boolean KeepPersistent )
```

*DLC: AB+, REP, REP+*

Tries to remove a costume of the given collectible. `KeepPersistent` is used to define if persistent costumes should be removed. If its set to `false`, it will only remove temporary costumes.

Tries to remove a costume of the given collectible. `KeepPersistent` is used to define if persistent costumes should be removed. If its set to `false`, it will only remove temporary costumes.

**Use Cases:**

- 调用 TryRemoveCollectibleCostume 完成对应 API 操作

**See also:** 



---

### TryRemoveNullCostume {#TryRemoveNullCostume}

```
void TryRemoveNullCostume ( NullItemID NullId )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 TryRemoveNullCostume 完成对应 API 操作

**See also:** 



---

### TryRemoveTrinket {#TryRemoveTrinket}

```
boolean TryRemoveTrinket ( TrinketType Type )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 TryRemoveTrinket 完成对应 API 操作

**See also:** 



---

### TryRemoveTrinketCostume {#TryRemoveTrinketCostume}

```
void TryRemoveTrinketCostume ( TrinketType Trinket )
```

*DLC: AB+, REP, REP+*

Tries to remove a trinket costume

Tries to remove a trinket costume

**Use Cases:**

- 调用 TryRemoveTrinketCostume 完成对应 API 操作

**See also:** 



---

### TryUseKey {#TryUseKey}

```
boolean TryUseKey ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 TryUseKey 完成对应 API 操作

**See also:** 



---

### UpdateCanShoot {#UpdateCanShoot}

```
void UpdateCanShoot ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 UpdateCanShoot 完成对应 API 操作

**See also:** 



---

### UseActiveItem {#UseActiveItem}

```
void UseActiveItem ( CollectibleType Item, UseFlags UseFlags = 0, ActiveSlot Slot = -1, int CustomVarData = 0 )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 UseActiveItem 完成对应 API 操作

**See also:** 



---

### void UseActiveItem ( [CollectibleType](enums/CollectibleType.md) Item, boolean ShowAnim = false, boolean KeepActiveItem = false, boolean AllowNonMainPlayer = true, boolean ToAddCostume = false, [ActiveSlot](enums/ActiveSlot.md) Slot = -1, int CustomVarData = 0 ) {#void UseActiveItem ( [CollectibleType](enums/CollectibleType.md) Item, boolean ShowAnim = false, boolean KeepActiveItem = false, boolean AllowNonMainPlayer = true, boolean ToAddCostume = false, [ActiveSlot](enums/ActiveSlot.md) Slot = -1, int CustomVarData = 0 )}

```
void UseCard ( Card ID, UseFlags UseFlags = 0 )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 void UseActiveItem ( [CollectibleType](enums/CollectibleType.md) Item, boolean ShowAnim = false, boolean KeepActiveItem = false, boolean AllowNonMainPlayer = true, boolean ToAddCostume = false, [ActiveSlot](enums/ActiveSlot.md) Slot = -1, int CustomVarData = 0 ) 完成对应 API 操作

**See also:** 



---

### UsePill {#UsePill}

```
void UsePill ( PillEffect ID, PillColor PillColor, UseFlags UseFlags = 0 )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 UsePill 完成对应 API 操作

**See also:** 



---

### UsePoopSpell {#UsePoopSpell}

```
void UsePoopSpell ( PoopSpellType type )
```

*DLC: REP, REP+*

Triggers one of Tainted ???'s poop spells (see [PoopSpellType](enums/PoopSpellType.md) enum)

Triggers one of Tainted ???'s poop spells (see [PoopSpellType](enums/PoopSpellType.md) enum)

**Use Cases:**

- 调用 UsePoopSpell 完成对应 API 操作

**See also:** 



---

### WillPlayerRevive {#WillPlayerRevive}

```
boolean WillPlayerRevive ( )
```

*DLC: AB+, REP, REP+*

This function will return true if the player has one or more extra lives or if a conditional revival item will work on the next death.

This function will return true if the player has one or more extra lives or if a conditional revival item will work on the next death.

**Use Cases:**

- 调用 WillPlayerRevive 完成对应 API 操作

**See also:** 



---

### BabySkin {#BabySkin}

```
BabySubType BabySkin
```

*DLC: AB+, REP, REP+*

P2 Skin section Used to hold the selected skin (in case of glitched baby it will pick a random one)

P2 Skin section Used to hold the selected skin (in case of glitched baby it will pick a random one)

**Use Cases:**

- 调用 BabySkin 完成对应 API 操作

**See also:** 



---

### CanFly {#CanFly}

```
boolean CanFly
```

*DLC: AB+, REP, REP+*

Player stat - Only change this in a callback to MC_EVALUATE_CACHE. Can the player fly over rocks and pits?

Player stat - Only change this in a callback to MC_EVALUATE_CACHE. Can the player fly over rocks and pits?

**Use Cases:**

- 调用 CanFly 完成对应 API 操作

**See also:** 



---

### ControllerIndex {#ControllerIndex}

```
const int ControllerIndex
```

*Modifiers: const*

**Use Cases:**

- 调用 ControllerIndex 完成对应 API 操作

**See also:** 



---

### ControlsCooldown {#ControlsCooldown}

```
int ControlsCooldown
```

*DLC: AB+, REP, REP+*

Specifies the number of frames the player's controls should be disabled. Decrements by 1 every frame, until it reaches 0. Used by the paralysis pill effect.

Specifies the number of frames the player's controls should be disabled. Decrements by 1 every frame, until it reaches 0. Used by the paralysis pill effect.

**Use Cases:**

- 调用 ControlsCooldown 完成对应 API 操作

**See also:** 



---

### ControlsEnabled {#ControlsEnabled}

```
boolean ControlsEnabled
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 ControlsEnabled 完成对应 API 操作

**See also:** 



---

### Damage {#Damage}

```
float Damage
```

*DLC: AB+, REP, REP+*

Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Damage Stat.**  How much damage do the players tears or other main weapons do?

Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Damage Stat.**  How much damage do the players tears or other main weapons do?

**Use Cases:**

- 调用 Damage 完成对应 API 操作

**See also:** 



---

### FireDelay {#FireDelay}

```
float FireDelay
```

*DLC: AB+, REP, REP+*

How long until the player can spawn their next tear?

How long until the player can spawn their next tear?

**Use Cases:**

- 调用 FireDelay 完成对应 API 操作

**See also:** 



---

### FriendBallEnemy {#FriendBallEnemy}

```
const EntityDesc FriendBallEnemy
```

*Modifiers: const*

**Use Cases:**

- 调用 FriendBallEnemy 完成对应 API 操作

**See also:** 



---

### HeadFrameDelay {#HeadFrameDelay}

```
int HeadFrameDelay
```

*DLC: AB+, REP, REP+*

Specifies the number of frames the player's head should be playing the shooting animation. Decrements by 1 every frame, until it reaches -1.

Specifies the number of frames the player's head should be playing the shooting animation. Decrements by 1 every frame, until it reaches -1.

**Use Cases:**

- 调用 HeadFrameDelay 完成对应 API 操作

**See also:** 



---

### IBSCharge {#IBSCharge}

```
float IBSCharge
```

*DLC: REP, REP+*

Internally used by IBS, increases based on damage dealt, range is 0-1

Internally used by IBS, increases based on damage dealt, range is 0-1

**Use Cases:**

- 调用 IBSCharge 完成对应 API 操作

**See also:** 



---

### ItemHoldCooldown {#ItemHoldCooldown}

```
int ItemHoldCooldown
```

*DLC: AB+, REP, REP+*

Used for avoiding player get stucked between rocks when switching a flying item with other active item.

Used for avoiding player get stucked between rocks when switching a flying item with other active item.

**Use Cases:**

- 调用 ItemHoldCooldown 完成对应 API 操作

**See also:** 



---

### LaserColor {#LaserColor}

```
Color LaserColor
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 LaserColor 完成对应 API 操作

**See also:** 



---

### Luck {#Luck}

```
float Luck
```

*DLC: AB+, REP, REP+*

Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Luck Stat.**  Better luck generally means better random events.

Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Luck Stat.**  Better luck generally means better random events.

**Use Cases:**

- 调用 Luck 完成对应 API 操作

**See also:** 



---

### MaxFireDelay {#MaxFireDelay}

```
float MaxFireDelay
```

*DLC: AB+, REP, REP+*

Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Tears Stat.**  How long between each tear can spawn?

Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Tears Stat.**  How long between each tear can spawn?

**Use Cases:**

- 调用 MaxFireDelay 完成对应 API 操作

**See also:** 



---

### MoveSpeed {#MoveSpeed}

```
float MoveSpeed
```

*DLC: AB+, REP, REP+*

Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Speed Stat.**  How fast can the player move?

Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Speed Stat.**  How fast can the player move?

**Use Cases:**

- 调用 MoveSpeed 完成对应 API 操作

**See also:** 



---

### QueuedItem {#QueuedItem}

```
QueueItemData QueuedItem
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 QueuedItem 完成对应 API 操作

**See also:** 



---

### SamsonBerserkCharge {#SamsonBerserkCharge}

```
int SamsonBerserkCharge
```

*DLC: REP, REP+*

Internally used by Tainted Samson, increases based on damage dealt, range is 0-100000

Internally used by Tainted Samson, increases based on damage dealt, range is 0-100000

**Use Cases:**

- 调用 SamsonBerserkCharge 完成对应 API 操作

**See also:** 



---

### SecondaryActiveItem {#SecondaryActiveItem}

```
ActiveItemDesc SecondaryActiveItem {: .copyable aria-label='Variables' data-altreturn='nil' }
```

*DLC: AB+*

**Use Cases:**

- 调用 SecondaryActiveItem 完成对应 API 操作

**See also:** 



---

### ShotSpeed {#ShotSpeed}

```
float ShotSpeed
```

*DLC: AB+, REP, REP+*

Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the ShotSpeed Stat.**

Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the ShotSpeed Stat.**

**Use Cases:**

- 调用 ShotSpeed 完成对应 API 操作

**See also:** 



---

### TearColor {#TearColor}

```
Color TearColor
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 TearColor 完成对应 API 操作

**See also:** 



---

### TearFallingAcceleration {#TearFallingAcceleration}

```
float TearFallingAcceleration
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 TearFallingAcceleration 完成对应 API 操作

**See also:** 



---

### TearFallingSpeed {#TearFallingSpeed}

```
float TearFallingSpeed
```

*DLC: AB+, REP, REP+*

Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How fast is the tear moving up or down when it spawns? Affects range.

Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How fast is the tear moving up or down when it spawns? Affects range.

**Use Cases:**

- 调用 TearFallingSpeed 完成对应 API 操作

**See also:** 



---

### TearFlags {#TearFlags}

```
TearFlags TearFlags
```

*DLC: AB+, REP, REP+*

Player stat - Only change this in a callback to MC_EVALUATE_CACHE. Various [TearFlags](enums/TearFlags.md).

Player stat - Only change this in a callback to MC_EVALUATE_CACHE. Various [TearFlags](enums/TearFlags.md).

**Use Cases:**

- 调用 TearFlags 完成对应 API 操作

**See also:** 



---

### TearHeight {#TearHeight}

```
float TearHeight
```

*DLC: AB+, REP, REP+*

Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How high above the ground is the tear when it spawns?

Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How high above the ground is the tear when it spawns?

**Use Cases:**

- 调用 TearHeight 完成对应 API 操作

**See also:** 



---

### TearRange {#TearRange}

```
float TearRange
```

*DLC: REP, REP+*

Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How far should a tear go when it spawns?

Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How far should a tear go when it spawns?

**Use Cases:**

- 调用 TearRange 完成对应 API 操作

**See also:** 



---

### TearsOffset {#TearsOffset}

```
Vector TearsOffset
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 TearsOffset 完成对应 API 操作

**See also:** 



---

## See Also

- [[Color]]
- [[Entity]]
- [[EntityBomb]]
- [[EntityFamiliar]]
- [[EntityKnife]]
- [[EntityLaser]]
- [[EntityPlayer]]
- [[EntityRef]]
- [[EntityTear]]
- [[GridEntity]]
- [[Input]]
- [[ItemConfig]]
- [[ItemConfigItem]]
- [[QueueItemData]]
- [[RNG]]
- [[Room]]
- [[Sprite]]
- [[TearParams]]
- [[TemporaryEffect]]
- [[TemporaryEffects]]
- [[Vector]]
