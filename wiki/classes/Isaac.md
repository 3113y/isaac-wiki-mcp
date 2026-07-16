---
title: Isaac
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 56
---

# Isaac

## Summary

Isaac 是《以撒的结合》忏悔版本提供的全局静态类，用于访问游戏核心功能，包括回调管理、实体查询、资源 ID 查找、时间与屏幕信息、生成事件、以及 MOD 存档数据检查等。所有方法通过点号调用，无需实例化。

## Related Types

- [[Entity]]
- [[EntityPlayer]]
- [[Game]]
- [[GridEntity]]
- [[ItemConfig]]
- [[Room]]
- [[Vector]]

## Key Methods

- [[#AddCallback|AddCallback]]
- [[#GetPlayer|GetPlayer]]
- [[#GetRoomEntities|GetRoomEntities]]
- [[#GetItemIdByName|GetItemIdByName]]
- [[#ExecuteCommand|ExecuteCommand]]

## Methods

### Functions

### AddCallback {#AddCallback}

```
void AddCallback ( table modRef, ModCallback|string callbackId, table callbackFn, int entityId )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

注册一个 MOD 回调函数，使其在特定游戏事件（由 callbackId 指定）发生时被调用。可限制仅在某个实体上触发。建议优先使用 ModReference 的等效方法。

添加一个MOD回调。

**Use Cases:**

- 监听玩家受伤事件并修改伤害
- 在生成新敌人时替换或增强该敌人
- 在房间变更时执行自定义逻辑

**See also:** 
[[#AddPriorityCallback|AddPriorityCallback]], [[#GetCallbacks|GetCallbacks]], [[#GetBuiltInCallbackState|GetBuiltInCallbackState]]


---

### AddPillEffectToPool {#AddPillEffectToPool}

```
PillColor AddPillEffectToPool ( PillEffect pillEffect )
```

*DLC: REP, REP+ | Modifiers: const*

将指定的胶囊效果添加到游戏胶囊池中，并返回该效果对应的胶囊颜色枚举值。用于 MOD 引入新胶囊时注册其效果。

将一个胶囊效果pillEffect加入到胶囊池中。

**Use Cases:**

- 注册自定义胶囊效果使其能在游戏中出现
- 初始化时将所有 MOD 胶囊效果一次性加入池子

**See also:** 
[[#GetPillEffectByName|GetPillEffectByName]]


---

### AddPriorityCallback {#AddPriorityCallback}

```
void AddPriorityCallback ( table modRef, ModCallback|string callbackId, CallbackPriority priority, table callbackFn, int entityId )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

注册一个具有优先级的 MOD 回调，控制多个同事件回调的执行顺序。优先级由 CallbackPriority 枚举指定。同样推荐使用 ModReference 对应方法。

添加一个MOD回调。该回调具有优先级，并根据优先级决定执行顺序。

**Use Cases:**

- 确保某些逻辑在其他 MOD 之前/之后执行
- 解决不同 MOD 在同一事件的冲突

**See also:** 
[[#AddCallback|AddCallback]], [[#GetCallbacks|GetCallbacks]]


---

### ConsoleOutput {#ConsoleOutput}

```
void ConsoleOutput ( string text )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

向游戏内控制台输出一行纯文本信息，效果等同于 print() 语句，常用于测试或调试显示。

**Use Cases:**

- 在开发时打印变量值以快速验证
- 向玩家展示 MOD 调试信息

**See also:** 
[[#DebugString|DebugString]]


---

### CountBosses {#CountBosses}

```
int CountBosses ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前房间内存在的头目（Boss）数量，可用于判断房间是否仍处于 BOSS 战状态。

**Use Cases:**

- 检查 BOSS 是否被击败以推进关卡
- 控制特殊道具或事件的触发条件

**See also:** 
[[#CountEnemies|CountEnemies]], [[#CountEntities|CountEntities]], [[#GetRoomEntities|GetRoomEntities]]


---

### CountEnemies {#CountEnemies}

```
int CountEnemies ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回当前房间内敌人的数量，可用于检查房间是否清空或判断战斗阶段。

**Use Cases:**

- 实现清空房间后打开特殊房门
- 根据敌人数目动态调整难度或奖励

**See also:** 
[[#CountBosses|CountBosses]], [[#CountEntities|CountEntities]], [[#GetRoomEntities|GetRoomEntities]]


---

### CountEntities {#CountEntities}

```
int CountEntities ( Entity Spawner, EntityType Type = EntityType.ENTITY_NULL, int Variant = -1, int SubType = -1 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

按生成者实体、类型、变体、子类型精确统计当前房间中符合条件的实体数量，支持忽略生成者和类型。

**Use Cases:**

- 检测某个生成者是否已产下特定子怪
- 统计房间内特定变体的敌人数量以触发机制

**See also:** 
[[#FindByType|FindByType]], [[#CountEnemies|CountEnemies]]


---

### DebugString {#DebugString}

```
void DebugString ( string str )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

向游戏日志文件（log.txt）写入一行调试信息，前缀为 [INFO] - Lua Debug:。适合长期记录或离线分析。

**Use Cases:**

- 记录难以即时观察的变量变化
- 排查崩溃前的游戏状态

**See also:** 
[[#ConsoleOutput|ConsoleOutput]]


---

### ExecuteCommand {#ExecuteCommand}

```
string ExecuteCommand ( string command )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

以字符串形式执行一条控制台指令，并返回指令的输出结果。可用于模拟玩家输入指令。

**Use Cases:**

- 代码方式给予玩家道具或效果
- 自动化测试中重置房间状态

**See also:** 
[[#ConsoleOutput|ConsoleOutput]]


---

### Explode {#Explode}

```
void Explode ( Vector pos, Entity source, float damage )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

在指定世界坐标位置产生一次爆炸，伤害源为给定实体，造成固定数值的伤害。可用于创建自定义爆炸效果。

**Use Cases:**

- 实现自爆饰品或主动道具
- 生成环境爆炸以打开秘密房间

**See also:** 
[[#GetFreeNearPosition|GetFreeNearPosition]], [[#GetRandomPosition|GetRandomPosition]]


---

### FindByType {#FindByType}

```
table FindByType ( EntityType Type, int Variant = -1, int SubType = -1, boolean Cache = false, boolean IgnoreFriendly = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前房间内所有符合指定类型、变体和子类型的实体列表，可包含任意变体/子类型，并支持缓存以优化连续查询。忽略带有 FLAG_NO_QUERY 标志的实体。

返回符合Type，Variant和SubType的所有实体。如果Variant/SubType为-1，表示包括任意Variant/SubType的实体。Cache为true时会缓存结果，一帧执行多次时可以使用。

**Use Cases:**

- 查找所有特定类型的敌人并施加效果
- 一键获取房间中所有掉落物以进行回收

**See also:** 
[[#FindInRadius|FindInRadius]], [[#GetRoomEntities|GetRoomEntities]], [[#CountEntities|CountEntities]]


---

### FindInRadius {#FindInRadius}

```
Entity[] FindInRadius ( Vector Position, float Radius, EntityPartition Partitions = 0xFFFFFFFF )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回以指定位置为中心、半径范围内的所有实体，可按实体分区筛选。结果按加载顺序而非距离排序。

返回中心为Position，半径为Radius范围内的所有由Partitions筛选的实体（包括所有 = 0xffffffff）

**Use Cases:**

- 实现范围溅射效果
- 制作磁力或排斥范围内的物品

**See also:** 
[[#FindByType|FindByType]], [[#GetRoomEntities|GetRoomEntities]]


---

### GetBuiltInCallbackState {#GetBuiltInCallbackState}

```
boolean GetBuiltInCallbackState ( function callbackId )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

查询游戏内置的某个回调是否仍在执行（未被禁用）。若回调 ID 不存在则返回 false。

获取内置回调状态。

**Use Cases:**

- 判断是否需要自己接管内置回调逻辑
- 调试时查看特定游戏系统是否被其他 MOD 关闭

**See also:** 
[[#AddCallback|AddCallback]], [[#GetCallbacks|GetCallbacks]]


---

### GetCallbacks {#GetCallbacks}

```
table GetCallbacks ( function callbackId, boolean createIfMissing )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取指定回调 ID 对应的所有 MOD 回调函数列表。若 createIfMissing 为 true 且列表不存在，会自动创建空表并附带参数匹配元表。

获取所有ID为`callbackId`的MOD回调。这些回调会表示为一个表，更多信息请查阅[自定义回调教程](tutorials/CustomCallbacks.md#run-behavior)。

**Use Cases:**

- 手动触发自定义回调链
- 读取已注册的回调数量以做保护

**See also:** 
[[#AddCallback|AddCallback]]


---

### GetCardIdByName {#GetCardIdByName}

```
Card GetCardIdByName ( string cardHudName )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

通过口袋物品 XML 文件中的 'hud' 属性值查找卡牌 ID，仅适用于 MOD 卡牌，原版卡牌需直接用枚举。

基于“pocketitems.xml”文件中定义的“hud”属性返回[卡牌ID](enums/Card.md) 。如果找不到具有该“hud”属性值的卡，则返回`-1`。

**Use Cases:**

- 初始化时获取所有自定义卡牌的 ID 以建立映射
- 根据 HUD 字符串动态决定卡牌效果

**See also:** 
[[#GetItemIdByName|GetItemIdByName]]


---

### GetChallenge {#GetChallenge}

```
Challenge GetChallenge ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前游戏正在进行挑战的 ID（如挑战 32 是愚人节）。未进行挑战时返回 0。

返回玩家当前正在进行的挑战的ID。如果玩家没有进行任何挑战，则返回0。

**Use Cases:**

- 根据当前挑战调整物品生成规则
- 在挑战中禁用某些 MOD 功能

**See also:** 
[[#GetChallengeIdByName|GetChallengeIdByName]]


---

### GetChallengeIdByName {#GetChallengeIdByName}

```
Challenge GetChallengeIdByName ( string challengeName )
```

*DLC: AB+, REP, REP+*

根据 challenges.xml 中的挑战名称（区分大小写）返回挑战 ID，找不到则返回 -1。

**Use Cases:**

- 通过配置文件读取挑战名并自动识别
- 创建通用挑战检测系统

**See also:** 
[[#GetChallenge|GetChallenge]]


---

### GetCostumeIdByPath {#GetCostumeIdByPath}

```
int GetCostumeIdByPath ( string path )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

根据 costumes2.xml 中定义的外观文件路径返回外观 ID，用于动态添加或检查玩家外观。

**Use Cases:**

- 在 MOD 初始化时根据路径获取特定外观编号
- 根据当前扮演角色替换外观

**See also:** 
[[#GetPlayerTypeByName|GetPlayerTypeByName]]


---

### GetCurseIdByName {#GetCurseIdByName}

```
LevelCurse GetCurseIdByName ( string curseName )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

通过 curses.xml 中的诅咒名称查找诅咒 ID，用于检查或设置当前层诅咒。

**Use Cases:**

- 读取当前层诅咒并以名字显示
- 根据诅咒名动态调整 MOD 行为

**See also:** 
[[#AddCallback|AddCallback]]


---

### GetEntityTypeByName {#GetEntityTypeByName}

```
EntityType GetEntityTypeByName ( string entityName )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

根据 entities2.xml 中的实体名称返回对应的 EntityType 枚举值，找不到返回 0。可用于动态获取 MOD 实体的类型。

**Use Cases:**

- 根据配置文件中的怪物名生成对应实体
- 兼容旧版通过名字查询实体的功能

**See also:** 
[[#GetEntityVariantByName|GetEntityVariantByName]], [[#FindByType|FindByType]]


---

### GetEntityVariantByName {#GetEntityVariantByName}

```
int GetEntityVariantByName ( string entityName )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

根据实体的名称返回其 Variant（变体）值，找不到返回 -1。常与 GetEntityTypeByName 配合获取完整实体标识。

**Use Cases:**

- 根据名称生成指定变体的敌人
- 在数据表中通过名字映射实体类型和变体

**See also:** 
[[#GetEntityTypeByName|GetEntityTypeByName]]


---

### GetFrameCount {#GetFrameCount}

```
int GetFrameCount ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回游戏自启动以来经过的总帧数（即使暂停或主菜单仍会增加），约 60 帧/秒。与 Game():GetFrameCount() 不同，后者只计数运行中帧。

**Use Cases:**

- 计算现实时间流逝（配合帧率）
- 制作始终更新的全局计时器

**See also:** 
[[#GetTime|GetTime]]


---

### GetFreeNearPosition {#GetFreeNearPosition}

```
Vector GetFreeNearPosition ( Vector pos, float step )
```

*DLC: AB+, REP, REP+*

在指定位置附近以步长 step 寻找一个未被占用的空区域（世界坐标），返回该位置。常用于安全生成实体。

**Use Cases:**

- 在玩家附近生成掉落物避免穿墙
- 为 GridSpawn 寻找合法位置

**See also:** 
[[#GridSpawn|GridSpawn]], [[#GetRandomPosition|GetRandomPosition]]


---

### GetItemConfig {#GetItemConfig}

```
ItemConfig GetItemConfig ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取全局唯一的 ItemConfig 对象，用于读取所有道具、饰品、胶囊等的配置信息。是访问 ItemConfig 的唯一入口。

**Use Cases:**

- 读取道具的品质、图标路径等属性
- 动态修改道具效果参数

**See also:** 
[[#GetItemIdByName|GetItemIdByName]]


---

### GetItemIdByName {#GetItemIdByName}

```
CollectibleType GetItemIdByName ( string itemName )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

根据 items.xml 中定义的道具名称（区分大小写）查找 CollectibleType ID，MOD 道具必备。找不到返回 -1。

**Use Cases:**

- 初始化时获取所有自定义道具的 ID 到数组
- 根据字符串命令给予玩家特定道具

**See also:** 
[[#GetItemConfig|GetItemConfig]]


---

### GetMusicIdByName {#GetMusicIdByName}

```
Music GetMusicIdByName ( string musicName )
```

*DLC: AB+, REP | Modifiers: const*

根据 music.xml 中的音乐名称返回对应的 Music 枚举 ID，找不到返回 -1。用于控制背景音乐或音轨。

**Use Cases:**

- 替换当前层背景音乐为自定义曲目
- 播放特定音乐作为事件标志

**See also:** 
[[#GetSoundIdByName|GetSoundIdByName]]


---

### GetPillEffectByName {#GetPillEffectByName}

```
PillEffect GetPillEffectByName ( string pillEffect )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

通过 pocketitems.xml 中的胶囊效果名称获取 PillEffect 枚举 ID，找不到返回 -1。常用于 MOD 胶囊效果识别。

**Use Cases:**

- 初始化时映射自定义胶囊效果名称到 ID
- 根据字符串动态触发特定胶囊效果

**See also:** 
[[#AddPillEffectToPool|AddPillEffectToPool]]


---

### GetPlayer {#GetPlayer}

```
EntityPlayer GetPlayer ( int playerID = 0 ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: const*

根据玩家索引（从 0 开始）获取对应的 EntityPlayer 实体。若玩家未初始化（如主菜单）则返回 nil。等同于 Game():GetPlayer()。

**Use Cases:**

- 获取当前控制的玩家实体施加状态
- 遍历所有玩家（如雅各和以扫）以同步效果

**See also:** 
[[#GetRoomEntities|GetRoomEntities]]


---

### GetPlayerTypeByName {#GetPlayerTypeByName}

```
PlayerType GetPlayerTypeByName ( string playerName , boolean Tainted = false )
```

*DLC: REP, REP+ | Modifiers: const*

通过 players.xml 中角色的名称获取 PlayerType ID。忏悔中需使用翻译占位符（如 #CAIN_NAME）。更适合 MOD 角色，原版角色建议直接用枚举。

**Use Cases:**

- 通过名字判断当前角色的类型
- 初始化 MOD 角色映射

**See also:** 
[[#GetPlayer|GetPlayer]]


---

### GetRandomPosition {#GetRandomPosition}

```
Vector GetRandomPosition ( )
```

*DLC: AB+, REP, REP+*

返回当前房间内的一个随机世界坐标位置，不保证是否被占用。常用于随机刷怪或爆物。

**Use Cases:**

- 随机刷新掉落物或敌人
- 在房间内随机位置播放特效

**See also:** 
[[#GetFreeNearPosition|GetFreeNearPosition]], [[#Explode|Explode]]


---

### GetRoomEntities {#GetRoomEntities}

```
Entity[] GetRoomEntities ( )
```

*DLC: AB+, REP, REP+*

返回当前房间内所有实体的快照表（遍历安全），与 Room:GetEntities() 的原始指针不同，推荐使用此方法。

**Use Cases:**

- 遍历所有实体以查找特定 NPC
- 实现全房间 AOE 效果

**See also:** 
[[#FindByType|FindByType]], [[#CountEnemies|CountEnemies]]


---

### GetScreenHeight {#GetScreenHeight}

```
float GetScreenHeight ( )
```

*DLC: AB+, REP, REP+*

返回游戏渲染屏幕的高度值（像素）。可用于 UI 元素定位或分辨率相关计算。

**Use Cases:**

- 将自定义 HUD 元素放置在屏幕合适位置
- 根据屏幕比例调整绘制内容

**See also:** 
[[#GetScreenWidth|GetScreenWidth]], [[#GetScreenPointScale|GetScreenPointScale]]


---

### GetScreenPointScale {#GetScreenPointScale}

```
float GetScreenPointScale ( )
```

*DLC: AB+, REP, REP+*

返回当前屏幕的缩放系数（1.0 或 2.0），取决于游戏窗口分辨率。用于精确像素绘制和布局。

**Use Cases:**

- 调整 UI 元素大小以适配不同缩放
- 计算屏幕逻辑坐标与实际像素的转换

**See also:** 
[[#GetScreenWidth|GetScreenWidth]], [[#GetScreenHeight|GetScreenHeight]]


---

### GetScreenWidth {#GetScreenWidth}

```
float GetScreenWidth ( )
```

*DLC: AB+, REP, REP+*

返回游戏渲染屏幕的宽度值（像素）。可与高度配合实现屏幕自适应。

**Use Cases:**

- 居中绘制文本或图形
- 制作全屏覆盖效果

**See also:** 
[[#GetScreenHeight|GetScreenHeight]], [[#GetScreenPointScale|GetScreenPointScale]]


---

### GetSoundIdByName {#GetSoundIdByName}

```
SoundEffect GetSoundIdByName ( string soundName )
```

*DLC: AB+, REP, REP+*

通过 sounds.xml 中的音效名称查找 SoundEffect ID，找不到返回 -1。用于播放指定音效。

**Use Cases:**

- 播放自定义音效或检查音效是否存在
- 根据字符串配置动态选择音效

**See also:** 
[[#GetMusicIdByName|GetMusicIdByName]]


---

### GetTextWidth {#GetTextWidth}

```
int GetTextWidth ( string str )
```

*DLC: AB+, REP, REP+*

使用与 RenderText 相同的字体（terminus8）计算指定字符串的像素宽度，辅助界面布局。

**Use Cases:**

- 提前计算文本宽度以实现右对齐
- 根据字符串长度动态调整 UI 框大小

**See also:** 



---

### GetTime {#GetTime}

```
int GetTime ( )
```

*DLC: AB+, REP, REP+*

返回自操作系统启动以来经过的毫秒数，不受游戏暂停或加载影响，适合测量真实时间间隔。

**Use Cases:**

- 制作基于真实时间的倒计时
- 衡量函数执行耗时

**See also:** 
[[#GetFrameCount|GetFrameCount]]


---

### GetTrinketIdByName {#GetTrinketIdByName}

```
TrinketType GetTrinketIdByName ( string trinketName )
```

*DLC: AB+, REP, REP+*

根据 items.xml 中饰品的名称返回 TrinketType ID，MOD 饰品必备。找不到返回 -1。

**Use Cases:**

- 初始化时获取所有自定义饰品的 ID
- 实现饰品检测功能

**See also:** 
[[#GetItemIdByName|GetItemIdByName]], [[#GetItemConfig|GetItemConfig]]


---

### GridSpawn {#GridSpawn}

```
GridEntity GridSpawn ( GridEntityType gridEntityType, int variant, Vector position, boolean forced )
```

*DLC: AB+, REP, REP+*

在指定世界坐标生成一个网格实体（如岩石、尖刺等）。强制参数可覆盖已存在的非实体网格，但有时不生效，建议配合 GetFreeNearPosition。

**Use Cases:**

- 动态生成障碍物改变地形
- 放置可破坏物或陷阱

**See also:** 
[[#GetFreeNearPosition|GetFreeNearPosition]]


---

### HasModData {#HasModData}

```
boolean HasModData ( table modRef )
```

*DLC: AB+, REP, REP+*

检查指定 MOD 是否通过 SaveModData 存储了存档数据，即存档文件夹中存在 saveX.dat 文件。

**Use Cases:**

- 判断 MOD 是否有需要加载的存档信息
- 在加载时决定是否初始化默认数据

**See also:** 



---

### LoadModData {#LoadModData}

```
string LoadModData ( table modRef )
```

*DLC: AB+, REP, REP+*

读取指定 Mod 的存档数据，返回字符串；若无数据则返回空字符串。

**Use Cases:**

- 加载玩家存档中的 Mod 数据
- 恢复自定义角色状态或世界改变

**See also:** 
[[#SaveModData|SaveModData]], [[#RemoveModData|RemoveModData]], [[#HasModData|HasModData]]


---

### RegisterMod {#RegisterMod}

```
void RegisterMod ( table modRef, string modName, int apiVersion )
```

*DLC: AB+, REP, REP+*

将 Mod 注册到游戏中，提供 Mod 名称和 API 版本，是 Mod 初始化的必要步骤。

**Use Cases:**

- 在 Mod 入口注册 Mod 实例
- 设置 API 版本以确保兼容性

**See also:** 
[[#AddCallback|AddCallback]], [[#GetItemConfig|GetItemConfig]]


---

### RemoveCallback {#RemoveCallback}

```
void RemoveCallback ( table modRef, ModCallback|string callbackId, table callbackFn )
```

*DLC: AB+, REP, REP+*

移除之前注册的指定回调函数，用于动态取消监听事件。

**Use Cases:**

- 停止对特定事件的响应
- 管理 Mod 生命周期中的回调绑定

**See also:** 
[[#AddCallback|AddCallback]], [[#RunCallback|RunCallback]], [[#GetCallbacks|GetCallbacks]]


---

### RemoveModData {#RemoveModData}

```
void RemoveModData ( table modRef )
```

*DLC: AB+, REP, REP+*

删除当前 Mod 的所有存档数据文件，常用于重置进度。

**Use Cases:**

- 清空 Mod 在某个存档槽位的数据
- 实现数据重置功能

**See also:** 
[[#LoadModData|LoadModData]], [[#SaveModData|SaveModData]], [[#HasModData|HasModData]]


---

### RenderScaledText {#RenderScaledText}

```
void RenderScaledText ( string str, float X, float Y, float ScaleX, float ScaleY, float R, float G, float B, float A )
```

*DLC: AB+, REP, REP+*

在屏幕上渲染带有缩放和颜色的文本，支持指定宽高缩放因子。

**Use Cases:**

- 绘制可伸缩的 HUD 元素
- 创建自定义菜单或提示

**See also:** 
[[#RenderText|RenderText]], [[#GetTextWidth|GetTextWidth]]


---

### RenderText {#RenderText}

```
void RenderText ( string str, float X, float Y, float R, float G, float B, float A )
```

*DLC: AB+, REP, REP+*

在屏幕指定位置以固定大小和颜色渲染文本。

**Use Cases:**

- 显示简单的调试信息
- 绘制不可缩放的标签

**See also:** 
[[#RenderScaledText|RenderScaledText]], [[#GetTextWidth|GetTextWidth]]


---

### RunCallback {#RunCallback}

```
void RunCallback ( ModCallback|string callbackId, ...)
```

*DLC: REP, REP+*

触发所有注册在指定 ID 下的回调，但不关心返回值。

**Use Cases:**

- 广播自定义事件通知其他 Mod
- 在特定游戏时刻触发扩展功能

**See also:** 
[[#RunCallbackWithParam|RunCallbackWithParam]], [[#AddCallback|AddCallback]], [[#GetCallbacks|GetCallbacks]]


---

### RunCallbackWithParam {#RunCallbackWithParam}

```
void RunCallbackWithParam ( ModCallback|string callbackId, object param, ...)
```

*DLC: REP, REP+ | Modifiers: const*

运行指定回调，遇到第一个有效的返回值即停止并返回该值；支持传递额外参数。

Runs all callbacks added under `callbackId`, breaking on the first return and returning that value.

**Use Cases:**

- 查询式回调（如是否启用某个功能）
- 实现有返回值的事件链

**See also:** 
[[#RunCallback|RunCallback]], [[#AddCallback|AddCallback]], [[#GetCallbacks|GetCallbacks]]


---

### SaveModData {#SaveModData}

```
void SaveModData ( table modRef, string data )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将字符串数据写入与 Mod 当前存档槽关联的 saveX.dat 文件。

**Use Cases:**

- 保存玩家进度或 Mod 状态
- 持久化自定义数据

**See also:** 
[[#LoadModData|LoadModData]], [[#RemoveModData|RemoveModData]], [[#HasModData|HasModData]]


---

### ScreenToWorld {#ScreenToWorld}

```
Vector ScreenToWorld ( Vector pos )
```

*DLC: AB+, REP, REP+*

将屏幕坐标转换为世界坐标，常用于基于鼠标位置进行实体交互。

**Use Cases:**

- 实现鼠标指向生成实体
- 将 UI 点击映射到游戏世界位置

**See also:** 
[[#WorldToScreen|WorldToScreen]], [[#ScreenToWorldDistance|ScreenToWorldDistance]]


---

### ScreenToWorldDistance {#ScreenToWorldDistance}

```
Vector ScreenToWorldDistance ( Vector pos )
```

*DLC: AB+, REP, REP+*

将屏幕距离（像素距离）转换为世界距离，保持方向不变。

___

**Use Cases:**

- 将 UI 拖拽距离转换为游戏内位移
- 适配不同分辨率下的操作手感

**See also:** 
[[#WorldToScreenDistance|WorldToScreenDistance]], [[#ScreenToWorld|ScreenToWorld]]


---

### SetBuiltInCallbackState {#SetBuiltInCallbackState}

```
void SetBuiltInCallbackState ( ModCallbacks callbackId, boolean state )
```

*DLC: AB+, REP, REP+*

启用或禁用内置回调的执行，游戏会自动管理，但 Mod 可强制覆盖。

Sets whether callbacks under `callbackId` will be ran by the game. The game uses this to activate a [ModCallbacks](enums/ModCallbacks.md) once a callback is added under one, or deactivate them when those callbacks have been removed.

**Use Cases:**

- 临时屏蔽某些内置事件以提高性能
- 调试时暂时关闭特定回调

**See also:** 
[[#GetBuiltInCallbackState|GetBuiltInCallbackState]], [[#AddCallback|AddCallback]]


---

### Spawn {#Spawn}

```
Entity Spawn ( EntityType entityType, int entityVariant, int entitySubtype, Vector position, Vector velocity, Entity Spawner )
```

*DLC: AB+, REP, REP+*

在指定世界位置生成一个实体，可设置类型、变体、子类型、速度和生成者。

**Use Cases:**

- 动态生成敌人、道具或效果
- 根据自定义条件创建实体

**See also:** 
[[#GridSpawn|GridSpawn]], [[#FindByType|FindByType]], [[#GetRoomEntities|GetRoomEntities]]


---

### WorldToRenderPosition {#WorldToRenderPosition}

```
Vector WorldToRenderPosition ( Vector pos )
```

*DLC: AB+, REP, REP+*

将世界坐标转换为渲染位置，用于将游戏内坐标映射到屏幕绘制层。

**Use Cases:**

- 在实体头顶绘制文本框
- 放置屏幕空间特效

**See also:** 
[[#WorldToScreen|WorldToScreen]], [[#ScreenToWorld|ScreenToWorld]]


---

### WorldToScreen {#WorldToScreen}

```
Vector WorldToScreen ( Vector pos )
```

*DLC: AB+, REP, REP+*

将世界坐标转换为屏幕坐标，便于在 UI 上表示游戏对象。

**Use Cases:**

- 制作小地图标记
- 显示角色状态栏指示器

**See also:** 
[[#ScreenToWorld|ScreenToWorld]], [[#WorldToScreenDistance|WorldToScreenDistance]]


---

### WorldToScreenDistance {#WorldToScreenDistance}

```
Vector WorldToScreenDistance ( Vector pos )
```

*DLC: AB+, REP, REP+*

将世界距离转换为屏幕距离，保持方向不变。

**Use Cases:**

- 根据实体间的世界距离绘制等比例的 UI 线段
- 调整特效大小以匹配屏幕缩放

**See also:** 
[[#ScreenToWorldDistance|ScreenToWorldDistance]], [[#WorldToScreen|WorldToScreen]]


---

## See Also

- [[Entity]]
- [[EntityPlayer]]
- [[Game]]
- [[GridEntity]]
- [[ItemConfig]]
- [[Room]]
- [[Vector]]
