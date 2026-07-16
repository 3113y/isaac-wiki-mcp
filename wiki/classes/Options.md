---
title: Options
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 27
---

# Options

## Summary

Options 类代表用户 options.ini 文件中的设置值，用于读取和修改游戏选项，如 HUD、音量、显示方式等。

## Related Types

- [[HUD]]

## Key Methods

- [[#HUDOffset|HUDOffset]]
- [[#ExtraHUDStyle|ExtraHUDStyle]]
- [[#ChargeBars|ChargeBars]]
- [[#Fullscreen|Fullscreen]]
- [[#FoundHUD|FoundHUD]]

## Methods

### Functions

### AnnouncerVoiceMode {#AnnouncerVoiceMode}

```
int AnnouncerVoiceMode
```

*DLC: AB+, REP, REP+ | Modifiers: const*

播音员语音模式：0 随机，1 关闭，2 始终开启。

0: random, 1: off, 2: always on

**Use Cases:**

- 根据该设置决定是否播放播音员语音
- 强制关闭播音员语音以避免干扰

**See also:** 



---

### BulletVisibility {#BulletVisibility}

```
boolean BulletVisibility
```

*DLC: REP, REP+ | Modifiers: const*

子弹可见性开关，true 显示子弹，false 隐藏子弹。

**Use Cases:**

- 读取玩家子弹可见性设置以决定是否显示自定义弹幕特效

**See also:** 



---

### CameraStyle {#CameraStyle}

```
int CameraStyle
```

*DLC: AB+, REP, REP+ | Modifiers: const*

摄像机风格：1 开启主动摄像机，2 关闭。

active cam 1: on, 2: off

**Use Cases:**

- 检查是否启用主动摄像机以调整屏幕震动或跟随效果

**See also:** 



---

### ChargeBars {#ChargeBars}

```
boolean ChargeBars
```

*DLC: AB+, REP, REP+ | Modifiers: const*

充能条显示开关，true 显示充能条。

**Use Cases:**

- 强制开启充能条以便玩家判断主动道具充能状态

**See also:** 
[[#FoundHUD|FoundHUD]]


---

### ConsoleFont {#ConsoleFont}

```
int ConsoleFont
```

*DLC: AB+, REP, REP+ | Modifiers: const*

控制台字体设置

0: default, 1: small, 2: tiny

**Use Cases:**

- 调用 ConsoleFont 完成对应 API 操作

**See also:** 



---

### DebugConsoleEnabled {#DebugConsoleEnabled}

```
boolean DebugConsoleEnabled
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 DebugConsoleEnabled 完成对应 API 操作

**See also:** 



---

### DisplayPopups {#DisplayPopups}

```
boolean DisplayPopups
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 DisplayPopups 完成对应 API 操作

**See also:** 



---

### ExtraHUDStyle {#ExtraHUDStyle}

```
int ExtraHUDStyle
```

*DLC: AB+, REP, REP+ | Modifiers: const*

0: off, 1: on, 2: mini

0: off, 1: on, 2: mini

**Use Cases:**

- 调用 ExtraHUDStyle 完成对应 API 操作

**See also:** 



---

### FadedConsoleDisplay {#FadedConsoleDisplay}

```
boolean FadedConsoleDisplay
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 FadedConsoleDisplay 完成对应 API 操作

**See also:** 



---

### Filter {#Filter}

```
boolean Filter
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Filter 完成对应 API 操作

**See also:** 



---

### FoundHUD {#FoundHUD}

```
boolean FoundHUD
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 FoundHUD 完成对应 API 操作

**See also:** 



---

### Fullscreen {#Fullscreen}

```
boolean Fullscreen
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Fullscreen 完成对应 API 操作

**See also:** 



---

### Gamma {#Gamma}

```
float Gamma
```

*DLC: AB+, REP, REP+ | Modifiers: static*

0.5-1.5

0.5-1.5

**Use Cases:**

- 调用 Gamma 完成对应 API 操作

**See also:** 



---

### HUDOffset {#HUDOffset}

```
float HUDOffset
```

*DLC: AB+, REP, REP+ | Modifiers: const*

0-1

0-1

**Use Cases:**

- 调用 HUDOffset 完成对应 API 操作

**See also:** 



---

### JacobEsauControls {#JacobEsauControls}

```
string JacobEsauControls
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Added with Repentance+.

Added with Repentance+.

**Use Cases:**

- 调用 JacobEsauControls 完成对应 API 操作

**See also:** 



---

### Language {#Language}

```
string Language
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Read only

Read only

**Use Cases:**

- 调用 Language 完成对应 API 操作

**See also:** 



---

### MapOpacity {#MapOpacity}

```
float MapOpacity
```

*DLC: AB+, REP, REP+*

0-1

0-1

**Use Cases:**

- 调用 MapOpacity 完成对应 API 操作

**See also:** 



---

### MaxRenderScale {#MaxRenderScale}

```
int MaxRenderScale
```

*DLC: AB+, REP, REP+ | Modifiers: const*

1-99

1-99

**Use Cases:**

- 调用 MaxRenderScale 完成对应 API 操作

**See also:** 



---

### MaxScale {#MaxScale}

```
int MaxScale
```

*DLC: AB+, REP, REP+ | Modifiers: static*

1-99

1-99

**Use Cases:**

- 调用 MaxScale 完成对应 API 操作

**See also:** 



---

### MouseControl {#MouseControl}

```
boolean MouseControl
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 MouseControl 完成对应 API 操作

**See also:** 



---

### MusicVolume {#MusicVolume}

```
float MusicVolume
```

*DLC: AB+, REP, REP+ | Modifiers: const*

0-1

0-1

**Use Cases:**

- 调用 MusicVolume 完成对应 API 操作

**See also:** 



---

### PauseOnFocusLost {#PauseOnFocusLost}

```
boolean PauseOnFocusLost
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 PauseOnFocusLost 完成对应 API 操作

**See also:** 



---

### RumbleEnabled {#RumbleEnabled}

```
boolean RumbleEnabled
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RumbleEnabled 完成对应 API 操作

**See also:** 



---

### SaveCommandHistory {#SaveCommandHistory}

```
boolean SaveCommandHistory
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SaveCommandHistory 完成对应 API 操作

**See also:** 



---

### SFXVolume {#SFXVolume}

```
float SFXVolume
```

*DLC: AB+, REP, REP+ | Modifiers: static*

0-1

0-1

**Use Cases:**

- 调用 SFXVolume 完成对应 API 操作

**See also:** 



---

### UseBorderlessFullscreen {#UseBorderlessFullscreen}

```
boolean UseBorderlessFullscreen
```

*DLC: AB+, REP | Modifiers: const*

Only takes effect if Fullscreen is also true.

Only takes effect if Fullscreen is also true.

**Use Cases:**

- 调用 UseBorderlessFullscreen 完成对应 API 操作

**See also:** 



---

### VSync {#VSync}

```
boolean VSync
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 VSync 完成对应 API 操作

**See also:** 



---

## See Also

- [[HUD]]
