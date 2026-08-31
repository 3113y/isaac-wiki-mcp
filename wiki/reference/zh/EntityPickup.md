---
tags:
  - Class
---
# Class "EntityPickup"

???+ info

    你可以通过以下函数获取此类：

    * [Entity.ToPickup()](Entity.md#topickup)

    ???+ example "Example Code"
        `local entity = Isaac.GetRoomEntities()[1]:ToPickup()`

## Class Diagram
--8<-- "zh/snippets/EntityClassDiagram.md"
## Functions

### Appear·Fast () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AppearFast ( ) {: .copyable aria-label='Functions' }

___

### Can·Reroll () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanReroll ( ) {: .copyable aria-label='Functions' }

___

<div class="rgon-extension" markdown="1">

### CanReroll () {: aria-label='Functions' }
#### boolean CanReroll ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>

### Get·Coin·Value () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetCoinValue ( ) {: .copyable aria-label='Functions' }
If this is a coin, return its face value, else zero.
___

### Is·Shop·Item () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsShopItem ( ) {: .copyable aria-label='Functions' }

___

### Morph () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void Morph ( [EntityType](enums/EntityType.md) Type, int Variant, int SubType, boolean KeepPrice = false, boolean KeepSeed = false, boolean IgnoreModifiers = false ) {: .copyable aria-label='Functions' }

**KeepSeed**: 如果设置为 true，将保留拾取物的初始 RNG 种子，而不是重置它

**IgnoreModifiers**: 如果设置为true，将忽略可能将此拾取物转变为其他类型的物品效果。具体来说，这可以用来防止道具受到堕化以撒的额外选择机制的影响。（例如，如果您手动生成一个任务道具，例如 Polaroid，它将受到堕化以撒的机制的影响，这通常是不可取的。要解决此问题，您可以在生成后立即将其变形为相同的实体类型/变体/子类型，并将此参数设置为 true。）
___

### Play·Drop·Sound () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PlayDropSound ( ) {: .copyable aria-label='Functions' }

___

### Play·Pickup·Sound () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PlayPickupSound ( ) {: .copyable aria-label='Functions' }

___

### Try·Open·Chest () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean TryOpenChest ( [EntityPlayer](EntityPlayer.md) Player = nil ) {: .copyable aria-label='Functions' }
**Player**: The player that opened this chest
___
## Variables

### Auto·Update·Price {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean AutoUpdatePrice  {: .copyable aria-label='Variables' }

___

### Charge {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Charge  {: .copyable aria-label='Variables' }

___

### OptionsPickupIndex {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int OptionsPickupIndex  {: .copyable aria-label='Variables' }

任何非 0 的值都会导致该物品与任何其他具有相同 OptionsPickupIndex 值的物品形成选项组。

当属于选项组的物品被拾取时，所有属于同一组的其他物品都会消失。

0 是默认值，表示该物品不属于任何组。
___

### Price {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Price  {: .copyable aria-label='Variables' }
该物品在商店中的价格。

???- info "堕化店长信息"

    在堕化店长身上，所有物品都应该有一个价格。但是，任何使用 Lua 生成的物品都不符合此规则，因此您必须手动设置价格。在分配价格的下一帧（例如 `1`）之后，它将自动调整为堕化店长的正确价格（例如 15）。这是由于 AutoUpdatePrice 功能造成的。

    该方法在大多数情况下都有效。然而，它在特殊房间（例如天使房）中会出现问题，有时价格会跳到错误的值，例如 24、99 等。解决此问题的方法是将 ShopItemId 设置为任意负值（例如 -1）。

___

### Shop·Item·Id {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ShopItemId  {: .copyable aria-label='Variables' }

如果在商店中, 这个值描述了这个物品在商店的哪一个槽中售卖。例如，如果商店有 6 个待售物品，则房间中的拾取物将具有 0、1、2、3、4 和 5 的商店物品 ID。

当生成一个新的道具时，ShopItemId 默认为 0。这会导致 D6 将道具重置为红心。通过将商店物品 ID 设置为 -1，可以修复此行为，使道具正确重置为另一个道具。然而，非道具可能会通过 D20 或类似物品重置为道具。

通过将商店物品 ID 设置为 -2，自动价格将为恶魔交易价格。否则，这与 -1 相同。

其他负值的行为与 -1 相同。

___

### State {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int State  {: .copyable aria-label='Variables' }

___

### Timeout {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Timeout  {: .copyable aria-label='Variables' }

使拾取物在一段时间后闪烁并消失，就像堕化玛姬掉落的临时生命值一样。该值每帧减少 1，达到 0 后拾取物消失。如果 Timeout 设置为 -1（正常拾取物的默认值），则拾取物将正常工作而不会消失。

___

### Touched {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean Touched  {: .copyable aria-label='Variables' }

___

### Wait {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Wait  {: .copyable aria-label='Variables' }

被用于道具，以强制执行一段时间，期间玩家将不会自动拾取道具。新的道具生成时，`Wait` 值为 20（对应于 20 帧游戏时间）。该值会随着游戏帧的推移而自动减少。

目前尚不清楚此值是否用于其他类型的拾取物。

___

<div class="rgon-only" markdown="1">

### AddCollectibleCycle () {: aria-label='Functions' }
#### boolean AddCollectibleCycle ( int id ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetAlternatePedestal () {: aria-label='Functions' }
#### int GetAlternatePedestal ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollectibleCycle () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)[] GetCollectibleCycle ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个表格，其中包含在其收藏品循环（例如错误王冠）中使用的所有 [CollectibleTypes](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)。

### GetDropDelay () {: aria-label='Functions' }
#### int GetDropDelay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetFlipCollectible () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetFlipCollectible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果存在 Flip 保存状态，则返回 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)，否则返回 `nil`。

___

### GetLootList () {: aria-label='Functions' }
#### [LootList](LootList.md) GetLootList ( boolean shouldAdvance = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回拾取物的 [LootList](LootList.md) 的**只读**版本。可以通过使用嗝屁猫之眼收藏品来查看拾取物中的战利品。

`shouldAdvance` 决定是否要前进 loot RNG。

___

### GetMegaChestLeftCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md) GetMegaChestLeftCollectible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果对打开的 Mega Chest 右侧的 EntityPickup 调用，则返回左侧的收藏品；否则返回 `nil`。

___

### GetMegaChestOtherCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md), boolean GetMegaChestRightCollectible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果对属于打开的 Mega Chest 的 EntityPickup 调用，则返回另一个收藏品，以及一个表示当前收藏品是否位于右侧的布尔值；否则返回 `nil`。

___

### GetMegaChestRightCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md) GetMegaChestRightCollectible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果对打开的 Mega Chest 左侧的 EntityPickup 调用，则返回右侧的收藏品；否则返回 `nil`。

___

### GetPickupGhost () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) GetPickupGhost ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回通过嗝屁猫之眼可见的 `EffectVariant.PICKUP_GHOST` 实体效果。如果不可见，则返回 `nil`。

### GetPriceSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetPriceSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRandomPickupVelocity () {: aria-label='Functions' }
#### [Vector](Vector.md) GetRandomPickupVelocity ( [Vector](Vector.md) Position, [RNG](RNG.md) RNG = nil, int VelocityType = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
`VelocityType` 1 会将拾取物朝下方的锥形区域射出，主要用于乞丐的奖励。
`VelocityType` 0 会将拾取物朝所需位置周围的随机方向射出。
`VelocityType` 似乎也会影响挑战房间中的拾取物，使其速度更慢。

???+ warning "Warning"

    这是一个静态函数，必须通过 `EntityPickup.GetRandomPickupVelocity(Position, RNG, VelocityType)` 调用。

___

### GetVarData () {: aria-label='Functions' }
#### int GetVarData ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### HasFlipData () {: aria-label='Functions' }
#### boolean HasFlipData ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果拾取物是收藏品且具有 Flip 保存状态，则返回 `true`。

___

### InitFlipState () {: aria-label='Functions' }
#### void InitFlipState ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) = CollectibleType.COLLECTIBLE_NULL, boolean SetupCollectibleGraphics = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
使用提供的 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) 为拾取物初始化翻转状态。

