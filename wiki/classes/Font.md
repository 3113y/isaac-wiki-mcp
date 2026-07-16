---
title: Font
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 14
---

# Font

## Summary

Font 类用于加载自定义字体、在屏幕上绘制各类文本（支持缩放、对齐与 Unicode），并提供字体度量查询和生命周期管理。

## Related Types

- [[FontRenderSettings]]
- [[KColor]]

## Key Methods

- [[#Load|Load]]
- [[#DrawString|DrawString]]
- [[#DrawStringUTF8|DrawStringUTF8]]
- [[#GetStringWidth|GetStringWidth]]

## Methods

### Constructors

### Font {#Font}

```
Font Font ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

构造一个空 Font 对象，供后续调用 Load 加载真正的字体文件。

**Use Cases:**

- 初始化字体实例
- 准备加载自定义字体

**See also:** 
[[#Load|Load]], [[#IsLoaded|IsLoaded]]


---

### Functions

### DrawString {#DrawString}

```
void DrawString ( string String, float PositionX, float PositionY, KColor RenderColor, int BoxWidth = 0, boolean Center = false )
```

*DLC: REP, REP+ | Modifiers: const*

将 UTF8 字符串转换为 UTF16 后绘制在屏幕上，支持通过 BoxWidth 和 Center 实现左对齐、右对齐或居中。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 绘制基础文本
- 实现文字居中或右对齐

**See also:** 
[[#DrawStringUTF8|DrawStringUTF8]], [[#DrawStringScaled|DrawStringScaled]], [[#GetStringWidth|GetStringWidth]]


---

### void DrawString ( string String, float PositionX, float PositionY, float sizeX, float sizeY, [KColor](KColor.md) RenderColor, [FontRenderSettings](FontRenderSettings.md) settings ) {#void DrawString ( string String, float PositionX, float PositionY, float sizeX, float sizeY, [KColor](KColor.md) RenderColor, [FontRenderSettings](FontRenderSettings.md) settings )}

```
void DrawStringScaled ( string String, float PositionX, float PositionY, float ScaleX, float ScaleY, KColor RenderColor, int BoxWidth = 0, boolean Center = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

通过给定尺寸和 FontRenderSettings 设置，将 UTF8 字符串转换为 UTF16 并绘制缩放后的文本。

Converts UTF8 to UTF16, then draws the scaled string on the screen.

**Use Cases:**

- 需要同时控制文字大小和高级渲染效果的场景
- 实现非等比缩放文本

**See also:** 
[[#DrawString|DrawString]], [[#DrawStringScaled|DrawStringScaled]], [[#DrawStringUTF8|DrawStringUTF8]], [[#GetStringWidth|GetStringWidth]]


---

### DrawStringScaledUTF8 {#DrawStringScaledUTF8}

```
void DrawStringScaledUTF8 ( string String, float PositionX, float PositionY, float ScaleX, float ScaleY, KColor RenderColor, int BoxWidth = 0, boolean Center = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

直接绘制缩放后的 Unicode 文本，无需 UTF8 到 UTF16 的中间转换。

Draws a scaled string of Unicode text on the screen.

**Use Cases:**

- 显示原生 Unicode 文本并缩放

**See also:** 
[[#DrawStringUTF8|DrawStringUTF8]], [[#DrawStringScaled|DrawStringScaled]]


---

### DrawStringUTF8 {#DrawStringUTF8}

```
void DrawStringUTF8 ( string String, float PositionX, float PositionY, KColor RenderColor, int BoxWidth = 0, boolean Center = false )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

直接绘制 Unicode 文本，支持 BoxWidth 和 Center 对齐，适合多语言显示。

Draws a string of Unicode text on the screen.

**Use Cases:**

- 绘制含特殊字符的文本
- 国际化 UI 渲染

**See also:** 
[[#DrawString|DrawString]], [[#GetStringWidthUTF8|GetStringWidthUTF8]]


---

### GetBaselineHeight {#GetBaselineHeight}

```
int GetBaselineHeight ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回从行顶部到底部的距离。

Returns the number of pixels from the absolute top of the line to the base of the characters.

**Use Cases:**

- 调用 GetBaselineHeight 完成对应 API 操作

**See also:** 



---

### GetCharacterWidth {#GetCharacterWidth}

```
int GetCharacterWidth ( char Character )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the width of a specific character in pixels.

Returns the width of a specific character in pixels.

**Use Cases:**

- 调用 GetCharacterWidth 完成对应 API 操作

**See also:** 



---

### GetLineHeight {#GetLineHeight}

```
int GetLineHeight ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the distance in pixels between each line of text.

Returns the distance in pixels between each line of text.

**Use Cases:**

- 调用 GetLineHeight 完成对应 API 操作

**See also:** 



---

### GetStringWidth {#GetStringWidth}

```
int GetStringWidth ( string String )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Converts a string from UTF8 to UTF16, and returns the string's width in pixels.

Converts a string from UTF8 to UTF16, and returns the string's width in pixels.

**Use Cases:**

- 调用 GetStringWidth 完成对应 API 操作

**See also:** 



---

### GetStringWidthUTF8 {#GetStringWidthUTF8}

```
int GetStringWidthUTF8 ( string String )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the string width of a Unicode text in pixels.

Returns the string width of a Unicode text in pixels.

**Use Cases:**

- 调用 GetStringWidthUTF8 完成对应 API 操作

**See also:** 



---

### IsLoaded {#IsLoaded}

```
boolean IsLoaded ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns whether a font is loaded or not.

Returns whether a font is loaded or not.

**Use Cases:**

- 调用 IsLoaded 完成对应 API 操作

**See also:** 



---

### Load {#Load}

```
void Load ( string FilePath )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Loads a font. To check that the font actually got loaded, call the [IsLoaded()](#isloaded) method afterwards.

Loads a font. To check that the font actually got loaded, call the [IsLoaded()](#isloaded) method afterwards.

**Use Cases:**

- 调用 Load 完成对应 API 操作

**See also:** 



---

### SetMissingCharacter {#SetMissingCharacter}

```
void SetMissingCharacter ( char MissingCharacter )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Sets the character that will be used when a missing character is encountered by the font.

Sets the character that will be used when a missing character is encountered by the font.

**Use Cases:**

- 调用 SetMissingCharacter 完成对应 API 操作

**See also:** 



---

### Unload {#Unload}

```
void Unload ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Unloads the font from memory.

Unloads the font from memory.

**Use Cases:**

- 调用 Unload 完成对应 API 操作

**See also:** 



---

## See Also

- [[Font]]
- [[FontRenderSettings]]
- [[KColor]]
