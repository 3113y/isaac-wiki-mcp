---
title: Input
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 8
---

# Input

## Summary

提供对键盘、鼠标和控制器输入的全局访问，用于查询按键状态、动作力度以及鼠标坐标。

## Related Types

- [[Vector]]

## Key Methods

- [[#GetActionValue|GetActionValue]]
- [[#GetMousePosition|GetMousePosition]]
- [[#IsActionPressed|IsActionPressed]]
- [[#IsActionTriggered|IsActionTriggered]]
- [[#IsMouseBtnPressed|IsMouseBtnPressed]]

## Methods

### Functions

### GetActionValue {#GetActionValue}

```
float GetActionValue ( ButtonAction action, int controllerId )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取指定动作按钮（如移动、射击等默认功能）当前的按下力度，键盘时为0或1，控制器可返回模拟摇杆的连续值。

**Use Cases:**

- 获取模拟摇杆方向力度以实现平滑速度控制
- 判断键盘动作键是否被按住
- 结合力度值实现渐进式蓄力效果

**See also:** 
[[#IsActionPressed|IsActionPressed]], [[#IsActionTriggered|IsActionTriggered]]


---

### GetButtonValue {#GetButtonValue}

```
float GetButtonValue ( Keyboard button, int controllerId )
```

*DLC: REP, REP+ | Modifiers: const*

获取指定键盘按键的当前按下值，已被官方建议用GetActionValue替代。

**Use Cases:**

- 兼容旧代码中的键盘按键查询

**See also:** 
[[#GetActionValue|GetActionValue]]


---

### GetMousePosition {#GetMousePosition}

```
Vector GetMousePosition ( boolean gameCoords )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回鼠标在游戏世界坐标（true）或屏幕渲染坐标中的当前位置。

**Use Cases:**

- 在鼠标位置渲染自定义文本或图标
- 判断鼠标是否悬停在某个实体或UI区域
- 将游戏坐标转换为屏幕坐标以显示工具提示

**See also:** 
[[#IsMouseBtnPressed|IsMouseBtnPressed]], [[#Isaac.WorldToScreen|Isaac.WorldToScreen]]


---

### IsActionPressed {#IsActionPressed}

```
boolean IsActionPressed ( ButtonAction action, int controllerId )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检测指定动作按钮是否正被按住（持续按下期间均返回true）。

**Use Cases:**

- 实现按住奔跑或蓄力攻击
- 在按钮按住期间持续触发逻辑（如连续射击）
- 结合力度对控制器摇杆进行持续检测

**See also:** 
[[#IsActionTriggered|IsActionTriggered]], [[#GetActionValue|GetActionValue]]


---

### IsActionTriggered {#IsActionTriggered}

```
boolean IsActionTriggered ( ButtonAction action, int controllerId )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检测指定动作按钮是否刚被按下（仅按下瞬间返回true，下一次调用不再为true）。

**Use Cases:**

- 实现单次触发的动作，如放置炸弹、使用主动道具
- 避免按住时重复触发同一效果
- 菜单中的确认按钮处理

**See also:** 
[[#IsActionPressed|IsActionPressed]]


---

### IsButtonPressed {#IsButtonPressed}

```
boolean IsButtonPressed ( Keyboard button, int controllerId )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

检测特定键盘按键是否正被按住。

**Use Cases:**

- 检测回车、空格等按键的持续按下
- 用于文本输入或调试快捷键
- 实现持续互动的自定义热键

**See also:** 
[[#IsButtonTriggered|IsButtonTriggered]]


---

### IsButtonTriggered {#IsButtonTriggered}

```
boolean IsButtonTriggered ( Keyboard button, int controllerId )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检测特定键盘按键是否刚被按下（仅按下瞬间返回true）。

**Use Cases:**

- 切换界面或开启/关闭菜单
- 单次触发的调试热键
- 避免长按导致的重复操作

**See also:** 
[[#IsButtonPressed|IsButtonPressed]]


---

### IsMouseBtnPressed {#IsMouseBtnPressed}

```
boolean IsMouseBtnPressed ( Mouse button )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检测指定鼠标按键是否被按下（支持左键、右键、中键等）。

**Use Cases:**

- 右键打开上下文菜单
- 左键点击交互对象
- 中键/侧键自定义快捷功能

**See also:** 
[[#GetMousePosition|GetMousePosition]]


---

## See Also

- [[Vector]]
