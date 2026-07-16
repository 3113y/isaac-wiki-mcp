---
title: Color
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 14
---

# Color

## Summary

Represents a color with RGBA channels and additional tint, colorize, and offset components for advanced sprite coloring.

## Key Methods

- [[#Color|Color]]
- [[#SetTint|SetTint]]
- [[#SetColorize|SetColorize]]
- [[#SetOffset|SetOffset]]

## Methods

### Constructors

### Color {#Color}

```
Color Color ( float R, float G, float B, float A = 1, float RO = 0, float GO = 0, float BO = 0 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Constructs a new Color instance with red, green, blue, alpha, and optional offset values.

**Use Cases:**

- Creating custom colors for entities or effects
- Setting initial sprite color properties

**See also:** 
[[#SetTint|SetTint]], [[#SetOffset|SetOffset]], [[#SetColorize|SetColorize]], [[#R|R]]


---

### Operators

### __mul {#__mul}

```
Color __mul ( Color right )
```

*DLC: REP, REP+ | Modifiers: const*

Multiplies two Color objects, blending their components using the * operator.

**Use Cases:**

- Combining color filters
- Darkening or tinting a base color

**See also:** 
[[#Color|Color]], [[#Lerp|Lerp]], [[#SetTint|SetTint]]


---

### Functions

### Color.Default {#Color.Default}

```
static Color Lerp ( Color m1, Color m2, float t )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Linearly interpolates between two colors by a progress factor t, returning the intermediate color.

**Use Cases:**

- Smooth color transitions for animations
- Harmless flash effects
- Gradual color changes over time

**See also:** 
[[#Lerp|Lerp]], [[#Color|Color]], [[#__mul|__mul]], [[#SetColorize|SetColorize]]


---

### Reset {#Reset}

```
void Reset ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Resets the color to its default state, likely clearing tint, colorize, and offset.

**Use Cases:**

- Restoring a sprite's original look
- Clearing temporary color modifications

**See also:** 
[[#SetTint|SetTint]], [[#SetColorize|SetColorize]], [[#SetOffset|SetOffset]]


---

### SetColorize {#SetColorize}

```
void SetColorize ( float Red, float Green, float Blue, float Amount )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Sets the colorize effect that grayscales the original, multiplies by given RGB, and blends back, preserving existing color animations.

**Use Cases:**

- Recoloring sprites while keeping creep flashing
- Applying a red, green, or blue shade filter
- Inverting sprite colors

**See also:** 
[[#SetTint|SetTint]], [[#SetOffset|SetOffset]], [[#R|R]], [[#G|G]]


---

### SetOffset {#SetOffset}

```
void SetOffset ( float RedOffset, float GreenOffset, float BlueOffset )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Defines an offset color added to the sprite after the tint is applied.

**Use Cases:**

- Adding a constant color boost
- Simulating ambient lighting effects

**See also:** 
[[#SetTint|SetTint]], [[#SetColorize|SetColorize]], [[#RO|RO]], [[#GO|GO]]


---

### SetTint {#SetTint}

```
void SetTint ( float RedTint, float GreenTint, float BlueTint, float AlphaTint )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Applies a multiplicative tint to the color's RGB and alpha channels.

**Use Cases:**

- Making a sprite semi-transparent
- Shifting the overall color tone

**See also:** 
[[#SetColorize|SetColorize]], [[#SetOffset|SetOffset]], [[#A|A]]


---

### A {#A}

```
float A
```

*DLC: AB+, REP, REP+ | Modifiers: const*

The alpha (transparency) component where 0 is fully transparent and 1 is fully opaque.

Alpha value of the color, where 0 is fully transparent, 1 is fully opaque.

**Use Cases:**

- Fading entities in or out
- Setting partial transparency for effects

**See also:** 
[[#SetTint|SetTint]], [[#Reset|Reset]]


---

### B {#B}

```
float B
```

*DLC: AB+, REP, REP+ | Modifiers: const*

The blue color component value, clamped between 0 and 1.

Blue value of the color. Number between 0 and 1.

**Use Cases:**

- Adjusting blue intensity
- Reading current blue value

**See also:** 
[[#R|R]], [[#G|G]], [[#Color|Color]]


---

### BO {#BO}

```
float BO
```

*DLC: AB+, REP, REP+ | Modifiers: const*

The blue offset value that can be positive or negative, added after tint.

Blue-Offset value of the color. Number can be positive or negative.

**Use Cases:**

- Fine-tuning blue channel beyond base range
- Correcting overall color balance

**See also:** 
[[#SetOffset|SetOffset]], [[#RO|RO]], [[#GO|GO]]


---

### G {#G}

```
float G
```

*DLC: AB+, REP, REP+ | Modifiers: const*

The green color component value, clamped between 0 and 1.

Green value of the color. Number between 0 and 1.

**Use Cases:**

- Setting green intensity
- Querying current green value

**See also:** 
[[#R|R]], [[#B|B]], [[#Color|Color]]


---

### GO {#GO}

```
float GO
```

*DLC: AB+, REP, REP+ | Modifiers: const*

The green offset value that can be positive or negative, added after tint.

Green-Offset value of the color. Number can be positive or negative.

**Use Cases:**

- Shifting green channel output
- Creating custom color effects

**See also:** 
[[#SetOffset|SetOffset]], [[#RO|RO]], [[#BO|BO]]


---

### R {#R}

```
float R
```

*DLC: AB+, REP, REP+ | Modifiers: static*

The red color component value, clamped between 0 and 1.

Red value of the color. Number between 0 and 1.

**Use Cases:**

- Controlling red intensity
- Retrieving current red value

**See also:** 
[[#G|G]], [[#B|B]], [[#Color|Color]]


---

### RO {#RO}

```
float RO
```

*DLC: AB+, REP, REP+ | Modifiers: const*

The red offset value that can be positive or negative, added after tint.

Red-Offset value of the color. Number can be positive or negative.

**Use Cases:**

- Boosting or reducing red channel
- Combining with other offsets for complex coloring

**See also:** 
[[#SetOffset|SetOffset]], [[#GO|GO]], [[#BO|BO]]


---

## See Also

- [[Color]]
