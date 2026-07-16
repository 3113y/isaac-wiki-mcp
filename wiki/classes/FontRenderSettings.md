---
title: FontRenderSettings
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 13
---

# FontRenderSettings

## Summary

用于配置通过 Font:DrawString() 渲染文本时的特殊行为，例如自动换行、截断、对齐方式、行高比例、最大字符数和缺失字符替代。

## Related Types

- [[Font]]

## Key Methods

- [[#FontRenderSettings|FontRenderSettings]]
- [[#EnableAutoWrap|EnableAutoWrap]]
- [[#EnableTruncation|EnableTruncation]]
- [[#SetAlignment|SetAlignment]]
- [[#SetMaxCharacters|SetMaxCharacters]]

## Methods

### Constructors

### FontRenderSettings {#FontRenderSettings}

```
FontRenderSettings FontRenderSettings ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

构造函数，创建一个新的 FontRenderSettings 实例，用于配置字体渲染行为。

**Use Cases:**

- 初始化渲染设置对象

**See also:** 
[[#EnableAutoWrap|EnableAutoWrap]], [[#SetAlignment|SetAlignment]], [[#SetMaxCharacters|SetMaxCharacters]]


---

### Functions

### EnableAutoWrap {#EnableAutoWrap}

```
void EnableAutoWrap ( boolean enabled )
```

*DLC: REP, REP+ | Modifiers: const*

启用或禁用文本自动换行功能。

**Use Cases:**

- 让长文本在到达边界时自动折行
- 禁用自动换行实现单行滚动

**See also:** 
[[#IsAutoWrapEnabled|IsAutoWrapEnabled]], [[#SetMaxCharacters|SetMaxCharacters]]


---

### EnableTruncation {#EnableTruncation}

```
void EnableTruncation ( boolean enabled )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

启用或禁用文本截断功能。

**Use Cases:**

- 限制文本显示长度，超出部分截断
- 防止UI文本溢出容器

**See also:** 
[[#IsTruncationEnabled|IsTruncationEnabled]], [[#SetMaxCharacters|SetMaxCharacters]]


---

### GetAlignment {#GetAlignment}

```
DrawStringAlignment GetAlignment ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取当前设置的文本对齐方式。

**Use Cases:**

- 检查绘制使用的对齐模式
- 条件渲染逻辑中判断对齐

**See also:** 
[[#SetAlignment|SetAlignment]]


---

### GetLineHeightModifier {#GetLineHeightModifier}

```
float GetLineHeightModifier ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取当前行高修改值。

**Use Cases:**

- 查看当前行距调节比例

**See also:** 
[[#SetLineHeightModifier|SetLineHeightModifier]]


---

### GetMaxCharacters {#GetMaxCharacters}

```
int GetMaxCharacters ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

获取当前设置的最大显示字符数。

**Use Cases:**

- 检查文本长度限制

**See also:** 
[[#SetMaxCharacters|SetMaxCharacters]]


---

### GetMissingCharacterOverride {#GetMissingCharacterOverride}

```
int GetMissingCharacterOverride ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取当字体缺失某个字符时使用的替代字符编码。

**Use Cases:**

- 查看当前后备字符设置

**See also:** 
[[#SetMissingCharacterOverride|SetMissingCharacterOverride]]


---

### IsAutoWrapEnabled {#IsAutoWrapEnabled}

```
boolean IsAutoWrapEnabled ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

判断自动换行是否启用。

**Use Cases:**

- 根据换行状态决定渲染逻辑

**See also:** 
[[#EnableAutoWrap|EnableAutoWrap]]


---

### IsTruncationEnabled {#IsTruncationEnabled}

```
boolean IsTruncationEnabled ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

判断文本截断是否启用。

**Use Cases:**

- 根据截断状态调整UI行为

**See also:** 
[[#EnableTruncation|EnableTruncation]]


---

### SetAlignment {#SetAlignment}

```
void SetAlignment ( DrawStringAlignment alignment )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置文本在绘制区域内的水平对齐方式。

**Use Cases:**

- 实现文本居中、左对齐或右对齐
- 通过代码动态改变标题排列

**See also:** 
[[#GetAlignment|GetAlignment]]


---

### SetLineHeightModifier {#SetLineHeightModifier}

```
void SetLineHeightModifier ( float value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置行高乘数，调整多行文本的行间距。

**Use Cases:**

- 压缩行距显示密集文本
- 增大行距提高可读性

**See also:** 
[[#GetLineHeightModifier|GetLineHeightModifier]]


---

### SetMaxCharacters {#SetMaxCharacters}

```
void SetMaxCharacters ( int maxChars )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

设置绘制文本时允许的最大字符数。

**Use Cases:**

- 限制文本显示长度，防止越界
- 截断过长的玩家名称或信息

**See also:** 
[[#GetMaxCharacters|GetMaxCharacters]], [[#EnableTruncation|EnableTruncation]]


---

### SetMissingCharacterOverride {#SetMissingCharacterOverride}

```
void SetMissingCharacterOverride ( int character )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

指定当字体缺少所需字符时使用的默认字符，该设置会覆盖 Font 级别的缺失字符设置。

Sets the default character used when a character that needs to be rendered is missing. This overrides previous [Font:SetMissingCharacter()](Font.md#setmissingcharacter) settings.

**Use Cases:**

- 为特定文本显示替代字符
- 统一替换缺失字符为'?'或方块

**See also:** 
[[#GetMissingCharacterOverride|GetMissingCharacterOverride]]


---

## See Also

- [[Font]]
