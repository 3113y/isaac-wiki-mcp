---
title: SFXManager
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 10
---

# SFXManager

## Summary

音效管理器，用于控制游戏中所有音效的播放、停止、音量调整、音高调整、循环音效与环境音效管理。

## Key Methods

- [[#Play|Play]]
- [[#Stop|Stop]]
- [[#AdjustPitch|AdjustPitch]]
- [[#AdjustVolume|AdjustVolume]]
- [[#SetAmbientSound|SetAmbientSound]]

## Methods

### Constructors

### SFXManager {#SFXManager}

```
SFXManager SFXManager ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

创建SFXManager实例，获取音效管理器的入口对象。

**Use Cases:**

- 在代码中获取全局音效管理器，以调用其所有方法

**See also:** 
[[#Play|Play]], [[#Stop|Stop]], [[#AdjustPitch|AdjustPitch]]


---

### Functions

### AdjustPitch {#AdjustPitch}

```
void AdjustPitch ( SoundEffect ID, float Pitch )
```

*DLC: REP, REP+ | Modifiers: const*

动态调整指定音效的音高，常用于使重复播放的声音产生变化。

mostly useful for repeating sounds

**Use Cases:**

- 让循环音效的音调随时间或条件改变
- 为重复音效添加音调偏移避免单调

**See also:** 
[[#Play|Play]], [[#AdjustVolume|AdjustVolume]], [[#SetAmbientSound|SetAmbientSound]]


---

### AdjustVolume {#AdjustVolume}

```
void AdjustVolume ( SoundEffect ID, float Volume )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

动态调整指定音效的音量，常用于控制重复播放声音的音量变化。

mostly useful for repeating sounds

**Use Cases:**

- 降低或提高循环音效的音量
- 根据游戏状态调节音效响度

**See also:** 
[[#AdjustPitch|AdjustPitch]], [[#Play|Play]], [[#SetAmbientSound|SetAmbientSound]]


---

### GetAmbientSoundVolume {#GetAmbientSoundVolume}

```
float GetAmbientSoundVolume ( SoundEffect ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

查询指定环境音效的当前音量值。

**Use Cases:**

- 读取环境音效音量以用于UI或逻辑判断

**See also:** 
[[#SetAmbientSound|SetAmbientSound]], [[#AdjustVolume|AdjustVolume]]


---

### IsPlaying {#IsPlaying}

```
boolean IsPlaying ( SoundEffect ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检测指定音效是否正在播放，返回布尔值。

**Use Cases:**

- 避免重复播放同一音效
- 根据播放状态切换逻辑

**See also:** 
[[#Play|Play]], [[#Stop|Stop]]


---

### Play {#Play}

```
void Play ( SoundEffect ID, float Volume = 1, int FrameDelay = 2, boolean Loop = false, float Pitch = 1, float Pan = 0 )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

播放音效，支持设置音量、播放冷却帧数、循环、音高和声相。注意FrameDelay参数表示再次播放的最小帧间隔而非延迟。

Despite its name, **FrameDelay** does NOT add a delay before the sound plays. Rather, it determines how many frames must pass before the sound can be played again.

**Use Cases:**

- 播放一次性或循环音效
- 控制音效的播放频率
- 自定义音效的空间定位（声相）

**See also:** 
[[#Stop|Stop]], [[#AdjustPitch|AdjustPitch]], [[#AdjustVolume|AdjustVolume]], [[#StopLoopingSounds|StopLoopingSounds]]


---

### Preload {#Preload}

```
void Preload ( SoundEffect ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

预加载音效资源，确保正式播放时不会因加载造成延迟或卡顿。

**Use Cases:**

- 在场景切换或关键时机提前加载常用音效
- 减少首次播放时的异步加载开销

**See also:** 
[[#Play|Play]]


---

### SetAmbientSound {#SetAmbientSound}

```
void SetAmbientSound ( SoundEffect ID, float Volume, float Pitch )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置环境背景音效，可同时指定音量与音高。

**Use Cases:**

- 在特定房间或事件中更换环境音效
- 调整环境音效的氛围参数

**See also:** 
[[#GetAmbientSoundVolume|GetAmbientSoundVolume]], [[#AdjustVolume|AdjustVolume]], [[#AdjustPitch|AdjustPitch]]


---

### Stop {#Stop}

```
void Stop ( SoundEffect ID )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

立即停止指定音效的播放。

**Use Cases:**

- 终止不再需要的音效
- 中断错误触发的持续声音

**See also:** 
[[#Play|Play]], [[#IsPlaying|IsPlaying]], [[#StopLoopingSounds|StopLoopingSounds]]


---

### StopLoopingSounds {#StopLoopingSounds}

```
void StopLoopingSounds ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

停止所有当前正在播放的循环音效，不影响一次性音效。

**Use Cases:**

- 清理所有循环音效以免重叠
- 在场景重置或暂停时使用

**See also:** 
[[#Play|Play]], [[#Stop|Stop]], [[#SetAmbientSound|SetAmbientSound]]


---
