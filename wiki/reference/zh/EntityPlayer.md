---
tags:
  - Class
  - Player
---
# Class "EntityPlayer"

???+ info
    你可以通过以下函数获取此类：

    * [Entity.ToPlayer()](Entity.md#toplayer)
    * [EntityFamiliar.Player](EntityFamiliar.md#player)
    * [EntityPlayer.GetMainTwin()](EntityPlayer.md#getmaintwin)
    * [EntityPlayer.GetOtherTwin()](EntityPlayer.md#getothertwin)
    * [EntityPlayer.GetSubPlayer()](EntityPlayer.md#getsubplayer)
    * [Game.GetNearestPlayer()](Game.md#getnearestplayer)
    * [Game.GetPlayer()](Game.md#getplayer)
    * [Game.GetRandomPlayer()](Game.md#getrandomplayer)
    * [Isaac.GetPlayer()](Isaac.md#getplayer)

    ???+ example "Example Code"
        `local player = Isaac.GetPlayer()`

## Class Diagram
--8<-- "zh/snippets/EntityClassDiagram.md"
## Functions

### Add·Black·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddBlackHearts ( int BlackHearts ) {: .copyable aria-label='Functions' }

给玩家添加黑心。1个单位是半颗心。用负数移除它们。

???- example "Example Code"

    This code adds 1 full black heart to the player.

    ```lua
    Isaac.GetPlayer():AddBlackHearts(2)
    ```

___

### Add·Blood·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddBloodCharge ( int Amount ) {: .copyable aria-label='Functions' }

给玩家添加血量充能。血量充能在除堕化伯大妮以外的角色上没有任何作用。

___

### Add·Blue·Flies () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) AddBlueFlies ( int Amount, [Vector](Vector.md) Position, [Entity](Entity.md) Target ) {: .copyable aria-label='Functions' }
???- info "Amount"

    饰品**鱼尾**将始终将此函数添加的苍蝇数量加倍。

___

### Add·Blue·Spider () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) AddBlueSpider ( [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }

???- example "Example Code"

    This code spawns 3 blue spiders at the player's position.

    ```lua
    local player = Isaac.GetPlayer()
    for _ = 1, 3 do
	player:AddBlueSpider(player.Position)
    end
    ```

___

### Add·Bombs () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddBombs ( int Amount ) {: .copyable aria-label='Functions' }

给玩家添加炸弹。用负数移除它们。

???- example "Example Code"

    This code removes 1 bomb from the player.

    ```lua
    Isaac.GetPlayer():AddBombs(-1)
    ```

___

### Add·Bone·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddBoneHearts ( int Hearts ) {: .copyable aria-label='Functions' }

给玩家添加骨心。1个单位是单颗骨心。用负数移除它们。

???- example "Example Code"

    This code adds 1 bone heart to the player.

    ```lua
    Isaac.GetPlayer():AddBoneHearts(1)
    ```

___

### Add·Broken·Hearts () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddBrokenHearts ( int BrokenHearts ) {: .copyable aria-label='Functions' }

给玩家添加碎心。1个单位是单颗碎心。用负数移除它们。

???- example "Example Code"

    This code adds 1 broken heart to the player, then takes it away.

    ```lua
    Isaac.GetPlayer():AddBrokenHearts(1)
    Isaac.GetPlayer():AddBrokenHearts(-1)
    ```
___

### Add·Cache·Flags () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCacheFlags ( [CacheFlag](enums/CacheFlag.md) CacheFlag ) {: .copyable aria-label='Functions' }

在下一次缓存重新计算中，将重新计算提供的缓存标志。

???- example "Example Code"

    This code will add several cacheflags.

    ```lua
    Isaac.GetPlayer():AddCacheFlags(CacheFlag.CACHE_DAMAGE | CacheFlag.CACHE_FIREDELAY | CacheFlag.CACHE_LUCK)
    ```
___

<div class="rgon-extension" markdown="1">

### AddCacheFlags () {: aria-label='Modified Functions' }
#### void AddCacheFlags ( [CacheFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/CacheFlag.html) CacheFlag, boolean EvaluateItems = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
现在接受一个可选的布尔值，用于确定在添加缓存标志后是否应自动调用 [EntityPlayer](EntityPlayer.md):EvaluateItems()。在大多数情况下，你可能希望这样做。

___

</div>

### Add·Card () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCard ( [Card](enums/Card.md) ID ) {: .copyable aria-label='Functions' }

___

### Add·Coins () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCoins ( int Amount ) {: .copyable aria-label='Functions' }

给玩家添加金币。用负数移除它们。

???- example "Example Code"

    This code adds 1 coin to the player.

    ```lua
    Isaac.GetPlayer():AddCoins(1)
    ```

___

### Add·Collectible () {: aria-label='Functions' }
[ ](#){: .rep .tooltip .badge }
#### void AddCollectible ( [CollectibleType](enums/CollectibleType.md) Type, int Charge = 0, boolean FirstTimePickingUp = true, [ActiveSlot](enums/ActiveSlot.md) Slot = ActiveSlot.SLOT_PRIMARY, int VarData = 0) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void AddCollectible ( [CollectibleType](enums/CollectibleType.md) Type, int Charge = 0, boolean FirstTimePickingUp = true, [ActiveSlot](enums/ActiveSlot.md) Slot = ActiveSlot.SLOT_PRIMARY, int VarData = 0, [ItemPoolType](enums/ItemPoolType.md) PoolType ) {: .copyable aria-label='Functions' }


设置 **FirstTimePickingUp** 为false 将不会添加物品的消耗品（钥匙、炸弹等），并且不会计入套装。

- Slot 0 是默认值 (normal active item)
- Slot 1 是 Schoolbag 使用的
- Slot 2 是用于口袋主动物品的

???- note "Notes"

	Slot 2 不能被用于开始时没有口袋主动物品的角色

VarData is used for the storage of a persistent context-sensitive value

???- note "Notes"

    这是一个使用 VarData 的所有物品的列表：

    - 魂火罐: 魂火会在下一次使用时生成 (最大12)
	- 无限骰, 空白卡, 透明符文, 安慰剂: 当前最大充能 (任何大于0的值)
	- Hold: 存储的便便
	    - 便便类型:
	    - [0] 无
	    - [1] 普通
	    - [2] 苍蝇
	    - [3] 火焰
	    - [4] 石化
	    - [5] 有毒
	    - [6] 黑色
	    - [7] 神圣
	    - [8] X-Lax
	    - [9] Fart
	    - [10] Bomb
	    - [11] Explosive Diarrhea
	    - [12+] Empty

___

### Add·Controls·Cooldown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddControlsCooldown ( int Cooldown ) {: .copyable aria-label='Functions' }

___

### Add·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCostume ( [ItemConfigItem](ItemConfig_Item.md) Item, boolean ItemStateOnly ) {: .copyable aria-label='Functions' }

___

### Add·Curse·Mist·Effect () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddCurseMistEffect ( ) {: .copyable aria-label='Functions' }

___

### Add·Dead·Eye·Charge () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddDeadEyeCharge ( ) {: .copyable aria-label='Functions' }

___

### Add·Dollar·Bill·Effect () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddDollarBillEffect ( ) {: .copyable aria-label='Functions' }

___

### Add·Eternal·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddEternalHearts ( int EternalHearts ) {: .copyable aria-label='Functions' }

给玩家添加永恒之心。1个单位是半颗心。用负数移除它们。

（注意，当你拥有超过一个时，永恒之心会自动变为完整的心。）

???- example "Example Code"

    This code adds 1 eternal heart to the player.

    ```lua
    Isaac.GetPlayer():AddEternalHearts(1)
    ```

___

### Add·Friendly·Dip () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddFriendlyDip ( int Subtype, [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }

???- note "Dip Subtypes"

    ```lua
    0: normal
    1: red
    2: corny
    3: golden
    4: rainbow
    5: black
    6: holy
    12: stone
    13: flaming
    14: poison
    20: brownie
    ```
___

### Add·Giga·Bombs () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddGigaBombs ( int GigaBombs ) {: .copyable aria-label='Functions' }

???- note "Notes"

    巨型炸弹不会增加炸弹计数，请确保提前增加炸弹数量！
	你不能添加超过玩家当前炸弹数量的巨型炸弹。

___

### Add·Golden·Bomb () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddGoldenBomb ( ) {: .copyable aria-label='Functions' }

___

### Add·Golden·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddGoldenHearts ( int Hearts ) {: .copyable aria-label='Functions' }

给玩家添加金心。1个单位是单颗金心。用负数移除它们。

???- example "Example Code"

    This code adds 1 golden heart to the player.

    ```lua
    Isaac.GetPlayer():AddGoldenHearts(1)
    ```

___

### Add·Golden·Key () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddGoldenKey ( ) {: .copyable aria-label='Functions' }

___

### Add·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddHearts ( int Hearts ) {: .copyable aria-label='Functions' }

给玩家添加红心。如果有空的心容器，则添加红心。1个单位是半颗心。用负数移除生命值。

???- example "Example Code"

    This code adds 1 full red heart to the player.

    ```lua
    Isaac.GetPlayer():AddHearts(2)
    ```

___

### Add·Item·Wisp () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) AddItemWisp ( [CollectibleType](enums/CollectibleType.md) Collectible, [Vector](Vector.md) Position, boolean AdjustOrbitLayer = false ) {: .copyable aria-label='Functions' }

___

### Add·Jar·Flies () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddJarFlies ( int Flies ) {: .copyable aria-label='Functions' }

___

### Add·Jar·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddJarHearts ( int Hearts ) {: .copyable aria-label='Functions' }

___

### Add·Keys () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddKeys ( int Amount ) {: .copyable aria-label='Functions' }

给玩家添加钥匙。用负数移除它们。

???- example "Example Code"

    This code adds 1 key to the player.

    ```lua
    Isaac.GetPlayer():AddKeys(1)
    ```

___

### Add·Max·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddMaxHearts ( int MaxHearts, boolean IgnoreKeeper ) {: .copyable aria-label='Functions' }

给玩家添加心容器。2个单位是一个完整的心容器。用负数移除它们。

???- note "Notes"

    可以添加半颗心容器到玩家身上。这将显示为常规心容器，但只能填充一半。

???- example "Example Code"

    This code adds 1 heart container to the player.

    ```lua
    Isaac.GetPlayer():AddMaxHearts(2, true)
    ```


???+ bug "Bugs"

    对店长无效。IgnoreKeeper 参数似乎无法按预期工作。

    最大心容器可以添加或移除到店长身上，而不管这个布尔值是什么。

    如果店长拥有贪婪的胃袋，而这个布尔值被设置为false，则无法添加最大心容器到店长身上，但可以正常移除。

    如果店长拥有贪婪的胃袋，而这个布尔值被设置为true，则可以正常添加或移除最大心容器到店长身上。

___

### Add·Minisaac () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) AddMinisaac ( [Vector](Vector.md) Position, boolean PlayAnim = true ) {: .copyable aria-label='Functions' }

___

### Add·Null·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddNullCostume ( [NullItemID](enums/NullItemID.md) NullId ) {: .copyable aria-label='Functions' }

___

### Add·Pill () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddPill ( [PillColor](enums/PillColor.md) Pill ) {: .copyable aria-label='Functions' }

___

### Add·Player·Form·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddPlayerFormCostume ( [PlayerForm](enums/PlayerForm.md) Form ) {: .copyable aria-label='Functions' }

添加给定变身的服装。

___

### Add·Poop·Mana () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddPoopMana ( int Num ) {: .copyable aria-label='Functions' }

添加（或移除）粪便消耗品。

___

### Add·Pretty·Fly () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddPrettyFly ( ) {: .copyable aria-label='Functions' }

___

### Add·Rotten·Hearts () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddRottenHearts ( int RottenHearts ) {: .copyable aria-label='Functions' }

添加腐烂的心。1个单位是半颗心。用负数移除腐烂的心。

???- example "Example Code"

    This code adds 1 full rotten heart to the player.

    ```lua
    Isaac.GetPlayer():AddRottenHearts(2)
    ```

___

### Add·Soul·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddSoulCharge ( int Amount ) {: .copyable aria-label='Functions' }

添加灵魂充能到玩家身上。灵魂充能对除了伯大妮以外的角色没有任何作用。

___

### Add·Soul·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddSoulHearts ( int SoulHearts ) {: .copyable aria-label='Functions' }

添加魂心到玩家。1个单位是半颗心。用负数移除它们。

???- example "Example Code"

    This code adds 1 full soul heart to the player.

    ```lua
    Isaac.GetPlayer():AddSoulHearts(2)
    ```

___

### Add·Swarm·Fly·Orbital () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) AddSwarmFlyOrbital ( [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }

___

### Add·Trinket () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddTrinket ( [TrinketType](enums/TrinketType.md) Type, boolean FirstTimePickingUp = true ) {: .copyable aria-label='Functions' }

- 如果玩家没有任何空的饰品槽，这个函数将不做任何事情。

- 如果玩家有一个空的饰品槽但已经有一个饰品，新饰品将进入第一个槽，现有饰品将被推回到第二个槽。

- 如果提供的参数为0或其他无效的饰品ID，游戏将崩溃。

- 将**FirstTimePickingUp**设置为false将不会为该物品生成或添加拾取物，也不会导致其计入变身。

???- example "Example Code"

    This code adds the golden variant of the Swallowed Penny trinket to the player.

    ```lua
    Isaac.GetPlayer():AddTrinket(TrinketType.TRINKET_SWALLOWED_PENNY | TrinketType.TRINKET_GOLDEN_FLAG)
    ```

___

### Add·Wisp () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) AddWisp ( [CollectibleType](enums/CollectibleType.md) Collectible, [Vector](Vector.md) Position, boolean AdjustOrbitLayer = false, boolean DontUpdate = false ) {: .copyable aria-label='Functions' }

魂火的类型可以通过Collectible来定义。如果ID与具有特殊魂火的主动物品不对应，则默认为常规蓝色魂火。

要访问特殊魂火变体，例如Delirious形式，您需要将`65536` (1 << 16)添加到ID。例如：Delirious Monstro的`id = s14`，因此魂火的ID为`65550`。

___

### Animate·Appear () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateAppear ( ) {: .copyable aria-label='Functions' }
播放在关卡开始时通常播放的动画。
___

### Animate·Card () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AnimateCard ( [Card](enums/Card.md) ID, string AnimName = "Pickup" ) {: .copyable aria-label='Functions' }

___

### Animate·Collectible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AnimateCollectible ( [CollectibleType](enums/CollectibleType.md) Collectible, string AnimName = "Pickup", string SpriteAnimName = "PlayerPickupSparkle" ) {: .copyable aria-label='Functions' }

`AnimName` 指 `001.000_player.anm2` 中的动画名称（例如 `Pickup` 或 `UseItem`）。 `SpriteAnimName` 指 `005.100_collectible.anm2` 中的动画名称（例如 `PlayerPickup` 或 `PlayerPickupSparkle`）。

___

### Animate·Happy () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateHappy ( ) {: .copyable aria-label='Functions' }

播放高兴动画，当服用正面药丸时播放。

???- example "Example Code"

    This code plays the happy animation.

    ```lua
    Isaac.GetPlayer():AnimateHappy()
    ```

### Animate·Light·Travel () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateLightTravel ( ) {: .copyable aria-label='Functions' }

播放在上升时进入光柱或进入大教堂时播放的动画。

???- example "Example Code"

	Plays the animation.

	```lua
	Isaac.GetPlayer():AnimateLightTravel()
	```

___

### Animate·Pickup () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AnimatePickup ( [Sprite](Sprite.md) sprite, boolean HideShadow = false, string AnimName = "Pickup" ) {: .copyable aria-label='Functions' }

播放拾取动画，使用任何提供的Sprite对象

HideShadow通常在渲染具有自定义阴影层的精灵时设置为true

___

### Animate·Pill () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AnimatePill ( [PillColor](enums/PillColor.md) Pill, string AnimName = "Pickup" ) {: .copyable aria-label='Functions' }

___

### Animate·Pitfall·In () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimatePitfallIn ( ) {: .copyable aria-label='Functions' }

造成1/2心的伤害并播放掉入陷阱的动画。

___

### Animate·Pitfall·Out () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimatePitfallOut ( ) {: .copyable aria-label='Functions' }

跳出陷阱的动画。

___

### Animate·Sad () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateSad ( ) {: .copyable aria-label='Functions' }

播放悲伤动画，当服用负面药丸时播放。

???- example "Example Code"

    Plays the sad animation.

	```lua
	Isaac.GetPlayer():AnimateSad()
	```
___

### Animate·Teleport () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateTeleport ( boolean Up ) {: .copyable aria-label='Functions' }

当传送到另一个房间时播放的动画。

___

### Animate·Trapdoor () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AnimateTrapdoor ( ) {: .copyable aria-label='Functions' }

播放跳下陷阱门的动画。

???- example "Example Code"

	Plays the animation of jumping down a trapdoor.

	```lua
	Isaac.GetPlayer():AnimateTrapdoor()
	```

___

### Animate·Trinket () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AnimateTrinket ( [TrinketType](enums/TrinketType.md) Trinket, string AnimName = "Pickup", string SpriteAnimName = "PlayerPickupSparkle" ) {: .copyable aria-label='Functions' }

___

### Are·Controls·Enabled () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean AreControlsEnabled ( ) {: .copyable aria-label='Functions' }

___

### Are·Opposing·Shoot·Directions·Pressed () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean AreOpposingShootDirectionsPressed ( ) {: .copyable aria-label='Functions' }

返回最近的移动输入中非零的摇杆方向，但在玩家停止后变为零。
___

### Can·Add·Collectible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean CanAddCollectible ( [CollectibleType](enums/CollectibleType.md) Type = CollectibleType.COLLECTIBLE_NULL ) {: .copyable aria-label='Functions' }

___

### Can·Pick·Black·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickBlackHearts ( ) {: .copyable aria-label='Functions' }

返回 true 如果玩家有容纳更多黑心的空间
___

### Can·Pick·Bone·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickBoneHearts ( ) {: .copyable aria-label='Functions' }

返回 true 如果玩家有容纳更多骨心的空间
___

### Can·Pick·Golden·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickGoldenHearts ( ) {: .copyable aria-label='Functions' }

返回 true 如果玩家有容纳更多金心的空间
___

### Can·Pick·Red·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickRedHearts ( ) {: .copyable aria-label='Functions' }

___

### Can·Pick·Rotten·Hearts () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean CanPickRottenHearts ( ) {: .copyable aria-label='Functions' }

返回 true 如果玩家有容纳更多腐心的空间
___

### Can·Pick·Soul·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickSoulHearts ( ) {: .copyable aria-label='Functions' }

返回 true 如果玩家有容纳更多魂心的空间
___

### Can·Pickup·Item () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanPickupItem ( ) {: .copyable aria-label='Functions' }

返回 true 如果玩家现在可以拾取物品
___

### Can·Shoot () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanShoot ( ) {: .copyable aria-label='Functions' }

___

### Can·Turn·Head () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanTurnHead ( ) {: .copyable aria-label='Functions' }

返回 true 如果头部应该对按键做出反应，否则返回 false
___

### Change·Player·Type () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void ChangePlayerType ( [PlayerType](enums/PlayerType.md) PlayerType ) {: .copyable aria-label='Functions' }

被用于改变一个玩家的类型。例如将该隐变成抹大拉。

在 MC_POST_PLAYER_INIT 中更改玩家类型将导致玩家获得该角色的默认物品。例如，抹大拉将获得她的美味的心，而无需您显式添加它。这里的例外包括可解锁物品（例如，以撒的 D6）和默认数量的心脏/钥匙/炸弹/硬币。您可以在初始化后更改玩家类型，但通常需要负责添加与该角色相关的任何物品。

将玩家类型更改为雅各布也会生成以扫。
___

### Check·Familiar () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void CheckFamiliar ( [FamiliarVariant](enums/FamiliarVariant.md) FamiliarVariant, int TargetCount, [RNG](RNG.md) rng, [ItemConfigItem](ItemConfig_Item.md) SourceItemConfigItem = nil, int FamiliarSubType = -1 ) {: .copyable aria-label='Functions' }

访问这个方法以生成与自定义可收集物品相关的适当数量的随从。

- 如果指定的目标数量少于当前的随从数量，它将生成更多，直到达到目标数量。

- 如果指定的目标数量大于当前的随从数量，它将去除随从，直到达到目标数量。

这意味着它应该在 EvaluateCache 回调中调用（当缓存标志等于 `CacheFlag.CACHE_FAMILIARS` 时）。

在大多数情况下，[:material-language-typescript:IsaacScript](https://isaacscript.github.io/) 用户应该使用 [`checkFamiliarFromCollectibles`](https://isaacscript.github.io/isaacscript-common/modules/functions_familiars.html#checkFamiliarFromCollectibles) 辅助函数，而不是直接使用此方法，因为它会自动计算适当的目标数量。

**FamiliarVariant**: 大多数情况下, 使用随从变体作为自定义随从的基础。

**TargetCount**: 期望该实体玩家应该拥有的此随从变体的数量。此参数可以简单地是当前实体玩家拥有的某个物品的数量。但是，如果您希望您的随从与怪物手册和朋友盒子协同作用，则此参数应为 `EntityPlayer:GetCollectibleNum(collectibleType) + EntityPlayer:GetEffects():GetCollectibleEffectNum(collectibleType)`。

**rng**: 可以是生成随从的可收集物品的 `EntityPlayer.GetCollectibleRNG` 的 RNG 对象。

**SourceItemConfigItem**: 生成此随从的 `ItemConfigItem`。默认情况下为 nil，但应始终指定，以便祭品祭坛正常工作。（它告知游戏如果随从被标记为“cansacrifice”实体标签，则应删除哪个可收集物品。）可以通过以下方式获得：`Isaac.GetItemConfig():GetCollectible(collectibleType)`

**FamiliarSubType**: 要检查的随从子类型。-1 匹配任何子类型。

???- example "Example Code"

    This code spawns 3 "Sister Maggy" familiars.

    ```lua
    local player = Isaac.GetPlayer()
    local sourceCollectibleID = CollectibleType.COLLECTIBLE_SAD_ONION
    local collectibleRNG = player:GetCollectibleRNG(sourceCollectibleID)
    local itemConfig = Isaac.GetItemConfig():GetCollectible(sourceCollectibleID)

    player:CheckFamiliar(FamiliarVariant.SISTER_MAGGY, 3, collectibleRNG, itemConfig)
    ```

___

### Clear·Costumes () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ClearCostumes ( ) {: .copyable aria-label='Functions' }

移除所有服装。
___

### Clear·Dead·Eye·Charge () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ClearDeadEyeCharge ( ) {: .copyable aria-label='Functions' }

___

<div class="rgon-extension" markdown="1">

### ClearDeadEyeCharge () {: aria-label='Modified Functions' }
#### void ClearDeadEyeCharge ( boolean Force = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
现在接受一个 `Force` 参数，以强制重置充能，而不是仅通过概率来决定是否重置。

</div>

### Clear·Temporary·Effects () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ClearTemporaryEffects ( ) {: .copyable aria-label='Functions' }

将在玩家退出房间时调用。

___

### Discharge·Active·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void DischargeActiveItem ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

设置您的主动物品的充能为 0，而不触发主动物品效果。

___

### Donate·Luck () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void DonateLuck ( int Luck ) {: .copyable aria-label='Functions' }

不像Luck属性应该在MC_EVALUATE_CACHE中设置，这个方法可以在任何地方使用，并会自动记住添加的任何额外运气。

___

### Do·Zit·Effect () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void DoZitEffect ( [Vector](Vector.md) Direction ) {: .copyable aria-label='Functions' }

发射一个青春痘，效果与“青春痘”物品发射的效果相同。

___

### Drop·Pocket·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void DropPocketItem ( int PocketNum, [Vector](Vector.md) Pos ) {: .copyable aria-label='Functions' }

扔下一个持有的口袋物品（卡片、药丸、符文……）从给定的物品槽在给定的位置。可能的口袋编号是 [0, 1, 2, 3]。扔下口袋主动物品或骰子袋骰子是无效的。

___

### Drop·Trinket () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void DropTrinket ( [Vector](Vector.md) DropPos, boolean ReplaceTick ) {: .copyable aria-label='Functions' }

___

### Evaluate·Items () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void EvaluateItems ( ) {: .copyable aria-label='Functions' }

触发一个缓存重新评估，将会触发 MC_EVALUATE_CACHE 回调。

在使用此函数之前，您需要先设置适当的缓存标志。请参阅下面的示例。

???- example "Example Code"

    This code re-evaluates all of the stats for the player.

    ```lua
    local player = Isaac.GetPlayer()
    player:AddCacheFlags(CacheFlag.CACHE_ALL)
    player:EvaluateItems()
    ```

___

### Fire·Bomb () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityBomb](EntityBomb.md) FireBomb ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, Entity Source = nil ) {: .copyable aria-label='Functions' }

___

### Fire·Brimstone () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityLaser](EntityLaser.md) FireBrimstone ( [Vector](Vector.md) Direction, Entity Source = nil, float DamageMultiplier = 1 ) {: .copyable aria-label='Functions' }

___

### Fire·Delayed·Brimstone () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityLaser](EntityLaser.md) FireDelayedBrimstone ( float Angle, [Entity](Entity.md) Parent ) {: .copyable aria-label='Functions' }

___

### Fire·Knife () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityKnife](EntityKnife.md) FireKnife ( [Entity](Entity.md) Parent, float RotationOffset = 0, boolean CantOverwrite = false, int SubType = 0, int Variant = 0 ) {: .copyable aria-label='Functions' }

???- note "Knife Variants"

    ```lua
    0: Mom's Knife
    1: Bone Club
    2: Bone Scythe
    3: Berserk Club
    4: Bag of Crafting
    5: Sumptorium
    9: Notched Axe
    10: Spirit Sword
    11: Tech Sword
    ```

___

### Fire·Tear () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityTear](EntityTear.md) FireTear ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, boolean CanBeEye = true, boolean NoTractorBeam = false, boolean CanTriggerStreakEnd = true, Entity Source = nil, float DamageMultiplier = 1 ) {: .copyable aria-label='Functions' }

- `CanBeEye`: 如果玩家拥有邪恶之眼物品，传递 true 允许泪水有机会成为眼泪。
- `NoTractorBeam`: 如果玩家拥有牵引光束物品，传递 true 意味着泪水将免受光束影响。
- `CanTriggerStreakEnd`: 如果玩家拥有死亡之眼物品，传递 false 意味着泪水将免于结束连击。

___

### Fire·Tech·Laser () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityLaser](EntityLaser.md) FireTechLaser ( [Vector](Vector.md) Position, [LaserOffset](enums/LaserOffset.md) OffsetID, [Vector](Vector.md) Direction, boolean LeftEye, boolean OneHit = false, Entity Source = nil, float DamageMultiplier = 1 ) {: .copyable aria-label='Functions' }

???+ bug "Bugs"

    `DamageMultiplier` 变量不影响当提供 [LASER_TECH2_OFFSET](enums/LaserOffset.md) 作为偏移量时。

___

### Fire·Tech·XLaser () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityLaser](EntityLaser.md) FireTechXLaser ( [Vector](Vector.md) Position, [Vector](Vector.md) Direction, float Radius, Entity Source = nil, float DamageMultiplier = 1 ) {: .copyable aria-label='Functions' }

___

### Flush·Queue·Item () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean FlushQueueItem ( ) {: .copyable aria-label='Functions' }

在动画完成后，或在特殊情况下调用以防止错误
___

### Full·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean FullCharge ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY, int Force = false ) {: .copyable aria-label='Functions' }

完全充能当前的主动物品。如果物品被完全充能，返回 true；否则返回 false。如果玩家拥有电池，它将首先尝试填充第一个充能槽，然后是电池槽。

**Force**: 如果设置为 true，物品将始终充能，即使它们通常无法通过电池充能

???- info "ActiveSlot"

    将 ActiveSlot 参数设置为 `-1` 将充能所有槽中的物品。

___

### Get·Active·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetActiveCharge ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

获取当前主动物品的充能值。
___

### Get·Active·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetActiveItem ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' data-altreturn='0' }

返回当前持有的主动物品。如果没有物品被持有，则返回 `0`。

___

### Get·Active·Sub·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetActiveSubCharge ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

获取当前主动物品的副充能值（即第二充能槽）。

???+ bug "Bug"

    这个函数似乎总是返回 0。使用 EntityPlayer:GetActiveCharge() 来获取任何类型的充能值。使用 EntityPlayer:GetBatteryCharge() 来获取第二个充能槽的充能值。

___

### Get·Active·Weapon·Entity () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) GetActiveWeaponEntity ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

___

### Get·Aim·Direction () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetAimDirection ( ) {: .copyable aria-label='Functions' }

___

### Get·Baby·Skin () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [BabySubType](enums/BabySubType.md) GetBabySkin ( ) {: .copyable aria-label='Functions' }

___

### Get·Battery·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetBatteryCharge ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

获取当前主动物品的第二充能槽的充能进度。该槽仅在你拥有可收集物品“电池”时处于激活状态。
___

### Get·Black·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetBlackHearts ( ) {: .copyable aria-label='Functions' }

这个函数并不返回黑心的数量；而是返回一个位掩码，用于表示哪些灵魂心是黑心。

???- example "Example"

    设想我们有以下血量的设置，其中 S 是灵魂心，B 是黑心：

    ```
    B S S B B S S B B
    ```

    Calling the function will return:

    ```lua
    Isaac.GetPlayer():GetBlackHearts() -- returns 409, which is 0001 1001 1001 in binary. Therefore, the read order is right to left.
    ```

    Quick code example to parse soul hearts vs black hearts:

    ```lua
    -- if you setup your hearts as described above then you'll get the following values
    -- GetSoulHearts = 18
    -- GetBlackHearts = 409
    local tbl = {}
    local player = Isaac.GetPlayer()
    -- loop over all the soul hearts
    -- divide by 2 because we need to go from half to whole hearts
    -- math.ceil to make sure we account for a possible half heart at the end
    for i = 0, math.ceil(player:GetSoulHearts() / 2) - 1 do
      -- you can also use BitSet128 here if you want: BitSet128(player:GetBlackHearts(),0):Get(i)
      table.insert(tbl, (player:GetBlackHearts() & (1 << i)) > 0 and 'B' or 'S')
    end
    if player:GetSoulHearts() % 2 ~= 0 then
      tbl[#tbl] = string.lower(tbl[#tbl]) -- lowercase to indicate half heart at end
    end
    print(table.concat(tbl, ' ')) -- prints: B S S B B S S B B
    ```

___

### Get·Blood·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetBloodCharge ( ) {: .copyable aria-label='Functions' }

返回玩家的血量充能值。

___

### Get·Body·Color () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [SkinColor](enums/SkinColor.md) GetBodyColor ( ) {: .copyable aria-label='Functions' }

___

### Get·Bomb·Flags () {: aria-label='Functions' }
[ ](#){: .abp .tooltip .badge }
#### int GetBombFlags ( ) {: .copyable aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetBombFlags ( boolean IsFetus = false ) {: .copyable aria-label='Functions' }

**IsFetus**: 如果设置为true，某些炸弹道具会随机设置flags。
___

### Get·Bomb·Variant () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [BombVariant](enums/BombVariant.md) GetBombVariant ( [TearFlags](enums/TearFlags.md) TearFlags, boolean ForceSmallBomb ) {: .copyable aria-label='Functions' }

通过传递泪弹标签为炸弹视觉效果添加额外效果，例如燃烧 -> 炙热炸弹，即使玩家没有道具炙热炸弹。 ForceSmallBomb 将覆盖 TEAR_PERSISTENT 的大炸弹变体。

___

### Get·Bone·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetBoneHearts ( ) {: .copyable aria-label='Functions' }

返回玩家的骨心数量。这个值并不像 `EntityPlayer.GetMaxHearts` 方法那样翻倍，所以如果例如玩家有 3 个骨心，这个函数将返回 3。

另请参阅 `EntityPlayer.GetEffectiveMaxHearts` 方法，该方法会考虑骨心。

___

### Get·Broken·Hearts () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetBrokenHearts ( ) {: .copyable aria-label='Functions' }

返回玩家的碎心数量。这个值并不像 `EntityPlayer.GetMaxHearts` 方法那样翻倍，所以如果例如玩家有 3 个碎心，这个函数将返回 3。

___

### Get·Card () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Card](enums/Card.md) GetCard ( int SlotId ) {: .copyable aria-label='Functions' data-altreturn='0' }

获取玩家在给定物品槽中持有的卡牌的 ID（0 = 主槽，1 = 副槽，2 或 3）。当槽中没有卡牌时返回 `0`。
___

### Get·Card·RNG () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [RNG](RNG.md) GetCardRNG ( [Card](enums/Card.md) ID ) {: .copyable aria-label='Functions' }

___

### Get·Collectible·Count () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetCollectibleCount ( ) {: .copyable aria-label='Functions' }

___

### Get·Collectible·Num () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetCollectibleNum ( [CollectibleType](enums/CollectibleType.md) Type, boolean OnlyCountTrueItems = false ) {: .copyable aria-label='Functions' }

**OnlyCountTrueItems**: 如果设置为 true，函数仅计算玩家实际拥有的可收集物品，并忽略 莉莉丝的淫魔、3美元 授予的物品等。
___

<div class="rgon-extension" markdown="1">

### GetCollectibleNum () {: aria-label='Modified Functions' }
#### int GetCollectibleNum ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean OnlyCountTrueItems = false, bool IgnoreSpoof = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
现在接受一个 `IgnoreSpoof` 参数，该参数会忽略固有物品。

</div>

### Get·Collectible·RNG () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [RNG](RNG.md) GetCollectibleRNG ( [CollectibleType](enums/CollectibleType.md) ID ) {: .copyable aria-label='Functions' }

获取道具的 [RNG](RNG.md) 对象。

???- example "示例代码"

    这段代码将为你提供道具“伤心洋葱”的 RNG 对象。

    ```lua
    local player = Isaac.GetPlayer()
    local collectibleRNG = player:GetCollectibleRNG(CollectibleType.COLLECTIBLE_SAD_ONION)
    ```

___

### Get·Costume·Null·Pos () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetCostumeNullPos ( string NullFrameName, boolean HeadScale, [Vector](Vector.md) Direction ) {: .copyable aria-label='Functions' }

___

### Get·Damage·Cooldown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetDamageCooldown ( ) {: .copyable aria-label='Functions' }

当玩家受到伤害时，他们会闪烁不同的颜色并获得无敌帧。此方法返回无敌帧的数量。通常，当玩家受到半颗心的伤害时，将获得 60 帧无敌时间；而受到一颗心的伤害时，将获得 120 帧无敌时间。此外，盲目的怒火饰品可以影响无敌帧的授予方式。

请注意，此函数返回的帧是渲染帧，而不是游戏帧。

___

### Get·Effective·Blood·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetEffectiveBloodCharge ( ) {: .copyable aria-label='Functions' }

返回玩家的血量充能。除堕化伯大妮外将返回 `0`。

___

### Get·Effective·Max·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetEffectiveMaxHearts ( ) {: .copyable aria-label='Functions' }

返回玩家在心容器和骨心中可以容纳的红心数量。1 个单位是半颗红心。

**Example：** 你有 3 个红心容器和 1 个骨心。6（红）+ 2（骨）= 8

___

### Get·Effective·Soul·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetEffectiveSoulCharge ( ) {: .copyable aria-label='Functions' }

返回玩家的灵魂充能。除伯大妮外将返回 `0`。

___

### Get·Effects () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [TemporaryEffects](TemporaryEffects.md) GetEffects ( ) {: .copyable aria-label='Functions' }

___

### Get·Eternal·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetEternalHearts ( ) {: .copyable aria-label='Functions' }

返回玩家的永恒之心数量。

___

### Get·Extra·Lives () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetExtraLives ( ) {: .copyable aria-label='Functions' }

返回玩家当前拥有的额外生命数量。

___

### Get·Fire·Direction () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Direction](enums/Direction.md) GetFireDirection ( ) {: .copyable aria-label='Functions' }

___

### Get·Flying·Offset () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetFlyingOffset ( ) {: .copyable aria-label='Functions' }

___

### Get·Golden·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetGoldenHearts ( ) {: .copyable aria-label='Functions' }

返回玩家的金心数量。

___

### Get·Greed·Donation·Break·Chance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### float GetGreedDonationBreakChance ( ) {: .copyable aria-label='Functions' }

___

### Get·Head·Color () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [SkinColor](enums/SkinColor.md) GetHeadColor ( ) {: .copyable aria-label='Functions' }

___

### Get·Head·Direction () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Direction](enums/Direction.md) GetHeadDirection ( ) {: .copyable aria-label='Functions' }

___

### Get·Heart·Limit () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetHeartLimit ( ) {: .copyable aria-label='Functions' }

___

### Get·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetHearts ( ) {: .copyable aria-label='Functions' }

返回玩家在心容器和骨心中的红心数量。1 个单位是半颗红心。

___

### Get·Item·State () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetItemState ( ) {: .copyable aria-label='Functions' }

___

### Get·Jar·Flies () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetJarFlies ( ) {: .copyable aria-label='Functions' }

___

### Get·Jar·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetJarHearts ( ) {: .copyable aria-label='Functions' }

___

### Get·Laser·Offset () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetLaserOffset ( [LaserOffset](enums/LaserOffset.md) ID, [Vector](Vector.md) Direction ) {: .copyable aria-label='Functions' }

___

### Get·Last·Action·Triggers () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetLastActionTriggers ( ) {: .copyable aria-label='Functions' }

___

### Get·Last·Damage·Flags () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetLastDamageFlags ( ) {: .copyable aria-label='Functions' }

___

### Get·Last·Damage·Source () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [EntityRef](EntityRef.md) GetLastDamageSource ( ) {: .copyable aria-label='Functions' }

___

### Get·Last·Direction () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetLastDirection ( ) {: .copyable aria-label='Functions' }

___

### Get·Main·Twin () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityPlayer](EntityPlayer.md) GetMainTwin ( ) {: .copyable aria-label='Functions' }

返回成对角色的主玩家或具有多种形态的角色的主形态。

- 当在雅各布或以扫身上调用时，返回雅各布。
- 当在堕化的遗骸或堕化的遗骸之魂身上调用时，返回堕化的遗骸。
- 当在堕化拉撒路或死亡的堕化拉撒路身上调用时，返回他们自己。如果玩家拥有长子权，则返回堕化的拉撒路。
- 当在任何其他角色上调用时，返回该角色。

___

### Get·Max·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetMaxHearts ( ) {: .copyable aria-label='Functions' }

返回玩家的心之容器数量。1 个单位是半颗心之容器。

___

### Get·Max·Pocket·Items () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetMaxPocketItems ( ) {: .copyable aria-label='Functions' }

获取玩家可以携带的道具数量。（默认 1，拥有多指畸形或类似效果时为 2）

If you have a pocket active, it also increments the number by one.

___

<div class="rgon-extension" markdown="1">

### GetMaxPocketItems () {: aria-label='Functions' }
#### int GetMaxPocketItems ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

</div>

### Get·Max·Poop·Mana () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetMaxPoopMana ( ) {: .copyable aria-label='Functions' }

返回玩家可以持有的最大粪便消耗品数量。

___

### Get·Max·Trinkets () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetMaxTrinkets ( ) {: .copyable aria-label='Functions' }

返回玩家可以携带的最大饰品数量。（默认 1，拥有妈妈的钱包或类似效果时为 2）

___

### Get·Modeling·Clay·Effect () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetModelingClayEffect ( ) {: .copyable aria-label='Functions' }

___

### Get·Movement·Direction () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Direction](enums/Direction.md) GetMovementDirection ( ) {: .copyable aria-label='Functions' }

___

### Get·Movement·Input () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetMovementInput ( ) {: .copyable aria-label='Functions' }

___

### Get·Movement·Joystick () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetMovementJoystick ( ) {: .copyable aria-label='Functions' }

___

### Get·Movement·Vector () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetMovementVector ( ) {: .copyable aria-label='Functions' }

___

### Get·Multi·Shot·Params () {: aria-label='Functions' }
[ ](#){: .rep .tooltip .badge }
#### MultiShotParams GetMultiShotParams ( [WeaponType](enums/WeaponType.md) WeaponType = WeaponType.WEAPON_TEARS ) {: .copyable aria-label='Functions' }

???+ bug "Bug"

    自从它返回的 UserData 不能直接编辑，因此此函数的返回值只能与 [GetMultiShotPositionVelocity()](#getmultishotpositionvelocity) 函数结合使用。
___

<div class="rgon-extension" markdown="1">

### GetMultiShotParams () {: aria-label='Modified Functions' }
#### [MultiShotParams](MultiShotParams.md) GetMultiShotParams ( [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) WeaponType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
现在返回一个合适的 `MultiShotParams` 对象。

</div>

### Get·Multi·Shot·Position·Velocity () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### [PosVel](PlayerTypes_PosVel.md) GetMultiShotPositionVelocity ( int LoopIndex, [WeaponType](enums/WeaponType.md) Weapon, [Vector](Vector.md) ShotDirection, float ShotSpeed, MultiShotParams params ) {: .copyable aria-label='Functions' }

调用此函数时，请在循环中使用，其中 LoopIndex 是 0 到当前 MultiShotParams 包含的泪水数量之间的数字。由于 MultiShotParams 目前无法通过 modding api 访问，因此您需要找到其他方法来获取该数量。

???+ bug "Removed Function"

    这个函数自忏悔版本 `v1.7.9b.J835` 以来不再存在！

___

<div class="rgon-extension" markdown="1">

### GetMultiShotPositionVelocity () {: aria-label='Modified Functions' }
#### [PosVel](https://wofsauge.github.io/IsaacDocs/rep/PlayerTypes_PosVel.html) GetMultiShotPositionVelocity ( int LoopIndex, [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) WeaponType, [Vector](Vector.md) ShotDirection, float ShotSpeed, [MultiShotParams](MultiShotParams.md) Params ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
与原版函数相比，此实现进一步增强，若 LoopIndex 高于 [MultiShotParams:GetNumTears()](MultiShotParams.md#getnumtears) 则会抛出错误。此函数在 1.7.8 之后的某个时间从 API 中消失了。

</div>

### Get·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### string GetName ( ) {: .copyable aria-label='Functions' }

返回玩家的名字(Isaac, Cain, Azazel,...)

___

### Get·NPCTarget () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) GetNPCTarget ( ) {: .copyable aria-label='Functions' }

同样，这个函数通常返回玩家。然而，在某些情况下，NPC 可以被重定向攻击另一个目标，在这种情况下，这个函数将返回替代目标（例如，在使用最好的朋友之后）。
___

### Get·Num·Blue·Flies () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetNumBlueFlies ( ) {: .copyable aria-label='Functions' }

___

### Get·Num·Blue·Spiders () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetNumBlueSpiders ( ) {: .copyable aria-label='Functions' }

___

### Get·Num·Bombs () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetNumBombs ( ) {: .copyable aria-label='Functions' }

___

### Get·Num·Coins () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetNumCoins ( ) {: .copyable aria-label='Functions' }

___

### Get·Num·Giga·Bombs () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetNumGigaBombs ( ) {: .copyable aria-label='Functions' }

___

### Get·Num·Keys () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetNumKeys ( ) {: .copyable aria-label='Functions' }

___

### Get·Other·Twin () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityPlayer](EntityPlayer.md) GetOtherTwin ( ) {: .copyable aria-label='Functions' }

返回双人角色的另一个角色或具有多种形式的角色的另一种形态。

- 当在雅各布身上调用时，返回以扫
- 当在以扫身上调用时，返回雅各布。
- 当在堕化遗骸身上调用时，返回堕化遗骸之魂。
- 当在堕化遗骸之魂上调用时，返回堕化遗骸。
- 当在堕化拉撒路身上调用时，仅当玩家拥有长子权时，它才会返回死亡的堕化拉撒路。否则，它返回 nil。
- 当在任何其他角色上调用时，返回 nil。
___

### Get·Pill () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [PillColor](enums/PillColor.md) GetPill ( int SlotId ) {: .copyable aria-label='Functions' data-altreturn='0' }

获得玩家在给定物品槽中持有的药丸的 ID (0 = 主槽, 1 = 副槽, 2 或 3) 当在给定槽中没有药丸时返回 `0`。
___

### Get·Pill·RNG () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [RNG](RNG.md) GetPillRNG ( [PillEffect](enums/PillEffect.md) ID ) {: .copyable aria-label='Functions' }

___

### Get·Player·Type () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [PlayerType](enums/PlayerType.md) GetPlayerType ( ) {: .copyable aria-label='Functions' }

___

### Get·Pocket·Item () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const PlayerPocketItem GetPocketItem ( int SlotId ) {: .copyable aria-label='Functions' }

获得玩家在给定物品槽中持有的口袋物品 (卡牌、药丸、符文) 的用户数据。

???+ bug "Bugs"

    此函数返回用户数据，无法处理。因此它是损坏的，不应使用！
___

<div class="rgon-extension" markdown="1">

### GetPocketItem () {: aria-label='Modified Functions' }
#### [PocketItem](PocketItem.md) GetPocketItem ( [PillCardSlot](enums/PillCardSlot.md) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
获取指定口袋槽中的卡片/药丸/符文。现在返回一个合适的 `PocketItem` 对象。

</div>

### Get·Poop·Mana () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetPoopMana ( ) {: .copyable aria-label='Functions' }

返回玩家当前持有的粪便数量

___

### Get·Poop·Spell () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [PoopSpellType](enums/PoopSpellType.md) GetPoopSpell ( int Position ) {: .copyable aria-label='Functions' }

返回玩家粪便队列中给定位置的粪便类型

___

### Get·Recent·Movement·Vector () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetRecentMovementVector ( ) {: .copyable aria-label='Functions' }

返回驱动玩家移动的摇杆方向，同时考虑到某些修饰符，例如禁用的控制和种子效果。

___

### Get·Rotten·Hearts () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetRottenHearts ( ) {: .copyable aria-label='Functions' }

___

### Get·Shooting·Input () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetShootingInput ( ) {: .copyable aria-label='Functions' }

返回一个向量，表示该玩家正在按下的射击输入方向。

???- info "Shooting Angle diagram"

    ![GetShootingInput diagram](images/infographics/GetShootingInput.png){: width='250' }

___

### Get·Shooting·Joystick () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetShootingJoystick ( ) {: .copyable aria-label='Functions' }

返回一个向量，表示该玩家正在按下的射击输入方向。

可以查看 [GetShootingInput](#getshootinginput) 方法的图像。

___

### Get·Smooth·Body·Rotation () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### float GetSmoothBodyRotation ( ) {: .copyable aria-label='Functions' }

___

### Get·Soul·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int GetSoulCharge ( ) {: .copyable aria-label='Functions' }

返回玩家当前的魂心充能的量。

___

### Get·Soul·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetSoulHearts ( ) {: .copyable aria-label='Functions' }

返回玩家当前的魂心数量。1 个单位是半颗心。

???- note "Notes"

    黑心计入此总数，因为游戏将其视为魂心。

___

### Get·Sub·Player () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityPlayer](EntityPlayer.md) GetSubPlayer ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

返回堕化遗骸的另一种形式。

___

### Get·Tear·Hit·Params () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [TearParams](TearParams.md) GetTearHitParams ( [WeaponType](enums/WeaponType.md) WeaponType, float DamageScale = 1, int TearDisplacement = 1, Entity Source = nil ) {: .copyable aria-label='Functions' }

被用于命中时计算的眼泪参数 (例如：严厉的爱，普通感冒)，DamageScale 用于基于伤害的缩放计算

___

### Get·Tear·Movement·Inheritance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetTearMovementInheritance ( [Vector](Vector.md) ShotDirection ) {: .copyable aria-label='Functions' }

___

### Get·Tear·Poison·Damage () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### float GetTearPoisonDamage ( ) {: .copyable aria-label='Functions' }

___

### Get·Tear·Range·Modifier () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetTearRangeModifier ( ) {: .copyable aria-label='Functions' }

对于实验性疗法，返回 `-1`、`0` 或 `1`，具体取决于范围的掷骰结果。

___

<div class="rgon-extension" markdown="1">

### GetTearRangeModifier () {: aria-label='Functions' }
#### int GetTearRangeModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used for Experimental Treatment and for stat boosts from Void.

Adds `2.5 * modifier` to the player's TearRange.

Experimental Treatment adds `-1`, `0` or `1` depending on the range rolled. Void may randomly add `1`.

___

</div>

### Get·Total·Damage·Taken () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetTotalDamageTaken ( ) {: .copyable aria-label='Functions' }

___

### Get·Tractor·Beam () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) GetTractorBeam ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

___

### Get·Trinket () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [TrinketType](enums/TrinketType.md) GetTrinket ( int TrinketIndex ) {: .copyable aria-label='Functions' data-altreturn='0' }

获取玩家在指定饰品槽（0 或 1）中持有的饰品 ID。当指定槽位没有饰品时，返回 `0`。
___

### Get·Trinket·Multiplier () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetTrinketMultiplier ( [TrinketType](enums/TrinketType.md) TrinketID ) {: .copyable aria-label='Functions' }
Gets the multiplier of a given Trinket effect. This is analog to the number of times the trinket effect is applied.

???- info "Multiplier Breakdown"
    * Per normal trinket of this type equipped / gulped : +1
    * Per golden trinket of this type equipped / gulped : +2
    * Mom's Box equipped : +1 (does not stack)
___

### Get·Trinket·RNG () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [RNG](RNG.md) GetTrinketRNG ( [TrinketType](enums/TrinketType.md) TrinketID ) {: .copyable aria-label='Functions' }

___

### Get·Velocity·Before·Update () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) GetVelocityBeforeUpdate ( ) {: .copyable aria-label='Functions' }

___

### Get·Zodiac·Effect () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetZodiacEffect ( ) {: .copyable aria-label='Functions' }

___

### Has·Collectible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasCollectible ( [CollectibleType](enums/CollectibleType.md) Type, boolean IgnoreModifiers = false ) {: .copyable aria-label='Functions' }
**IgnoreModifiers**: If set to true, only counts collectibles the player actually owns and ignores effects granted by items like Zodiac, 3 Dollar Bill and Lemegeton

___

<div class="rgon-extension" markdown="1">

### HasCollectible () {: aria-label='Modified Functions' }
#### boolean HasCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean IgnoreModifiers = false, boolean IgnoreSpoof = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
现在接受一个 `IgnoreSpoof` 参数，该参数会忽略固有物品。

___

</div>

### Has·Curse·Mist·Effect () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasCurseMistEffect ( ) {: .copyable aria-label='Functions' }

___

### Has·Full·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasFullHearts ( ) {: .copyable aria-label='Functions' }

___

### Has·Full·Hearts·And·Soul·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasFullHeartsAndSoulHearts ( ) {: .copyable aria-label='Functions' }

___

### Has·Golden·Bomb () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasGoldenBomb ( ) {: .copyable aria-label='Functions' }

___

### Has·Golden·Key () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasGoldenKey ( ) {: .copyable aria-label='Functions' }

___

### Has·Invincibility () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasInvincibility ( [DamageFlag](enums/DamageFlag.md) Flags = 0 ) {: .copyable aria-label='Functions' }
returns true when player is in an invincibility state
___

### Has·Player·Form () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasPlayerForm ( [PlayerForm](enums/PlayerForm.md) Form ) {: .copyable aria-label='Functions' }

___

### Has·Timed·Item () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasTimedItem ( ) {: .copyable aria-label='Functions' }
Returns true if you have a timed active item *(such as Brown Nugget)* in the first active slot

___

### Has·Trinket () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean HasTrinket ( [TrinketType](enums/TrinketType.md) Type, boolean IgnoreModifiers = false ) {: .copyable aria-label='Functions' }
**IgnoreModifiers**: If set to true, only counts trinkets the player actually holds and ignores effects granted by other items

___

### Has·Weapon·Type () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasWeaponType ( [WeaponType](enums/WeaponType.md) WeaponType ) {: .copyable aria-label='Functions' }

___

### Init·Baby·Skin () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void InitBabySkin ( ) {: .copyable aria-label='Functions' }

___

### Is·Black·Heart () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsBlackHeart ( int Heart ) {: .copyable aria-label='Functions' }
This can be used instead of GetBlackHearts to figure out which soul hearts are black hearts.

???- example "Example"
    Imagine we have the following setup of hearts, where S is a soul heart and B is a black heart:

    ```
    B S S B B S S B B
    ```

    Each soul heart is composed of two halves. Only the odd numbers seem to trigger this function. Even numbers always return false. The following assumes that the indexing starts at 1 rather than 0, but regardless, it's the odd numbers that work here. The indexing here only applies to your soul/black hearts. It doesn't matter if you have other red/bone/etc hearts.

    ```
    B(1,2) S(3,4) S(5,6) B(7,8) B(9,10) S(11,12) S(13,14) B(15,16) B(17,18)
    ```

    ```lua
    Isaac.GetPlayer():IsBlackHeart(1) -- returns true (black heart)
    Isaac.GetPlayer():IsBlackHeart(2) -- returns false (not useful)
    Isaac.GetPlayer():IsBlackHeart(3) -- returns false (soul heart)
    -- 1,7,9,15,17 all return true (black hearts)
    ```

    Quick code example to parse soul hearts vs black hearts:

    ```lua
    -- if you setup your hearts as described above then you'll get the following value
    -- GetSoulHearts = 18
    local tbl = {}
    local player = Isaac.GetPlayer()
    -- loop over all the soul heart odd indexes
    for i = 1, player:GetSoulHearts(), 2 do
      table.insert(tbl, player:IsBlackHeart(i) and 'B' or 'S')
    end
    if player:GetSoulHearts() % 2 ~= 0 then
      tbl[#tbl] = string.lower(tbl[#tbl]) -- lowercase to indicate half heart at end
    end
    print(table.concat(tbl, ' ')) -- prints: B S S B B S S B B
    ```

___

### Is·Bone·Heart () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsBoneHeart ( int heart ) {: .copyable aria-label='Functions' }
This can be used to figure out the ordering of bone hearts amongst soul/black hearts.

???- example "Example"
    Imagine we have the following setup of hearts:

    ```
    BONE SOUL BONE BLACK BONE
    ```

    The indexing here is for whole hearts, and the index starts at 0. The indexing takes into account bone/soul/black hearts. It doesn't matter if you have other heart types (e.g. red hearts).

    ```lua
    Isaac.GetPlayer():IsBoneHeart(0) -- returns true (bone heart)
    Isaac.GetPlayer():IsBoneHeart(1) -- returns false (soul heart)
    Isaac.GetPlayer():IsBoneHeart(3) -- returns false (black heart)
    -- 0,2,4 all return true (bone hearts)
    ```

    Quick code example to parse soul hearts vs black hearts vs bone hearts:

    ```lua
    -- if you setup your hearts as described above then you'll get the following values
    -- GetSoulHearts = 4
    -- GetBoneHearts = 3
    local tbl = {}
    local player = Isaac.GetPlayer()
    -- first, figure out the soul/black heart order
    for i = 1, player:GetSoulHearts(), 2 do
      table.insert(tbl, player:IsBlackHeart(i) and 'BLACK' or 'SOUL')
    end
    if player:GetSoulHearts() % 2 ~= 0 then
      tbl[#tbl] = string.lower(tbl[#tbl]) -- lowercase to indicate half heart at end
    end
    -- second, figure out where bone hearts fit into the soul/black/bone heart order
    -- divide soul hearts by 2 to get whole hearts, bone hearts are already in whole heart increments
    for i = 0, math.ceil(player:GetSoulHearts() / 2) + player:GetBoneHearts() - 1 do
      if player:IsBoneHeart(i) then
        table.insert(tbl, i + 1, 'BONE')
      end
    end
    print(table.concat(tbl, ' ')) -- prints: BONE SOUL BONE BLACK BONE
    ```

___

### Is·Coop·Ghost () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean IsCoopGhost ( ) {: .copyable aria-label='Functions' }
In a multiplayer game, if a player dies, they will return as a tiny ghost. This method returns true if the player is a co-op ghost.

___

### Is·Extra·Animation·Finished () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsExtraAnimationFinished ( ) {: .copyable aria-label='Functions' }

___

### Is·Full·Sprite·Rendering () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsFullSpriteRendering ( ) {: .copyable aria-label='Functions' }

___

### Is·Held·Item·Visible () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsHeldItemVisible ( ) {: .copyable aria-label='Functions' }

___

### Is·Holding·Item () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsHoldingItem ( ) {: .copyable aria-label='Functions' }
Is Player holding up an item (card/collectible/etc)
___

### Is·Item·Queue·Empty () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsItemQueueEmpty ( ) {: .copyable aria-label='Functions' }

___

### Is·P2Appearing () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsP2Appearing ( ) {: .copyable aria-label='Functions' }

___

### Is·Pos·In·Spot·Light () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsPosInSpotLight ( [Vector](Vector.md) Position ) {: .copyable aria-label='Functions' }
Returns true if the `position` is in the AOE of the **Night Light** item.

___

### Is·Sub·Player () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsSubPlayer ( ) {: .copyable aria-label='Functions' }
Returns true if the player object was returned from the `EntityPlayer.GetSubPlayer` method. (This method is not related to multiplayer.)

Additionally, this also returns true for the player object representing Dead Tainted Lazarus that fires at the beginning of the run in the PostPlayerInit callback. (The PostPlayerInit callback fires first for Dead Tainted Lazarus before firing for the normal Tainted Lazarus.)

___

### Needs·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean NeedsCharge ( [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

This will always return false for active items that have `chargetype="special"` set in the `items.xml` file, even if they are not fully charged.

___

### Play·Extra·Animation () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PlayExtraAnimation ( string Animation ) {: .copyable aria-label='Functions' }

___

### Queue·Extra·Animation () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void QueueExtraAnimation ( string Animation ) {: .copyable aria-label='Functions' }

___

### Queue·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void QueueItem ( [ItemConfigItem](ItemConfig_Item.md) Item, int Charge = 0, boolean Touched = false, boolean Golden = false, int VarData = 0 ) {: .copyable aria-label='Functions' }
When the player touches a collectible or trinket, they are not granted it immediately. Instead, the item is queued for the duration of the animation where the player holds the item above their head. When the animation is finished, the item in the queue will be granted. This method adds a new item to the item queue. If the player is not currently playing an animation, then the queued item will simply be awarded instantly.

Also see `FlushQueueItem()`, `IsItemQueueEmpty()`, and `QueuedItem`.
___

### Remove·Black·Heart () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveBlackHeart ( int BlackHeart ) {: .copyable aria-label='Functions' }

___

### Remove·Blue·Fly () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveBlueFly ( ) {: .copyable aria-label='Functions' }

___

### Remove·Blue·Spider () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveBlueSpider ( ) {: .copyable aria-label='Functions' }

___

### Remove·Collectible () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void RemoveCollectible ( [CollectibleType](enums/CollectibleType.md) Type, boolean IgnoreModifiers = false, [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY, boolean RemoveFromPlayerForm = true ) {: .copyable aria-label='Functions' }
**IgnoreModifiers**: Ignores collectible effects granted by other items (i.e. Void)

**Slot**: Sets the active slot this collectible should be removed from

**RemoveFromPlayerForm**: If successfully removed and part of a transformation, decrease that transformation's counter by 1
___

### Remove·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveCostume ( [ItemConfigItem](ItemConfig_Item.md) Item ) {: .copyable aria-label='Functions' }
Removes a given costume based on its item config entry.

???- example "Example code"
    This code removes the costume of the Spoon Bender collectible.
    ```lua
    local player = Isaac.GetPlayer()
    local itemConfig = Isaac.GetItemConfig()
    local itemConfigItem = itemConfig:GetCollectible(CollectibleType.COLLECTIBLE_SPOON_BENDER)
    player:RemoveCostume(itemConfigItem)
    ```

___

### Remove·Curse·Mist·Effect () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void RemoveCurseMistEffect ( ) {: .copyable aria-label='Functions' }

___

### Remove·Golden·Bomb () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveGoldenBomb ( ) {: .copyable aria-label='Functions' }

___

### Remove·Golden·Key () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveGoldenKey ( ) {: .copyable aria-label='Functions' }

___

### Remove·Skin·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveSkinCostume ( ) {: .copyable aria-label='Functions' }
Removes player-specific costumes like Magdalene's hair or Cain's eyepatch.

___

### Render·Body () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderBody ( [Vector](Vector.md) position ) {: .copyable aria-label='Functions' }

___

### Render·Glow () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderGlow ( [Vector](Vector.md) position ) {: .copyable aria-label='Functions' }

___

### Render·Head () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderHead ( [Vector](Vector.md) position ) {: .copyable aria-label='Functions' }

___

### Render·Top () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderTop ( [Vector](Vector.md) position ) {: .copyable aria-label='Functions' }

___

### Replace·Costume·Sprite () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ReplaceCostumeSprite ( [ItemConfigItem](ItemConfig_Item.md) Item, string SpritePath, int SpriteId ) {: .copyable aria-label='Functions' }

___

### Reset·Damage·Cooldown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ResetDamageCooldown ( ) {: .copyable aria-label='Functions' }

___

### Reset·Item·State () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ResetItemState ( ) {: .copyable aria-label='Functions' }
[Room](Room.md) transitions call this to prevent lock ups.
___

### Respawn·Familiars () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RespawnFamiliars ( ) {: .copyable aria-label='Functions' }
Respawns all familiars associated to the player.

___

### Revive () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Revive ( ) {: .copyable aria-label='Functions' }
Revives the player.

???+ bug "Bugs"
    Exiting the run at any point after this function is called will make it so that the run can't be continued.
___

### Set·Active·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetActiveCharge ( int Charge, [ActiveSlot](enums/ActiveSlot.md) ActiveSlot = ActiveSlot.SLOT_PRIMARY ) {: .copyable aria-label='Functions' }

___

### Set·Blood·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetBloodCharge ( int Amount ) {: .copyable aria-label='Functions' }

Sets the amount of Blood Charge the player has. Blood Charge does not do anything on characters besides Tainted Bethany.

___

### Set·Card () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetCard ( int SlotId, [Card](enums/Card.md) ID ) {: .copyable aria-label='Functions' }

Change the card/rune the player is holding in the given itemslot (0 or 1).
___

### Set·Full·Hearts () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetFullHearts ( ) {: .copyable aria-label='Functions' }

___

### Set·Min·Damage·Cooldown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetMinDamageCooldown ( int DamageCooldown ) {: .copyable aria-label='Functions' }

___

### Set·Pill () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetPill ( int SlotId, [PillColor](enums/PillColor.md) Pill ) {: .copyable aria-label='Functions' }

Change the pill the player is holding in the given itemslot (0 or 1).

___

### Set·Pocket·Active·Item() {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetPocketActiveItem ( [CollectibleType](enums/CollectibleType.md) Type, [ActiveSlot](enums/ActiveSlot.md) Slot, boolean KeepInPools ) {: .copyable aria-label='Functions' }

Sets the player's pocket active item to the given active item.
Slot can be either SLOT_POCKET or SLOT_POCKET2.
Items added to SLOT_POCKET2 will always be removed upon being used.
If KeepInPools is set to true, the item will not be removed from the item pools.
Use this to let the player start with a custom active item in their pocket active slot right away.

???+ bug "Bugs"
    Calling this function inside PostPlayerInit callback causes a crash when continuing a saved run after closing and reopening the game, unless KeepInPools argument is set to true.
___

### Set·Shooting·Cooldown () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetShootingCooldown ( int Cooldown ) {: .copyable aria-label='Functions' }

___

### Set·Soul·Charge () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetSoulCharge ( int Amount ) {: .copyable aria-label='Functions' }

Sets the amount of Soul Charge the player has. Soul Charge does not do anything on characters besides Bethany.

___

### Set·Target·Trap·Door () {: aria-label='Functions' }
[ ](#){: .abp .tooltip .badge }
#### void SetTargetTrapDoor ( [GridEntity](GridEntity.md) TrapDoor ) {: .copyable aria-label='Functions' }

This function got removed with Repentance.

___

### Shoot·Red·Candle () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ShootRedCandle ( [Vector](Vector.md) Direction ) {: .copyable aria-label='Functions' }
for ghost pepper item + poop and farts
___

<div class="rgon-extension" markdown="1">

### Shoot·Red·Candle () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ShootRedCandle ( [Vector](Vector.md) Direction ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
for ghost pepper item + poop and farts
___

</div>

### Spawn·Maw·Of·Void () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityLaser](EntityLaser.md) SpawnMawOfVoid ( int Timeout ) {: .copyable aria-label='Functions' }

___

### Stop·Extra·Animation () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void StopExtraAnimation ( ) {: .copyable aria-label='Functions' }

___

### Swap·Active·Items () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SwapActiveItems ( ) {: .copyable aria-label='Functions' }
Swaps active items in the **Schoolbag** activeslot

___

### Throw·Blue·Spider () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) ThrowBlueSpider ( [Vector](Vector.md) Position, [Vector](Vector.md) Target ) {: .copyable aria-label='Functions' }

___

### Throw·Friendly·Dip () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) ThrowFriendlyDip ( int Subtype, [Vector](Vector.md) Position, [Vector](Vector.md) Target ) {: .copyable aria-label='Functions' }

???- note "Dip Subtypes"
    ```lua
    0: normal
    1: red
    2: corny
    3: golden
    4: rainbow
    5: black
    6: holy
    12: stone
    13: flaming
    14: poison
    20: brownie
    ```
___

### Throw·Held·Entity () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [Entity](Entity.md) ThrowHeldEntity ( [Vector](Vector.md) Velocity ) {: .copyable aria-label='Functions' }

___

### Trigger·Book·Of·Virtues () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void TriggerBookOfVirtues ( [CollectibleType](enums/CollectibleType.md) Type = CollectibleType.COLLECTIBLE_NULL, int Charge = 0 ) {: .copyable aria-label='Functions' }
Works only if the player has the **Book of Virtues** item, otherwise does nothing

___

### Try·Hold·Entity () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean TryHoldEntity ( [Entity](Entity.md) Entity ) {: .copyable aria-label='Functions' }

___

### Try·Hold·Trinket () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean TryHoldTrinket ( [TrinketType](enums/TrinketType.md) Type ) {: .copyable aria-label='Functions' }
Returns true if an active item pickup cooldown is over. returns true if trinket can be added, else false
___

### Try·Remove·Collectible·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void TryRemoveCollectibleCostume ( [CollectibleType](enums/CollectibleType.md) Collectible, boolean KeepPersistent ) {: .copyable aria-label='Functions' }
Tries to remove a costume of the given collectible. `KeepPersistent` is used to define if persistent costumes should be removed. If its set to `false`, it will only remove temporary costumes.

???- example "Example code"
    This code removes the costume of the Spoon Bender collectible.
    ```lua
    local player = Isaac.GetPlayer()
    player:TryRemoveCollectibleCostume(CollectibleType.COLLECTIBLE_SPOON_BENDER, false)
    ```
___

### Try·Remove·Null·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void TryRemoveNullCostume ( [NullItemID](enums/NullItemID.md) NullId ) {: .copyable aria-label='Functions' }

___

### Try·Remove·Trinket () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean TryRemoveTrinket ( [TrinketType](enums/TrinketType.md) Type ) {: .copyable aria-label='Functions' }

___

### Try·Remove·Trinket·Costume () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void TryRemoveTrinketCostume ( [TrinketType](enums/TrinketType.md) Trinket ) {: .copyable aria-label='Functions' }
Tries to remove a trinket costume
___

### Try·Use·Key () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean TryUseKey ( ) {: .copyable aria-label='Functions' }

___

### Update·Can·Shoot () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void UpdateCanShoot ( ) {: .copyable aria-label='Functions' }

___

### Use·Active·Item () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void UseActiveItem ( [CollectibleType](enums/CollectibleType.md) Item, [UseFlags](enums/UseFlag.md) UseFlags = 0, [ActiveSlot](enums/ActiveSlot.md) Slot = -1, int CustomVarData = 0 ) {: .copyable aria-label='Functions' }

#### void UseActiveItem ( [CollectibleType](enums/CollectibleType.md) Item, boolean ShowAnim = false, boolean KeepActiveItem = false, boolean AllowNonMainPlayer = true, boolean ToAddCostume = false, [ActiveSlot](enums/ActiveSlot.md) Slot = -1, int CustomVarData = 0 ) {: .copyable .secondH4 aria-label='Functions' }
**Slot**: The active slot this item was used from (set to -1 if this item wasn't triggered by any active slot)

**CustomVarData**: `UseFlag.USE_CUSTOMVARDATA` needs to be provided in `UseFlags` otherwise this field is ignored

???- note "Notes"
	This method will increment the number of CollectibleEffects (see [Temporary Effects](TemporaryEffects.md)) of the passed item by 1 for the current room, and will trigger any associated MC_USE_ITEM callbacks. As of Repentance, this method can also be used on Passive and Familiar ItemTypes.
___

<div class="rgon-extension" markdown="1">

### UseActiveItem () {: aria-label=' Modified Functions' }
#### [UseActiveItemResultFlags](enums/UseActiveItemResultFlag.md) UseActiveItem ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Item, [UseFlags](https://wofsauge.github.io/IsaacDocs/rep/enums/UseFlag.html) UseFlags = 0, [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot = -1, int CustomVarData = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Now has a return value, a bitmask of [UseActiveItemResultFlags](enums/UseActiveItemResultFlag.md).

???+ note "Return behavior"
	`UseActiveItemResultFlags.REMOVE` is possible to not be passed even if the item would be removed normally. It will not be passed if any of the following conditions are met:
	- `UseFlag.USE_OWNED` is not passed for vanilla items.
	- `UseFlag.USE_VOID` is passed for any items.
___

## Modified Variables
___

</div>

### Use·Card () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void UseCard ( [Card](enums/Card.md) ID, [UseFlags](enums/UseFlag.md) UseFlags = 0 ) {: .copyable aria-label='Functions' }

___

### Use·Pill () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void UsePill ( [PillEffect](enums/PillEffect.md) ID, [PillColor](enums/PillColor.md) PillColor, [UseFlags](enums/UseFlag.md) UseFlags = 0  ) {: .copyable aria-label='Functions' }

___

### Use·Poop·Spell () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void UsePoopSpell ( [PoopSpellType](enums/PoopSpellType.md) type ) {: .copyable aria-label='Functions' }
Triggers one of Tainted ???'s poop spells (see [PoopSpellType](enums/PoopSpellType.md) enum)

___

### Will·Player·Revive () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean WillPlayerRevive ( ) {: .copyable aria-label='Functions' }
This function will return true if the player has one or more extra lives or if a conditional revival item will work on the next death.

Right now, there are 3 items that grant conditional extra lives:

* Guppy's Collar - This function will successfully predict whether or not the next revive from Guppy's Collar will work or not. (50% chance)
* Broken Ankh - This function will successfully predict whether or not the next revive from Broken Ankh will work or not. (22.22% chance)
* Mysterious Paper - This function will only successfully predict the revive from Missing Poster every 4 frames, because it evaluates only one of its 4 possible item effects each frame.

___
## Variables

### Baby·Skin {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [BabySubType](enums/BabySubType.md) BabySkin  {: .copyable aria-label='Variables' }
P2 Skin section Used to hold the selected skin (in case of glitched baby it will pick a random one)

???+ bug "Bugs"
    This variable actually contains userdata and is not usable within API. Attempt to change it will results in a crash.

___

<div class="rgon-extension" markdown="1">

### BabySkin {: aria-label='Modified Variables' }
#### [BabySubType](https://wofsauge.github.io/IsaacDocs/rep/enums/BabySubType.html) BabySkin [ ](#){: .rgonorplus .tooltip .badge }  {: .copyable aria-label='Modified Variables' }
与默认行为相同，但现在会返回正确的整数值而非用户数据。

___

</div>

### Can·Fly {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanFly  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. Can the player fly over rocks and pits?
___

### Controller·Index {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const int ControllerIndex  {: .copyable aria-label='Variables' }

___

### Controls·Cooldown {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ControlsCooldown  {: .copyable aria-label='Variables' }
Specifies the number of frames the player's controls should be disabled. Decrements by 1 every frame, until it reaches 0. Used by the paralysis pill effect.

At 0 or less, does not block player control.
___

### Controls·Enabled {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean ControlsEnabled  {: .copyable aria-label='Variables' }

___

### Damage {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Damage  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Damage Stat.**  How much damage do the players tears or other main weapons do?
___

### Fire·Delay {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float FireDelay  {: .copyable aria-label='Variables' }
How long until the player can spawn their next tear?

???- note "Version Difference"
	In the Afterbirth+ version of the modding api, this variable is an integer

___

### Friend·Ball·Enemy {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const EntityDesc FriendBallEnemy  {: .copyable aria-label='Variables' }

???+ bug "Bugs"
    This function returns userdata that cant be edited or accessed.
___

<div class="rgon-extension" markdown="1">

### FriendBallEnemy {: aria-label='Modified Variables' }
#### [EntityDesc](EntityDesc.md) FriendBallEnemy [ ](#){: .rgonorplus .tooltip .badge }  {: .copyable aria-label='Modified Variables' }
Same as default, but now returns a proper class instead of userdata.

___


## Functions

</div>

### Head·Frame·Delay {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int HeadFrameDelay  {: .copyable aria-label='Variables' }
Specifies the number of frames the player's head should be playing the shooting animation. Decrements by 1 every frame, until it reaches -1.

At negative values, the player's head does not play the shooting animation.
___

### IBS·Charge {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### float IBSCharge  {: .copyable aria-label='Variables' }
Internally used by IBS, increases based on damage dealt, range is 0-1
___

### Item·Hold·Cooldown {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int ItemHoldCooldown  {: .copyable aria-label='Variables' }
Used for avoiding player get stucked between rocks when switching a flying item with other active item.
___

### Laser·Color {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Color](Color.md) LaserColor  {: .copyable aria-label='Variables' }

___

### Luck {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Luck  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Luck Stat.**  Better luck generally means better random events.
___

### Max·Fire·Delay {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float MaxFireDelay  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Tears Stat.**  How long between each tear can spawn?

???- note "Version Difference"
	In the Afterbirth+ version of the modding api, this variable is an integer

___

### Move·Speed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float MoveSpeed  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the Speed Stat.**  How fast can the player move?
___

### Queued·Item {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [QueueItemData](QueueItemData.md) QueuedItem  {: .copyable aria-label='Variables' }

- When Isaac picks up a collectible or a trinket, he holds it above his head for a while. At this point, the collectible/trinket is not actually put into his inventory yet.
- In other words, the item is queued for insertion until the animation completes, at which point the queue is processed and the item is inserted.
- `QueuedItem` holds a object of type `QueueItemData` that describes the item that a player is currently holding above their head.
- `QueuedItem` is never nil, even if the player is not currently holding up any item. (However, `player.QueuedItem.Item` will be nil if they are not currently holding up any item.)
- This only stores data for collectibles and trinkets. It does not store any data for pocket items (even though Isaac plays a similar "holding above head" animation for pocket items).
- Also see `FlushQueueItem()`, `IsItemQueueEmpty()`, and `QueueItem()`.
___

### Samson·Berserk·Charge {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### int SamsonBerserkCharge  {: .copyable aria-label='Variables' }
Internally used by Tainted Samson, increases based on damage dealt, range is 0-100000
___

### Secondary·Active·Item {: aria-label='Variables' }
[ ](#){: .abp .tooltip .badge }
#### [ActiveItemDesc](PlayerTypes_ActiveItemDesc.md) SecondaryActiveItem  {: .copyable aria-label='Variables' data-altreturn='nil' }

???+ bug "Bug"
    This function does not exist anymore in Repentance. As of right now, there is no other function to get the [ActiveItemDesc](PlayerTypes_ActiveItemDesc.md) of any active item the player holds. Until this is fixed, this info will stay here.
___

### Shot·Speed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float ShotSpeed  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE.  **This is equal to the ShotSpeed Stat.**

Defines how fast the tear travel when spawned.

The default velocity of a tear shot is 10 times the players ShotSpeed.

___

### Tear·Color {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Color](Color.md) TearColor  {: .copyable aria-label='Variables' }

___

### Tear·Falling·Acceleration {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float TearFallingAcceleration  {: .copyable aria-label='Variables' }

___

### Tear·Falling·Speed {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float TearFallingSpeed  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How fast is the tear moving up or down when it spawns? Affects range.
___

### Tear·Flags {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [TearFlags](enums/TearFlags.md) TearFlags {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. Various [TearFlags](enums/TearFlags.md).

???- example "Example Code"
    This code makes Isaac's tears spectral.
    ```lua

    function mod:OnEvaluateTearFlags(player, flag)
        player.TearFlags = player.TearFlags | TearFlags.TEAR_SPECTRAL
    end
    mod:AddCallback(ModCallbacks.MC_EVALUATE_CACHE, mod.OnEvaluateTearFlags, CacheFlag.CACHE_TEARFLAG)
    ```

___

### Tear·Height {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float TearHeight  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How high above the ground is the tear when it spawns?

???- example "Example Code"
    This code gives Isaac a +5 range up.

    ```lua
    function mod:OnEvaluateRange(player, flag)
        -- we give -5 because the TearHeight stat is always negative; the lower the number - the further the tear travels
        player.TearHeight = player.TearHeight - 5
    end
    mod:AddCallback(ModCallbacks.MC_EVALUATE_CACHE, mod.OnEvaluateRange, CacheFlag.CACHE_RANGE)
    ```

___

### Tear·Range {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### float TearRange  {: .copyable aria-label='Variables' }
Player stat - Only change this in a callback to MC_EVALUATE_CACHE. How far should a tear go when it spawns?

???+ info "Info"
    This stat needs to be multiplied by 40, because it calculates the range based on tile length.

???- example "Example Code"
    This code gives Isaac a +2 range up.

    ```lua
    function mod:OnEvaluateRange(player, flag)
        player.TearRange = player.TearRange + (2 * 40)
    end
    mod:AddCallback(ModCallbacks.MC_EVALUATE_CACHE, mod.OnEvaluateRange, CacheFlag.CACHE_RANGE)
    ```

___

### Tears·Offset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) TearsOffset  {: .copyable aria-label='Variables' }

<div class="rgon-only" markdown="1">

### AddCollectibleEffect () {: aria-label='Modified Functions' }
#### void AddCollectibleEffect ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) CollectibleType, bool ApplyCostume = false, int Cooldown = VanillaCooldown, bool Additive = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Shortcut of TemporaryEffects:AddCollectibleEffect with extra arguments to handle cooldown. The additive parameter determines whether the cooldown should be added to the pre-existing cooldown value or set as that value. You can use negative cooldown values with additive to reduce the pre-existing cooldown.

___

### AddNullItemEffect () {: aria-label='Modified Functions' }
#### void AddNullItemEffect ( [NullItemID](https://wofsauge.github.io/IsaacDocs/rep/enums/NullItemID.html) NullItemID, bool ApplyCostume = false, int Cooldown = VanillaCooldown, bool Additive = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Shortcut of TemporaryEffects:AddNullItemEffect with extra arguments to handle cooldown. The additive parameter determines whether the cooldown should be added to the pre-existing cooldown value or set as that value. You can use negative cooldown values with additive to reduce the pre-existing cooldown.

___

### AddTrinketEffect () {: aria-label='Modified Functions' }
#### void AddTrinketEffect ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) TrinketType, bool ApplyCostume = false, int Cooldown = VanillaCooldown, bool Additive = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Shortcut of TemporaryEffects:AddTrinketEffect with extra arguments to handle cooldown. The additive parameter determines whether the cooldown should be added to the pre-existing cooldown value or set as that value. You can use negative cooldown values with additive to reduce the pre-existing cooldown.


___

### AddActiveCharge () {: aria-label='Functions' }
#### int AddActiveCharge ( int Charge, [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot = ActiveSlot.SLOT_PRIMARY, boolean FlashHUD = true, boolean Overcharge = false, boolean Force = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the true amount of charge added, which may have been capped by the targeted item's MaxCharge.

???- info "Info"

    `FlashHUD` 似乎是多余的。无论使用 `true` 还是 `false`，充能条都会闪烁。

### AddBoneOrbital () {: aria-label='Functions' }
#### void AddBoneOrbital ( [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### AddCandyHeartBonus () {: aria-label='Functions' }
#### void AddCandyHeartBonus ( [CacheFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/CacheFlag.html) CacheFlag = 0, int Amount = 1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Adds a random stat bonus as if the player had collected a heart with Candy Heart. Can specify a CacheFlag to force the bonus onto a specific stat. Stats are only applied while the player has Candy Heart.

___

### AddCustomCacheTag () {: aria-label='Functions' }
#### void AddCustomCacheTag ( string OR \{string, string, ...\}, boolean EvaluateItems = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Add CustomCacheTag(s) to be evaluated next time EvaluateItems runs (which is right now, if the optional boolean is passed).

### AddInnateCollectible () {: aria-label='Functions' }
#### void AddInnateCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, int Amount = 1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ bug "Bug"

    目前此函数会直接修改 WispCollectiblesList 的内容，因此如果此列表在精灵初始化/删除时更新，或者玩家退出游戏，你添加的固有物品将不会被保存。

### AddLeprosy () {: aria-label='Functions' }
#### void AddLeprosy ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Info"

    目前此功能仍然限制最多生成三个跟班，若要更改此限制，需要进一步修改。

### AddLocust () {: aria-label='Functions' }
#### void AddLocust ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???- info "Supported Items"

    有一些物品会生成独特的蝗虫
    - Fire Mind
    - Holy Light
    - Scorpio
    - Mutant Spider
    - 120 Volt
    - Breakfast (default)
    - Brimstone
    - Number One
    - The Inner Eye
    - The Common Cold
    - Jacob's Ladder
    - Blood of the Martyr
    - Halo of Flies
    - Spoon Bender
    - Ipecac
    - Cricket's Head

### AddSmeltedTrinket () {: aria-label='Functions' }
#### boolean AddSmeltedTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, boolean FirstTimePickingUp = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
直接将一个吞下的饰品添加到玩家的库存中。如果饰品成功添加，则返回 `true`，否则返回 `false`。

Returns ``true`` if the trinket was successfully added, otherwise ``false``.

___

### AddSoulLocketBonus () {: aria-label='Functions' }
#### void AddSoulLocketBonus ( [CacheFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/CacheFlag.html) CacheFlag = 0, int Amount = 1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Adds a random stat bonus as if the player had collected a heart with Soul Locket. Can specify a CacheFlag to force the bonus onto a specific stat. Stats are only applied while the player has Soul Locket.

___

### AddUrnSouls () {: aria-label='Functions' }
#### void AddUrnSouls ( int Count = 0 ) {: .copyable aria-label='Functions' }   [ ](#){: .rgonorplus .tooltip .badge }

___

### BlockCollectible () {: aria-label='Functions' }
#### void BlockCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) {: .copyable aria-label='Functions' }   [ ](#){: .rgonorplus .tooltip .badge }
阻止提供的 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)。这会使游戏认为你没有该物品，即使它在你的库存中。

### CanAddCollectibleToInventory () {: aria-label='Functions' }
#### boolean CanAddCollectibleToInventory ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CanCrushRocks () {: aria-label='Functions' }
#### boolean CanCrushRocks ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???- info "Info"

    如果玩家拥有以下物品/效果/变身之一，则返回 `true`。
    - The Nail
    - Thunder Thighs
    - Leo
    - Stompy
    - Mega Mush

### CanOverrideActiveItem () {: aria-label='Functions' }
#### boolean CanOverrideActiveItem ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CanUsePill () {: aria-label='Functions' }
#### boolean CanUsePill ( [PillEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/PillEffect.html) ID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
根据某些条件（通常与生命值相关），确定玩家是否可以使用给定的药丸效果。

### CheckFamiliarEx () {: aria-label='Functions' }
#### [EntityFamiliar](EntityFamiliar.md)[] CheckFamiliarEx ( int [FamiliarVariant](https://wofsauge.github.io/IsaacDocs/rep/enums/FamiliarVariant.html) Familiar, int TargetCount, [RNG](RNG.md) rng, [ItemConfigItem](ItemConfig_Item.md) SourceItemConfigItem = nil, int FamiliarSubType = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
[CheckFamiliar](https://wofsauge.github.io/IsaacDocs/rep/EntityPlayer.html#checkfamiliar) 的一个版本，它会将该函数生成的所有跟班作为一个表返回。

### ClearCollectibleAnim () {: aria-label='Functions' }
#### void ClearCollectibleAnim ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ClearQueueItem () {: aria-label='Functions' }
#### void ClearQueueItem ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CreateAfterimage () {: aria-label='Functions' }
#### void CreateAfterimage ( int Duration, [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Creates an afterimage of the player that fades over the course of the given duration, similar to those created by items such as A Pony and Mars.

___

### DropCollectible () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md) DropCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, [EntityPickup](EntityPickup.md) ExistingPedestal = nil, boolean RemoveFromPlayerForm = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

### DropCollectibleByHistoryIndex () {: aria-label='Functions' }
#### [EntityPickup](EntityPickup.md) DropCollectibleByHistoryIndex ( int Idx, [EntityPickup](EntityPickup.md) ExistingPedestal = nil ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果设置了 `ExistingPedestal`，则该基座中包含的收藏品将被替换为掉落的收藏品，而不是生成一个新的基座。

### EnableWeaponType () {: aria-label='Functions' }
#### void EnableWeaponType ( [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) Weapon, boolean Set ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### FireBrimstoneBall () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) FireBrimstoneBall ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, [Vector](Vector.md) Offset = Vector.Zero ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Info"

___

### GetActionHoldDrop () {: aria-label='Functions' }
#### int GetActionHoldDrop ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
How long the player holds the drop-button.
___

### GetActiveItemDesc () {: aria-label='Functions' }
#### [ActiveItemDesc](https://wofsauge.github.io/IsaacDocs/rep/PlayerTypes_ActiveItemDesc.html) GetActiveItemDesc ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot = ActiveSlot.SLOT_PRIMARY ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetActiveItemSlot () {: aria-label='Functions' }
#### [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) GetActiveItemSlot ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetActiveMaxCharge () {: aria-label='Functions' }
#### int GetActiveMaxCharge ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetActiveMinUsableCharge () {: aria-label='Functions' }
#### int GetActiveMinUsableCharge ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetActiveWeaponNumFired () {: aria-label='Functions' }
#### int GetActiveWeaponNumFired ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBagOfCraftingContent () {: aria-label='Functions' }
#### [BagOfCraftingPickup](enums/BagOfCraftingPickup.md)[] GetBagOfCraftingContent ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBagOfCraftingOutput () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) GetBagOfCraftingOutput ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBagOfCraftingSlot () {: aria-label='Functions' }
#### [BagOfCraftingPickup](enums/BagOfCraftingPickup.md) GetBagOfCraftingSlot ( int SlotID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
获取给定 `SlotID` 中合成袋的当前内容。

### GetBladderCharge () {: aria-label='Functions' }
#### int GetBladderCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家停止射击并为肾结石物品充能时的当前充能值。

___

### GetBlinkLockTime () {: aria-label='Functions' }
#### int GetBlinkLockTime ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
How long the player's head will play the fired-frame sprite.

___

### GetBloodLustCounter () {: aria-label='Functions' }
#### int GetBloodLustCounter ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBodyMoveDirection () {: aria-label='Functions' }
#### [Vector](Vector.md) GetBodyMoveDirection ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBombPlaceDelay () {: aria-label='Functions' }
#### int GetBombPlaceDelay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
默认炸弹放置延迟为 `30 帧`。

___

### GetBodySprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetBodySprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Temporary copy of body player sprite while null animation is active.

___

### GetCambionConceptionState () {: aria-label='Functions' }
#### int GetCambionConceptionState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家使用恶魔受胎物品受到伤害的次数。

___

### GetCandyHeartBonus () {: aria-label='Functions' }
#### table GetCandyHeartBonus ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of fields corresponding to each stat that Candy Heart can increase and the active amount of bonuses tied to each stat.

The fields are: `FireDelay`, `Damage`, `TearRange`, `ShotSpeed`, `Luck`, `MoveSpeed`.

___

### GetCambionPregnancyLevel () {: aria-label='Functions' }
#### int GetCambionPregnancyLevel ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
对应恶魔受胎服装的当前可见状态（0 - 2）。

___

### GetCharmOfTheVampireKills () {: aria-label='Functions' }
#### int GetCharmOfTheVampireKills ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollectiblesList () {: aria-label='Functions' }
#### table GetCollectiblesList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个表，其中包含玩家拥有的每个收藏品的数量，不计算固有物品。
???- example "示例代码"
    这段代码打印玩家拥有的悲伤洋葱的数量
    ```lua
    local collectiblesList = player:GetCollectiblesList()
    print(collectiblesList[CollectibleType.COLLECTIBLE_SAD_ONION])
    ```

### GetConceptionFamiliarFlags () {: aria-label='Functions' }
#### [ConceptionFamiliarFlag](enums/ConceptionFamiliarFlag.md) GetConceptionFamiliarFlags ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the bitmask corresponding to which familiars have been spawned by Cambion/Immaculate Conception. The additional familiars provided by this bitmask are spawned during familiar cache evaluation, but only while the player has one of those two items.

### GetCostumeLayerMap () {: aria-label='Functions' }
#### table GetCostumeLayerMap ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家服装精灵层数据的表格，包含以下字段：
| Field | Type | Comment |
| :-- | :-- | :-- |
| costumeIndex | int | 该层活跃/可见服装的索引。若该层无服装，值为 `-1`. |
| priority | int | 对应动画文件（anm2）的精灵层 ID。若该层无服装，值为 `-1`. |
| layerID | int | 服装在 `costumes2.xml` 中列出的优先级。若该层无服装，值为 `-1` |
| isBodyLayer | boolean | 若服装是身体服装则为 `true` ，否则（包括该层无服装时）为 `false`. |

???- info "More Layer Map Info"

    返回表格的索引顺序与 `PlayerSpriteLayer` 对应。但由于 Lua 和 C++ 数组起始索引的差异，`CostumeLayerMap` 的索引需减 1 ，且其 `costumeIndex` 需加 1 才能获取准确信息

    下方代码片段用于显示所有当前已占用的服装层，打印内容格式为：`PlayerSpriteLayer - 层名称 - 物品名称/NullItemID - Anm2 文件路径` 

    ???+ example "Example Code"

        ```lua
            local player = Isaac.GetPlayer()
            local map = Isaac.GetPlayer():GetCostumeLayerMap()
            print("-------------------------------------------------------------------")
            local costumeSpriteDescs = player:GetCostumeSpriteDescs()
            for layer, mapData in ipairs(map) do
                if mapData.costumeIndex == -1 then goto continue end
                local costumeSpriteDesc = costumeSpriteDescs[mapData.costumeIndex + 1]
                local sprite = costumeSpriteDesc:GetSprite()
                local itemConfig = costumeSpriteDesc:GetItemConfig()
                local layerName = sprite:GetLayer(mapData.layerID):GetName()
                local costumeName = itemConfig.Name ~= "" and Isaac.GetString("Items", itemConfig.Name) or "NullItemID "..itemConfig.ID
                local spritePath = sprite:GetFilename()
                print(layer - 1, "-", layerName, "-", costumeName, "-", spritePath)
                ::continue::
            end
            print("-------------------------------------------------------------------")
        ```

### GetCostumeSpriteDescs () {: aria-label='Functions' }
#### [CostumeSpriteDesc](CostumeSpriteDesc.md)[] GetCostumeSpriteDescs ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个 [CostumeSpriteDesc](CostumeSpriteDesc.md) 类型的表。

### GetCustomCacheValue () {: aria-label='Functions' }
#### float GetCustomCacheValue ( string CustomCacheTag ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回指定自定义缓存标签的当前缓存值。如果提供的标签尚未评估，则默认返回 `0`。
有关自定义缓存的更多信息，请参阅 [items.xml](xml/items.md)。

### GetD8DamageModifier () {: aria-label='Functions' }
#### float GetD8DamageModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetD8FireDelayModifier () {: aria-label='Functions' }
#### float GetD8FireDelayModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetD8RangeModifier () {: aria-label='Functions' }
#### float GetD8RangeModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetD8SpeedModifier () {: aria-label='Functions' }
#### float GetD8SpeedModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDamageModifier () {: aria-label='Functions' }
#### int GetDamageModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

该修饰符以固定值的形式加到玩家的伤害属性上。

“实验性治疗” 根据随机生成的伤害值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

### GetDeadEyeCharge () {: aria-label='Functions' }
#### int GetDeadEyeCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDeathAnimName () {: aria-label='Functions' }
#### string GetDeathAnimName ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

返回玩家死亡动画的名称。

???+ info "Return info"

    可能返回以下字符串：
    - `Death` - 常规死亡动画名称。
    - `LostDeath` - 当玩家扮演 “游魂”、处于 “Lost Curse” 状态、扮演 “遗骸之魂” 或处于 “堕化雅各之魂” 时。

### GetEdenDamage () {: aria-label='Functions' }
#### float GetEdenDamage ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家伊甸随机属性中伤害属性的偏移量。

### GetEdenFireDelay () {: aria-label='Functions' }
#### float GetEdenFireDelay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家伊甸随机属性中射击延迟属性的偏移量。

### GetEdenLuck () {: aria-label='Functions' }
#### float GetEdenLuck ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家伊甸随机属性中幸运属性的偏移量。

### GetEdenRange () {: aria-label='Functions' }
#### float GetEdenRange ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家伊甸随机属性中射程属性的偏移量。

### GetEdenShotSpeed () {: aria-label='Functions' }
#### float GetEdenShotSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家伊甸随机属性中射击速度属性的偏移量。

### GetEdenSpeed () {: aria-label='Functions' }
#### float GetEdenSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家伊甸随机属性中移动速度属性的偏移量。

### GetEnterPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetEnterPosition ( ) {: .copyable aria-label='Functions' }         [ ](#){: .rgonorplus .tooltip .badge }

___

### GetEntityConfigPlayer () {: aria-label='Functions' }
#### [EntityConfigPlayer](EntityConfigPlayer.md) GetEntityConfigPlayer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetEpiphoraCharge () {: aria-label='Functions' }
#### int GetEpiphoraCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetEveSumptoriumCharge () {: aria-label='Functions' }
#### int GetEveSumptoriumCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回 “堕化夏娃” 固有 “圣血吸管” 能力的当前充能值。

### GetFireDelayModifier () {: aria-label='Functions' }
#### int GetFireDelayModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

为玩家提供 `0.5 * 修饰符` 的固定每秒眼泪数加成。

“实验性治疗” 根据随机生成的射击延迟值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

### GetFlippedForm () {: aria-label='Functions' }
#### [EntityPlayer](EntityPlayer.md) GetFlippedForm ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回当前角色的翻转形态（仅适用于 “堕化拉撒路”）。
否则返回 `nil`。

### GetFocusEntity () {: aria-label='Functions' }
#### [Entity](Entity.md) GetFocusEntity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回活动相机用于确定相机焦点的实体。这可以是 [标记](https://bindingofisaacrebirth.fandom.com/wiki/Marked) 目标 [EntityEffect](EntityEffect.md) 或武器实体。
如果这些都不存在，则返回 `nil`。

### GetFootprintColor () {: aria-label='Functions' }
#### [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) GetFootprintColor ( boolean LeftFootprint ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetForgottenSwapFormCooldown () {: aria-label='Functions' }
#### int GetForgottenSwapFormCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetGlitchBabySubType () {: aria-label='Functions' }
#### int GetGlitchBabySubType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetGlyphOfBalanceDrop () {: aria-label='Functions' }
#### table GetGlyphOfBalanceDrop ( int Variant = -1, int SubType = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个表，其中包含可能掉落的 [平衡符号](https://bindingofisaacrebirth.fandom.com/wiki/Glyph_of_Balance) 的变体和子类型。

### GetGnawedLeafTimer () {: aria-label='Functions' }
#### int GetGnawedLeafTimer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetGreedsGulletHearts () {: aria-label='Functions' }
#### int GetGreedsGulletHearts ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetHallowedGroundCountdown () {: aria-label='Functions' }
#### int GetHallowedGroundCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家从 “圣地大便/伯列恒之星” 光环中保留属性的宽限期倒计时。

### GetHeadDirectionLockTime () {: aria-label='Functions' }
#### int GetHeadDirectionLockTime ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
玩家头部应强制保持当前方向的时长。`-1`（或更低）表示当前方向未被锁定。

### GetHealthType () {: aria-label='Functions' }
#### [HealthType](enums/HealthType.md) GetHealthType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetHeldEntity () {: aria-label='Functions' }
#### [Entity](Entity.md) GetHeldEntity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果玩家当前没有手持实体，则返回 `nil`。
返回玩家举在头顶的实体，例如可投掷的红色炸弹或 [背摔！](https://bindingofisaacrebirth.fandom.com/wiki/Suplex!)。

### GetHeldSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetHeldSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
获取玩家进行涉及将精灵举在头顶的动画时使用的 [Sprite](Sprite.md) 对象，例如使用主动道具时。

### GetHistory () {: aria-label='Functions' }
#### [History](History.md) GetHistory ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetImmaculateConceptionState () {: aria-label='Functions' }
#### int GetImmaculateConceptionState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家使用 “圣灵受胎” 道具收集到的红心数量。在生成跟班/魂心后重置为 0。

___

### GetItemStateCooldown () {: aria-label='Functions' }
#### int GetItemStateCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetKeepersSackBonus () {: aria-label='Functions' }
#### int GetKeepersSackBonus ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
获取玩家持有 [“店主的胯袋”](https://bindingofisaacrebirth.fandom.com/wiki/Keeper's_Sack) 时花费的硬币数量。

### GetLaserColor () {: aria-label='Functions' }
#### [Color](Color.md) GetLaserColor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetLuckModifier () {: aria-label='Functions' }
#### int GetLuckModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

该修饰符直接添加到玩家的幸运属性上。

“实验性治疗” 根据随机生成的幸运值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

___

### GetMaggyHealthDrainCooldown () {: aria-label='Functions' }
#### int GetMaggyHealthDrainCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMaggySwingCooldown () {: aria-label='Functions' }
#### int GetMaggySwingCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回 “堕化抹大拉” 受到伤害后挥击攻击的冷却剩余帧数。如果玩家不是 “堕化抹大拉”，则返回 `0`。

### GetMarkedTarget () {: aria-label='Functions' }
#### [EntityEffect](https://wofsauge.github.io/IsaacDocs/rep/EntityEffect.html) GetMarkedTarget ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回代表 [标记](https://bindingofisaacrebirth.fandom.com/wiki/Marked) 道具目标的实体效果。

如果目标未显示在地面上，此函数返回 `nil`。

### GetMaxBladderCharge () {: aria-label='Functions' }
#### int GetMaxBladderCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家停止射击并为 “肾结石” 道具充能时的最大充能值。

### GetMaxBombs () {: aria-label='Functions' }
#### int GetMaxBombs ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家当前可持有的最大炸弹数量。

### GetMaxCoins () {: aria-label='Functions' }
#### int GetMaxCoins ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家当前可持有的最大硬币数量。

### GetMaxKeys () {: aria-label='Functions' }
#### int GetMaxKeys ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家当前可持有的最大钥匙数量。

### GetMaxPeeBurstCooldown () {: aria-label='Functions' }
#### int GetMaxPeeBurstCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回 “肾结石” 道具的最大攻击持续时间。

### GetMegaBlastDuration () {: aria-label='Functions' }
#### int GetMegaBlastDuration ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMetronomeCollectibleID () {: aria-label='Functions' }
#### int GetMetronomeCollectibleID ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMovingBoxContents () {: aria-label='Functions' }
#### [EntitiesSaveStateVector](EntitiesSaveStateVector.md) GetMovingBoxContents ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家通过 “移动箱” 道具存储的拾取物。

### GetNextUrethraBlockFrame () {: aria-label='Functions' }
#### int GetNextUrethraBlockFrame ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家停止射击并开始为 [“肾结石”](https://bindingofisaacrebirth.fandom.com/wiki/Kidney_Stone) 道具充能的帧数。

___

### GetPlanCKillCountdown () {: aria-label='Functions' }
#### int GetPlanCKillCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPeeBurstCooldown () {: aria-label='Functions' }
#### int GetPeeBurstCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回 [“肾结石”](https://bindingofisaacrebirth.fandom.com/wiki/Kidney_Stone) 道具的攻击持续时间。

___

### GetPotatoPeelerUses () {: aria-label='Functions' }
#### int GetPotatoPeelerUses ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used to increment [Cube of Meat](https://bindingofisaacrebirth.wiki.gg/wiki/Cube_of_Meat) familiar form.

___

### GetPlayerFormCounter () {: aria-label='Functions' }
#### int GetPlayerFormCounter ( [PlayerForm](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerForm.html) PlayerFormID ) {: .copyable aria-label='Functions' }  [ ](#){: .rgonorplus .tooltip .badge }
返回玩家与指定变身相关联的道具数量。

___

### GetPlayerHUD () {: aria-label='Functions' }
#### [PlayerHUD](PlayerHUD.md) GetPlayerHUD ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPlayerIndex () {: aria-label='Functions' }
#### int GetPlayerIndex ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPonyCharge () {: aria-label='Functions' }
#### int GetPonyCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回 “一匹小马” 或 “白色小马” 道具充能效果停用前的剩余帧数。

### GetPurityState () {: aria-label='Functions' }
#### [PurityState](enums/PurityState.md) GetPurityState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回 [“纯洁”](https://bindingofisaacrebirth.fandom.com/wiki/Purity) 道具效果的当前状态。如果玩家没有 “纯洁” 道具，则返回 `PurityState.BLUE`。

### GetRedStewBonusDuration () {: aria-label='Functions' }
#### int GetRedStewBonusDuration ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回 “红炖菜” 道具伤害加成效果的剩余帧数。

___

### GetRevelationCharge () {: aria-label='Functions' }
#### float GetRevelationCharge ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomDamage () {: aria-label='Functions' }
#### float GetRockBottomDamage ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomLuck () {: aria-label='Functions' }
#### float GetRockBottomLuck ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomMaxFireDelay () {: aria-label='Functions' }
#### float GetRockBottomMaxFireDelay ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomMoveSpeed () {: aria-label='Functions' }
#### float GetRockBottomMoveSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomShotSpeed () {: aria-label='Functions' }
#### float GetRockBottomShotSpeed ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRockBottomTearRange () {: aria-label='Functions' }
#### float GetRockBottomTearRange ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetShotSpeedModifier () {: aria-label='Functions' }
#### int GetShotSpeedModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

为玩家的射击速度增加 `0.2 * 修饰符`。

“实验性治疗” 根据随机生成的射击速度值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

### GetSmeltedTrinkets () {: aria-label='Functions' }
#### table GetSmeltedTrinkets ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html)[] TrinketList = nil ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of smelted trinkets and their corresponding amounts. The returned table contains the following fields:

|字段|类型|说明|
|:--|:--|:--|
| goldenTrinketAmount | int | |
| trinketAmount | int | |

The optional TrinketList param can be used as a filter to only return the provided TrinketTypes for better performance.

___

### GetSmeltedTrinketDesc () {: aria-label='Functions' }
#### table GetSmeltedTrinketDesc ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of the provided smelted trinket and their corresponding amounts. The returned table contains the following fields:

|Field|Type|Comment|
|:--|:--|:--|
| trinketAmount | int | |
| goldenTrinketAmount | int | |

___

### GetSoulLocketBonus () {: aria-label='Functions' }
#### table GetSoulLocketBonus ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of fields corresponding to each stat that Soul Locket can increase and the active amount of bonuses tied to each stat.

The fields are: `FireDelay`, `Damage`, `TearRange`, `ShotSpeed`, `Luck`, `MoveSpeed`.

___

### GetSpecialGridCollision () {: aria-label='Functions' }
#### int GetSpecialGridCollision ( [Vector](Vector.md) Position = self.Position ) {: .copyable aria-label='Functions' }       [ ](#){: .rgonorplus .tooltip .badge }

___

### GetSpeedModifier () {: aria-label='Functions' }
#### int GetSpeedModifier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

为玩家的移动速度增加 `0.2 * 修饰符`。

“实验性治疗” 根据随机生成的移动速度值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

### GetSpoofedCollectiblesList () {: aria-label='Functions' }
#### table[] GetSpoofedCollectiblesList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

|字段|类型|说明|
|:--|:--|:--|
| 道具 ID | [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) | |
| 追加数量 | int | |
| 是否被阻挡 | boolean | |

___

### GetStatMultiplier () {: aria-label='Functions' }
#### float GetStatMultiplier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the multiplier added to stats gained from any items.

???- info "Multipliers"
    - **Tainted Bethany**: x0.75
    - **Cracked Crown**: x1.2

___

### GetSuplexAimCountdown () {: aria-label='Functions' }
#### int GetSuplexAimCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSuplexLandPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetSuplexLandPosition ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSuplexState () {: aria-label='Functions' }
#### int GetSuplexState ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSuplexTargetPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetSuplexTargetPosition ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetTearDisplacement () {: aria-label='Functions' }
#### int GetTearDisplacement ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家的眼泪偏移值，用于判断玩家从哪只眼睛射击。

???+ info "Return info"

___

### GetTearsCap () {: aria-label='Functions' }
#### int GetTearsCap ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the soft tears cap. Default is `5.0`. Not affected by firedelay modifiers.

___

### GetTotalActiveCharge () {: aria-label='Functions' }
#### int GetTotalActiveCharge ( [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetUrnSouls () {: aria-label='Functions' }
#### int GetUrnSouls ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetVoidedCollectiblesList () {: aria-label='Functions' }
#### [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)[] GetVoidedCollectiblesList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个包含所有被 “虚空” 道具吞噬的主动道具 [CollectibleTypes](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) 的表。

### GetWeapon () {: aria-label='Functions' }
#### [Weapon](Weapon.md) GetWeapon ( int Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回相应插槽中的武器对象，如果未找到武器则返回 `nil`。插槽编号必须在 `0` 到 `4` 之间。

???- info "Info"

    武器插槽及其说明：
    - `0` - 备用武器，如 “缺口斧” 和 “灵魂瓮”。
    - `1` - 主武器。
    - `2` - 额外武器。原版游戏中很少有这种情况，但模组可以填充此插槽。
    - `3` - 额外武器。
    - `4` - 额外武器。
    始终检查是否为 `nil`，即使是插槽 `1`，因为它可以被模组通过 [Isaac.DestroyWeapon()](Isaac.md#destroyweapon) 删除。

### GetWeaponModifiers () {: aria-label='Functions' }
#### int GetWeaponModifiers ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个 [WeaponModifiers](enums/WeaponModifier.md) 类型的位掩码。

### GetWildCardItem () {: aria-label='Functions' }
#### int GetWildCardItem ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家最后使用的道具，再次使用 “万能卡” 时将激活该道具。

如果玩家使用了主动道具，则返回其 `CollectibleType`。如果玩家使用了消耗品，则返回其变体。如果玩家使用了 “问号卡”，则返回 `1`。如果玩家之前从未使用过主动道具，则返回 `0`。

### GetWildCardItemType () {: aria-label='Functions' }
#### [PocketItemType](enums/PocketItemType.md) GetWildCardItemType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回玩家最后使用的道具类型，再次使用 “万能卡” 时将激活该道具。

如果玩家使用了消耗品（包括 “问号卡”），则返回 `ItemType.ITEM_PASSIVE`。如果玩家之前从未使用过主动道具，则返回 `255`。

### GetWispCollectiblesList () {: aria-label='Functions' }
#### table GetWispCollectiblesList ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个与玩家拥有的道具幽灵对应的 [CollectibleTypes](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) 表。

___

### HasCamoEffect () {: aria-label='Functions' }
#### boolean HasCamoEffect ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### HasChanceRevive () {: aria-label='Functions' }
#### boolean HasChanceRevive ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果玩家的额外生命计数上会显示 “?”，则返回 true（即玩家拥有 “嗝屁猫的项圈”，或在 REPENTOGON 的 [自定义标签 items.xml 属性](xml/items.md) 中有 `chancerevive` 字符串的模组复活道具）。

___

### HasForcedCamoEffect () {: aria-label='Functions' }
#### boolean HasForcedCamoEffect ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### HasGoldenTrinket () {: aria-label='Functions' }
#### boolean HasGoldenTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果玩家拥有指定 [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) 的金色变体，则返回 true。

### HasInstantDeathCurse () {: aria-label='Functions' }
#### boolean HasInstantDeathCurse ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
当玩家处于由下水道的白色火焰或 “游魂的魂石” 触发的 “游魂诅咒” 形态时（或在 “堕化雅各布” 的幽灵形态下被 “堕化以扫” 触摸时），返回 true。

### HasPoisonImmunity () {: aria-label='Functions' }
#### boolean HasPoisonImmunity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IncrementPlayerFormCounter () {: aria-label='Functions' }
#### void IncrementPlayerFormCounter ( [PlayerForm](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerForm.html) Form, int Count ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
增加或减少玩家向某一变身的计数器。`Count` 可以为负数，以减少 [PlayerForm](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerForm.html)。

### InitPostLevelInitStats () {: aria-label='Functions' }
#### void InitPostLevelInitStats ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
在使用 `InitTwin` 生成具有 “特殊” 眼泪的角色（如 “游魂”、“莉莉丝”、“阿撒兹勒” 等）后调用此函数，否则他们将不会拥有正确的眼泪类型。

### InitTwin () {: aria-label='Functions' }
#### [EntityPlayer](EntityPlayer.md) InitTwin ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) PlayerType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
初始化一个由玩家同一控制器控制的新玩家。

???+ bug "Bug"

    双胞胎玩家在保存并继续游戏时会与其主双胞胎不同步。这会在单人游戏中导致软锁，因为游戏会提示连接控制器。
    我们已从 \_Kilburn 处确认，这在原版角色中是硬编码处理的。我们需要为此添加一个解决方案。

### IsCollectibleAnimFinished () {: aria-label='Functions' }
#### boolean IsCollectibleAnimFinished ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, string Animation ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果与道具关联的动画可见，则返回 true。

### IsCollectibleBlocked () {: aria-label='Functions' }
#### boolean IsCollectibleBlocked ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) 被阻挡，则返回 true。道具只能通过 [BlockCollectible](EntityPlayer.md#blockcollectible) 函数阻挡。

### IsCollectibleCostumeVisible () {: aria-label='Functions' }
#### boolean IsCollectibleCostumeVisible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, int PlayerSpriteLayerID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果与道具关联的服装可见，则返回 `true`。

### IsEntityValidTarget () {: aria-label='Functions' }
#### boolean IsEntityValidTarget ( [Entity](Entity.md) Entity ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsFootstepFrame () {: aria-label='Functions' }
#### boolean IsFootstepFrame ( int Foot = -1 ) {: .copyable aria-label='Functions' }        [ ](#){: .rgonorplus .tooltip .badge }
???+ info "Info"

    - `-1` - 每 12 帧返回 true。
    - `0` - 每 24 帧返回 true。
    - `1` - 始终为 false。

### IsHeadless () {: aria-label='Functions' }
#### boolean IsHeadless ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果玩家因 “断头台”、“侵体蜘蛛”、“剪刀” 和 “飞头攻击” 等道具而无头，则返回 `true`。

### IsHologram () {: aria-label='Functions' }
#### boolean IsHologram ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果玩家是拥有 “长子名分” 的 “堕化拉撒路” 的非激活形态，则返回 `true`。

### IsInvisible () {: aria-label='Functions' }
#### boolean IsInvisible ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果玩家拥有 “褪色的全家福/迷彩内裤” 效果，则返回 `true`。

### IsItemCostumeVisible () {: aria-label='Functions' }
#### boolean IsItemCostumeVisible ( [ItemConfig_Item](ItemConfig_Item.md) Item, int PlayerSpriteLayerID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
#### boolean IsItemCostumeVisible ( [ItemConfig_Item](ItemConfig_Item.md) Item, int PlayerSpriteLayerName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsLocalPlayer () {: aria-label='Functions' }
#### boolean IsLocalPlayer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于在线游戏。如果是本地玩家，则返回 `true`，否则返回 `false`。

### IsNullItemCostumeVisible () {: aria-label='Functions' }
#### boolean IsNullItemCostumeVisible ( int nullItem, int layerID = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
#### boolean IsNullItemCostumeVisible ( int nullItem, string layerName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsPacifist () {: aria-label='Functions' }
#### boolean IsPacifist ( ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsPostLevelInitFinished () {: aria-label='Functions' }
#### boolean IsPostLevelInitFinished ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsUrethraBlocked () {: aria-label='Functions' }
#### boolean IsUrethraBlocked ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
当玩家因为 [“肾结石”](https://bindingofisaacrebirth.fandom.com/wiki/Kidney_Stone) 道具充能而无法射击时，返回 true。

### MorphToCoopGhost () {: aria-label='Functions' }
#### void MorphToCoopGhost ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将玩家转变为合作幽灵。

### PlayCollectibleAnim () {: aria-label='Functions' }
#### void PlayCollectibleAnim ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, boolean CheckBodyLayers, string AnimationName, int Frame = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
播放与提供的道具关联的动画。

### PlayDelayedSFX () {: aria-label='Functions' }
#### void PlayDelayedSFX ( [SoundEffect](https://wofsauge.github.io/IsaacDocs/rep/enums/SoundEffect.html) ID, int SoundDelay = 0, int FrameDelay = 2, float Volume = 1.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Plays a sound effect after a delay.

___

### PlayItemNullAnimation () {: aria-label='Functions' }
#### boolean PlayItemNullAnimation ( string AnimationName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns ``true`` if animation was set successfully, ``false`` otherwise. Useful for item state/hold items.

___

### RemoveCollectibleByHistoryIndex () {: aria-label='Functions' }
#### void RemoveCollectibleByHistoryIndex ( int Index ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
从玩家处移除与指定历史索引关联的道具。

### RemovePocketItem () {: aria-label='Functions' }
#### void RemovePocketItem ( [PillCardSlot](enums/PillCardSlot.md) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### RemovePoopSpell () {: aria-label='Functions' }
#### void RemovePoopSpell ( int Position = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
从指定队列位置移除便便法术，并将其后的所有法术向前移动以填充空位。最后一个位置将随机选择一个新法术填充。便便法术仅由 “堕化？？？” 使用。

### RerollAllCollectibles () {: aria-label='Functions' }
#### void RerollAllCollectibles ( [RNG](RNG.md) rng, boolean includeActiveItems ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
重新随机玩家的所有道具。

### ResetPlayer () {: aria-label='Functions' }
#### void ResetPlayer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ info "Info"

    此函数由 “创世纪” 主动道具使用。

### ReviveCoopGhost () {: aria-label='Functions' }
#### boolean ReviveCoopGhost ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SalvageCollectible () {: aria-label='Functions' }
#### void SalvageCollectible ( [EntityPickup](EntityPickup.md) Pickup, [RNG](RNG.md) rng = PickupDropRNG, [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) Pool = ItemPoolType.POOL_NULL) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
产生随机数量的各种拾取物，类似于 “堕化该隐” 的能力。

???+ info "Info"

___

### SetActionHoldDrop () {: aria-label='Functions' }
#### void SetActionHoldDrop ( int duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetActiveVarData () {: aria-label='Functions' }
#### void SetActiveVarData ( int VarData, [ActiveSlot](https://wofsauge.github.io/IsaacDocs/rep/enums/ActiveSlot.html) Slot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBagOfCraftingContent () {: aria-label='Functions' }
#### void SetBagOfCraftingContent ( [BagOfCraftingPickup](enums/BagOfCraftingPickup.md)[] ContentTable ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将合成袋的内容设置为表中的内容。表必须使用有效的 [BagOfCraftingPickup](enums/BagOfCraftingPickup.md) ID。表可以短于 8，此时剩余索引将设置为空。

### SetBagOfCraftingOutput () {: aria-label='Functions' }
#### void SetBagOfCraftingOutput ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将玩家合成袋的输出设置为指定道具。

### SetBagOfCraftingSlot () {: aria-label='Functions' }
#### void SetBagOfCraftingSlot ( int SlotID, [BagOfCraftingPickup](enums/BagOfCraftingPickup.md) PickupID ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将玩家合成袋的指定插槽设置为指定拾取物。

If a slot is set to empty (0 - `BagOfCraftingPickup.BOC_NONE`) then all slots after it will automatically be shifted down to fill the empty space.

___

### SetBlackHeart () {: aria-label='Functions' }
#### void SetBlackHeart ( int BlackHeart ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBladderCharge () {: aria-label='Functions' }
#### void SetBladderCharge ( int Charge ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
由 [“肾结石”](https://bindingofisaacrebirth.fandom.com/wiki/Kidney_Stone) 道具使用。
???+ bug "Bug"

___

### SetBlinkLockTime () {: aria-label='Functions' }
#### void SetBlinkLockTime ( int Time ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBloodLustCounter () {: aria-label='Functions' }
#### void SetBloodLustCounter ( int Counter ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBombPlaceDelay () {: aria-label='Functions' }
#### void SetBombPlaceDelay ( int Delay ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetCambionConceptionState () {: aria-label='Functions' }
#### void SetCambionConceptionState ( int State ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家使用 “恶魔受胎” 道具受到的伤害量。

请注意，游戏仅在玩家受到伤害且此计数器达到 15、30、60 或 90 时才会生成跟班。你不能直接使用此函数触发诞生。

### SetCanShoot () {: aria-label='Functions' }
#### boolean SetCanShoot ( boolean CanShoot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
立即禁用（或启用）玩家的射击能力。基础游戏主要在特殊挑战中使用此功能。

___

### SetCharmOfTheVampireKills () {: aria-label='Functions' }
#### void SetCharmOfTheVampireKills ( int KillAmount ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetConceptionFamiliarFlags () {: aria-label='Functions' }
#### void SetConceptionFamiliarFlags ( [ConceptionFamiliarFlag](enums/ConceptionFamiliarFlag.md) Flags ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置与 “恶魔受胎/圣灵受胎” 生成的跟班对应的位掩码。此位掩码提供的额外跟班在跟班缓存评估期间生成，但仅当玩家拥有这两个道具之一时才会生成。

### SetControllerIndex () {: aria-label='Functions' }
#### void SetControllerIndex ( int Idx ) {: .copyable aria-label='Functions' }         [ ](#){: .rgonorplus .tooltip .badge }
更改玩家的控制器索引。

___

### SetD8DamageModifier () {: aria-label='Functions' }
#### void SetD8DamageModifier ( float Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetD8FireDelayModifier () {: aria-label='Functions' }
#### void SetD8FireDelayModifier ( float Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetD8RangeModifier () {: aria-label='Functions' }
#### void SetD8RangeModifier ( float Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetD8SpeedModifier () {: aria-label='Functions' }
#### void SetD8SpeedModifier ( float Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetDamageModifier () {: aria-label='Functions' }
#### void SetDamageModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

该修饰符以固定伤害的形式应用于玩家。

“实验性治疗” 根据随机生成的伤害值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

### SetEdenDamage () {: aria-label='Functions' }
#### void SetEdenDamage ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家伊甸随机属性中伤害属性的偏移量。对非伊甸或堕化伊甸的玩家无效。

### SetEdenFireDelay () {: aria-label='Functions' }
#### void SetEdenFireDelay ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家伊甸随机属性中射击延迟属性的偏移量。对非伊甸或堕化伊甸的玩家无效。

### SetEdenLuck () {: aria-label='Functions' }
#### void SetEdenLuck ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家伊甸随机属性中幸运属性的偏移量。对非伊甸或堕化伊甸的玩家无效。

### SetEdenRange () {: aria-label='Functions' }
#### void SetEdenRange ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家伊甸随机属性中射程属性的偏移量。对非伊甸或堕化伊甸的玩家无效。

### SetEdenShotSpeed () {: aria-label='Functions' }
#### void SetEdenShotSpeed ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家伊甸随机属性中射击速度属性的偏移量。对非伊甸或堕化伊甸的玩家无效。

### SetEdenSpeed () {: aria-label='Functions' }
#### void SetEdenSpeed ( float Value ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家伊甸随机属性中移动速度属性的偏移量。对非伊甸或堕化伊甸的玩家无效。

### SetEveSumptoriumCharge () {: aria-label='Functions' }
#### void SetEveSumptoriumCharge ( int ChargeNum ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置 “堕化夏娃” 固有 “吸食器” 能力的当前充能值。

### SetFireDelayModifier () {: aria-label='Functions' }
#### void SetFireDelayModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

为玩家提供 `0.5 * 修饰符` 的固定每秒眼泪数。

“实验性治疗” 根据随机生成的射击延迟值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

### SetFootprintColor () {: aria-label='Functions' }
#### void SetFootprintColor ( [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor.html) color, boolean RightFoot = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家的脚印颜色。

___

### SetForceCamoEffect () {: aria-label='Functions' }
#### void SetForceCamoEffect ( boolean Force ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetForgottenSwapFormCooldown () {: aria-label='Functions' }
#### void SetForgottenSwapFormCooldown ( int Cooldown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

    此函数目前会导致游戏崩溃 - 将在未来更新中修复。

### SetGnawedLeafTimer () {: aria-label='Functions' }
#### void SetGnawedLeafTimer ( int Timer ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetHallowedGroundCountdown () {: aria-label='Functions' }
#### void SetHallowedGroundCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家从 “圣地大便/伯列恒之星” 光环中保留属性的宽限期倒计时。

### SetHeadDirection () {: aria-label='Functions' }
#### void SetHeadDirection ( [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html) Direction, int Time, boolean Force = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将玩家的头部动画锁定到指定的 [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html)。`Force` 参数将覆盖现有的头部方向锁定，例如使用 “妈妈的刀” 时的锁定。

### SetHeadDirectionLockTime () {: aria-label='Functions' }
#### void SetHeadDirectionLockTime ( int Time ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家头部应强制保持当前方向的时长。

### SetImmaculateConceptionState () {: aria-label='Functions' }
#### void SetImmaculateConceptionState ( int State ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家使用 “圣灵受胎” 道具收集到的红心数量。

请注意，游戏仅在玩家拾取红心时检查是否生成跟班，因此你不能直接使用此函数触发该效果。

如果你设置的值大于 14，该值将自动上限为 14，这意味着下一次拾取红心将生成一个跟班。

### SetItemState () {: aria-label='Functions' }
#### void SetItemState ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将玩家的道具状态更改为指定道具。这通常用于玩家在激活前举在头顶的道具（如 “鲍勃的烂头”、“玻璃大炮”）。

___

### SetItemStateCooldown  () {: aria-label='Functions' }
#### void SetItemStateCooldown  ( int Cooldown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetKeepersSackBonus () {: aria-label='Functions' }
#### void SetKeepersSackBonus ( int Bonus ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家 [“店主的胯袋”](https://bindingofisaacrebirth.fandom.com/wiki/Keeper's_Sack) 道具的当前硬币奖励。

### SetLaserColor () {: aria-label='Functions' }
#### void SetLaserColor ( [Color](Color.md) color ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家的激光颜色。

### SetLuckModifier () {: aria-label='Functions' }
#### void SetLuckModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

该修饰符直接添加到玩家的幸运属性上。

“实验性治疗” 根据随机生成的幸运值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

___

### SetMaggyHealthDrainCooldown () {: aria-label='Functions' }
#### void SetMaggyHealthDrainCooldown ( int Cooldown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetMaggySwingCooldown () {: aria-label='Functions' }
#### void SetMaggySwingCooldown ( int Cooldown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将 “堕化抹大拉” 挥击攻击的冷却时间设置为指定的帧数。

### SetMaxBladderCharge () {: aria-label='Functions' }
#### void SetMaxBladderCharge ( int Charge ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家停止射击并为 “肾结石” 道具充能时的最大充能值。

### SetMegaBlastDuration () {: aria-label='Functions' }
#### void SetMegaBlastDuration ( int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将 “超级喷射” 激光的持续时间设置为指定的帧数。如果激光尚未激活，将其持续时间设置为大于零的值将激活该效果。

???+ bug "Bug"

    如果 “超级喷射” 激光处于激活状态，并且你再次调用此函数并设置较低的持续时间，激光将在指定帧数过去后仍然存在，直到玩家离开房间。

### SetNextUrethraBlockFrame () {: aria-label='Functions' }
#### void SetNextUrethraBlockFrame ( int Frame ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置玩家停止射击并开始为 “肾结石” 道具充能的帧数。

___

### SetPlanCKillCountdown () {: aria-label='Functions' }
#### void SetPlanCKillCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetPonyCharge () {: aria-label='Functions' }
#### void SetPonyCharge ( int Time ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将 “小黑马” 和 “小白马” 道具的充能效果持续时间设置为指定的帧数。

### SetPoopSpell () {: aria-label='Functions' }
#### void SetPoopSpell ( int Slot, [PoopSpellType](https://wofsauge.github.io/IsaacDocs/rep/enums/PoopSpellType.html) PoopSpellType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将便便列表中的指定插槽设置为一种便便类型。这仅由 “堕化？？？” 使用。

___

### SetPotatoPeelerUses () {: aria-label='Functions' }
#### void SetPotatoPeelerUses ( int Amount ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetPurityState () {: aria-label='Functions' }
#### void SetPurityState ( [PurityState](enums/PurityState.md) State ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置 [“纯洁”](https://bindingofisaacrebirth.fandom.com/wiki/Purity) 道具效果的当前状态。

### SetRedStewBonusDuration () {: aria-label='Functions' }
#### void SetRedStewBonusDuration ( int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将 `红豆汤` 道具的伤害加成持续时间设置为指定的帧数。将持续时间设置为大于 0 的值将激活该效果（如果尚未激活）。

___

### SetRevelationCharge () {: aria-label='Functions' }
#### void SetRevelationCharge ( float Charge ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomDamage () {: aria-label='Functions' }
#### void SetRockBottomDamage ( float Damage ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomLuck () {: aria-label='Functions' }
#### void SetRockBottomLuck ( float Luck ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomMaxFireDelay () {: aria-label='Functions' }
#### void SetRockBottomMaxFireDelay ( float MaxFireDelay ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomMoveSpeed () {: aria-label='Functions' }
#### void SetRockBottomMoveSpeed ( float MoveSpeed ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomShotSpeed () {: aria-label='Functions' }
#### void SetRockBottomShotSpeed ( float ShotSpeed ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRockBottomTearRange () {: aria-label='Functions' }
#### void SetRockBottomTearRange ( float TearRange ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetShotSpeedModifier () {: aria-label='Functions' }
#### void SetShotSpeedModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

为玩家的射击速度增加 `0.2 * 修饰符`。

“实验性治疗” 根据随机生成的射击速度值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

### SetSpeedModifier () {: aria-label='Functions' }
#### void SetSpeedModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

为玩家的移动速度增加 `0.2 * 修饰符`。

“实验性治疗” 根据随机生成的移动速度值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

___

### SetSuplexAimCountdown () {: aria-label='Functions' }
#### void SetSuplexAimCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetSuplexLandPosition () {: aria-label='Functions' }
#### void SetSuplexLandPosition ( [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetSuplexState () {: aria-label='Functions' }
#### void SetSuplexState ( int State ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetSuplexTargetPosition () {: aria-label='Functions' }
#### void SetSuplexTargetPosition ( [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetTearPoisonDamage () {: aria-label='Functions' }
#### void SetTearPoisonDamage ( float Damage ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetTearRangeModifier () {: aria-label='Functions' }
#### void SetTearRangeModifier ( int Modifier ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
用于 “实验性治疗” 和 “虚空” 带来的属性提升。

为玩家的眼泪射程增加 `2.5 * 修饰符`。

“实验性治疗” 根据随机生成的射程值增加 `-1`、`0` 或 `1`。“虚空” 可能会随机增加 `1`。

### SetUrethraBlock () {: aria-label='Functions' }
#### void SetUrethraBlock ( boolean Blocked ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
设置 “肾结石” 道具的眼泪狂轰滥炸攻击是否即将激活。如果玩家没有 “肾结石” 道具，该效果将立即激活。

???+ bug "Bug"

    将 `Blocked` 参数设置为 `false` 似乎没有任何效果。

### SetWeapon () {: aria-label='Functions' }
#### void SetWeapon ( [Weapon](Weapon.md) Weapon, int WeaponSlot ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
将指定 `WeaponSlot` 中的活动武器设置为指定武器。
???- info "Info"

    武器插槽及其说明：
    - `0` - 备用武器，如 “缺口斧” 和 “灵魂瓮”。
    - `1` - 主武器。
    - `2` - 额外武器。原版游戏中很少有这种情况，但模组可以填充此插槽。
    - `3` - 额外武器。
    - `4` - 额外武器。
    始终检查是否为 `nil`，即使是插槽 `1`，因为它可以被模组通过 [Isaac.DestroyWeapon()](Isaac.md#destroyweapon) 删除

### ShootBlueCandle () {: aria-label='Functions' }
#### void ShootBlueCandle ( [Vector](Vector.md) Direction ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
使玩家从 “蜡烛” 道具发射蓝色火焰。

### ShuffleCostumes () {: aria-label='Functions' }
#### void ShuffleCostumes ( int Seed = Random( ) ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
随机化当前的服装。

### SpawnAquariusCreep () {: aria-label='Functions' }
#### [EntityEffect](https://wofsauge.github.io/IsaacDocs/rep/EntityEffect.html) SpawnAquariusCreep ( [TearParams](https://wofsauge.github.io/IsaacDocs/rep/TearParams.html) TearParams = self.TearParams) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
生成一个类似于 “宝瓶座” 产生的爬行效果，包括继承玩家的 `TearParams`。支持传递自定义的 `TearParams`。

???+ info "Info"
    供参考，游戏通常是这样计算 `TearParams` 的：

    ``player->GetTearHitParams(&params, WeaponType.WEAPON_TEARS, (*player->GetTearPoisonDamage() * 0.666f) / player->_damage, -(int)(-Isaac::Random(2) != 0) & 2 - 1, nil)``

### SpawnClot () {: aria-label='Functions' }
#### void SpawnClot ( [Vector](Vector.md) pos, boolean AllowPlayerDeath = false ) {: .copyable aria-label='Functions' }  [ ](#){: .rgonorplus .tooltip .badge }
作用类似于使用 “吸食器”，移除生命值并生成一个与移除的生命值类型相同的血块。如果设置了 `AllowPlayerDeath`，即使移除的生命值会导致玩家死亡，也会生成一个血块。

### SpawnSaturnusTears () {: aria-label='Functions' }
#### int SpawnSaturnusTears ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
生成一圈类似于 “土星” 道具的眼泪，围绕玩家旋转。

### SwapForgottenForm () {: aria-label='Functions' }
#### boolean SwapForgottenForm ( boolean Force = false, boolean NoEffects = false) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
If the player is The Forgotten/The Soul, the two will swap forms. Otherwise, this function does nothing.

`Force` will swap even if the subplayer doesn't have any health, or while a room/stage transition is active. `NoEffects` will disable the dust effect & fade from white when switching from The Soul to The Forgotten.

Returns `true` on success, otherwise `false`.

___

### SyncConsumableCounts () {: aria-label='Functions' }
#### void SyncConsumableCounts ( [EntityPlayer](EntityPlayer.md) Player, int CollectibleFlags ) {: .copyable aria-label='Functions' }       [ ](#){: .rgonorplus .tooltip .badge }

___

### Teleport () {: aria-label='Functions' }
#### void Teleport ( [Vector](Vector.md) Position, boolean DoEffects = true, boolean TeleportTwinPlayers = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
`DoEffects` 控制是否播放传送动画和音效。`TeleportTwinPlayers` 控制双胞胎玩家（如 “以扫”、拥有 “诞生之权” 的 “堕化拉撒路”）是否与该玩家一起传送。
将玩家传送到房间内的指定位置。

### TriggerRoomClear () {: aria-label='Functions' }
#### void TriggerRoomClear ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
触发玩家身上类似于房间清理的效果（如为主动道具充能）。

### TryAddToBagOfCrafting () {: aria-label='Functions' }
#### boolean TryAddToBagOfCrafting ( [EntityPickup](EntityPickup.md) Pickup ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Tries to add the specified pickup to the player's Bag of Crafting. Returns true if successful.

### TryDecreaseGlowingHourglassUses () {: aria-label='Functions' }
#### void TryDecreaseGlowingHourglassUses ( int Uses, boolean ForceHourglass = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
尝试减少玩家拥有的 “发光沙漏” 道具的剩余使用次数。`ForceHourglass` 参数将立即移除所有充能并将 “发光沙漏” 变为普通沙漏形态。

???+ bug "Bug"

    无论你指定移除的数字有多大，`Uses` 仅减少 1。

### TryFakeDeath () {: aria-label='Functions' }
#### boolean TryFakeDeath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
在玩家当前位置生成一个玩家的副本，并播放死亡动画和音效。

### TryForgottenThrow () {: aria-label='Functions' }
#### boolean TryForgottenThrow ( [Vector](Vector.md) Direction ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果玩家持有 “堕化遗骸”，他将朝指定方向被抛出。

### TryPreventDeath () {: aria-label='Functions' }
#### boolean TryPreventDeath ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
成功时返回 `true`，否则返回 `false`。
根据角色的 [HealthType](enums/HealthType.md)，如果角色没有剩余的心之容器，则添加一个以防止死亡。

### TryRemoveSmeltedTrinket () {: aria-label='Functions' }
#### void TryRemoveSmeltedTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) ID ) {: .copyable aria-label='Functions' }     [ ](#){: .rgonorplus .tooltip .badge }
尝试从玩家处移除指定的熔炼饰品。

### UnblockCollectible () {: aria-label='Functions' }
#### void UnblockCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
解除通过 [BlockCollectible](EntityPlayer.md#blockcollectible) 阻挡的 [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html)。

### UpdateIsaacPregnancy () {: aria-label='Functions' }
#### void UpdateIsaacPregnancy ( boolean UpdateCambion ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果你想更新 [“恶魔受胎”](https://bindingofisaacrebirth.fandom.com/wiki/Cambion_Conception) 服装，则设置为 `true`，否则更新 [“圣灵受胎”](https://bindingofisaacrebirth.fandom.com/wiki/Immaculate_Conception) 服装。

### VoidHasCollectible () {: aria-label='Functions' }
#### boolean VoidHasCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
如果指定的道具已被 “虚空” 道具吞噬，则返回 true。
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

### AddInnateTrinket () {: aria-label='Functions' }
#### void AddInnateTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, int Amount = 1, string GroupKey = "", int Duration = -1, bool AddCostume = true ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Same as AddInnateCollectible but for trinkets. Note that golden trinkets must be added/removed separately.

___

### BlockTrinket () {: aria-label='Functions' }
#### void BlockTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket ) {: .copyable aria-label='Functions' }   [ ](#){: .rgonplus .tooltip .badge }
Blocks the provided [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html). This will make it so the game thinks you don't have the trinket, even if it's in your inventory.

___

### ClearInnateItemGroup () {: aria-label='Modified Functions' }
#### void ClearInnateItemGroup ( string GroupKey ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Remove all innate collectibles and trinkets added under the specified group.

___

### CalculateBagOfCraftingOutput () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge }
#### static [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html), [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) CalculateBagOfCraftingOutput ( [BagOfCraftingPickup](enums/BagOfCraftingPickup.md)[] pickups ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBloodGushSprite () {: aria-label='Functions' }
#### [Sprite](Sprite.md) GetBloodGushSprite ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sprite used for things like Scissors and The Intruder.

___

### GetDonateLuck () {: aria-label='Functions' }
#### int GetDonateLuck ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetErrorTrinketEffect () {: aria-label='Functions' }
#### [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) GetErrorTrinketEffect ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the current trinket effect that would be mimicked by the "Error" trinket (`TrinketType.TRINKET_ERROR`), regardless of if the player has it.

Note that this effect is based entirely on the current room's [SpawnSeed](https://wofsauge.github.io/IsaacDocs/rep/RoomDescriptor.html#spawnseed), and can be also obtained from [RoomDescriptor](RoomDescriptor.md#geterrortrinketeffect). This player function is just provided as a convenience.

___

### GetImExcitedSpeedupCountdown () {: aria-label='Functions' }
#### int GetImExcitedSpeedupCountdown ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetInnateCollectibleCount () {: aria-label='Functions' }
#### int GetInnateCollectibleCount ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, string GroupKey = "" ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns how many innate copies of this collectible are currently in the specified group.

___

### GetInnateCollectibleGroup () {: aria-label='Functions' }
#### table GetInnateCollectibleGroup ( string GroupKey ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of the innate collectibles currently in the specified group.

The returned table has [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) as the keys and current counts as the values. If no copies of the item are in the group, it will not have an entry in the table.

___

### GetInnateTrinketCount () {: aria-label='Functions' }
#### int GetInnateTrinketCount ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, string GroupKey = "" ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns how many innate copies of this trinket are currently in the specified group.

Note that golden trinkets are counted separately.

___

### GetInnateTrinketGroup () {: aria-label='Functions' }
#### table GetInnateTrinketGroup ( string GroupKey ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of the innate trinket currently in the specified group.

The returned table has [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) as the keys and current counts as the values. If no copies of the item are in the group, it will not have an entry in the table.

Note that golden trinkets are counted separately.

___

### GetMawOfTheVoidCharge () {: aria-label='Functions' }
#### int GetMawOfTheVoidCharge ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMontezumaRevengeCharge () {: aria-label='Functions' }
#### int GetMontezumaRevengeCharge ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetRUAWizardTimer () {: aria-label='Functions' }
#### int GetRUAWizardTimer ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IsTrinketBlocked () {: aria-label='Functions' }
#### boolean IsTrinketBlocked ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns true if the [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) was blocked. Collectibles can only be blocked by use of [BlockTrinket](EntityPlayer.md#blocktrinket).

___

### RemoveInnateCollectible () {: aria-label='Functions' }
#### int RemoveInnateCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, int Amount = 1, string GroupKey = "" ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Removes innate collectibles from the specified group. Returns the actual number of innate items removed.

___

### RemoveInnateTrinket () {: aria-label='Functions' }
#### int RemoveInnateTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, int Amount = 1, string GroupKey = "" ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Removes innate trinkets from the specified group. Returns the actual number of innate items removed.

Note that golden trinkets must be added/removed separately.

___

### SetDonateLuck () {: aria-label='Functions' }
#### void SetDonateLuck ( int Value ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Does not trigger cache evaluation.

For simply incrementing this luck, consider the [DonateLuck](https://wofsauge.github.io/IsaacDocs/rep/EntityPlayer.html?h=donateluck#donateluck) function instead.

___

### SetImExcitedSpeedupCountdown () {: aria-label='Functions' }
#### void SetImExcitedSpeedupCountdown ( int Countdown ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetInnateCollectibleCount () {: aria-label='Functions' }
#### int SetInnateCollectibleCount ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, int NewCount, string GroupKey = "", boolean AddCostume = true ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Changes the current count of an innate collectible in the specified group. Triggers cache evals and callbacks appropriately if any items needed to be added or removed to reach the desired count, and returns the number of items added or removed (removals are negative). Does nothing if the count is already the desired value.

___

### SetInnateCollectibleGroup () {: aria-label='Functions' }
#### void SetInnateCollectibleGroup ( string GroupKey, table NewCounts, boolean AddCostume = true ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Updates the contents of the specified innate collectible group to match the provided table. The table must use [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) for the keys and the desired counts as the values.

Any items currently in the group but not specified in the table are removed. Triggers cache evals and callbacks appropriately if any items need to be added or removed to reach their desired count.

___

### SetInnateTrinketCount () {: aria-label='Functions' }
#### int SetInnateTrinketCount ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket, int NewCount, string GroupKey = "", boolean AddCostume = true ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Changes the current count of an innate trinket in the specified group. Automatically triggers cache evals and callbacks appropriately if any items needed to be added or removed to reach the desired count, and returns the number of items added or removed (removals are negative). Does nothing if the count is already the desired value.

Note that golden trinkets are counted separately.

___

### SetInnateTrinketGroup () {: aria-label='Functions' }
#### void SetInnateTrinketGroup ( string GroupKey, table NewCounts, boolean AddCostume = true ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Updates the contents of the specified innate collectible group to match the provided table. The table must use [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) for the keys and the desired counts as the values.

Any items currently in the group but not specified in the table are removed. Triggers cache evals and callbacks appropriately if any items need to be added or removed to reach their desired count.

Note that golden trinkets are counted separately.

___

### SetMawOfTheVoidCharge () {: aria-label='Functions' }
#### void SetMawOfTheVoidCharge ( int Charge ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetMontezumaRevengeCharge () {: aria-label='Functions' }
#### void SetMontezumaRevengeCharge ( int Charge ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetRUAWizardTimer () {: aria-label='Functions' }
#### void SetRUAWizardTimer ( int timer ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetTearDisplacement () {: aria-label='Functions' }
#### void SetTearDisplacement ( int Displacement ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the player's TearDisplacement value, which represents which eye the player is shooting from.

Note that the game will typically alternate this value BEFORE shooting a tear.

???+ info "TearDisplacement"
    - `1` Right eye
    - `-1` Left eye

___

### UnblockTrinket () {: aria-label='Functions' }
#### void UnblockTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) Trinket ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Unblocks the [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) that was blocked through [BlockTrinket](EntityPlayer.md#blocktrinket).

___

</div>
