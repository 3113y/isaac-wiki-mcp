---
title: Sprite
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 44
---

# Sprite

## Summary

The Sprite class manages loading, playing, and rendering of 2D animations from .anm2 files. It supports layers, overlays, frame‑by‑frame control, and visual transformations like flip, rotation, scaling, and color tint.

## Related Types

- [[Color]]
- [[KColor]]
- [[Vector]]

## Key Methods

- [[#Play|Play]]
- [[#Render|Render]]
- [[#Update|Update]]
- [[#GetAnimation|GetAnimation]]

## Methods

### Constructors

### Sprite {#Sprite}

```
Sprite Sprite ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Creates a new, unloaded Sprite object. It must be loaded with an .anm2 file before it can display anything.

**Use Cases:**

- Initializing a custom sprite for rendering
- Replacing an entity's default sprite

**See also:** 
[[#Load|Load]], [[#Play|Play]], [[#Render|Render]]


---

### Functions

### GetAnimation {#GetAnimation}

```
string GetAnimation ( )
```

*DLC: REP, REP+ | Modifiers: const*

Returns the name of the main animation currently playing on the sprite.

返回当前正在播放的动画的名称.

**Use Cases:**

- Checking what animation is active
- Conditional logic based on animation name

**See also:** 
[[#Play|Play]], [[#SetAnimation|SetAnimation]], [[#IsPlaying|IsPlaying]]


---

### GetDefaultAnimation {#GetDefaultAnimation}

```
string GetDefaultAnimation ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the default animation name set in the loaded .anm2 file.

从当前加载的 anm2 文件中返回 `DefaultAnimation` 的值.

**Use Cases:**

- Retrieving the fallback animation
- Resetting to default after a custom animation

**See also:** 
[[#Load|Load]], [[#Play|Play]]


---

### GetDefaultAnimationName {#GetDefaultAnimationName}

```
string GetDefaultAnimationName ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

An alias for GetDefaultAnimation; returns the default animation name from the .anm2 file.

从当前加载的 anm2 文件中返回 `DefaultAnimation` 的值.

**Use Cases:**

- Same as GetDefaultAnimation

**See also:** 
[[#GetDefaultAnimation|GetDefaultAnimation]], [[#Load|Load]]


---

### GetFilename {#GetFilename}

```
string GetFilename ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the file path of the currently loaded .anm2 file.

返回精灵上加载的 anm2 文件的路径.

**Use Cases:**

- Verifying which spritesheet is loaded
- Debugging or conditional file checks

**See also:** 
[[#Load|Load]], [[#Reload|Reload]]


---

### GetFrame {#GetFrame}

```
int GetFrame ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns the current frame number of the main animation.

返回当前正在渲染的动画的帧序号.

**Use Cases:**

- Checking animation progress
- Triggering effects when a specific frame is reached

**See also:** 
[[#SetFrame|SetFrame]], [[#Update|Update]], [[#IsFinished|IsFinished]]


---

### GetLayerCount {#GetLayerCount}

```
int GetLayerCount ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the number of layers defined in the loaded .anm2 file; all animations use the same count.

返回精灵上加载的 anm2 文件中的图层数量。所有动画使用相同数量的图层.

**Use Cases:**

- Iterating over layers manually
- Checking available layers before replacement

**See also:** 
[[#ReplaceSpritesheet|ReplaceSpritesheet]], [[#LoadGraphics|LoadGraphics]], [[#RenderLayer|RenderLayer]]


---

### GetOverlayAnimation {#GetOverlayAnimation}

```
string GetOverlayAnimation ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the name of the currently playing overlay animation.

返回当前播放的叠加动画的名称。（叠加动画是可以与正常动画同时播放的独立次要动画。）

**Use Cases:**

- Checking overlay state
- Coordinating main and overlay animations

**See also:** 
[[#PlayOverlay|PlayOverlay]], [[#SetOverlayAnimation|SetOverlayAnimation]], [[#IsOverlayPlaying|IsOverlayPlaying]]


---

### GetOverlayFrame {#GetOverlayFrame}

```
int GetOverlayFrame ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the current frame number of the overlay animation.

返回当前正在渲染的叠加动画的帧编号。（叠加动画是可以与正常动画同时播放的独立次要动画。）

**Use Cases:**

- Precisely timing overlay effects
- Coordinating overlay with main animation

**See also:** 
[[#SetOverlayFrame|SetOverlayFrame]], [[#PlayOverlay|PlayOverlay]], [[#IsOverlayFinished|IsOverlayFinished]]


---

### GetTexel {#GetTexel}

```
KColor GetTexel ( Vector SamplePos, Vector RenderPos, float AlphaThreshold, int LayerID = 0 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Samples the pixel color at a given position, useful for reading a rendered sprite's pixel data.

返回精灵在给定采样位置的像素颜色。RenderPos 可以忽略并设置为零向量

**Use Cases:**

- Collision or interaction based on sprite color
- Creating special effects that read the underlying sprite

**See also:** 
[[#Render|Render]], [[#SetFrame|SetFrame]]


---

### IsEventTriggered {#IsEventTriggered}

```
boolean IsEventTriggered ( string EventName )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns whether a named event is currently triggering in the animation (true only during the frame it triggers).

如果动画中指定的事件当前正在触发，则返回 true.

**Use Cases:**

- Detecting animation events (e.g., projectiles, footsteps)
- Synchronising sound or game logic with animation events

**See also:** 
[[#WasEventTriggered|WasEventTriggered]], [[#Update|Update]]


---

### IsFinished {#IsFinished}

```
boolean IsFinished ( string AnimationName )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns true if the named animation has finished playing.

**Use Cases:**

- Checking if a specific animation completed
- Transitioning to a new animation when finished

**See also:** 
[[#Play|Play]], [[#SetAnimation|SetAnimation]], [[#Update|Update]]


---

### boolean IsFinished ( ) {#boolean IsFinished ( )}

```
boolean IsLoaded ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns true if the last call to Sprite:Load() completed successfully.

如果使用Sprite:Load()加载的动画加载成功了，则为true

**Use Cases:**

- Verifying file loading before playing
- Handling missing .anm2 files gracefully

**See also:** 
[[#IsLoaded|IsLoaded]], [[#Load|Load]], [[#Play|Play]], [[#Render|Render]]


---

### IsOverlayFinished {#IsOverlayFinished}

```
boolean IsOverlayFinished ( string AnimationName )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns true if the named overlay animation has finished playing.

**Use Cases:**

- Determining when to remove an overlay effect
- Chaining overlay animations

**See also:** 
[[#PlayOverlay|PlayOverlay]], [[#SetOverlayAnimation|SetOverlayAnimation]], [[#RemoveOverlay|RemoveOverlay]]


---

### boolean IsOverlayFinished ( ) {#boolean IsOverlayFinished ( )}

```
boolean IsOverlayPlaying ( string AnimationName )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns true if the named overlay animation is currently playing.

**Use Cases:**

- Checking overlay status without hardcoding
- Conditionally playing a different overlay

**See also:** 
[[#IsOverlayPlaying|IsOverlayPlaying]], [[#PlayOverlay|PlayOverlay]], [[#GetOverlayAnimation|GetOverlayAnimation]], [[#SetOverlayAnimation|SetOverlayAnimation]]


---

### boolean IsOverlayPlaying ( ) {#boolean IsOverlayPlaying ( )}

```
boolean IsPlaying ( string AnimationName )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns true if the named main animation is currently playing.

**Use Cases:**

- Checking if a specific animation is active
- Conditionally changing spritesheet or graphics

**See also:** 
[[#IsPlaying|IsPlaying]], [[#Play|Play]], [[#GetAnimation|GetAnimation]], [[#SetAnimation|SetAnimation]]


---

### boolean IsPlaying ( ) {#boolean IsPlaying ( )}

```
void Load ( string ANM2Path, boolean LoadGraphics )
```

*DLC: AB+, REP, REP+*

Loads an .anm2 file from the given path, optionally loading its graphics immediately.

加载给定的 anm2 文件。每个精灵必须加载一个 anm2 文件才能显示任何内容.

**Use Cases:**

- Initialising a new sprite with animations
- Switching between different animation sets at runtime

**See also:** 
[[#Load|Load]], [[#IsLoaded|IsLoaded]], [[#LoadGraphics|LoadGraphics]], [[#Reload|Reload]]


---

### LoadGraphics {#LoadGraphics}

```
void LoadGraphics ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Manually loads the PNG graphics referenced by the .anm2 file. Necessary when graphics loading was deferred.

用于加载精灵的 anm2 中指定的 PNG 文件。通常，只有在之前向`Sprite.Load`方法的`loadGraphics`参数传递了 `false`，或者调用了`Sprite.ReplaceSpritesheet`方法时，才会调用此方法.

**Use Cases:**

- Loading graphics after replacing a spritesheet
- Optimising by calling later to avoid load at creation

**See also:** 
[[#ReplaceSpritesheet|ReplaceSpritesheet]], [[#Load|Load]]


---

### Play {#Play}

```
void Play ( string AnimationName, boolean Force )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Starts playing the specified main animation from frame 0, with an optional force flag to interrupt any current animation.

开始执行给定的动画，从第 0 帧开始。调用此方法后，必须在每个更新帧上调用`Sprite.Update`方法（如果要在渲染回调中更新动画，请确保仅在偶数帧上运行），以便将动画推进到下一帧。（通常，您还会使用`Sprite.IsFinished`方法检查动画是否完成。）

**Use Cases:**

- Triggering an animation (e.g., attack, idle)
- Resetting animation state

**See also:** 
[[#Update|Update]], [[#IsPlaying|IsPlaying]], [[#IsFinished|IsFinished]], [[#SetAnimation|SetAnimation]]


---

### PlayOverlay {#PlayOverlay}

```
void PlayOverlay ( string AnimationName, boolean Force )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Starts playing the specified overlay animation from frame 0, with an optional force flag.

开始执行给定的叠加动画，从第 0 帧开始。（叠加动画是可以与正常动画同时播放的独立次要动画。）调用此方法后，必须在每个更新帧上调用Sprite.Update方法（如果要在渲染回调中更新动画，请确保仅在偶数帧上运行），以便将动画推进到下一帧。（通常，您还会使用Sprite.IsOverlayFinished方法检查动画是否完成。）

**Use Cases:**

- Adding a secondary effect (e.g., tears, shield overlay)
- Playing HUD overlays on top of base animation

**See also:** 
[[#IsOverlayFinished|IsOverlayFinished]], [[#IsOverlayPlaying|IsOverlayPlaying]], [[#RemoveOverlay|RemoveOverlay]]


---

### PlayRandom {#PlayRandom}

```
void PlayRandom ( int Seed )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Plays a random animation from the loaded .anm2 file using the given seed.

从当前加载的 anm2 文件中播放随机动画.

**Use Cases:**

- Randomizing idle or reaction animations
- Creating varied visual feedback

**See also:** 
[[#Play|Play]], [[#GetAnimation|GetAnimation]]


---

### Reload {#Reload}

```
void Reload ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Reloads the currently loaded .anm2 file, discarding all runtime changes.

重新加载anm2文件

**Use Cases:**

- Resetting to original spritesheet
- Applying changes after hot‑reloading graphics

**See also:** 
[[#Load|Load]], [[#LoadGraphics|LoadGraphics]]


---

### RemoveOverlay {#RemoveOverlay}

```
void RemoveOverlay ( )
```

*DLC: AB+, REP, REP+*

Stops and removes the currently playing overlay animation.

取消执行给定的叠加动画

**Use Cases:**

- Hiding an overlay effect when no longer needed
- Resetting overlay state

**See also:** 
[[#PlayOverlay|PlayOverlay]], [[#IsOverlayPlaying|IsOverlayPlaying]], [[#IsOverlayFinished|IsOverlayFinished]]


---

### Render {#Render}

```
void Render ( Vector Position, Vector Vector TopLeftClamp = Vector.Zero, Vector BottomRightClamp = Vector.Zero )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Draws the sprite at a screen position, with optional clamping for cropping.

在给定的屏幕位置渲染精灵对象，其中 (0, 0) 是屏幕的左上角。

**Use Cases:**

- Rendering sprites in a render callback
- Clipping large sprites to fit a UI area

**See also:** 
[[#Update|Update]], [[#Load|Load]], [[#RenderLayer|RenderLayer]]


---

### RenderLayer {#RenderLayer}

```
void RenderLayer ( int LayerId, Vector Position, Vector TopLeftClamp = Vector.Zero, Vector BottomRightClamp = Vector.Zero )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Draws a single layer of the sprite at a screen position, ignoring other layers.

在给定的屏幕位置渲染精灵的特定图层，其中 (0,0) 是屏幕的左上角。

**Use Cases:**

- Rendering only a specific element (e.g., body, overlay)
- Compositing custom visual effects

**See also:** 
[[#GetLayerCount|GetLayerCount]], [[#ReplaceSpritesheet|ReplaceSpritesheet]]


---

### ReplaceSpritesheet {#ReplaceSpritesheet}

```
void ReplaceSpritesheet ( int LayerId, string PngFilename )
```

*DLC: AB+, REP | Modifiers: const*

Replaces the PNG spritesheet for a specific layer without changing other layers. Graphics must be reloaded afterwards.

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- Skinning individual parts of a sprite
- Dynamic texture swapping for modded entities

**See also:** 
[[#LoadGraphics|LoadGraphics]], [[#Load|Load]], [[#GetLayerCount|GetLayerCount]]


---

### boolean ReplaceSpritesheet ( int LayerId, string PngFilename ) {#boolean ReplaceSpritesheet ( int LayerId, string PngFilename )}

```
void Reset ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Resets the sprite to a default state (details depend on implementation).

**Use Cases:**

- Re‑initialising a sprite after heavy modifications

**See also:** 
[[#Reset|Reset]], [[#Load|Load]], [[#Reload|Reload]]


---

### SetAnimation {#SetAnimation}

```
boolean SetAnimation ( string AnimationName, boolean Reset = true )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Selects the given main animation without starting playback from frame 0; can optionally reset to frame 0.

**Use Cases:**

- Switching animations while preserving frame position (when Reset=false)
- Changing direction animations smoothly

**See also:** 
[[#Play|Play]], [[#GetAnimation|GetAnimation]], [[#IsPlaying|IsPlaying]]


---

### SetFrame {#SetFrame}

```
void SetFrame ( int FrameNum )
```

*DLC: REP, REP+ | Modifiers: const*

Jumps the main animation to a specific frame number, without playing it.

**Use Cases:**

- Creating static sprites or icons
- Setting a specific frame for a non‑animated sprite

**See also:** 
[[#GetFrame|GetFrame]], [[#SetLastFrame|SetLastFrame]], [[#Update|Update]]


---

### void SetFrame ( string AnimationName, int FrameNum ) {#void SetFrame ( string AnimationName, int FrameNum )}

```
void SetLastFrame ( )
```

*DLC: AB+, REP, REP+*

Switches to the named animation and jumps to a specific frame in one call.

**Use Cases:**

- Instantly showing a particular animation frame
- Starting a new animation at a custom point

**See also:** 
[[#SetFrame|SetFrame]], [[#SetAnimation|SetAnimation]], [[#Play|Play]]


---

### SetLayerFrame {#SetLayerFrame}

```
void SetLayerFrame ( int LayerId, int FrameNum )
```

*DLC: AB+, REP, REP+*

Sets the frame of a specific layer independently.

**Use Cases:**

- Animating individual layers separately
- Fixing a layer while the rest animates

**See also:** 
[[#RenderLayer|RenderLayer]], [[#GetLayerCount|GetLayerCount]]


---

### SetOverlayAnimation {#SetOverlayAnimation}

```
boolean SetOverlayAnimation ( string AnimationName, bool Reset = true )
```

*DLC: AB+, REP, REP+*

Selects the given overlay animation without forcing playback from frame 0; can optionally preserve the current frame.

**Use Cases:**

- Smoothly switching overlay animations
- Keeping overlay in sync with main animation

**See also:** 
[[#PlayOverlay|PlayOverlay]], [[#GetOverlayAnimation|GetOverlayAnimation]], [[#SetOverlayFrame|SetOverlayFrame]]


---

### SetOverlayFrame {#SetOverlayFrame}

```
void SetOverlayFrame ( string AnimationName, int FrameNum )
```

*DLC: AB+, REP, REP+*

Jumps the overlay animation to a specific frame.

**Use Cases:**

- Positioning overlay precisely
- Creating static overlays

**See also:** 
[[#GetOverlayFrame|GetOverlayFrame]], [[#SetOverlayAnimation|SetOverlayAnimation]]


---

### SetOverlayRenderPriority {#SetOverlayRenderPriority}

```
void SetOverlayRenderPriority ( boolean RenderFirst )
```

*DLC: AB+, REP, REP+*

Determines whether the overlay is rendered before or after the main sprite.

**Use Cases:**

- Layering effects (e.g., behind or in front of the main sprite)

**See also:** 
[[#Render|Render]], [[#RenderLayer|RenderLayer]]


---

### Stop {#Stop}

```
void Stop ( )
```

*DLC: AB+, REP, REP+*

Stops the main animation immediately.

**Use Cases:**

- Halting an animation when an entity dies or disappears
- Pausing animation logic

**See also:** 
[[#Play|Play]], [[#SetAnimation|SetAnimation]], [[#Update|Update]]


---

### Update {#Update}

```
void Update ( )
```

*DLC: AB+, REP, REP+*

Advances the main and overlay animations by one frame. Must be called each render/update cycle.

**Use Cases:**

- Driving animation playback every frame
- Ensuring sprite animations progress

**See also:** 
[[#Render|Render]], [[#Play|Play]], [[#IsFinished|IsFinished]]


---

### WasEventTriggered {#WasEventTriggered}

```
boolean WasEventTriggered ( string EventName )
```

*DLC: AB+, REP, REP+*

Returns true if the named event was triggered at any point during the current animation loop.

如果动画中指定的事件在某个时刻被触发，则返回 true，并在动画停止播放前保持为 true.

**Use Cases:**

- Detecting past animation events even if missed in real‑time
- Triggering game logic after the event has passed

**See also:** 
[[#IsEventTriggered|IsEventTriggered]], [[#Play|Play]], [[#Update|Update]]


---

### Color {#Color}

```
Color Color
```

*DLC: AB+, REP, REP+*

Modulates the sprite's colour; can be used to tint, brighten, or darken the whole sprite.

**Use Cases:**

- Adding dynamic colour effects (damage flash, poison)
- Setting a fixed colour for UI sprites

**See also:** 
[[#Render|Render]], [[#Update|Update]]


---

### FlipX {#FlipX}

```
boolean FlipX
```

*DLC: AB+, REP, REP+*

Flips the sprite horizontally when rendering.

**Use Cases:**

- Facing a character left or right
- Mirroring effects

**See also:** 
[[#Render|Render]], [[#SetFrame|SetFrame]]


---

### FlipY {#FlipY}

```
boolean FlipY
```

*DLC: AB+, REP, REP+*

Flips the sprite vertically when rendering.

**Use Cases:**

- Upside‑down effects, reflected sprites

**See also:** 
[[#Render|Render]]


---

### Offset {#Offset}

```
Vector Offset
```

*DLC: AB+, REP, REP+*

Offsets the sprite’s render position, separate from the position argument in Render.

**Use Cases:**

- Fine‑tuning sprite placement without changing render coordinates
- Making sprites float slightly above/below the intended point

**See also:** 
[[#Render|Render]]


---

### PlaybackSpeed {#PlaybackSpeed}

```
float PlaybackSpeed
```

*DLC: AB+, REP, REP+*

Multiplier for animation speed; 1.0 is normal speed.

**Use Cases:**

- Slowing down or speeding up animations
- Matching animation speed to gameplay pace

**See also:** 
[[#Update|Update]]


---

### Rotation {#Rotation}

```
float Rotation
```

*DLC: AB+, REP, REP+*

Rotation angle in degrees applied to the sprite when rendering.

**Use Cases:**

- Rotating sprites for weapons or spinning effects
- Turning a sprite to match aim direction

**See also:** 
[[#Render|Render]]


---

### Scale {#Scale}

```
Vector Scale
```

*DLC: AB+, REP, REP+*

2‑dimensional scaling factor for the sprite’s width and height.

**Use Cases:**

- Resizing sprites for UI or effect size changes
- Stretching sprites for distortion effects

**See also:** 
[[#Render|Render]]


---

## See Also

- [[Color]]
- [[KColor]]
- [[Sprite]]
- [[Vector]]
