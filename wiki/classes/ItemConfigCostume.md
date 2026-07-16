---
title: ItemConfigCostume
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 8
---

# ItemConfigCostume

## Summary

提供道具服装配置的只读数据，包括动画路径、覆盖标志、备用皮肤、飞行状态、颜色覆盖、优先级和肤色等信息，用于 mod 中读取和判断道具的外观效果。

## Related Types

- [[Color]]

## Key Methods

- [[#Anm2Path|Anm2Path]]
- [[#ID|ID]]
- [[#Priority|Priority]]
- [[#HasOverlay|HasOverlay]]
- [[#SkinColor|SkinColor]]

## Methods

### Functions

### Anm2Path {#Anm2Path}

```
string Anm2Path
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回该道具服装的动画文件路径（.anm2 文件），用于定位和加载动画资源。

**Use Cases:**

- 获取动画文件路径以自定角色外貌渲染
- 检查动画资源是否存在或加载特定动画

**See also:** 
[[#ID|ID]], [[#Priority|Priority]]


---

### HasOverlay {#HasOverlay}

```
boolean HasOverlay
```

*DLC: REP, REP+ | Modifiers: const*

布尔值，指示服装是否包含覆盖图层（如特效叠加层）。

**Use Cases:**

- 判断道具是否会向角色添加额外图层
- 决定是否绘制叠加效果，避免重叠异常

**See also:** 
[[#HasSkinAlt|HasSkinAlt]], [[#IsFlying|IsFlying]]


---

### HasSkinAlt {#HasSkinAlt}

```
boolean HasSkinAlt
```

*DLC: AB+, REP, REP+ | Modifiers: const*

布尔值，指示服装是否提供备用皮肤外观，常用于支持多种外观的道具。

**Use Cases:**

- 检查道具是否有备选皮肤，用于皮肤切换功能
- 确认是否需要展示皮肤选择界面

**See also:** 
[[#HasOverlay|HasOverlay]], [[#SkinColor|SkinColor]]


---

### ID {#ID}

```
int ID
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回服装的唯一整数标识 ID，可与 Collectible 等关联进行识别。

**Use Cases:**

- 标识和比对不同道具的服装配置
- 作为查找或存储服装数据的键值

**See also:** 
[[#Anm2Path|Anm2Path]], [[#Priority|Priority]]


---

### IsFlying {#IsFlying}

```
boolean IsFlying
```

*DLC: AB+, REP, REP+ | Modifiers: const*

布尔值，表示该服装是否让角色呈现飞行状态的外观。

**Use Cases:**

- 判断道具是否改变角色为飞行外观
- 在角色状态变化时应用对应的飞行服装

**See also:** 
[[#HasOverlay|HasOverlay]], [[#Priority|Priority]]


---

### OverwriteColor {#OverwriteColor}

```
boolean OverwriteColor
```

*DLC: AB+, REP, REP+ | Modifiers: static*

布尔值，指示服装是否会覆盖角色的原始颜色，可能影响与其他颜色效果的叠加。

**Use Cases:**

- 决定是否允许服装改变角色颜色，避免冲突
- 配合肤色数据实现正确的颜色修改

**See also:** 
[[#SkinColor|SkinColor]], [[#HasSkinAlt|HasSkinAlt]]


---

### Priority {#Priority}

```
int Priority
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回整数优先级，用于在多个服装同时生效时决定显示哪一套，数值越高越优先。

**Use Cases:**

- 控制服装的渲染顺序，解决多层服装叠加问题
- 调整不同道具服装的显示优先级

**See also:** 
[[#Anm2Path|Anm2Path]], [[#ID|ID]]


---

### SkinColor {#SkinColor}

```
SkinColor SkinColor
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回 SkinColor 对象以获取肤色数据，但该字段因返回 UserData 而存在 bug，实际无法正常使用。

???+ bug "Bug"

**Use Cases:**

- 理论上用于获取肤色进行自定义颜色调整（目前不可用）

**See also:** 
[[#OverwriteColor|OverwriteColor]]


---

## See Also

- [[Color]]
