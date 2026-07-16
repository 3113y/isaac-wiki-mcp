---
title: GridEntityRock
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 8
---

# GridEntityRock

## Summary

表示网格中的岩石实体，提供动画状态和视觉表现的控制，支持普通岩石与大岩石的帧管理、瓦砾动画等。

## Inheritance

- Inherits from: [[GridEntity]]

## Related Types

- [[Entity]]
- [[Sprite]]

## Key Methods

- [[#GetBigRockFrame|GetBigRockFrame]]
- [[#SetBigRockFrame|SetBigRockFrame]]
- [[#UpdateAnimFrame|UpdateAnimFrame]]
- [[#GetRubbleAnim|GetRubbleAnim]]
- [[#GetSprite|GetSprite]]

## Methods

### Functions

### GetBigRockFrame {#GetBigRockFrame}

```
int GetBigRockFrame ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前大岩石的动画帧索引，用于同步动画状态或判断特定帧。

**Use Cases:**

- 检测大岩石是否到达断裂关键帧
- 配合其他实体根据帧数播放音效

**See also:** 
[[#SetBigRockFrame|SetBigRockFrame]], [[#UpdateAnimFrame|UpdateAnimFrame]], [[#FrameCnt|FrameCnt]]


---

### GetRubbleAnim {#GetRubbleAnim}

```
string GetRubbleAnim ( )
```

*DLC: REP, REP+ | Modifiers: const*

返回当前瓦砾动画的名称字符串，表示岩石被破坏后残留物的动画类型。

**Use Cases:**

- 根据瓦砾动画决定后续生成物的样式
- 在脚本中根据动画名禁用或启用碰撞

**See also:** 
[[#RubbleAnim|RubbleAnim]], [[#Anim|Anim]]


---

### GetSprite {#GetSprite}

```
const Sprite GetSprite ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取该岩石精灵的只读 Sprite 对象，用于精细控制渲染或动画替换。

Same as the Repentance exclusive function [GetSprite()](GridEntity.md#getsprite).

**Use Cases:**

- 覆盖岩石的默认精灵来源
- 同步外部特效与岩石的动画位置

**See also:** 
[[#UpdateAnimFrame|UpdateAnimFrame]], [[#Anim|Anim]]


---

### SetBigRockFrame {#SetBigRockFrame}

```
void SetBigRockFrame ( int Frame )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将大岩石的动画帧设置为指定值，用于跳转或重置动画进度。

**Use Cases:**

- 播放岩石碎裂的关键帧序列
- 重置动画以循环表现特殊状态

**See also:** 
[[#GetBigRockFrame|GetBigRockFrame]], [[#UpdateAnimFrame|UpdateAnimFrame]], [[#FrameCnt|FrameCnt]]


---

### UpdateAnimFrame {#UpdateAnimFrame}

```
void UpdateAnimFrame ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

手动推进一帧岩石的动画，用于自定义更新循环中控制动画速度。

**Use Cases:**

- 在暂停菜单外保持动画同步
- 实现慢动作或快进效果

**See also:** 
[[#GetBigRockFrame|GetBigRockFrame]], [[#SetBigRockFrame|SetBigRockFrame]], [[#FrameCnt|FrameCnt]], [[#GetSprite|GetSprite]]


---

### Anim {#Anim}

```
string Anim
```

*DLC: AB+, REP, REP+ | Modifiers: static*

字符串属性，表示岩石当前使用的主体动画名称（如普通、大岩石等）。

**Use Cases:**

- 获取或更改岩石的动画集
- 判断岩石当前处于何种形态

**See also:** 
[[#GetSprite|GetSprite]], [[#RubbleAnim|RubbleAnim]], [[#UpdateAnimFrame|UpdateAnimFrame]]


---

### FrameCnt {#FrameCnt}

```
int FrameCnt
```

*DLC: AB+, REP, REP+ | Modifiers: const*

整数属性，保存当前动画的时间计数器，与帧推进相关。

**Use Cases:**

- 读取或修改动画播放进度
- 配合自定义动画速度使用

**See also:** 
[[#UpdateAnimFrame|UpdateAnimFrame]], [[#GetBigRockFrame|GetBigRockFrame]]


---

### RubbleAnim {#RubbleAnim}

```
string RubbleAnim
```

*DLC: AB+, REP, REP+ | Modifiers: const*

字符串属性，存储岩石被破坏后瓦砾的动画名称。

**Use Cases:**

- 决定岩石破碎后的视觉表现
- 根据瓦砾类型触发不同掉落

**See also:** 
[[#GetRubbleAnim|GetRubbleAnim]], [[#Anim|Anim]]


---

## See Also

- [[Entity]]
- [[GridEntity]]
- [[Sprite]]
