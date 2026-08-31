---
tags:
  - 全局
  - 类
  - Isaac
---
# 全局类 "Isaac"

???+ info "提示"
    你可以通过全局表`Isaac`来获取该类。

    **访问Isaac类的方法时，需要使用`.`（句点）而不是`:`（冒号）！**

    ???+ example "示例代码"
    ```lua
    local player = Isaac.GetPlayer()
    ```

## 函数

### Add·Callback () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddCallback ( table modRef, [ModCallback](enums/ModCallbacks.md)|string callbackId, table callbackFn, int entityId ) {: .copyable aria-label='Functions' }
添加一个MOD回调。

推荐使用[Mod Reference](ModReference.md)的[AddCallback](ModReference.md#addcallback)函数而非该函数。

___

### Add·Pill·Effect·To·Pool () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [PillColor](enums/PillColor.md) AddPillEffectToPool ( [PillEffect](enums/PillEffect.md) pillEffect ) {: .copyable aria-label='Functions' }
将一个胶囊效果pillEffect加入到胶囊池中。

返回加入的胶囊的[胶囊颜色](enums/PillColor.md)。

___

### Add·Priority·Callback () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddPriorityCallback ( table modRef, [ModCallback](enums/ModCallbacks.md)|string callbackId, [CallbackPriority](enums/CallbackPriority.md) priority, table callbackFn, int entityId ) {: .copyable aria-label='Functions' }
添加一个MOD回调。该回调具有优先级，并根据优先级决定执行顺序。

推荐使用[Mod Reference](ModReference.md)的[AddPriorityCallback](ModReference.md#addcallback)函数而非该函数。

___

### Console·Output () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ConsoleOutput ( string text ) {: .copyable aria-label='Functions' }

向控制台打印一行文本。

???- example "示例代码"
    你可以使用该示例作为替代。
    ```lua
    Isaac.ConsoleOutput("This is a Test.")
    -- 输出: This is a Test.

    -- 替代以下代码:
    print("This is a Test.")
    -- 输出: This is a Test.

    ```

___

### Count·Bosses () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int CountBosses ( ) {: .copyable aria-label='Functions' }

返回本房间内的头目数量。
___

### Count·Enemies () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int CountEnemies ( ) {: .copyable aria-label='Functions' }

返回本房间内的敌人数量。
___

### Count·Entities () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### int CountEntities ( [Entity](Entity.md) Spawner, [EntityType](enums/EntityType.md) Type = EntityType.ENTITY_NULL, int Variant = -1, int SubType = -1 ) {: .copyable aria-label='Functions' }

返回本房间内的满足指定需求的实体数量。

- `Spawner`为该实体的创建者。（可以为`:::lua nil`）
- `Type`为该实体的类型。（可以为`:::lua EntityType.ENTITY_NULL`）
- `Variant`和`Subtype`为该实体的变体和子类型。（可以为`:::lua -1`）

___

### Debug·String () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void DebugString ( string str ) {: .copyable aria-label='Functions' }

向日志文件打印一行文本。你可以在这里找到文件：`:::lua %systemdrive%\Users\%username%\Documents\My Games\Binding of Isaac Repentance\log.txt`

???- example "示例代码"
    这行代码会向log.txt打印`:::lua "This is a Test."`。
    ```lua
    Isaac.DebugString("This is a Test.")
    -- Output: [INFO] - Lua Debug: This is a Test.
    ```

___

### Execute·Command () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### string ExecuteCommand ( string command ) {: .copyable aria-label='Functions' }

执行一个控制台指令。

关于如何使用指令，见[控制台教程](tutorials/DebugConsole.md)。
___

### Explode () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Explode ( [Vector](Vector.md) pos, [Entity](Entity.md) source, float damage ) {: .copyable aria-label='Functions' }

在pos位置生成一次爆炸。其伤害源实体为source，伤害为damage。
___

### Find·By·Type () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### table FindByType ( [EntityType](enums/EntityType.md) Type, int Variant = -1, int SubType = -1, boolean Cache = false, boolean IgnoreFriendly = false ) {: .copyable aria-label='Functions' }
返回符合Type，Variant和SubType的所有实体。如果Variant/SubType为-1，表示包括任意Variant/SubType的实体。Cache为true时会缓存结果，一帧执行多次时可以使用。

如果一个实体拥有`EntityFlag.FLAG_NO_QUERY`实体标志，它不会出现在查询结果中。如果需要获取拥有该实体标志的实体，应该改为使用`GetRoomEntities`函数。

___

<div class="rgon-extension" markdown="1">

### FindByType () {: aria-label='Modified Functions' }

#### [Entity](Entity.md)[] FindByType ( [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) Type, int Variant = -1, int SubType = -1, boolean Cache = false, boolean IgnoreFriendly = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }

与原版功能相同，但速度快得多。

___

</div>

### Find·In·Radius () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [Entity](Entity.md)[] FindInRadius ( [Vector](Vector.md) Position, float Radius, [EntityPartition](enums/EntityPartition.md) Partitions = 0xFFFFFFFF  ) {: .copyable aria-label='Functions' }
返回中心为Position，半径为Radius范围内的所有由Partitions筛选的实体（包括所有 = 0xffffffff）

该函数不根据实体距离中心的距离，而是根据他们加载的顺序排序。
___

<div class="rgon-extension" markdown="1">

### FindInRadius () {: aria-label='Modified Functions' }

#### [Entity](Entity.md)[] FindInRadius ( [Vector](Vector.md) Position, float Radius, [EntityPartition](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityPartition.html) Partitions = 0xFFFFFFFF  ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }

与原版功能相同，但速度快得多，并且修复了效果搜索的问题。

___

</div>

### Get·Built·In·Callback·State () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### boolean GetBuiltInCallbackState ( function callbackId ) {: .copyable aria-label='Functions' }
获取内置回调状态。

如果ID为`callbackId`的回调会被游戏执行，返回`true`。如果不存在ID为`callbackId`的回调，会返回`false`。
___

### Get·Callbacks () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### table GetCallbacks ( function callbackId, boolean createIfMissing ) {: .copyable aria-label='Functions' }
获取所有ID为`callbackId`的MOD回调。这些回调会表示为一个表，更多信息请查阅[自定义回调教程](tutorials/CustomCallbacks.md#run-behavior)。

游戏会将所有ID为`callbackId`的回调加进一个表里，`callbackId`是其索引，而值则是一个包含所有ID为`callbackId`的回调的表。

如果`createIfMissing`为`true`，并且不存在ID为`callbackId`的回调，游戏会自动创建一个包含ID为`callbackId`的回调的空表，用于增加新的回调。这个空表包含一个具有默认元函数`__matchParams`的元表，而这个元函数会在添加回调，并且检查指定的额外参数是否匹配时被调用。每当一个回调被添加时，这个元函数也会被使用，其参数`createIfMissing`为`true`。

如果`createIfMissing`为`false`或者`nil`，并且不存在ID为`callbackId`的回调，该函数返回一个空表。

___

### Get·Card·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Card](enums/Card.md) GetCardIdByName ( string cardHudName ) {: .copyable aria-label='Functions' }
基于“pocketitems.xml”文件中定义的“hud”属性返回[卡牌ID](enums/Card.md) 。如果找不到具有该“hud”属性值的卡，则返回`-1`。

???+ warning "警告"
    该函数的名称具有误导性，该函数只能使用卡片的“hud”属性值，而不能使用卡牌的名称。

???+ bug "漏洞"
    此函数不适用于原版卡片/符文，因为它们在pocketitems.xml文件中的条目中没有定义“hud”属性。您需要使用[Card](enums/Card.md)枚举来获取原版的ID。

???- example "示例代码"
    以下代码获取一张MOD卡牌的卡牌ID。
    ```xml
    <pocketitems>
        <card type="tarot" pickup="1" description="some description"  name="My new card" hud="my_modded_card" />
    </pocketitems>
    ```
    ```lua
    Isaac.GetCardIdByName("my_modded_card")
    ```

___

### Get·Challenge () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Challenge](enums/Challenge.md) GetChallenge ( ) {: .copyable aria-label='Functions' }
返回玩家当前正在进行的挑战的ID。如果玩家没有进行任何挑战，则返回0。
___

### Get·Challenge·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Challenge](enums/Challenge.md) GetChallengeIdByName ( string challengeName ) {: .copyable aria-label='Functions' }

根据挑战的名称返回挑战的ID。（文件：challenges.xml）如果找不到具有该名称的挑战，则返回`-1`（区分大小写）。

???- example "示例代码"
    以下代码获取挑战“愚人节”的挑战ID。
    ```lua
    Isaac.GetChallengeIdByName("Aprils fool")
    --返回：32
    ```

___

### Get·Costume·Id·By·Path () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetCostumeIdByPath ( string path ) {: .copyable aria-label='Functions' }

根据外观的文件路径返回外观的ID。（文件：costumes2.xml）如果找不到具有该路径的外观，则返回`-1`。

???- example "示例代码"
    以下代码获取套装“拉了！”的外观ID。
    ```lua
    Isaac.GetCostumeIdByPath("gfx/characters/n027_Transformation_Poop.anm2")
    --返回：27
    ```

___

### Get·Curse·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [LevelCurse](enums/LevelCurse.md) GetCurseIdByName ( string curseName ) {: .copyable aria-label='Functions' }

根据诅咒的名称返回诅咒的ID。（文件：curses.xml）如果找不到具有该名称的诅咒，则返回`-1`。

???- example "示例代码"
    以下代码获取未知诅咒的诅咒ID。
    ```lua
    Isaac.GetCurseIdByName("Curse of the Unknown")
    --返回：4
    ```

___

### Get·Entity·Type·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityType](enums/EntityType.md) GetEntityTypeByName ( string entityName ) {: .copyable aria-label='Functions' }

根据实体的名称返回实体的EntityType。（文件：entities2.xml）如果找不到具有该名称的实体，则返回`0`。

???- note "注意"
    没有该函数的SubType版本。

???- example "示例代码"
    以下代码获取燃烧裂口尸的EntityType。
    ```lua
    Isaac.GetEntityTypeByName("Flaming Gaper")
    --返回：10
    ```

___

### Get·Entity·Variant·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetEntityVariantByName ( string entityName ) {: .copyable aria-label='Functions' }

根据实体的名称返回实体的Variant。（文件：entities2.xml）如果找不到具有该名称的实体，则返回`-1`。

???- note "注意"
    没有该函数的SubType版本。

???- example "示例代码"
    以下代码获取燃烧裂口尸的Variant。

    ```lua
    Isaac.GetEntityVariantByName("Flaming Gaper")
    --返回：2
    ```

___

### Get·Frame·Count () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetFrameCount ( ) {: .copyable aria-label='Functions' }

返回整个游戏正在运行的帧数。即使游戏暂停或在主菜单中，计数器也会增加！

1秒大致等于60帧。

因此，此函数的工作方式与[`:::lua Game():GetFrameCount()`](Game.md#getframecount)截然不同。

___

### Get·Free·Near·Position () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetFreeNearPosition ( [Vector](Vector.md) pos, float step ) {: .copyable aria-label='Functions' }

返回距离位置pos最近的空区域。
___

### Get·Item·Config () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [ItemConfig](ItemConfig.md) GetItemConfig ( ) {: .copyable aria-label='Functions' }

获取ItemConfig对象。

这是唯一可以访问`ItemConfig`对象的方法。
___

### Get·Item·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [CollectibleType](enums/CollectibleType.md) GetItemIdByName ( string itemName ) {: .copyable aria-label='Functions' }

根据道具名称返回道具的ID。（文件：items.xml）如果找不到具有该名称的道具，则返回`-1`。

???- example "示例代码"
    以下代码获取一个MOD道具的ID。
    ```xml
    <passive id="1" name="My Mod Item" description="some description" gfx="my_modded_item.png"/>
    ```
    ```lua
    Isaac.GetItemIdByName("My Mod Item")
    ```

___

### Get·Music·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Music](enums/Music.md) GetMusicIdByName ( string musicName ) {: .copyable aria-label='Functions' }

返回一个音乐的ID。（文件：music.xml）如果找不到具有该名称的音乐，则返回`-1`。

???- example "示例代码"
    以下代码获取标题界面的音乐ID。

    ```lua
    Isaac.GetMusicIdByName("Title Screen")
    --返回：61
    ```

___

### Get·Pill·Effect·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [PillEffect](enums/PillEffect.md) GetPillEffectByName ( string pillEffect ) {: .copyable aria-label='Functions' }

根据胶囊效果的名称返回胶囊效果ID。（文件：pocketitems.xml）如果找不到具有该名称的胶囊效果，则返回`-1`。

???- example "示例代码"
    以下代码获取“我能永远看清！”的胶囊效果ID。

    ```lua
    Isaac.GetPillEffectByName("I can see forever!")
    --返回：23
    ```

___

### Get·Player () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [EntityPlayer](EntityPlayer.md) GetPlayer ( int playerID = 0 ) {: .copyable aria-label='Functions' data-altreturn='nil' }

返回与提供的玩家ID匹配的EntityPlayer。玩家ID从0开始并向上递增。例如，当扮演雅各布和以扫时，雅各布的玩家ID将为0，以扫的玩家ID为1。

如果传递了无效的玩家ID（例如-20或20），则函数将假定玩家索引为0。

如果在任何玩家初始化之前调用此函数（即在主菜单中调用它），则此函数会返回`nil`。

此函数与[`Game():GetPlayer()`](Game.md#GetPlayer)相同。

???- example "示例代码"

    ```lua
    local function getPlayers()
      local game = Game()
      local numPlayers = game:GetNumPlayers()

      local players = {}
      for i = 0, numPlayers - 1 do
        local player = Isaac.GetPlayer(i)
        table.insert(players, player)
      end

      return players
    end
    ```

___

### Get·Player·Type·By·Name () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### [PlayerType](enums/PlayerType.md) GetPlayerTypeByName ( string playerName , boolean Tainted = false ) {: .copyable aria-label='Functions' }

根据角色的名称返回角色类型（ID）。（文件：players.xml）如果找不到具有该名称的角色，则返回`-1`。

???+ warning "警告"
    在《忏悔》中，角色名字被设置为可翻译文本，并且会使用翻译占位符作为他们的“基本名称”。例如，要获取该隐的[角色类型](enums/PlayerType.md)，你需要使用名称`#CAIN_NAME`而非`Cain`。
    建议对MOD角色使用该函数，而对原版角色直接使用[PlayerType](enums/PlayerType.md)枚举。

???- example "示例代码"
    以下代码获取阿撒泻勒的角色类型。

    ```lua
    -- 忏悔：
    Isaac.GetPlayerTypeByName("#AZAZEL_NAME") --返回: 7

    -- 胎衣+:
    Isaac.GetPlayerTypeByName("Azazel") --Returns: 7

    ```

___

### Get·Random·Position () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) GetRandomPosition ( ) {: .copyable aria-label='Functions' }

返回当前房间内的随机位置。

返回值是一个向量，表示世界坐标中的位置。
___

### Get·Room·Entities () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md)[] GetRoomEntities ( ) {: .copyable aria-label='Functions' }

返回一个可遍历的表，该表包含调用函数时房间中的所有实体。

此行为不同于[`Room::GetEntities()`](Room.md#GetEntities)，后者返回一个原始指针，指向在任何给定时间存储房间所有实体的数组。

**对于大多数用例，建议使用[`Isaac.GetRoomEntities（）`](Isaac.md#getroomnentities)！**

???- example "示例代码"
    以下代码打印房间中每个实体的Type、Variant和SubType。

    ```lua
    for i, entity in ipairs(Isaac.GetRoomEntities()) do
        print(entity.Type, entity.Variant, entity.SubType)
    end

    ```

___

<div class="rgon-extension" markdown="1">

### GetRoomEntities () {: aria-label='Modified Functions' }

#### [Entity](Entity.md)[] GetRoomEntities ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }

与原版功能相同，但速度快得多。

___

</div>

### Get·Screen·Height () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### float GetScreenHeight ( ) {: .copyable aria-label='Functions' }

获取游戏屏幕的高度（以像素为单位）。
___

### Get·Screen·Point·Scale () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### float GetScreenPointScale ( ) {: .copyable aria-label='Functions' }

返回一个表示屏幕“缩放”程度的数字。

根据游戏窗口的分辨率，可以是`1.0`或`2.0`等。

???- example "视频演示"
    <figure class="video_container">
        <video controls="true" allowfullscreen="true" muted="true" style="width:25rem">
            <source src="./customData/screen-point-scale.mp4" type="video/mp4">
        </video>
        <figcaption>演示游戏窗口的大小如何改变此函数返回的值。</figcaption>
    </figure>

___

### Get·Screen·Width () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### float GetScreenWidth ( ) {: .copyable aria-label='Functions' }

获取游戏屏幕的宽度（以像素为单位）。
___

### Get·Sound·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [SoundEffect](enums/SoundEffect.md) GetSoundIdByName ( string soundName ) {: .copyable aria-label='Functions' }

根据音效的名称返回[SoundEffect](enums/SoundEffect.md)。（文件：sounds.xml）如果找不到具有该名称的音效，则返回`-1`。

???- example "示例代码"
    以下代码获取名为"Custom Sound Effect"的音效ID。

    ```lua
    Isaac.GetSoundIdByName("Custom Sound Effect")

    ```

___

### Get·Text·Width () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetTextWidth ( string str ) {: .copyable aria-label='Functions' }

基于“terminus8”字体（与Isaac.RenderText()中使用的字体相同），返回给定字符串的宽度（以像素为单位）。

___

### Get·Time () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetTime ( ) {: .copyable aria-label='Functions' }

返回自计算机操作系统启动以来的当前时间（以毫秒为单位）。

这与经过了多少帧无关，对于测量经过了多少实时时间非常有用。（帧并不是一个很好的时间指标，因为游戏会在每层过渡动画和房间过渡动画时加载新数据，然后锁定。）

例如，您可以使用它来实现基于实时的屏幕速度运行计时器，或者将一个函数的性能影响与另一个函数进行比较。

___

### Get·Trinket·Id·By·Name () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [TrinketType](enums/TrinketType.md) GetTrinketIdByName ( string trinketName ) {: .copyable aria-label='Functions' }

根据饰品的名称返回其饰品ID。（文件：items.xml）如果找不到具有该名称的饰品，则返回`-1`。

???- example "示例代码"
    以下代码获取一个MOD饰品的ID。
    ```xml
    <trinket id="1" name="My Mod Trinket" description="some description" gfx="my_modded_trinket.png"/>
    ```
    ```lua
    Isaac.GetTrinketIdByName("My Mod Trinket")
    ```

___

### Grid·Spawn () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [GridEntity](GridEntity.md) GridSpawn ( [GridEntityType](enums/GridEntityType.md) gridEntityType, int variant, [Vector](Vector.md) position, boolean forced ) {: .copyable aria-label='Functions' }

在给定位置（世界坐标）生成一个[网格实体](GridEntity.md)。

???+ bug "Bugs"
    “forced”参数可以用于在某些特定情况下覆盖给定位置的网格实体。例如：不能覆盖一块岩石，但可以覆盖已经被炸毁的岩石。你可以通过`Isaac.GetFreeNearPosition`查询一个位置是否被认为是空地。通过检查返回的网格实体的类型，可以确保正确进行了替换。否则，你可能需要删除给定位置的网格实体，然后在其位置生成其他内容。

例如，要在房间中央生成一块超级标记石头：

```lua
local game = Game()
local room = game:GetRoom()
local centerPos = room:GetCenterPos()
Isaac.GridSpawn(GridEntityType.GRID_ROCK_SS, 0, centerPos, true)
```

___

### Has·Mod·Data () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasModData ( table modRef ) {: .copyable aria-label='Functions' }

如果您的mod使用“SaveModData()”函数存储了数据——换句话说，如果你的mod的数据文件夹中有一个“saveX.dat”文件，则返回`true`。

有3个“saveX.dat”文件，每个存档一个。数字表示它对应的存档，由游戏自动确定。

对于AB+，它们存储在“main.lua”文件旁边的mod文件夹中。

对于忏悔，它们存储在游戏文件中“mods”文件夹旁边的“data”文件夹中。

建议使用[Mod Reference](ModReference.md#hasdata)的[HasData](ModReference.md#HasData)函数而非该函数。
___

### Load·Mod·Data () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### string LoadModData ( table modRef ) {: .copyable aria-label='Functions' }

返回使用“SaveModData()”函数存储在“saveX.dat”文件中的字符串。如果您的mod的数据中没有“saveX.dat”文件，此函数将返回一个空字符串。

有3个“saveX.dat”文件，每个存档一个。数字表示它对应的存档，由游戏自动确定。

如果在主菜单中调用此函数，默认情况下，它将返回存档1的保存数据。

对于AB+，它们存储在“main.lua”文件旁边的mod文件夹中。

对于忏悔，它们存储在游戏文件中“mods”文件夹旁边的“data”文件夹中。

建议使用[Mod Reference](ModReference.md#hasdata)的[LoadData](ModReference.md#HasData)函数而非该函数。
___

### Register·Mod () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RegisterMod ( table modRef, string modName, int apiVersion ) {: .copyable aria-label='Functions' }

在游戏中注册一个表以使用[Mod Reference](ModReference.md)。

建议改用全局的[RegisterMod](GlobalFunctions.md#RegisterMod)函数。

___

### Remove·Callback () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveCallback ( table modRef, [ModCallback](enums/ModCallbacks.md)|string callbackId, table callbackFn ) {: .copyable aria-label='Functions' }

移除一个MOD回调。

推荐使用[Mod Reference](ModReference.md)的[RemoveCallback](ModReference.md#addcallback)函数而非该函数。

___

### Remove·Mod·Data () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveModData ( table modRef ) {: .copyable aria-label='Functions' }

如果存在储存的“saveX.dat”文件，将其删除。

有3个“saveX.dat”文件，每个存档一个。数字表示它对应的存档，由游戏自动确定。

建议使用[Mod Reference](ModReference.md#hasdata)的[RemoveData](ModReference.md#HasData)函数而非该函数。
___

### Render·Scaled·Text () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderScaledText ( string str, float X, float Y, float ScaleX, float ScaleY, float R, float G, float B, float A ) {: .copyable aria-label='Functions' }

在屏幕上渲染缩放后的文本。X和Y坐标需要在屏幕坐标（X[0，~500) Y[0，~350) ）中。ScaleX、ScaleY、R、G、B和A需要在[0,1]之间。

某些比例值可能会导致字体显示变形和像素化。

???- example "示例代码"
    以下代码在屏幕上显示玩家的位置。

    ```lua
    local player = Isaac.GetPlayer()
    local text = "X: " .. player.Position.X .. ", Y: " .. player.Position.Y
    Isaac.RenderScaledText(text, 50, 50, 0.5, 0.5, 1, 1, 1, 1)
    ```

___

### Render·Text () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RenderText ( string str, float X, float Y, float R, float G, float B, float A ) {: .copyable aria-label='Functions' }

在屏幕上渲染默认大小的文本。X和Y坐标需要在屏幕坐标（X[0，~500) Y[0，~350) ）中。ScaleX、ScaleY、R、G、B和A需要在[0,1]之间。

???- example "示例代码"
    以下代码在屏幕上显示玩家的位置。

    ```lua
    local player = Isaac.GetPlayer()
    local pos = player.Position
    Isaac.RenderText("X: "..pos.X.." Y: "..pos.Y, 50, 50, 1 ,1 ,1 ,1 )

    ```

___

### Run·Callback () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void RunCallback ( [ModCallback](enums/ModCallbacks.md)|string callbackId, ...) {: .copyable aria-label='Functions' }

执行所有ID为`callbackId`的MOD回调，会在第一个返回值出现时中断，并使该函数返回该值。
___

### Run·Callback·With·Param () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void RunCallbackWithParam ( [ModCallback](enums/ModCallbacks.md)|string callbackId, object param, ...) {: .copyable aria-label='Functions' }
Runs all callbacks added under `callbackId`, breaking on the first return and returning that value.

执行所有可选参数为`param`的`callbackId`的MOD回调，会在第一个返回值出现时中断，并使该函数返回该值。
___

### Save·Mod·Data () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SaveModData ( table modRef, string data ) {: .copyable aria-label='Functions' }

向“saveX.dat”存储一串字符串。存储的数据在重开一局和游戏重启之后也会存在，因此非常适合存储持久数据。

有3个“saveX.dat”文件，每个存档一个。数字表示它对应的存档，由游戏自动确定。

对于AB+，它们存储在“main.lua”文件旁边的mod文件夹中。

对于忏悔，它们存储在游戏文件中“mods”文件夹旁边的“data”文件夹中。

建议使用[Mod Reference](ModReference.md#hasdata)的[SaveData](ModReference.md#HasData)函数而非该函数。
___

### Screen·To·World () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) ScreenToWorld ( [Vector](Vector.md) pos ) {: .copyable aria-label='Functions' }

将屏幕坐标（也称为窗口坐标）转换为世界坐标。这可以用于根据屏幕上的某一点获取房间中的特定位置。

世界坐标为x[0，inf) y[0，inf)。
___

### Screen·To·World·Distance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) ScreenToWorldDistance ( [Vector](Vector.md) pos ) {: .copyable aria-label='Functions' }
___

### Set·Built·In·Callback·State () {: aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void SetBuiltInCallbackState ( [ModCallbacks](enums/ModCallbacks.md) callbackId, boolean state ) {: .copyable aria-label='Functions' }
Sets whether callbacks under `callbackId` will be ran by the game. The game uses this to activate a [ModCallbacks](enums/ModCallbacks.md) once a callback is added under one, or deactivate them when those callbacks have been removed.

设置内置回调状态。

作用未知。
___

### Spawn () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) Spawn ( [EntityType](enums/EntityType.md) entityType, int entityVariant, int entitySubtype, [Vector](Vector.md) position, [Vector](Vector.md) velocity, [Entity](Entity.md) Spawner ) {: .copyable aria-label='Functions' }

在给定位置生成一个实体。如果位置不是空的，会在最近的空位置生成。

存在两个生成实体的函数。一个是[Isaac.Spawn()](Isaac.md#spawn)（该函数），用于以随机种子生成一个实体；另一个是[Game():Spawn()](Game.md#spawn)，用于以特定种子生成一个实体。但由于一个BUG，[Isaac.Spawn()](Isaac.md#spawn)有概率生成种子为0的实体，会导致游戏崩溃。如果需要生成一个拥有随机种子的实体，应该总是使用一个自定义的辅助函数，其使用[Random()](GlobalFunctions.md#random)获取种子，在种子为0时将其改为1，并且使用[Game():Spawn()](Game.md#spawn)来生成实体。([IsaacScript](https://isaacscript.github.io/)用户使用`spawn`辅助函数就可以了，它自己就会使用`Game.Spawn`。)

???- example "示例代码"
    以下代码在本房间的中央生成一个随机道具。
    ```lua
    Isaac.Spawn(EntityType.ENTITY_PICKUP, PickupVariant.PICKUP_COLLECTIBLE, 0, Vector(320,280), Vector(0,0), nil)
    ```

???+ bug "Bug"
    由于随机种子使用的是[Random()](GlobalFunctions.md#random)函数，会导致生成的实体的InitSeed可能为0。如果这个实体要用到随机数生成器，游戏会崩溃。
___

### World·To·Render·Position () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) WorldToRenderPosition ( [Vector](Vector.md) pos ) {: .copyable aria-label='Functions' }

将世界坐标（又名游戏坐标）转换为渲染坐标。这可以用于在房间中的固定位置渲染事物。渲染坐标系为x[0，inf) y[0，inf)。它定义当前房间中渲染平面上的位置。

???- example "示例代码"
    以下代码在鼠标光标的位置渲染“Test”，与游戏是否处于全屏无关。
    ```lua
    local mousePos = Input.GetMousePosition(true)
    local renderpos = Isaac.WorldToRenderPosition(mousePos) * 2
    Isaac.RenderText("test", renderpos.X, renderpos.Y, 1 ,1 ,1 ,1 )
    ```

___

### World·To·Screen () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) WorldToScreen ( [Vector](Vector.md) pos ) {: .copyable aria-label='Functions' }

将世界坐标（又名游戏坐标）转换为屏幕（又名窗口）坐标。这可以用来渲染实体旁边的东西。屏幕坐标系为x[0，inf) y[0，inf)。通常情况下，它一直到~500x ~300y。

返回值向量包含整数值或以.5结尾的数字。

???- example "示例代码"
    以下代码在角色的位置渲染“Test”，会跟随角色移动。
    ```lua
    local player = Isaac.GetPlayer()
    local screenpos = Isaac.WorldToScreen(player.Position)
    Isaac.RenderText("test", screenpos.X, screenpos.Y, 1 ,1 ,1 ,1 )
    ```

___

### World·To·Screen·Distance () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) WorldToScreenDistance ( [Vector](Vector.md) pos ) {: .copyable aria-label='Functions' }

___

<div class="rgon-only" markdown="1">

### AllMarksFilled () {: aria-label='Functions' }

#### int AllMarksFilled ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

检查给定角色是否已完成所有标记，并返回一个整数，表示完成这些标记的最高难度。
???- info "Note"

  难度等级如下：
  - `0` - 未完成
  - `1` - 普通
  - `2` - 困难

___

### AllTaintedCompletion () {: aria-label='Functions' }

#### int AllTaintedCompletion ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [TaintedMarksGroup](enums/TaintedMarksGroup.md) Group) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

检查给定角色是否已完成所有与受污染解锁相关的标记，并返回一个整数，表示完成这些标记的最高难度。

???- info "Note"

  难度等级如下：
  - `0` - 未完成
  - `1` - 普通
  - `2` - 困难

___

### CanStartTrueCoop () {: aria-label='Functions' }

#### boolean CanStartTrueCoop ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### CenterCursor () {: aria-label='Functions' }

#### void CenterCursor ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

将窗口鼠标光标移动到游戏窗口的中心。这是一个非常小众但很有用的功能，如果您想使用光标控制进行任何奇特的操作并完全控制它。如果 Isaac.exe 失去焦点，它不会移动光标。

???- info "Note"

    请记住，屏幕中心不一定是房间的中心，它只是游戏窗口的中心（如果您处于全屏模式，则是实际屏幕的中心）。

___

### ClearBossHazards () {: aria-label='Functions' }

#### void ClearBossHazards ( boolean IgnoreNPCs = false ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }

清除所有弹幕。如果 `IgnoreNPCs` 为 false，还会清除所有能够关闭门的非友方 NPC。

___

### ClearChallenge () {: aria-label='Functions' }

#### void ClearChallenge ( int challengeid) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

将相应 `challengeid` 的挑战标记为已完成。

___

### ClearCompletionMarks () {: aria-label='Functions' }

#### void ClearCompletionMarks ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

删除给定角色的所有完成标记。

___

### CreateTimer () {: aria-label='Functions' }

#### [EntityEffect](https://wofsauge.github.io/IsaacDocs/rep/EntityEffect.html) CreateTimer ( function Function, int Interval, int Times, boolean Persistent ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

此计时器在每次游戏更新时调用。这意味着计时器仅考虑游戏正在积极运行且未暂停的帧，并使用更新帧作为其延迟参数（每秒 30 帧）。
生成一个计时器实体效果。该实体将在 `Interval` 帧后开始运行 `Function` 函数，并将重复执行 `Times` 次。`Persistent` 控制此计时器是在当前房间“死亡”，还是跨房间持续存在。

???- info "计时器行为"

    如果您的用例需要计时器考虑暂停时间，请使用在 RENDER 回调上运行的自定义计时器。

___

### CreateWeapon () {: aria-label='Functions' }

#### [Weapon](Weapon.md) CreateWeapon ( [WeaponType](https://wofsauge.github.io/IsaacDocs/rep/enums/WeaponType.html) Type, [Entity](Entity.md) Owner ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

创建并返回一个 [Weapon](Weapon.md) 对象。它不会自动被 `owner` 使用，必须与 `Isaac.SetWeaponType` 一起使用。

___

### DestroyWeapon () {: aria-label='Functions' }

#### void DestroyWeapon ( [Weapon](Weapon.md) Weapon ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

销毁提供的 [Weapon](Weapon.md) 对象。

___

### DrawLine () {: aria-label='Functions' }

#### void DrawLine ( [Vector](Vector.md) StartPos, [Vector](Vector.md) EndPos, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor) StartColor, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor) EndColor, int Thickness ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

在当前渲染帧中，在两个给定位置之间绘制一条线。

___

### DrawQuad () {: aria-label='Functions' }

#### void DrawQuad ( [Vector](Vector.md) TopLeftPos, [Vector](Vector.md) TopRightPos, [Vector](Vector.md) BottomLeftPos, [Vector](Vector.md) BottomRightPos, [KColor](https://wofsauge.github.io/IsaacDocs/rep/KColor) Color, int Thickness ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

在当前渲染帧中，在两个给定位置之间绘制一条线。游戏内部使用自己的结构体 DestinationQuad 来实现此功能，但我还没有将其添加到 Lua 中 :crocodile:

___

### FillCompletionMarks () {: aria-label='Functions' }

#### void FillCompletionMarks ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

完成给定角色的所有完成标记。

___

### FindInCapsule () {: aria-label='Functions' }

#### [Entity](Entity.md)[] FindInCapsule ( [Capsule](Capsule.md) Capsule, [EntityPartitions](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityPartition.html) Partitions = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

返回给定胶囊内的实体，并根据分区掩码进行过滤。

___

### FindTargetPit () {: aria-label='Functions' }

#### int FindTargetPit ( [Vector](Vector.md) Position, [Vector](Vector.md) TargetPosition, int PitIndex = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetAchievementIdByName () {: aria-label='Functions' }

#### int GetAchievementIdByName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

按名称获取成就 ID。

___

### GetAllowedDoorsMaskForRoomShape () {: aria-label='Functions' }
#### [DoorMask](enums/DoorMask.md) GetAllowedDoorsMaskForRoomShape ( [RoomShape](https://wofsauge.github.io/IsaacDocs/rep/enums/RoomShape.html) RoomShape ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a [DoorMask](enums/DoorMask.md) representing all [DoorSlots](https://wofsauge.github.io/IsaacDocs/rep/enums/DoorSlot.html) allowed for the given [RoomShape](https://wofsauge.github.io/IsaacDocs/rep/enums/RoomShape.html).

___

### GetAxisAlignedUnitVectorFromDir () {: aria-label='Functions' }

#### [Vector](Vector.md) GetAxisAlignedUnitVectorFromDir ( [Direction](https://wofsauge.github.io/IsaacDocs/rep/enums/Direction.html) Direction = -1 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBackdropIdByName () {: aria-label='Functions' }

#### int GetBackdropIdByName ( string BackdropName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBossColorIdxByName () {: aria-label='Functions' }

#### int GetBossColorIdxByName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

按名称获取 boss 颜色索引，该索引通常是 boss 变为所需颜色所需的子类型。当然，您实际上需要在 xml 中为您的颜色条目命名，此功能才能正常工作（后缀通常不起作用，因为它不是必需的）。

___

### GetButtonsSprite () {: aria-label='Modified Functions' }
#### [Sprite](Sprite.md) GetButtonsSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回控制器按钮精灵。

___

### GetClipboard () {: aria-label='Functions' }

#### string GetClipboard ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

获取剪贴板的内容，前提是它们是文本形式，否则将返回 nil。

___

### GetCollectibleSpawnPosition () {: aria-label='Functions' }

#### [Vector](Vector.md) GetCollectibleSpawnPosition ( [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCompletionMark () {: aria-label='Functions' }

#### int GetCompletionMark ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [CompletionType](enums/CompletionType.md) Mark) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

获取特定角色的完成标记值，值范围从 `0` 到 `2`（0 = 未完成，1 = 普通，2 = 困难）。

___

### GetCompletionMarks () {: aria-label='Functions' }

#### table GetCompletionMarks ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

返回一个包含给定角色所有标记的表

???- info "Table structure & usage"

    该表具有以下字段

    - 角色类型（PlayerType）：包含与标记相关的 [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html).
    - MomsHeart: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Isaac: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Satan: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - BossRush: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - BlueBaby: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Lamb: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - MegaSatan: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - UltraGreed: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Hush: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - UltraGreedier：困难贪婪模式，值为 2；大多情况下与 UltraGreed 重复，无需设置
    - Delirium: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Mother: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Beast: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况

    ```lua
    local marks = Isaac.GetCompletionMarks(0)
    if (marks.MomsHeart > 0) then
        print("got mom")
    end
    if (marks.Lamb >= 2) then
        print("GOATED ON H4RD")
    end
    if (Isaac.GetCompletionMarks(0).Delirium > 0) then --doing it the lazy way, fitting deliriums theme
        print("Got Deli")
    end
    ```

___

### GetCurrentStageConfigId () {: aria-label='Functions' }

#### [StbType](enums/StbType.md) GetCurrentStageConfigId ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

获取当前阶段的当前 stageconfigId/stbType，或者您想称呼的 stages.xml 的 ID。

___

### GetCursorSprite () {: aria-label='Functions' }

#### [Sprite](Sprite.md) GetCursorSprite ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

当 `Options.MouseControl` 设置为 true 时，返回渲染的光标精灵。

___

### GetCutsceneIdByName () {: aria-label='Functions' }

#### table GetCutsceneIdByName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

按名称获取过场动画 ID。

___

### GetDwmWindowAttribute () {: aria-label='Functions' }

#### [DwmWindowAttribute](enums/DwmWindowAttribute.md) GetDwmWindowAttribute ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetEntitySubTypeByName () {: aria-label='Functions' }

#### int GetEntitySubTypeByName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

按实体名称获取实体子类型。

___

### GetGiantBookIdByName () {: aria-label='Functions' }

#### int GetGiantBookIdByName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

按名称获取巨型书籍 ID。对于原版巨型书籍，gfx xml 属性中的 png 文件名用作巨型书籍名称。

___

### GetLoadedModules () {: aria-label='Functions' }

#### table GetLoadedModules ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

返回一个键值表，包含所有已加载的脚本文件，其中键是给定脚本文件的名称或路径，值是加载该文件后的返回值（在大多数情况下是 true 或一个表）。

___

### GetLocalizedString () {: aria-label='Functions' }

#### string GetLocalizedString ( string Category, string Key, int Language ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

返回给定类别中与给定键关联的翻译字符串。翻译以作为参数给出的语言 ID/语言代码提供。

___

### GetModChallengeClearCount () {: aria-label='Functions' }

#### int GetModChallengeClearCount ( int challengeid ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

返回自定义挑战被通关的次数。如果该挑战被设置为未完成，则该次数将重置。

___

### GetNanoTime () {: aria-label='Functions'}
#### int GetNanoTime ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a high-resolution timestamp in nanoseconds. Useful for evaluating the performance cost of functions in a non-test environment or for high-precision clocks.

???- info "Note"
	The clock is precise enough to detect the time that passed between two subsequent calls of `Isaac.GetNanoTime()`

___

### GetNullItemIdByName () {: aria-label='Functions' }

#### int GetNullItemIdByName ( string NullItemName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPersistentGameData () {: aria-label='Functions' }

#### [PersistentGameData](PersistentGameData.md) GetPersistentGameData ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPoolIdByName () {: aria-label='Functions' }

#### [ItemPoolType](https://wofsauge.github.io/IsaacDocs/rep/enums/ItemPoolType.html) GetPoolIdByName ( string PoolName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

返回给定自定义池的 ID。如果未找到该池，则返回 `-1`。

___

### GetRenderPosition () {: aria-label='Functions' }

#### [Vector](Vector.md) GetRenderPosition ( [Vector](Vector.md) Position, boolean Scale = true ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetString () {: aria-label='Functions' }

#### string GetString ( string Category, string Key ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

返回给定类别中与给定键关联的翻译字符串。翻译以当前选定的语言提供。

___

### GetWindowTitle () {: aria-label='Functions' }

#### string GetWindowTitle ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

返回游戏窗口标题上附加的文本。

___

### IsChallengeDone () {: aria-label='Functions' }

#### boolean IsChallengeDone ( int challengeid ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

如果相应 challengeid 的挑战已完成，则返回 `true`。

___

### IsInGame () {: aria-label='Functions' }

#### boolean IsInGame ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

如果 `Game` 不为 nil 且当前状态正确，则返回 `true`。

___

### LevelGeneratorEntry () {: aria-label='Functions' }

#### [LevelGeneratorEntry](LevelGeneratorEntry.md) LevelGeneratorEntry ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

创建一个新的空白 [LevelGeneratorEntry](LevelGeneratorEntry.md) 对象。

___

### MarkChallengeAsNotDone () {: aria-label='Functions' }

#### void MarkChallengeAsNotDone ( int challengeid ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

将挑战标记为未完成。

___

### PlayCutscene () {: aria-label='Functions' }

#### int PlayCutscene ( int ID, boolean ClearGameState = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

播放提供的 ID 对应的过场动画。使用 Isaac.GetCutsceneIdByName 来获取 ID，或者如果您愿意，也可以使用原版的枚举。

___

### RenderCollectionItem () {: aria-label='Functions' }
#### void RenderCollectionItem ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) Collectible, [Vector](Vector.md) Position, [Vector](Vector.md) Scale = Vector.One, [Color](Color.md) Color = Color.Default ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Renders item collection sprite from collection menu/death screen. 
___

### ReworkBirthright () {: aria-label='Functions' }
#### void ReworkBirthright ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) playerType ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Marks the player's birthright as reworked, making the game not execute the item's original passive logic.
Can only be set during mod load.

___

### ReworkCollectible () {: aria-label='Functions' }
#### void ReworkCollectible ( [CollectibleType](https://wofsauge.github.io/IsaacDocs/rep/enums/CollectibleType.html) collectible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Marks the collectible as reworked, making the game not execute the item's original passive logic.
Can only be set during mod load.
**NOTE** Does not prevent the UseActiveItem logic from running.

___

### ReworkTrinket () {: aria-label='Functions' }
#### void ReworkTrinket ( [TrinketType](https://wofsauge.github.io/IsaacDocs/rep/enums/TrinketType.html) trinket ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Marks the trinket as reworked, making the game not execute the trinket's original passive logic.
Can only be set during mod load.

___

### SetClipboard () {: aria-label='Functions' }

#### boolean SetClipboard ( string ClipboardData ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

将剪贴板的内容设置为提供的字符串。

___

### SetCompletionMark () {: aria-label='Functions' }

#### void SetCompletionMark ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [CompletionType](enums/CompletionType.md) Mark, int Value) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

将角色的完成标记设置为匹配从 `0` 到 `2` 的特定值（0 = 未完成，1 = 普通，2 = 困难）。

___

### SetCompletionMarks () {: aria-label='Functions' }

#### void SetCompletionMarks ( table Marks ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

将角色的完成标记设置为匹配输入表。需要一个包含该角色所有标记的表，为了方便起见，建议从 [GetCompletionMarks](Isaac.md#getcompletionmarks) 获取该表。

???- info "Table structure & usage"

    该表具有以下字段:

    - PlayerType: containing the [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) asociated to the marks

    - Delirium: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - MegaSatan: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Mother: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - UltraGreed: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - BlueBaby: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - UltraGreedier: 困难贪婪模式,值2 ，大多冗余，无需设置
    - BossRush: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Beast: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Isaac: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Lamb: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - MomsHeart: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Hush: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况
    - Satan: [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) 值为 0 - 2，表示完成情况

    ```lua
    local marks = Isaac.GetCompletionMarks(0) --getting the current table
    marks.MomsHeart = 2 --Isaac now will have the hard mark on MHeart
    marks.Satan = 1 --Isaac will now have the normal mark on Satan
    marks.BlueBaby = 0 --Removes the BlueBaby Mark if its present
    Isaac.SetCompletionMarks(marks) --Impacts the changes on the player
    ```

___

### SetCurrentFloorBackdrop () {: aria-label='Functions' }

#### void SetCurrentFloorBackdrop ( int BackdropId ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

将当前楼层的默认房间背景更改为匹配输入的 ID。此更改在保存/继续游戏时不会保留，因此请确保考虑到这一点。

___

### SetCurrentFloorMusic () {: aria-label='Functions' }

#### void SetCurrentFloorMusic ( int MusicId ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

将当前楼层的音乐曲目更改为匹配输入的 ID。此更改在保存/继续游戏时不会保留，因此请确保考虑到这一点。

___

### SetCurrentFloorName () {: aria-label='Functions' }

#### void SetCurrentFloorName ( string Name ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

将当前楼层的显示名称更改为匹配输入的 ID。此更改在保存/继续游戏时不会保留，因此请确保考虑到这一点。

### SetDwmWindowAttribute () {: aria-label='Functions' }

#### void SetDwmWindowAttribute ( [DwmWindowAttribute](enums/DwmWindowAttribute.md) Attribute ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetIcon () {: aria-label='Functions' }

#### void SetIcon ( int IsaacIcon OR string IconPath, boolean BypassSize) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

设置游戏窗口上的 16x16 图标。不会更新其他地方的图标，例如任务栏。
`IsaacIcon` 为 `0` 表示正常图标，`1` 表示受污染图标。
`IconPath` 接受一个 .ico 文件的路径。
`BypassSize` 绕过 16x16 分辨率限制。

___

### SetWindowTitle () {: aria-label='Functions' }

#### void SetWindowTitle ( string Title ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

设置游戏窗口标题上附加的文本。

___

### ShowErrorDialog () {: aria-label='Functions' }

#### [DialogReturn](enums/DialogReturn.md) ShowErrorDialog ( string Title, string Text, [DialogIcons](enums/DialogIcons.md) Icon = DialogIcons.ERROR, [DialogButtons](enums/DialogButtons.md) Buttons = DialogButtons.OK ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

显示一个 Win32 消息框。可以使用 `icon` 和 `buttons` 参数进行控制。返回一个 [`DialogReturn`](enums/DialogReturn.md) 值，表示按下的按钮。

???- info "Note"

    请记住，游戏手柄对此弹出窗口不起作用，您需要使用鼠标/键盘或触摸屏，并且在某些环境（如 Steam Deck）中窗口标题可能不会显示，因此不要过于依赖它。

___

### SpawnBoss () {: aria-label='Functions' }
#### [EntityNPC](EntityNPC.md) SpawnBoss ( int Type, int Variant, int SubType, [Vector](Vector.md) Position, [Vector](Vector.md) Velocity, [Entity](Entity.md) Spawner, int Seed = ? ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Spawns an NPC forcing it to be a Boss, returning true for IsBoss(), giving it a boss bar, playing the boss end single on kill in appropiate rooms and other qualities that you may expect from a boss entity, even if the entity is normally not a Boss.

___

### StartNewGame () {: aria-label='Functions' }

#### void StartNewGame ( [PlayerType](https://wofsauge.github.io/IsaacDocs/rep/enums/PlayerType.html) Character, [Challenge](https://wofsauge.github.io/IsaacDocs/rep/enums/Challenge.html) Challenge = ChallengeType.CHALLENGE_NULL, [Difficulty](https://wofsauge.github.io/IsaacDocs/rep/enums/Difficulty.html) Mode = Difficulty.DIFFICULTY_NORMAL, int Seed = Random ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

使用指定的参数开始新游戏。可以从主菜单使用。

___

### TriggerWindowResize () {: aria-label='Functions' }

#### void TriggerWindowResize ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

模拟窗口大小调整，对于刷新一些选项更改（如 `MaxRenderScale`）很有用。

___

### UnClearChallenge () {: aria-label='Functions' }
#### void UnClearChallenge ( int challengeid) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets the challenge of the corresponding `challengeid` to not completed. While it does work with vanilla challenges, it is not recommended to use it on those, as there are no instances of challenges being uncompleted in vanilla, so it could lead to unexpected behaviour in specific scenarios. 

___

### WorldToMenuPosition () {: aria-label='Functions' }

#### [Vector](Vector.md) WorldToMenuPosition ( [MainMenu](enums/MainMenuType.md) MenuId, [Vector](Vector.md) Position ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

将输入的世界位置转换为固定的主菜单位置，该位置根据所选的枚举而变化。重要的是要像 WorldToRender 一样，每一帧都重新转换此位置，以便在菜单更改或窗口大小调整时正确渲染。

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留其上游来源。

### RenderToWorld () {: aria-label='Functions' }
#### [Vector](Vector.md) RenderToWorld ( [Vector](Vector.md) Pos ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Transfers Render coordinates into World coordinates.

Unlike [Isaac.ScreenToWorld](https://wofsauge.github.io/IsaacDocs/rep/Isaac.html#screentoworld) (which transfers Window coordinates into World coordinates), this is the true inverse of [Isaac.WorldToScreen](https://wofsauge.github.io/IsaacDocs/rep/Isaac.html#worldtoscreen) (which transfers World coordinates into Render coordinates).

???- info "Screen coordinate systems"
	The game uses 2 distinct coordinate systems when interacting with the Screen:

	- "Window" coordinates: the actual pixel position within the game window (OS-level).
	- "Render" coordinates: an abstract coordinate system independent of window size or scaling.

	Almost all functions that are used to interact with the screen use or return a position in **Render** coordinates.
	The only 2 exceptions are:

	- `Isaac.ScreenToWorld`: which converts **Window** coordinates into World coordinates.
	- `Input.GetMousePosition(false)`: which returns the mouse position in **Window** coordinates.

???- info "Pixel snapping behavior"
	Alongside converting the World coordinates into Render coordinates, `Isaac.WorldToScreen` snaps the render coordinates to the closest pixel perfect position.
	This means that converting Render coordinates into World coordinates, then back into Render coordinates is not guaranteed to return the original result; unless
	it is in a pixel perfect position.

___

### LoadModDataFromFolder () {: aria-label='Functions' }
#### void LoadModDataFromFolder ( string FolderName ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable aria-label='Functions' }
Similar to [LoadModData](https://wofsauge.github.io/IsaacDocs/rep/Isaac.html#loadmoddata), but lets you read the saveX.dat file from any existing mod data folder, even if that mod is not currently enabled.

___

</div>
