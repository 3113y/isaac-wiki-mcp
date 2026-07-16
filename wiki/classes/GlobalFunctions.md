---
title: GlobalFunctions
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 17
---

# GlobalFunctions

## Summary

《以撒的结合》全局函数集，提供各种核心对象的构造函数、管理器获取以及实用工具函数，是 mod 开发的基础接口。

## Related Types

- [[BitSet128]]
- [[Color]]
- [[Entity]]
- [[EntityPtr]]
- [[EntityRef]]
- [[Font]]
- [[Game]]
- [[Isaac]]
- [[KColor]]
- [[MusicManager]]
- [[ProjectileParams]]
- [[RNG]]
- [[Room]]
- [[SFXManager]]
- [[Sprite]]
- [[Vector]]

## Key Methods

- [[#RegisterMod|RegisterMod]]
- [[#Game|Game]]
- [[#GetPtrHash|GetPtrHash]]
- [[#Random|Random]]
- [[#SFXManager|SFXManager]]

## Methods

### Functions

### BitSet128 {#BitSet128}

```
BitSet128 BitSet128 ( int Low = 0, int High = 0 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

构造一个 128 位标志集对象，用于存储超过 64 个布尔标志或位运算值。

**Use Cases:**

- 存储大量解锁标志
- 实现自定义状态位

**See also:** 



---

### Color {#Color}

```
Color Color ( float R, float G, float B, float A = 1, float RO = 0, float GO = 0, float BO = 0 )
```

*DLC: REP, REP+ | Modifiers: const*

构造一个通用颜色对象，用于渲染中的色调、偏移等设置。

**Use Cases:**

- 设置实体颜色
- 绘制彩色文本

**See also:** 
[[#KColor|KColor]]


---

### EntityPtr {#EntityPtr}

```
EntityPtr EntityPtr ( Entity entity )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

创建一个不拥有所有权的实体指针对象，用于安全引用可能被销毁的实体。

**Use Cases:**

- 在回调中保存实体引用
- 延迟访问实体

**See also:** 
[[#EntityRef|EntityRef]], [[#GetPtrHash|GetPtrHash]]


---

### EntityRef {#EntityRef}

```
EntityRef EntityRef ( Entity entity )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

创建一个实体引用对象，提供对实体的访问并能在实体无效时返回 nil。

**Use Cases:**

- 安全获取实体状态
- 在实体可能消失时进行条件判断

**See also:** 
[[#EntityPtr|EntityPtr]], [[#GetPtrHash|GetPtrHash]]


---

### Font {#Font}

```
Font Font ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

创建一个字体对象，用于加载位图字体并在屏幕上绘制字符串。

**Use Cases:**

- 自定义 UI 文本
- 绘制 HUD 信息

**See also:** 
[[#KColor|KColor]]


---

### Game {#Game}

```
Game Game ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取当前游戏实例对象，用于查询暂停状态、房间信息等全局游戏属性。

**Use Cases:**

- 检测游戏是否暂停
- 访问游戏整体设置

**See also:** 



---

### KColor {#KColor}

```
KColor KColor ( float red, float green, float blue, float alpha )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

构造专门用于 Font 对象的颜色，提供 RGB 及透明度。

**Use Cases:**

- 设置字体颜色
- 与 Font:DrawString 配合

**See also:** 
[[#Font|Font]], [[#Color|Color]]


---

### MusicManager {#MusicManager}

```
MusicManager MusicManager ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取音乐管理器对象，用于控制背景音乐的播放、暂停等。

**Use Cases:**

- 禁用背景音乐
- 切换音乐曲目

**See also:** 
[[#SFXManager|SFXManager]]


---

### ProjectileParams {#ProjectileParams}

```
ProjectileParams ProjectileParams ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

创建一个抛射体参数对象，用于定义发射子弹时的各种属性。

**Use Cases:**

- 自定义弹幕行为
- 设置子弹速度、伤害等

**See also:** 



---

### RegisterMod {#RegisterMod}

```
Mod Reference RegisterMod ( string modName, int apiVersion )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

注册当前 mod，返回 mod 引用，是所有 mod 必须首先调用的入口函数。

**Use Cases:**

- mod 初始化
- 注册回调与保存数据

**See also:** 



---

### RNG {#RNG}

```
RNG RNG ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

创建一个新的随机数生成器对象，用于可控的随机序列。

**Use Cases:**

- 控制物品生成随机
- 实现可复现的随机

**See also:** 
[[#Random|Random]]


---

### SFXManager {#SFXManager}

```
SFXManager SFXManager ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取音效管理器对象，用于播放、停止游戏音效。

**Use Cases:**

- 播放自定义音效
- 停止特定音效

**See also:** 
[[#MusicManager|MusicManager]]


---

### Sprite {#Sprite}

```
Sprite Sprite ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

创建一个精灵对象，用于加载和显示动画帧。

**Use Cases:**

- 渲染自定义实体
- 界面动画

**See also:** 



---

### Vector {#Vector}

```
Vector Vector ( float x, float y)
```

*DLC: AB+, REP, REP+ | Modifiers: const*

创建一个二维向量对象，用于位置、速度等数学运算。

**Use Cases:**

- 设置实体位置
- 计算移动方向

**See also:** 
[[#RandomVector|RandomVector]]


---

### GetPtrHash {#GetPtrHash}

```
int GetPtrHash ( Object object )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回对象指针的哈希值，用于可靠判断两个引用是否指向同一游戏对象。

Returns a hash-value of the pointer given as an input value. Valid inputs are any Isaac object, including `:::lua Entity`, `:::lua Room`, `:::lua RNG`, `:::lua Sprite`, `:::lua Game` etc.

**Use Cases:**

- 比较回调中的 entity 与保存的 entity
- 避免直接指针比较的错误

**See also:** 
[[#EntityPtr|EntityPtr]], [[#EntityRef|EntityRef]]


---

### Random {#Random}

```
int Random ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回一个 0 到 2^32 之间的伪随机整数，适合非种子的简单随机需求。

Returns a random integer between 0 and 2^32. It is tested to be inclusive on the lower end and exclusive on the higher end.

**Use Cases:**

- 生成随机偏移
- 临时决定概率

**See also:** 
[[#RNG|RNG]]


---

### RandomVector {#RandomVector}

```
Vector RandomVector ( )
```

*DLC: AB+, REP, REP+*

返回一个长度为 1 的随机方向向量，可乘以长度以获得任意距离的随机方向。

Returns a random vector with length 1. Multiply this vector by a number for larger random vectors.

**Use Cases:**

- 生成随机弹幕方向
- 物品随机掉落偏移

**See also:** 
[[#Vector|Vector]]


---

## See Also

- [[BitSet128]]
- [[Color]]
- [[Entity]]
- [[EntityPtr]]
- [[EntityRef]]
- [[Font]]
- [[Game]]
- [[Isaac]]
- [[KColor]]
- [[MusicManager]]
- [[ProjectileParams]]
- [[RNG]]
- [[Room]]
- [[SFXManager]]
- [[Sprite]]
- [[Vector]]
