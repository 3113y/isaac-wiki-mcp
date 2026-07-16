---
title: MusicManager
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 20
---

# MusicManager

## Summary

MusicManager 用于控制游戏音乐的播放、切换、淡入淡出、暂停、恢复、音量调整、音调滑动以及音乐队列管理。

## Key Methods

- [[#Play|Play]]
- [[#Fadein|Fadein]]
- [[#Fadeout|Fadeout]]
- [[#Crossfade|Crossfade]]
- [[#Disable|Disable]]

## Methods

### Constructors

### MusicManager {#MusicManager}

```
MusicManager MusicManager ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

构造一个 MusicManager 实例，用于后续的音乐控制操作。

**Use Cases:**

- 获取 MusicManager 对象以便调用音乐相关方法

**See also:** 
[[#Disable|Disable]], [[#Enable|Enable]], [[#Play|Play]]


---

### Functions

### Crossfade {#Crossfade}

```
void Crossfade ( Music ID, float FadeRate = 0.08 )
```

*DLC: REP, REP+ | Modifiers: const*

交叉淡入淡出到指定音乐 ID，平滑切换当前播放的音乐。注意 ID 参数需在合法范围内，否则游戏会崩溃。

???+ bug "Bug"

**Use Cases:**

- 平滑过渡到新背景音乐
- 根据游戏状态动态切换配乐

**See also:** 
[[#Play|Play]], [[#Fadein|Fadein]], [[#Fadeout|Fadeout]], [[#GetCurrentMusicID|GetCurrentMusicID]]


---

### Disable {#Disable}

```
void Disable ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

禁用音乐管理器，停止所有音乐播放。

**Use Cases:**

- 暂停全部音乐以便播放特殊音效
- 在特定场景静音所有音乐

**See also:** 
[[#Enable|Enable]], [[#IsEnabled|IsEnabled]], [[#Pause|Pause]]


---

### DisableLayer {#DisableLayer}

```
void DisableLayer ( int LayerId = 0 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

禁用指定音乐层，静音该层的音乐播放。

**Use Cases:**

- 禁用额外音轨层以简化音效
- 调节音乐分层表现

**See also:** 
[[#EnableLayer|EnableLayer]], [[#IsLayerEnabled|IsLayerEnabled]], [[#Disable|Disable]]


---

### Enable {#Enable}

```
void Enable ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

（重新）启用音乐管理器，恢复被禁用前的音乐播放状态。

**Use Cases:**

- 恢复因 Disable 暂停的音乐
- 从静音状态回到正常音乐

**See also:** 
[[#Disable|Disable]], [[#Play|Play]], [[#Resume|Resume]]


---

### EnableLayer {#EnableLayer}

```
void EnableLayer ( int LayerId = 0, boolean Instant = false )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

启用指定音乐层，并允许立即生效或渐变恢复。

**Use Cases:**

- 动态加入额外音乐层
- 实现分层音乐效果

**See also:** 
[[#DisableLayer|DisableLayer]], [[#IsLayerEnabled|IsLayerEnabled]], [[#VolumeSlide|VolumeSlide]]


---

### Fadein {#Fadein}

```
void Fadein ( Music ID, float Volume = 1, float FadeRate = 0.08 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

以淡入方式播放指定音乐，可设置目标音量和淡入速率。

**Use Cases:**

- 营造场景逐渐转换的氛围
- 平滑引入新的背景音乐

**See also:** 
[[#Play|Play]], [[#Crossfade|Crossfade]], [[#Fadeout|Fadeout]], [[#VolumeSlide|VolumeSlide]]


---

### Fadeout {#Fadeout}

```
void Fadeout ( float FadeRate = 0.08 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将当前音乐淡出至静音，可自定义淡出速率。

**Use Cases:**

- 结束当前音乐时的平滑消失
- 准备切换到下一首音乐

**See also:** 
[[#Fadein|Fadein]], [[#Crossfade|Crossfade]], [[#Disable|Disable]]


---

### GetCurrentMusicID {#GetCurrentMusicID}

```
Music GetCurrentMusicID ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取当前正在播放的音乐 ID，用于查询播放状态。

**Use Cases:**

- 检查当前播放曲目是否正确
- 根据当前音乐 ID 执行后续操作

**See also:** 
[[#GetQueuedMusicID|GetQueuedMusicID]], [[#Play|Play]], [[#Crossfade|Crossfade]]


---

### GetQueuedMusicID {#GetQueuedMusicID}

```
Music GetQueuedMusicID ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取队列中等待播放的音乐 ID，若队列为空则返回当前音乐 ID。

if nothing is queued, return the current music id

**Use Cases:**

- 查看即将播放的音乐
- 判断是否有排队音乐

**See also:** 
[[#Queue|Queue]], [[#GetCurrentMusicID|GetCurrentMusicID]]


---

### IsEnabled {#IsEnabled}

```
boolean IsEnabled ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

查询音乐管理器当前是否处于启用状态。

**Use Cases:**

- 判断声音是否被禁用
- 根据启用状态调整 UI 或逻辑

**See also:** 
[[#Enable|Enable]], [[#Disable|Disable]]


---

### IsLayerEnabled {#IsLayerEnabled}

```
boolean IsLayerEnabled ( int LayerId = 0 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检查指定音乐层是否当前处于启用状态。

**Use Cases:**

- 监控额外音轨层的状态
- 实现依赖层状态的逻辑

**See also:** 
[[#EnableLayer|EnableLayer]], [[#DisableLayer|DisableLayer]]


---

### Pause {#Pause}

```
void Pause ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

暂停当前音乐播放，保留播放位置可用于后续恢复。

**Use Cases:**

- 在菜单或对话时暂停背景音乐
- 临时静音场景

**See also:** 
[[#Resume|Resume]], [[#Disable|Disable]], [[#Enable|Enable]]


---

### PitchSlide {#PitchSlide}

```
void PitchSlide ( float TargetPitch )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将音乐音调滑动到目标值，实现变速或变调效果。

**Use Cases:**

- 制造紧张或缓慢的游戏氛围
- 配合游戏速度变化调整音乐

**See also:** 
[[#ResetPitch|ResetPitch]], [[#Play|Play]], [[#VolumeSlide|VolumeSlide]]


---

### Play {#Play}

```
void Play ( Music ID, float Volume = 1 )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

立即播放指定音乐 ID，可设置音量。注意 ID 参数需合法，否则会崩溃。

???+ bug "Bug"

**Use Cases:**

- 强制切换背景音乐
- 开始播放特定场景的音乐

**See also:** 
[[#Crossfade|Crossfade]], [[#Fadein|Fadein]], [[#Queue|Queue]], [[#GetCurrentMusicID|GetCurrentMusicID]]


---

### Queue {#Queue}

```
void Queue ( Music ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将指定音乐 ID 加入播放队列，在当前音乐结束后自动播放。

**Use Cases:**

- 顺序播放多首音乐
- 安排音乐播放顺序

**See also:** 
[[#GetQueuedMusicID|GetQueuedMusicID]], [[#Play|Play]], [[#Crossfade|Crossfade]]


---

### ResetPitch {#ResetPitch}

```
void ResetPitch ( )
```

*DLC: AB+, REP, REP+*

将音乐音调重置回默认值，取消之前的音调滑动效果。

**Use Cases:**

- 恢复正常音调
- 在音调特效结束后还原

**See also:** 
[[#PitchSlide|PitchSlide]]


---

### Resume {#Resume}

```
void Resume ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

恢复之前暂停的音乐播放，继续从暂停位置播放。

**Use Cases:**

- 退出菜单后恢复音乐
- 继续被中断的背景音乐

**See also:** 
[[#Pause|Pause]], [[#Disable|Disable]], [[#Enable|Enable]]


---

### UpdateVolume {#UpdateVolume}

```
void UpdateVolume ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

将音乐音量立即设置为选项菜单中定义的音量值。

**Use Cases:**

- 同步设置变更后的音量
- 重置因脚本修改的音量

**See also:** 
[[#VolumeSlide|VolumeSlide]], [[#Fadein|Fadein]], [[#Fadeout|Fadeout]]


---

### VolumeSlide {#VolumeSlide}

```
void VolumeSlide ( float TargetVolume, float FadeRate = 0.08 )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

平滑滑动音乐音量到目标值，可控制滑动速率。

**Use Cases:**

- 动态调整音乐远近感
- 实现角色进入特殊区域时的音量变化

**See also:** 
[[#Fadein|Fadein]], [[#Fadeout|Fadeout]], [[#UpdateVolume|UpdateVolume]]


---
