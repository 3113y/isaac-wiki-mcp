---
title: HUD
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 13
---

# HUD

## Summary

管理游戏 HUD 显示，包括刷新多玩家布局、控制充能条闪烁、更新缓存、显示物品拾取文字及控制可见性等核心 UI 功能。

## Related Types

- [[EntityPlayer]]
- [[ItemConfigItem]]

## Key Methods

- [[#AssignPlayerHUDs|AssignPlayerHUDs]]
- [[#FlashChargeBar|FlashChargeBar]]
- [[#InvalidateActiveItem|InvalidateActiveItem]]
- [[#SetVisible|SetVisible]]
- [[#ShowItemText|ShowItemText]]

## Methods

### Functions

### AssignPlayerHUDs {#AssignPlayerHUDs}

```
void AssignPlayerHUDs ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

刷新 HUD，主要针对多玩家状态下角色父子关系变更后，重新布局主 HUD 上的健康显示等元素。

Refreshes the HUD (e.g. Characters that have Parent specified no longer show their health in the main HUD).

**Use Cases:**

- 设置或解除角色父子关系后刷新 HUD
- 变更多玩家模式下主角色的显示状态

**See also:** 
[[#InvalidateActiveItem|InvalidateActiveItem]], [[#InvalidateCraftingItem|InvalidateCraftingItem]], [[#Update|Update]], [[#PostUpdate|PostUpdate]]


---

### FlashChargeBar {#FlashChargeBar}

```
void FlashChargeBar ( EntityPlayer Player, ActiveSlot ActiveSlot )
```

*DLC: REP, REP+ | Modifiers: const*

让指定玩家指定主动道具槽的充能条闪烁，模拟充能变化效果，但不实际改变充能值。

Causes the charge bar of the active item in the specified slot to blink as if it had gained charges

**Use Cases:**

- 自定义主动道具充能反馈效果
- 提示玩家充能即将发生变化

**See also:** 
[[#InvalidateActiveItem|InvalidateActiveItem]], [[#AssignPlayerHUDs|AssignPlayerHUDs]]


---

### InvalidateActiveItem {#InvalidateActiveItem}

```
void InvalidateActiveItem ( EntityPlayer Player, ActiveSlot ActiveSlot )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

强制刷新指定主动道具槽的显示，用于在不通过常规给予/移除道具方式修改槽位后保持界面同步。

Forces the specified active item slot to update, this might be useful for functions that modify an active item slot without directly giving or removing items

**Use Cases:**

- 直接修改主动道具槽数据后刷新界面
- 自定义道具切换逻辑后更新 HUD

**See also:** 
[[#FlashChargeBar|FlashChargeBar]], [[#AssignPlayerHUDs|AssignPlayerHUDs]], [[#Update|Update]]


---

### InvalidateCraftingItem {#InvalidateCraftingItem}

```
void InvalidateCraftingItem ( EntityPlayer Player )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

强制刷新 Bag of Crafting 的合成预览输出，确保配方更改后界面即时反映新结果。

Forces the crafting output from Bag of Crafting to update (this might become useful in the future)

**Use Cases:**

- 修改合成配方或原材料后更新预览
- 扩展 Bag of Crafting 功能时同步 UI

**See also:** 
[[#InvalidateActiveItem|InvalidateActiveItem]], [[#AssignPlayerHUDs|AssignPlayerHUDs]], [[#Update|Update]]


---

### IsVisible {#IsVisible}

```
boolean IsVisible ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前 HUD 是否可见，用于判断是否需要在自定义渲染或逻辑中处理 HUD 可见状态。

Returns false if HUD is invisible and true otherwise.

**Use Cases:**

- 在自定义渲染前检查 HUD 是否可见以避免冲突
- 根据 HUD 状态切换其他 UI 元素的显示

**See also:** 
[[#SetVisible|SetVisible]], [[#Render|Render]], [[#PostUpdate|PostUpdate]]


---

### PostUpdate {#PostUpdate}

```
void PostUpdate ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

每帧更新后期调用，可能用于处理 HUD 的额外刷新逻辑，通常由游戏引擎内部触发。

___

**Use Cases:**

- 内部维护 HUD 状态
- 调试或扩展 HUD 更新流程

**See also:** 
[[#Update|Update]], [[#Render|Render]], [[#AssignPlayerHUDs|AssignPlayerHUDs]]


---

### Render {#Render}

```
void Render ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

执行 HUD 的渲染操作，由引擎在合适的渲染阶段调用，一般不应直接调用。

___

**Use Cases:**

- 内部渲染 HUD 各元素
- 可能的自定义 HUD 渲染插件利用

**See also:** 
[[#Update|Update]], [[#PostUpdate|PostUpdate]], [[#SetVisible|SetVisible]]


---

### SetVisible {#SetVisible}

```
void SetVisible ( boolean Visible = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置 HUD 的可见性，可完全开启或关闭整个 HUD 的显示。

Turns the HUD on or off.

**Use Cases:**

- 暂时隐藏 HUD 以提供沉浸式体验
- 根据游戏状态动态显示 HUD

**See also:** 
[[#IsVisible|IsVisible]], [[#Render|Render]], [[#Update|Update]]


---

### ShowFortuneText {#ShowFortuneText}

```
void ShowFortuneText ( string MainString, string SecondaryString, ... )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

显示类似预言机（Fortune Teller）的文字提示，支持可变参数以展示自定义多行文本。

Allows to display fortune streak with text. Accepts unlimited amount of arguments.

**Use Cases:**

- 模拟预言机或抽奖给出提示
- 显示多行自定义叙事性文字

**See also:** 
[[#ShowItemText|ShowItemText]], [[#SetVisible|SetVisible]]


---

### ShowItemText {#ShowItemText}

```
void ShowItemText ( string MainString, string SecondaryString, boolean IsCurseDisplay = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

显示类似物品拾取的 streak 文本，可自定义主副字符串，并可标记为诅咒提示。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 模拟捡起物品但实际未添加物品
- 显示自定义提示如警告信息

**See also:** 
[[#ShowFortuneText|ShowFortuneText]], [[#FlashChargeBar|FlashChargeBar]]


---

### void ShowItemText ( string MainString, string SecondaryString, boolean IsCurseDisplay = false, boolean StackUpText ) {#void ShowItemText ( string MainString, string SecondaryString, boolean IsCurseDisplay = false, boolean StackUpText )}

```
void ShowItemText ( EntityPlayer Player, ItemConfigItem Item)
```

*DLC: AB+, REP, REP+ | Modifiers: const*

显示物品拾取文本，并可指定是否显示堆叠计数文字（StackUpText），用于道具层数变化提示。

**Use Cases:**

- 显示多层道具堆叠的拾取提示
- 模拟带堆叠效果的物品获取

**See also:** 
[[#ShowItemText|ShowItemText]], [[#ShowFortuneText|ShowFortuneText]], [[#FlashChargeBar|FlashChargeBar]]


---

### ShowItemText {#ShowItemText}

```
void ShowItemText ( EntityPlayer Player, ItemConfigItem Item, boolean StackUpText )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 ShowItemText 完成对应 API 操作

**See also:** 



---

### Update {#Update}

```
void Update ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Update 完成对应 API 操作

**See also:** 



---

## See Also

- [[EntityPlayer]]
- [[HUD]]
- [[ItemConfigItem]]
