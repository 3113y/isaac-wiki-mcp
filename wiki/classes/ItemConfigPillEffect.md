---
title: ItemConfigPillEffect
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 11
---

# ItemConfigPillEffect

## Summary

代表一个药丸效果的配置信息，可通过ItemConfig.GetPillEffect()获取，提供可用性检查、解锁成就、播音员设置、ID、名称等只读属性。

## Key Methods

- [[#IsAvailable|IsAvailable]]
- [[#AchievementID|AchievementID]]
- [[#GreedModeAllowed|GreedModeAllowed]]
- [[#ID|ID]]
- [[#Name|Name]]

## Methods

### Functions

### IsAvailable {#IsAvailable}

```
boolean IsAvailable ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检查该药丸效果在当前游戏环境（如模式、解锁状态）下是否可用。

**Use Cases:**

- 在随机生成药丸前过滤不可用的效果
- 确认特定药丸效果是否因达成条件而解锁

**See also:** 
[[#AchievementID|AchievementID]], [[#GreedModeAllowed|GreedModeAllowed]]


---

### AchievementID {#AchievementID}

```
int AchievementID
```

*DLC: REP, REP+ | Modifiers: const*

返回解锁该药丸效果的成就ID，未关联成就时默认返回-1。

**Use Cases:**

- 检查药丸效果是否已被玩家解锁
- 追踪需要哪些成就来解锁指定药丸

**See also:** 
[[#IsAvailable|IsAvailable]], [[#ID|ID]]


---

### AnnouncerDelay {#AnnouncerDelay}

```
int AnnouncerDelay
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回与该药丸效果关联的播报员语音延迟值。

**Use Cases:**

- 自定义或调试药丸的播报员播放时序

**See also:** 
[[#AnnouncerVoice|AnnouncerVoice]], [[#AnnouncerVoiceSuper|AnnouncerVoiceSuper]]


---

### AnnouncerVoice {#AnnouncerVoice}

```
int AnnouncerVoice
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回该药丸效果使用的普通播报员语音ID。

**Use Cases:**

- 查询或读取药丸效果的播报员语音资源

**See also:** 
[[#AnnouncerDelay|AnnouncerDelay]], [[#AnnouncerVoiceSuper|AnnouncerVoiceSuper]]


---

### AnnouncerVoiceSuper {#AnnouncerVoiceSuper}

```
int AnnouncerVoiceSuper
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回该药丸效果使用的超级播报员语音ID。

**Use Cases:**

- 获取药丸效果在超级播报员模式下的语音资源

**See also:** 
[[#AnnouncerVoice|AnnouncerVoice]], [[#AnnouncerDelay|AnnouncerDelay]]


---

### EffectClass {#EffectClass}

```
int EffectClass
```

*DLC: AB+, REP, REP+ | Modifiers: static*

原本应返回效果主类，但由于已知Bug，该变量返回userdata而非有效整数，不推荐使用。

???+ bug "Bug"

**Use Cases:**

- 注意避免使用此属性，它不可靠

**See also:** 
[[#EffectSubClass|EffectSubClass]]


---

### EffectSubClass {#EffectSubClass}

```
int EffectSubClass
```

*DLC: AB+, REP, REP+ | Modifiers: const*

原本应返回效果子类，但由于已知Bug，该变量返回userdata而非有效整数，不推荐使用。

???+ bug "Bug"

**Use Cases:**

- 注意避免使用此属性，它不可靠

**See also:** 
[[#EffectClass|EffectClass]]


---

### GreedModeAllowed {#GreedModeAllowed}

```
boolean GreedModeAllowed
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回该药丸效果是否允许在贪婪模式中出现，默认为true。

**Use Cases:**

- 在贪婪模式中过滤可用的药丸列表
- 判断特定药丸效果在贪婪模式是否被禁用

**See also:** 
[[#IsAvailable|IsAvailable]]


---

### ID {#ID}

```
int ID
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回药丸效果的内部标识ID。

**Use Cases:**

- 用于精确比较或存储药丸效果
- 作为PillEffect枚举值的直接参考

**See also:** 
[[#Name|Name]]


---

### MimicCharge {#MimicCharge}

```
int MimicCharge
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回与该药丸效果相关的模仿者充能数值。

**Use Cases:**

- 查询药丸效果在模仿者机制中的充能消耗

**See also:** 



---

### Name {#Name}

```
string Name
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回药丸效果的名字字符串。但在Repentance版本中，返回的是格式化的键名（如#BALLS_OF_STEEL_NAME）而非游戏内实际名称。

**Use Cases:**

- 获取药丸效果的内部名称标识
- 注意需要额外处理才能得到可读的游戏内名称

**See also:** 
[[#ID|ID]]


---
