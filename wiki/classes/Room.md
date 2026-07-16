---
title: Room
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 117
---

# Room

## Summary

表示游戏中的当前房间，提供对房间内实体、网格、门、寻路、碰撞、状态等的全面访问，支持修改和查询房间内容。

## Related Types

- [[Color]]
- [[Entity]]
- [[EntityList]]
- [[EntityRef]]
- [[GridEntity]]
- [[GridEntityDoor]]
- [[GridEntityPoop]]
- [[Vector]]

## Key Methods

- [[#GetGridEntity|GetGridEntity]]
- [[#GetEntities|GetEntities]]
- [[#CheckLine|CheckLine]]
- [[#DestroyGrid|DestroyGrid]]
- [[#FindFreePickupSpawnPosition|FindFreePickupSpawnPosition]]

## Methods

### Functions

### CheckLine {#CheckLine}

```
(boolean, Vector) CheckLine ( Vector Pos1, Vector Pos2, LinecheckMode Mode, int GridPathThreshold = 0, boolean IgnoreWalls = false, boolean IgnoreCrushable = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

在两个位置之间执行射线检测，返回是否有障碍物以及第一个命中点。

返回2个值:

**Use Cases:**

- 判断敌人是否能看到玩家
- 计算抛射物是否会击中障碍物
- 检测存在视线连通性

**See also:** 
[[#GetGridCollision|GetGridCollision]], [[#GetGridCollisionAtPos|GetGridCollisionAtPos]]


---

### DamageGrid {#DamageGrid}

```
boolean DamageGrid ( int Index, int Damage )
```

*DLC: REP, REP+ | Modifiers: const*

对指定索引的网格实体（如便便、火焰）造成伤害。

对Grid Entity造成伤害,目前涉及 [GridEntityPoop](GridEntityPoop.md) 和 GridEntity_Fire。如果找到可受伤的实体(并可能造成伤害)则返回true,否则返回false。被眼泪、炸弹、某些NPC等使用。

**Use Cases:**

- 模拟炸弹或眼泪对网格实体的伤害
- 脚本化移除便便或火堆

**See also:** 
[[#DestroyGrid|DestroyGrid]]


---

### DamageGridWithSource {#DamageGridWithSource}

```
boolean DamageGridWithSource ( int Index, int Damage, EntityRef Source )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

带伤害来源地对网格实体造成伤害，可应用实体来源的效果。

___

**Use Cases:**

- 实现由特定玩家或敌人触发的网格破坏
- 统一伤害来源以触发相关成就或道具效果

**See also:** 
[[#DamageGrid|DamageGrid]]


---

### DestroyGrid {#DestroyGrid}

```
boolean DestroyGrid ( int Index, boolean Immediate )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

摧毁指定索引的网格实体，可移除岩石、打开隐藏门等。

内部调用DamageGrid来对Poop/Fire造成伤害,移除岩石并打开隐藏门。

**Use Cases:**

- 脚本移除挡路岩石
- 触发打开隐藏房间门的效果

**See also:** 
[[#DamageGrid|DamageGrid]]


---

### DestroyGridWithSource {#DestroyGridWithSource}

```
boolean DestroyGridWithSource ( int Index, boolean Immediate, EntityRef Source )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

带来源地摧毁网格实体，允许指定伤害来源。

___

**Use Cases:**

- 记录谁摧毁了网格实体
- 与DamageGridWithSource配合使用

**See also:** 
[[#DestroyGrid|DestroyGrid]]


---

### EmitBloodFromWalls {#EmitBloodFromWalls}

```
void EmitBloodFromWalls ( int Duration, int Count )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

从墙壁发射血液效果，常用于恐怖主题房间。

**Use Cases:**

- 创建血腥氛围的视觉效果

**See also:** 



---

### FindFreePickupSpawnPosition {#FindFreePickupSpawnPosition}

```
Vector FindFreePickupSpawnPosition ( Vector Pos, float InitialStep = 0, boolean AvoidActiveEntities = false, boolean AllowPits = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

在给定坐标附近寻找不会与其他拾取物或固体网格重叠的生成位置。

从 `Pos` 开始,尝试找到一个自由的生成位置,使新生成的拾取物不会与已生成的拾取物或固体Grid元素(如岩石或陷阱)碰撞。返回的位置将对齐到网格。如果找不到自由位置,则返回原始位置(对齐到网格)。

**Use Cases:**

- 生成多个拾取物而不堆叠
- 确保战利品可以正常捡起

**See also:** 
[[#FindFreeTilePosition|FindFreeTilePosition]]


---

### FindFreeTilePosition {#FindFreeTilePosition}

```
Vector FindFreeTilePosition ( Vector Pos, float DistanceThreshold )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

在指定位置附近寻找最近的自由格子，受距离阈值限制。

基于位置查找最近的自由格子。如果采样的格子的平方距离小于 `DistanceThresholdSQ`,则立即停止。

**Use Cases:**

- 快速获得可用的空网格位置
- 避免在障碍物上生成实体

**See also:** 
[[#FindFreePickupSpawnPosition|FindFreePickupSpawnPosition]]


---

### GetAliveBossesCount {#GetAliveBossesCount}

```
int GetAliveBossesCount ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前房间内存活的首领（Boss）数量。

**Use Cases:**

- 判断首领战是否结束
- 控制门开启条件

**See also:** 
[[#GetAliveEnemiesCount|GetAliveEnemiesCount]]


---

### GetAliveEnemiesCount {#GetAliveEnemiesCount}

```
int GetAliveEnemiesCount ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前房间内存活的普通敌人数量。

**Use Cases:**

- 确定房间是否被清理
- 触发清理奖励或开门

**See also:** 
[[#GetAliveBossesCount|GetAliveBossesCount]]


---

### GetAwardSeed {#GetAwardSeed}

```
int GetAwardSeed ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回用于生成房间奖励的随机种子值。

**Use Cases:**

- 预测或修改掉落物
- 调试战利品生成

**See also:** 



---

### GetBackdropType {#GetBackdropType}

```
BackdropType GetBackdropType ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取当前房间的背景类型。

返回当前房间的BackdropType。

**Use Cases:**

- 检测房间是否属于特定场景，如熔岩层或地下室

**See also:** 



---

### GetBossID {#GetBossID}

```
int GetBossID ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回房间中第一个首领的Boss ID（非实体类型）。

返回房间中第一个首领的boss ID。否则返回0。

**Use Cases:**

- 识别首领种类以触发特殊逻辑
- 显示Boss血条或图标

**See also:** 
[[#GetAliveBossesCount|GetAliveBossesCount]]


---

### GetBottomRightPos {#GetBottomRightPos}

```
Vector GetBottomRightPos ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回房间内部右下角的坐标（墙内）。

返回房间右下角的位置,在墙边界内部。

**Use Cases:**

- 计算房间边界
- 限制实体移动范围

**See also:** 
[[#GetCenterPos|GetCenterPos]], [[#GetClampedPosition|GetClampedPosition]]


---

### GetBrokenWatchState {#GetBrokenWatchState}

```
int GetBrokenWatchState ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取房间的时间流速状态：正常、减速或加速。

返回房间是否被减速、加速或均无。

**Use Cases:**

- 处理损坏怀表效果
- 调整自定义敌人或弹幕速度

**See also:** 



---

### GetCenterPos {#GetCenterPos}

```
Vector GetCenterPos ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回房间的中心位置坐标。

返回房间中心位置。

**Use Cases:**

- 用于生成特效或实体于房间中心
- 计算相对位置

**See also:** 
[[#GetBottomRightPos|GetBottomRightPos]]


---

### GetClampedGridIndex {#GetClampedGridIndex}

```
int GetClampedGridIndex ( Vector Position )
```

*DLC: AB+, REP, REP+*

将世界坐标转换为网格索引，若坐标超出房间则钳位到最近有效索引。

返回位于 `Position` 的网格索引。如果 `Position` 超出边界,则锁定到最近的网格索引。

**Use Cases:**

- 安全地将任意位置映射到网格操作

**See also:** 
[[#GetGridIndex|GetGridIndex]]


---

### GetClampedPosition {#GetClampedPosition}

```
Vector GetClampedPosition ( Vector Pos, float Margin )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将给定位置钳位到房间墙壁内部，并留有指定边距。

返回被锁定在房间墙壁内的 `Pos`,距离边界有 `Margin` 单位的半径。

**Use Cases:**

- 防止实体移出房间
- 保证生成点位于可见区域内

**See also:** 
[[#GetBottomRightPos|GetBottomRightPos]]


---

### GetDecorationSeed {#GetDecorationSeed}

```
int GetDecorationSeed ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回用于生成房间装饰（如蛛网、血迹）的种子值。

**Use Cases:**

- 保持房间装饰的一致性
- 调试装饰布局

**See also:** 
[[#GetAwardSeed|GetAwardSeed]]


---

### GetDeliriumDistance {#GetDeliriumDistance}

```
int GetDeliriumDistance ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取与百变怪（Delirium）相关的距离值。

**Use Cases:**

- 判断百变怪行为或进度

**See also:** 



---

### GetDevilRoomChance {#GetDevilRoomChance}

```
float GetDevilRoomChance ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前层的恶魔房/天使房总概率值（可超过100%）。

**Use Cases:**

- 计算实际恶魔/天使房出现几率
- 制作概率显示插件

**See also:** 
[[#GetBrokenWatchState|GetBrokenWatchState]]


---

### GetDoor {#GetDoor}

```
GridEntityDoor GetDoor ( DoorSlot Slot ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取指定门槽位置的网格实体门对象。

返回给定 [DoorSlot](enums/DoorSlot.md) 位置的 [GridEntityDoor](GridEntityDoor.md)。如果没有门在那里则返回 `nil`。

**Use Cases:**

- 打开、关闭或修改门
- 检测门的状态

**See also:** 
[[#GetDoorSlotPosition|GetDoorSlotPosition]]


---

### GetDoorSlotPosition {#GetDoorSlotPosition}

```
Vector GetDoorSlotPosition ( DoorSlot Slot )
```

*DLC: AB+, REP, REP+*

返回指定门槽的世界坐标位置。

**Use Cases:**

- 在门附近生成效果或实体

**See also:** 
[[#GetDoor|GetDoor]]


---

### GetDungeonRockIdx {#GetDungeonRockIdx}

```
int GetDungeonRockIdx ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前房间的地牢岩石风格索引。

**Use Cases:**

- 确定房间岩石外观用于纹理替换

**See also:** 
[[#GetGridEntity|GetGridEntity]]


---

### GetEnemyDamageInflicted {#GetEnemyDamageInflicted}

```
float GetEnemyDamageInflicted ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回当前帧内房间中所有敌人受到的总伤害量。

返回当前帧内房间中所有敌人损失的总HP数量。

**Use Cases:**

- 实现需要充能的道具（如狂怒！）
- 计算玩家伤害输出统计

**See also:** 
[[#GetAliveEnemiesCount|GetAliveEnemiesCount]]


---

### GetEntities {#GetEntities}

```
EntityList GetEntities ( )
```

*DLC: AB+, REP | Modifiers: const*

获取指向当前房间所有实体的原始数组，迭代时反映当前逻辑帧状态。

返回一个指向存储当前房间中所有实体的数组的原始指针。因此,迭代返回值将始终迭代当前逻辑帧期间房间中存在的实体,而不管GetEntities最初何时被调用。

**Use Cases:**

- 遍历房间所有实体进行自定义操作
- 注意：多数情况下推荐使用Isaac.GetRoomEntities

**See also:** 
[[#GetAliveEnemiesCount|GetAliveEnemiesCount]], [[#GetAliveBossesCount|GetAliveBossesCount]]


---

### GetFrameCount {#GetFrameCount}

```
int GetFrameCount ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回房间进入后经过的帧数。

返回房间活跃的帧数。当玩家离开房间或退出运行时重置为 `0`。

**Use Cases:**

- 计时房间内事件
- 实现随时间变化的敌人模式

**See also:** 



---

### GetGridCollision {#GetGridCollision}

```
GridCollisionClass GetGridCollision ( int GridIndex )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取指定网格索引位置的碰撞等级。

**Use Cases:**

- 检查该位置是否为不可通过
- 用于寻路或生成安全检测

**See also:** 
[[#GetGridEntity|GetGridEntity]]


---

### GetGridCollisionAtPos {#GetGridCollisionAtPos}

```
GridCollisionClass GetGridCollisionAtPos ( Vector Pos )
```

*DLC: REP, REP+ | Modifiers: const*

根据世界坐标获取该位置的网格碰撞等级。

返回房间中此位置处的Grid Entity的 [GridCollisionClass](enums/GridCollisionClass.md)。

**Use Cases:**

- 简化基于坐标的碰撞查询

**See also:** 
[[#GetGridCollision|GetGridCollision]]


---

### GetGridEntity {#GetGridEntity}

```
GridEntity GetGridEntity ( int Index ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

根据网格索引获取网格实体（岩石、便便、火等）。

返回此网格索引处的 [GridEntity](GridEntity.md)。如果找不到 [GridEntity](GridEntity.md) 则返回 `nil`。

**Use Cases:**

- 读取或修改特定格子的实体
- 获取实体类型以决定行为

**See also:** 
[[#GetGridEntityFromPos|GetGridEntityFromPos]]


---

### GetGridEntityFromPos {#GetGridEntityFromPos}

```
GridEntity GetGridEntityFromPos ( Vector Position ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

根据世界坐标获取网格实体。

返回房间中此位置处的 [GridEntity](GridEntity.md)。如果找不到 [GridEntity](GridEntity.md) 则返回 `nil`。

**Use Cases:**

- 方便地从位置直接获取网格实体

**See also:** 
[[#GetGridEntity|GetGridEntity]]


---

### GetGridHeight {#GetGridHeight}

```
int GetGridHeight ( )
```

*DLC: AB+, REP, REP+*

返回房间网格的垂直格子数量。

**Use Cases:**

- 计算房间尺寸
- 遍历所有网格单元

**See also:** 
[[#GetGridWidth|GetGridWidth]], [[#GetGridSize|GetGridSize]]


---

### GetGridIndex {#GetGridIndex}

```
int GetGridIndex ( Vector Position )
```

*DLC: AB+, REP, REP+*

将世界坐标转换为网格索引，无效坐标返回-1。

返回位于 `Position` 的网格索引。对于无效索引返回 `-1`。

**Use Cases:**

- 确定特定坐标对应的网格编号
- 与GetGridPosition配合使用

**See also:** 
[[#GetClampedGridIndex|GetClampedGridIndex]]


---

### GetGridPath {#GetGridPath}

```
int GetGridPath ( int Index )
```

*DLC: AB+, REP, REP+*

获取指定网格索引的寻路开销值，值越高越不可通过。

Grid path是网格方块的一个属性,表示穿过该网格单元的“成本”。它用于寻路算法,该算法搜索到给定位置的最低成本路径。如果网格单元的值大于0,它可以阻止Grid Entity在该方块上生成。因此,您可以通过将Grid path重置为0来绕过它,然后生成Grid Entity。

**Use Cases:**

- 控制寻路算法
- 检查格子是否被障碍物阻塞

**See also:** 
[[#GetGridPathFromPos|GetGridPathFromPos]]


---

### GetGridPathFromPos {#GetGridPathFromPos}

```
int GetGridPathFromPos ( Vector Position )
```

*DLC: AB+, REP, REP+*

根据世界坐标获取格子的寻路成本。

**Use Cases:**

- 快速查询坐标处寻路障碍
- 敌人移动逻辑

**See also:** 
[[#GetGridPath|GetGridPath]]


---

### GetGridPosition {#GetGridPosition}

```
Vector GetGridPosition ( int GridIndex )
```

*DLC: AB+, REP, REP+*

将网格索引转换为世界坐标位置。

返回 `GridIndex` 的世界位置,即使 `GridIndex` 是无效的。

**Use Cases:**

- 在特定网格位置生成实体或效果
- 与GetGridIndex互逆操作

**See also:** 
[[#GetGridIndex|GetGridIndex]]


---

### GetGridSize {#GetGridSize}

```
int GetGridSize ( )
```

*DLC: AB+, REP, REP+*

返回房间网格单元格的总数。

**Use Cases:**

- 获取房间总格子数用于遍历

**See also:** 
[[#GetGridWidth|GetGridWidth]], [[#GetGridHeight|GetGridHeight]]


---

### GetGridWidth {#GetGridWidth}

```
int GetGridWidth ( )
```

*DLC: AB+, REP, REP+*

返回房间网格的横向格子数量。

**Use Cases:**

- 计算网格边界和坐标转换

**See also:** 
[[#GetGridHeight|GetGridHeight]]


---

### GetLaserTarget {#GetLaserTarget}

```
Vector GetLaserTarget ( Vector Pos, Vector Dir )
```

*DLC: AB+, REP, REP+*

计算激光（如科技、机器宝宝）的最终命中点，遇到大便、火、岩石等障碍物即停止。

返回激光束(科技、机器宝宝)的命中位置。通常这是直线上遇到的第一个大便、火、岩石、TNT或墙壁。

**Use Cases:**

- 模拟激光的终点
- 获取激光实际作用位置

**See also:** 
[[#CheckLine|CheckLine]]


---

### GetLavaIntensity {#GetLavaIntensity}

```
float GetLavaIntensity ( )
```

*DLC: AB+, REP, REP+*

获取熔岩的当前强度，受冷却效果影响逐渐降低。

通常返回1,除非熔岩正在被“冲水！”或其他房间洪水效果冷却,在这种情况下它将逐渐减少到0。

**Use Cases:**

- 检测熔岩是否处于伤害状态
- 实现与水互动相关的机制

**See also:** 



---

### GetLightingAlpha {#GetLightingAlpha}

```
float GetLightingAlpha ( )
```

*DLC: AB+, REP, REP+*

返回房间光照透明度值，用于控制光照叠加效果。

**Use Cases:**

- 自定义光照强度
- 判断房间暗度

**See also:** 
[[#GetRenderMode|GetRenderMode]]


---

### GetLRoomAreaDesc {#GetLRoomAreaDesc}

```
LRoomAreaDesc GetLRoomAreaDesc ( )
```

*DLC: AB+, REP, REP+*

返回房间区域描述数据（LRoomAreaDesc），包含区域类型和边界等。

**Use Cases:**

- 高级房间布局分析
- 自定义区域渲染

**See also:** 
[[#GetLRoomTileDesc|GetLRoomTileDesc]]


---

### GetLRoomTileDesc {#GetLRoomTileDesc}

```
LRoomTileDesc GetLRoomTileDesc ( )
```

*DLC: AB+, REP, REP+*

返回房间瓦片描述数据（LRoomTileDesc），用于获取地面瓦片纹理和属性。

**Use Cases:**

- 自定义地面纹理绘制
- 瓦片状态检查

**See also:** 
[[#GetLRoomAreaDesc|GetLRoomAreaDesc]]


---

### GetRandomPosition {#GetRandomPosition}

```
Vector GetRandomPosition ( float Margin )
```

*DLC: AB+, REP, REP+*

在房间内生成一个随机坐标，避开障碍物，可指定安全边距。

返回房间中的一个随机位置,距离任何障碍物有 `Margin` 单位的半径。此位置不与网格对齐。

**Use Cases:**

- 随机生成敌人或物品
- 随机传送目标点

**See also:** 
[[#FindFreePickupSpawnPosition|FindFreePickupSpawnPosition]], [[#FindFreeTilePosition|FindFreeTilePosition]]


---

### GetRandomTileIndex {#GetRandomTileIndex}

```
int GetRandomTileIndex ( int Seed )
```

*DLC: AB+, REP, REP+*

根据种子生成随机网格瓦片索引，用于确定性随机选择瓦片。

**Use Cases:**

- 随机替换或生成瓦片
- 与种子绑定的地形变化

**See also:** 
[[#GetGridIndex|GetGridIndex]]


---

### GetRedHeartDamage {#GetRedHeartDamage}

```
boolean GetRedHeartDamage ( )
```

*DLC: AB+, REP, REP+*

检测玩家在当前房间是否受到非自伤的红心伤害，离开房间后重置。

如果玩家在房间中对红心容器受到非自我造成的伤害,则返回 `true`。如果玩家离开房间或退出运行,则重置为 `false`。

**Use Cases:**

- 成就或事件触发条件
- 恶魔房生成概率计算

**See also:** 
[[#GetEnemyDamageInflicted|GetEnemyDamageInflicted]]


---

### GetRenderMode {#GetRenderMode}

```
RenderMode GetRenderMode ( )
```

*DLC: REP, REP+*

返回当前渲染模式枚举，如水面反射或普通，用于调整自定义绘制。

返回RenderMode枚举,可用于根据上下文以不同方式渲染实体(例如自定义水面反射)。

**Use Cases:**

- 实现水面反射效果
- 根据渲染模式切换纹理

**See also:** 
[[#GetRenderScrollOffset|GetRenderScrollOffset]]


---

### GetRenderScrollOffset {#GetRenderScrollOffset}

```
const Vector GetRenderScrollOffset ( )
```

*DLC: REP, REP+ | Modifiers: const*

返回摄像机滚动偏移和屏幕抖动偏移的合成向量，用于计算正确的屏幕坐标。

摄像机滚动偏移和屏幕抖动偏移都在这里表示。

**Use Cases:**

- 将世界坐标转换为屏幕坐标
- 特效跟随屏幕抖动

**See also:** 
[[#GetRenderSurfaceTopLeft|GetRenderSurfaceTopLeft]]


---

### GetRenderSurfaceTopLeft {#GetRenderSurfaceTopLeft}

```
const Vector GetRenderSurfaceTopLeft ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回地板和墙壁纹理渲染的左上角世界坐标。

地板和墙壁纹理将被渲染的位置。

**Use Cases:**

- 对齐自定义地面装饰
- 绘制房间背景参考点

**See also:** 
[[#GetTopLeftPos|GetTopLeftPos]]


---

### GetRoomConfigStage {#GetRoomConfigStage}

```
int GetRoomConfigStage ( )
```

*DLC: AB+, REP, REP+*

返回当前房间设计对应的关卡阶段ID（如地下室、洞窟等）。

返回该房间设计所适用的关卡ID。

**Use Cases:**

- 判断房间所属楼层
- 替换房间布局时参考

**See also:** 
[[#GetType|GetType]]


---

### GetRoomShape {#GetRoomShape}

```
RoomShape GetRoomShape ( )
```

*DLC: AB+, REP, REP+*

返回房间形状枚举，如狭长、L形、普通等。

**Use Cases:**

- 调整AI寻路策略
- 判断房间结构

**See also:** 
[[#IsLShapedRoom|IsLShapedRoom]]


---

### GetSecondBossID {#GetSecondBossID}

```
int GetSecondBossID ( )
```

*DLC: AB+, REP, REP+*

返回“坏事成双”房间中第二个Boss的ID，没有则返回0。

返回坏事成双房间中第二个boss的boss ID。否则返回0。

**Use Cases:**

- 双Boss战斗特殊UI
- 识别次要Boss

**See also:** 
[[#GetBossID|GetBossID]]


---

### GetSeededCollectible {#GetSeededCollectible}

```
CollectibleType GetSeededCollectible ( int Seed, bool NoDecrease = false )
```

*DLC: AB+, REP, REP+*

根据种子从道具池中抽取道具，可选择不从池中移除，用于预览或试算。

当 `NoDecrease` 为true时,返回的道具将不会从它们来自的道具池中移除。

**Use Cases:**

- 宝箱预览机制
- 模拟道具生成

**See also:** 
[[#GetAwardSeed|GetAwardSeed]]


---

### GetShopLevel {#GetShopLevel}

```
int GetShopLevel ( )
```

*DLC: AB+, REP, REP+*

返回房间的商店等级，影响商品品质和数量。

**Use Cases:**

- 商店UI显示等级
- 修改商店生成规则

**See also:** 
[[#GetType|GetType]]


---

### GetSpawnSeed {#GetSpawnSeed}

```
int GetSpawnSeed ( )
```

*DLC: AB+, REP, REP+*

返回房间的生成种子，用于确定性随机生成各种实体。

**Use Cases:**

- 保证生成的一致性
- 与道具、敌人联动

**See also:** 
[[#GetAwardSeed|GetAwardSeed]], [[#GetDecorationSeed|GetDecorationSeed]]


---

### GetTintedRockIdx {#GetTintedRockIdx}

```
int GetTintedRockIdx ( )
```

*DLC: AB+, REP, REP+*

返回房间中染色岩石的网格索引，常用于寻找隐藏房间入口的标记。

**Use Cases:**

- 自动标记染色岩石
- 隐藏房间探测提示

**See also:** 
[[#GetDungeonRockIdx|GetDungeonRockIdx]]


---

### GetTopLeftPos {#GetTopLeftPos}

```
Vector GetTopLeftPos ( )
```

*DLC: AB+, REP, REP+*

返回房间可行走区域边界内的左上角世界坐标。

返回墙壁内部的左上角位置。

**Use Cases:**

- 计算房间可用面积
- 生成位置上限

**See also:** 
[[#GetBottomRightPos|GetBottomRightPos]]


---

### GetType {#GetType}

```
RoomType GetType ( )
```

*DLC: AB+, REP, REP+*

返回房间类型枚举，如普通、宝箱、Boss、商店等。

**Use Cases:**

- 识别房间功能
- 决定特殊行为

**See also:** 
[[#GetRoomShape|GetRoomShape]]


---

### GetWaterCurrent {#GetWaterCurrent}

```
Vector GetWaterCurrent ( )
```

*DLC: REP, REP+*

返回房间内水流的方向和强度向量，用于推动实体。

返回与房间中任何水流对应的向量。

**Use Cases:**

- 模拟水流冲击效果
- 调整玩家移动轨迹

**See also:** 
[[#HasWater|HasWater]]


---

### HasCurseMist {#HasCurseMist}

```
boolean HasCurseMist ( )
```

*DLC: REP, REP+*

判断玩家是否处于废弃矿井的诅咒迷雾环境中。

如果玩家在废弃矿井内,则返回 `true`。

**Use Cases:**

- 视觉特效开关
- 探测废矿层特殊机制

**See also:** 
[[#IsMirrorWorld|IsMirrorWorld]]


---

### HasLava {#HasLava}

```
boolean HasLava ( )
```

*DLC: REP, REP+*

检测房间中是否包含熔岩网格。

如果房间包含熔岩,则返回 `true`。

**Use Cases:**

- 伤害判定或AI避让
- 环境效果提示

**See also:** 
[[#HasWaterPits|HasWaterPits]]


---

### HasSlowDown {#HasSlowDown}

```
boolean HasSlowDown ( )
```

*DLC: AB+, REP, REP+*

检测房间是否因损坏怀表或药丸效果而处于减速状态。

**Use Cases:**

- 界面提示减速状态
- 调整游戏节奏

**See also:** 
[[#GetBrokenWatchState|GetBrokenWatchState]]


---

### HasTriggerPressurePlates {#HasTriggerPressurePlates}

```
boolean HasTriggerPressurePlates ( )
```

*DLC: AB+, REP, REP+*

返回房间中是否存在压力板（触发机关）。

如果房间中有一个或多个压力板,则返回 `true`。

**Use Cases:**

- 解谜元素检测
- 触发陷阱机制

**See also:** 
[[#IsAmbushActive|IsAmbushActive]]


---

### HasWater {#HasWater}

```
boolean HasWater ( )
```

*DLC: AB+, REP, REP+*

检测房间中是否有水（不包括熔岩等特殊液体）。

**Use Cases:**

- 溺水机制触发
- 游泳效果判断

**See also:** 
[[#HasWaterPits|HasWaterPits]]


---

### HasWaterPits {#HasWaterPits}

```
boolean HasWaterPits ( )
```

*DLC: AB+, REP, REP+*

检测房间中是否包含液体陷坑（如沥青、熔岩等）。

如果房间包含有液体的陷阱(例如矿洞中的熔岩、阴湿深牢中的沥青等),则返回 `true`。

**Use Cases:**

- 危险环境识别
- 自定义伤害源

**See also:** 
[[#HasLava|HasLava]]


---

### InvalidatePickupVision {#InvalidatePickupVision}

```
void InvalidatePickupVision ( )
```

*DLC: REP, REP+*

使嗝屁猫的眼睛提供的宝箱预览在下一帧强制更新。

让来自嗝屁猫的眼睛的宝箱预览在下一帧更新。

**Use Cases:**

- 刷新宝箱预览效果
- 与特定道具联动

**See also:** 



---

### IsAmbushActive {#IsAmbushActive}

```
boolean IsAmbushActive ( )
```

*DLC: AB+, REP, REP+*

判断房间的伏击事件是否处于激活状态。

**Use Cases:**

- 控制敌人波次生成
- 锁门条件判断

**See also:** 
[[#IsAmbushDone|IsAmbushDone]]


---

### IsAmbushDone {#IsAmbushDone}

```
boolean IsAmbushDone ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

判断伏击事件是否已经完全结束。

**Use Cases:**

- 触发开门或奖励
- 结束战斗事件

**See also:** 
[[#IsClear|IsClear]]


---

### IsClear {#IsClear}

```
boolean IsClear ( )
```

*DLC: AB+, REP, REP+*

返回房间是否已清空（没有敌人或特殊事件未完成）。

**Use Cases:**

- 决定是否可以开门
- 成就检测

**See also:** 
[[#GetAliveEnemiesCount|GetAliveEnemiesCount]]


---

### IsCurrentRoomLastBoss {#IsCurrentRoomLastBoss}

```
boolean IsCurrentRoomLastBoss ( )
```

*DLC: AB+, REP, REP+*

判断当前房间是否是XL楼层中的第二个Boss房。

如果当前房间是XL楼层上的第二个头目房,则返回 `true`。否则返回 `false`。

**Use Cases:**

- XL楼层特殊处理
- Boss房音乐切换

**See also:** 
[[#GetRoomConfigStage|GetRoomConfigStage]]


---

### IsDoorSlotAllowed {#IsDoorSlotAllowed}

```
boolean IsDoorSlotAllowed ( DoorSlot Slot )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检查指定的门槽位置在当前房间定义中是否允许存在门。

返回提供的门槽对于当前房间是否有效。这取决于STB/XML文件中的房间定义。(Basement Renovator将有效的门显示为棕色,将无效的门显示为白色。)此方法返回的值与给定槽位是否存在门无关。

**Use Cases:**

- 自定义房间门生成
- 验证门操作合法性

**See also:** 
[[#GetDoor|GetDoor]]


---

### IsFirstEnemyDead {#IsFirstEnemyDead}

```
boolean IsFirstEnemyDead ( )
```

*DLC: AB+, REP, REP+*

判断当前房间中第一个生成的敌人是否已死亡。

**Use Cases:**

- 触发特殊奖励或事件
- 战斗阶段划分

**See also:** 
[[#GetAliveEnemiesCount|GetAliveEnemiesCount]]


---

### IsFirstVisit {#IsFirstVisit}

```
boolean IsFirstVisit ( )
```

*DLC: AB+, REP, REP+*

检测玩家是否首次进入此房间（本局游戏内）。

**Use Cases:**

- 首次进入特殊掉落
- 触发剧情对话

**See also:** 
[[#GetFrameCount|GetFrameCount]]


---

### IsInitialized {#IsInitialized}

```
boolean IsInitialized ( )
```

*DLC: AB+, REP, REP+*

判断房间是否已完成初始化并可以安全交互。

**Use Cases:**

- 确保获取信息时房间就绪
- 延迟初始化逻辑

**See also:** 



---

### IsLShapedRoom {#IsLShapedRoom}

```
boolean IsLShapedRoom ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

判断当前房间是否是L形房间。

**Use Cases:**

- 调整摄像机边界
- 生成位置计算

**See also:** 
[[#GetRoomShape|GetRoomShape]]


---

### IsMirrorWorld {#IsMirrorWorld}

```
boolean IsMirrorWorld ( )
```

*DLC: REP, REP+ | Modifiers: const*

检测玩家是否处于镜子维度（下到镜子层）中。

如果玩家在镜子维度内,则返回true。

**Use Cases:**

- 镜子层特殊逻辑
- 实体行为切换

**See also:** 
[[#HasCurseMist|HasCurseMist]]


---

### IsPositionInRoom {#IsPositionInRoom}

```
boolean IsPositionInRoom ( Vector Pos, float Margin )
```

*DLC: AB+, REP, REP+*

判断给定世界坐标（带安全边距）是否位于房间可行走边界内。

如果给定的位置在房间内,则返回 `true`。`Margin` 用作位置周围的半径,该半径也需要在房间边界内。房间边界是可行走区域和墙壁之间的位置。因此,墙壁内和黑色虚空中的位置确实被计为房间“外部”。

**Use Cases:**

- 防止实体出界
- 验证生成位置

**See also:** 
[[#GetClampedPosition|GetClampedPosition]]


---

### IsSacrificeDone {#IsSacrificeDone}

```
boolean IsSacrificeDone ( )
```

*DLC: AB+, REP, REP+*

判断献祭房的献祭进度是否已完成。

**Use Cases:**

- 控制献祭奖励弹出
- 检查献祭状态

**See also:** 
[[#IsClear|IsClear]]


---

### KeepDoorsClosed {#KeepDoorsClosed}

```
void KeepDoorsClosed ( )
```

*DLC: AB+, REP, REP+*

强制关闭所有门并保持关闭状态，直到达到某项条件。

**Use Cases:**

- Boss战锁门
- 剧情事件封锁

**See also:** 
[[#IsAmbushActive|IsAmbushActive]]


---

### MamaMegaExplosion {#MamaMegaExplosion}

```
void MamaMegaExplosion ( Vector Position )
```

*DLC: AB+, REP, REP+*

在指定位置触发妈妈炸弹的巨型爆炸效果，可能破坏房间内网格和实体。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 自定义大范围破坏效果
- 模拟炸弹道具

**See also:** 
[[#DestroyGrid|DestroyGrid]]


---

### void MamaMegaExplosion ( [Vector](Vector.md) Position = Vector.Zero, [EntityPlayer](EntityPlayer.md) Player = nil ) {#void MamaMegaExplosion ( [Vector](Vector.md) Position = Vector.Zero, [EntityPlayer](EntityPlayer.md) Player = nil )}

```
void PlayMusic ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

播放此房间使用的默认音乐曲目。可用于在播放不同曲目后重置音乐。

播放此房间使用的音乐曲目。在播放不同的曲目后用于重置音乐。

**Use Cases:**

- 切换音乐后恢复房间默认背景音乐

**See also:** 
[[#PlayMusic|PlayMusic]]


---

### RemoveDoor {#RemoveDoor}

```
void RemoveDoor ( DoorSlot Slot )
```

*DLC: AB+, REP, REP+*

移除指定门槽处的门。

**Use Cases:**

- 在事件中临时封锁或开放某些出口

**See also:** 



---

### RemoveGridEntity {#RemoveGridEntity}

```
void RemoveGridEntity ( int GridIndex, int PathTrail, boolean KeepDecoration )
```

*DLC: AB+, REP, REP+*

移除指定网格索引处的网格实体，并可控制是否保留装饰和路径痕迹。

**Use Cases:**

- 动态清除障碍物以改变房间布局

**See also:** 



---

### Render {#Render}

```
void Render ( )
```

*DLC: AB+, REP, REP+*

手动触发房间的渲染更新。

**Use Cases:**

- 在自定义修改后强制重绘房间

**See also:** 



---

### RespawnEnemies {#RespawnEnemies}

```
void RespawnEnemies ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

重新生成房间内的所有敌人，效果类似七面骰道具。

用于七面骰道具。

**Use Cases:**

- 重置房间敌人配置

**See also:** 



---

### ScreenWrapPosition {#ScreenWrapPosition}

```
Vector ScreenWrapPosition ( Vector Pos, float Margin )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

对坐标进行屏幕边缘包裹处理：如果位置正好在房间右边界外，则移动到左边界，实现无限循环效果。

返回屏幕包裹后的 `Pos` (如果它刚好在房间右侧外面,它将被移动到房间的左侧,依此类推)

**Use Cases:**

- 用于需要穿过墙壁无缝移动的特效

**See also:** 



---

### SetAmbushDone {#SetAmbushDone}

```
void SetAmbushDone ( boolean Value )
```

*DLC: AB+, REP, REP+*

设置伏击是否已经完成的状态标志。

**Use Cases:**

- 控制房间内伏击事件的触发逻辑

**See also:** 



---

### SetBrokenWatchState {#SetBrokenWatchState}

```
void SetBrokenWatchState ( int State )
```

*DLC: AB+, REP, REP+*

设置房间的时间流速状态：加速、减速或正常（参见 GetBrokenWatchState 的值）。

加速、减速或从当前房间移除这些状态中的任何一个。有关 `State` 的不同值,请参见 [GetBrokenWatchState](#getbrokenwatchstate) 中的说明部分。

**Use Cases:**

- 实现自定义道具或诅咒对房间时间的影响

**See also:** 



---

### SetCardAgainstHumanity {#SetCardAgainstHumanity}

```
void SetCardAgainstHumanity ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

触发'反人类卡牌'效果，使房间铺满便便。

**Use Cases:**

- 模拟卡牌效果

**See also:** 



---

### SetClear {#SetClear}

```
void SetClear ( boolean Clear )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置房间的清理标志（如天使房用来控制敌人是否已清空）。

用于天使房，以便当天使生成时可以将房间清理标志设置为false。

**Use Cases:**

- 在天使房等场景中重置清理状态以防止奖励提前触发

**See also:** 



---

### SetFirstEnemyDead {#SetFirstEnemyDead}

```
void SetFirstEnemyDead ( boolean Value )
```

*DLC: AB+, REP, REP+*

设置是否是第一个敌人死亡的状态。

**Use Cases:**

- 控制与首杀相关的特殊逻辑

**See also:** 



---

### SetFloorColor {#SetFloorColor}

```
void SetFloorColor ( Color FloorColor )
```

*DLC: AB+, REP, REP+*

对当前房间的地板纹理应用一个颜色修改器。

允许您对当前房间的地板纹理应用颜色修改器。

**Use Cases:**

- 自定义房间氛围，如诅咒或祝福效果

**See also:** 



---

### SetGridPath {#SetGridPath}

```
boolean SetGridPath ( int Index, int Value )
```

*DLC: AB+, REP, REP+*

设置指定网格索引的寻路成本值（GridPath），可用来允许或阻止实体生成。

Grid path是网格方块的一个属性,表示穿过该网格单元的“成本”。它用于寻路算法,该算法搜索到给定位置的最低成本路径。如果网格单元的值大于 `0`,它可以阻止Grid Entity在该方块上生成。因此,您可以通过将Grid path重置为0来绕过它,然后生成Grid Entity。

**Use Cases:**

- 清空寻路值以便在其他区域生成网格实体
- 动态调整敌人寻路优先级

**See also:** 



---

### SetRedHeartDamage {#SetRedHeartDamage}

```
void SetRedHeartDamage ( )
```

*DLC: AB+, REP, REP+*

将房间内尚未结算的红心伤害标记为生效。

**Use Cases:**

- 处理自定义红心伤害结算

**See also:** 



---

### SetSacrificeDone {#SetSacrificeDone}

```
void SetSacrificeDone ( boolean Done )
```

*DLC: AB+, REP, REP+*

设置当前房间的献祭是否已完成。

**Use Cases:**

- 控制房间献祭事件的触发

**See also:** 



---

### SetSlowDown {#SetSlowDown}

```
void SetSlowDown ( int Duration )
```

*DLC: AB+, REP, REP+*

对房间应用减速效果，持续指定逻辑帧数（每秒30帧）。

对 `Duration` 个逻辑帧应用减速效果(每秒30个逻辑帧)。

**Use Cases:**

- 实现破损怀表或特定药丸的效果

**See also:** 



---

### SetWallColor {#SetWallColor}

```
void SetWallColor ( Color WallColor )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

对当前房间的墙壁纹理应用一个颜色修改器。

允许您对当前房间的墙壁纹理应用颜色修改器。

**Use Cases:**

- 改变房间墙壁外观以配合主题或状态

**See also:** 



---

### ShopReshuffle {#ShopReshuffle}

```
void ShopReshuffle ( boolean KeepCollectibleIdx, boolean ReselectSaleItem )
```

*DLC: AB+, REP, REP+*

重新随机商店物品，并可选择是否保留收藏品索引和重新选择打折物品。

**Use Cases:**

- 模拟补货效果或自定义商店刷新

**See also:** 



---

### ShopRestockFull {#ShopRestockFull}

```
void ShopRestockFull ( )
```

*DLC: AB+, REP, REP+*

完全补货商店库存并重新随机物品，类似使用补货机。

像使用补货机一样，补充商店库存并重新随机物品。

**Use Cases:**

- 恢复已售罄的商店

**See also:** 



---

### ShopRestockPartial {#ShopRestockPartial}

```
void ShopRestockPartial ( )
```

*DLC: AB+, REP, REP+*

部分补货商店库存（仅补充已售出的道具）。

**Use Cases:**

- 精细控制商店刷新

**See also:** 



---

### SpawnClearAward {#SpawnClearAward}

```
void SpawnClearAward ( )
```

*DLC: AB+, REP, REP+*

触发生成清理房间后的奖励（如道具或掉落物）。

**Use Cases:**

- 手动发放房间奖励

**See also:** 



---

### SpawnGridEntity {#SpawnGridEntity}

```
boolean SpawnGridEntity ( int GridIndex, GridEntityType Type, int Variant, int Seed, int VarData )
```

*DLC: AB+, REP, REP+*

在指定网格索引生成一个指定类型的网格实体。

**Use Cases:**

- 动态放置岩石、尖刺、火堆等障碍物

**See also:** 



---

### StopRain {#StopRain}

```
void StopRain ( )
```

*DLC: REP, REP+*

停止房间中所有的雨效果。

停止房间中的任何雨效果。

**Use Cases:**

- 在清理房间或改变天气时移除雨

**See also:** 



---

### TriggerClear {#TriggerClear}

```
void TriggerClear ( boolean Silent = false )
```

*DLC: REP, REP+*

触发所有房间清理效果（如打开门、生成奖励），但并不实际将房间标记为已清理。

触发所有房间清除效果(并不实际清除房间)。

**Use Cases:**

- 模拟清理房间但不改变游戏状态

**See also:** 



---

### TryMakeBridge {#TryMakeBridge}

```
boolean TryMakeBridge ( GridEntity pit, GridEntity rock )
```

*DLC: AB+, REP, REP+*

尝试在给定的沟壑上创建一座桥。返回是否成功。

尝试在给定的沟壑上创建一座桥。如果创建成功则返回 `true`。否则返回 `false`。

**Use Cases:**

- 允许玩家或实体跨过沟壑

**See also:** 



---

### TryPlaceLadder {#TryPlaceLadder}

```
void TryPlaceLadder ( Vector PlayerPos, Vector PlayerVelocity, Entity Ladder )
```

*DLC: AB+*

此方法在忏悔版本中被移除，原本用于尝试放置梯子。

此函数在忏悔中被移除。

**Use Cases:**

- 不可用

**See also:** 



---

### TrySpawnBlueWombDoor {#TrySpawnBlueWombDoor}

```
boolean TrySpawnBlueWombDoor ( boolean FirstTime = true, boolean IgnoreTime = false, boolean Force = false )
```

*DLC: AB+, REP, REP+*

尝试生成通往蓝子宫的门。可通过参数控制是否忽略时间限制或强制生成。

尝试生成一扇通往蓝子宫的门。

**Use Cases:**

- 手动打开蓝子宫入口

**See also:** 



---

### TrySpawnBossRushDoor {#TrySpawnBossRushDoor}

```
boolean TrySpawnBossRushDoor ( boolean IgnoreTime = false, boolean Force = false )
```

*DLC: AB+, REP, REP+*

尝试生成通往头目车轮战的门。可忽略时间限制或强制生成。

尝试生成一扇通往头目车轮战的门。

**Use Cases:**

- 在自定义条件下开启Boss Rush

**See also:** 



---

### TrySpawnDevilRoomDoor {#TrySpawnDevilRoomDoor}

```
boolean TrySpawnDevilRoomDoor ( boolean Animate = false, boolean Force = false )
```

*DLC: AB+, REP, REP+*

尝试生成通往恶魔房或天使房的门。可播放动画或强制生成。

尝试生成一扇通往恶魔房或天使房的门。

**Use Cases:**

- 模拟恶魔房开启

**See also:** 



---

### TrySpawnMegaSatanRoomDoor {#TrySpawnMegaSatanRoomDoor}

```
boolean TrySpawnMegaSatanRoomDoor ( boolean Force = false )
```

*DLC: AB+, REP, REP+*

尝试生成通往超级撒但房间的门。可强制生成。

尝试生成一扇通往超级撒但的门。

**Use Cases:**

- 自定义场景下开启超级撒但战

**See also:** 



---

### TrySpawnSecretExit {#TrySpawnSecretExit}

```
boolean TrySpawnSecretExit ( boolean Animate = false, boolean Force = false )
```

*DLC: REP, REP+*

根据当前楼层尝试生成通往下水道、矿洞或陵墓的秘密出口。可播放动画或强制生成。

根据当前楼层，尝试生成一扇通往下水道、矿洞或陵墓的门。

**Use Cases:**

- 在合适楼层手动开启隐藏出口

**See also:** 



---

### TrySpawnSecretShop {#TrySpawnSecretShop}

```
boolean TrySpawnSecretShop ( boolean Force = false )
```

*DLC: REP, REP+*

尝试在当前房间内生成一个通往会员商店的活板门。可强制生成。

尝试在当前房间内生成一个通往会员商店的活板门。

**Use Cases:**

- 模拟会员商店入口

**See also:** 



---

### TrySpawnSpecialQuestDoor {#TrySpawnSpecialQuestDoor}

```
boolean TrySpawnSpecialQuestDoor ( )
```

*DLC: REP, REP+*

尝试生成通往下水道镜子维度或矿洞废弃矿井的特殊任务门。

尝试生成一扇通往下水道中的镜子维度的门，或矿洞中的废弃矿井。

**Use Cases:**

- 开启特定区域入口

**See also:** 



---

### TrySpawnTheVoidDoor {#TrySpawnTheVoidDoor}

```
boolean TrySpawnTheVoidDoor ( boolean Force = false )
```

*DLC: AB+, REP, REP+*

尝试生成通往包含虚空传送门的房间的入口。可强制生成。

尝试生成一扇通往包含虚空传送门的房间的门。

**Use Cases:**

- 打开通往虚空的路径

**See also:** 



---

### TurnGold {#TurnGold}

```
void TurnGold ( )
```

*DLC: AB+, REP, REP+*

对房间内所有网格实体应用金色色调，类似击败困难究极贪婪后的效果。

对房间中的所有Grid Entity应用金色色调。这与游戏在击败困难究极贪婪后所做的效果相同。

**Use Cases:**

- 实现自定义金牛座或黄金主题效果

**See also:** 



---

### Update {#Update}

```
void Update ( )
```

*DLC: AB+, REP, REP+*

执行房间的逻辑更新（通常每帧自动调用）。

更新当前房间。

**Use Cases:**

- 在手动控制游戏循环时调用

**See also:** 



---

### WorldToScreenPosition {#WorldToScreenPosition}

```
Vector WorldToScreenPosition ( Vector WorldPos )
```

*DLC: AB+, REP, REP+*

将世界坐标转换为屏幕坐标。

**Use Cases:**

- 界面元素定位

**See also:** 



---

## See Also

- [[Color]]
- [[Entity]]
- [[EntityList]]
- [[EntityRef]]
- [[GridEntity]]
- [[GridEntityDoor]]
- [[GridEntityPoop]]
- [[Room]]
- [[Vector]]