___

### IsBlind () {: aria-label='Functions' }
#### boolean IsBlind ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果拾取物是收藏品基座且处于隐藏状态，则返回 `true`。对于非收藏品实体拾取物，始终返回 `false`。

???+ warning "Warning"

    此值不考虑盲目诅咒，它仅反映通常在不涉及诅咒的情况下处于盲目状态的拾取物的盲目状态。例如：隐藏路线的额外物品。

___

### MakeShopItem () {: aria-label='Functions' }
#### void MakeShopItem ( int ShopItemID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ReloadGraphics () {: aria-label='Functions' }
#### void ReloadGraphics ( boolean IgnoreBlind ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### RemoveCollectibleCycle () {: aria-label='Functions' }
#### void RemoveCollectibleCycle ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetAlternatePedestal () {: aria-label='Functions' }
#### void SetAlternatePedestal ( int PedestalType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置物品基座的图形。对非收藏品实体拾取物无效。

___

### SetDropDelay () {: aria-label='Functions' }
#### void SetDropDelay ( int Delay ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetForceBlind () {: aria-label='Functions' }
#### void SetForceBlind ( boolean SetBlind ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
像盲目诅咒一样隐藏基座物品。对非收藏品实体拾取物无效。

___

### SetNewOptionsPickupIndex () {: aria-label='Functions' }
#### int SetNewOptionsPickupIndex ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回新的拾取物索引。

___

### SetupCollectibleGraphics () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge }
#### static void SetupCollectibleGraphics ( [Sprite](Sprite.md) Sprite, integer Layer, [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean Blind = false, integer Seed = Random(), boolean LoadGraphics = false  ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
静态方法。用于将精灵对象指定图层的 spritesheet 替换为收藏品精灵。Seed 用于在愚人节挑战中选择随机收藏品。

___

### SetVarData () {: aria-label='Functions' }
#### void SetVarData ( int VarData ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### TriggerTheresOptionsPickup () {: aria-label='Functions' }
#### void TriggerTheresOptionsPickup ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
移除与目标拾取物具有相同选项组（OptionsPickupIndex）的拾取物。

___

### TryFlip () {: aria-label='Functions' }
#### boolean TryFlip ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
尝试翻转收藏品，例如在使用翻转物品对带有第二个全息收藏品（位于第一个后面）的收藏品基座进行操作时。如果成功则返回 `true`，否则返回 `false`；如果用于非收藏品实体拾取物，也返回 `false`。

___

### TryInitOptionCycle () {: aria-label='Functions' }
#### boolean TryInitOptionCycle ( int NumCycle ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
使收藏品基座开始循环显示指定数量的收藏品，包括其自身的收藏品类型。

___

### TryRemoveCollectible () {: aria-label='Functions' }
#### boolean TryRemoveCollectible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果成功从基座上移除了一个收藏品，则返回 `true`。如果基座已经为空，或者对非收藏品实体拾取物调用此函数，则返回 `false`。
尝试从物品基座上移除收藏品。

___

### UpdatePickupGhosts () {: aria-label='Functions' }
#### void UpdatePickupGhosts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
根据拾取物当前的 [LootList](LootList.md) 更新 `EffectVariant.PICKUP_GHOST` 实体效果。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

</div>
