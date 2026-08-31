---
tags:
  - Globals
  - Class
---
# Class "Color"

???+ info
    This class can be accessed by using its constructor or the following function:

    * [Entity.Color](Entity.md#color)
    * [Entity.SplatColor](Entity.md#splatcolor)
    * [EntityPlayer.LaserColor](EntityPlayer.md#lasercolor)
    * [EntityPlayer.TearColor](EntityPlayer.md#tearcolor)
    * [ProjectileParams.Color](ProjectileParams.md#color)
    * [Sprite.Color](Sprite.md#color)
    * [TearParams.TearColor](TearParams.md#tearcolor)

    ???+ example "Example Code"
        ```lua
        local myRedColor = Color(1,0,0,1)
        ```

## Constructors

### Color () {: aria-label='Constructors' }
[ ](#){: .reporplus .tooltip .badge }
#### [Color](Color.md) Color ( float R, float G, float B, float A = 1, float RO = 0, float GO = 0, float BO = 0 ) {: .copyable aria-label='Constructors' }

Constructor for the "Color" class.

When using the [Font](Font.md) class, use [KColor()](KColor.md) instead.

Colors are made of three separate components, tint, colorize and offset. Tint acts like a color multiplicator. Offset is a color which is added after the tint is applied. Colorize is complicated. See the `:::lua SetColorize()` function for a detailed description.

R, G, B, A, RO, GO and BO accept numbers between 0 and 1.
___
## Operators

<div class="rgon-extension" markdown="1">

### Color () {: aria-label='Modified Constructors' }
#### [Color](Color.md) Color ( float R = 1, float G = 1, float B = 1, float A = 1, float RO = 0, float GO = 0, float BO = 0, float RC = 0, float GC = 0, float BC = 0, float AC = 0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Constructors' }
所有参数现在均为可选参数，也可以通过构造函数设置 `Colorize`。

___

</div>

### __mul () {: aria-label='Operators' }
[ ](#){: .alldlc .tooltip .badge }
#### [Color](Color.md) __mul ( [Color](Color.md) right ) {: .copyable aria-label='Operators' }

Defines the multiplication of two [Color](Color.md) objects using the `*` operator.
___
## Constants

### Color.Default {: aria-label='Constants' }
[ ](#){: .reporplus .tooltip .badge }

Equivalent to `:::lua Color(1, 1, 1, 1)`, the color white.
___
## Functions

### Lerp () {: aria-label='Functions' }
[ ](#){: .static .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### static [Color](Color.md) Lerp ( [Color](Color.md) m1, [Color](Color.md) m2, float t ) {: .copyable aria-label='Functions' }

Linear Interpolation between two colors. `:::lua t` is the "progress" of the interpolation. Setting `:::lua t = 0.5` means that the color in the middle of m1 and m2 will be returned.
___

### Reset () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Reset ( ) {: .copyable aria-label='Functions' }

___

### Set·Colorize () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetColorize ( float Red, float Green, float Blue, float Amount ) {: .copyable aria-label='Functions' }

The colorize function can be used to change the color of sprites. Its the best for that purpose, since it does not affect existing coloranimations like the flashing of creep.

The values can be between 0 and 1 for normal coloration. if you use higher numbers the color gets more vibrant.

???- note "Notes"
    The alpha component determines how much colorization must be applied. The function takes the original color, converts it to grayscale, multiplies it by the RGB components and then blends it back with the original color. The alpha value determines the blending factor.
    Colorization is applied after the tint and before the offset function.

???- example "Example Code"
    - `:::lua SetColorize(1, 1, 1, 1)` will turn the sprite into grayscale.
    - `:::lua SetColorize(1, 0, 0, 1)` will turn it red but not as a red tint but as shades of red.
    - `:::lua SetColorize(1, 1, 1, 2)` will invert the sprite without touching its luminosity.

    This code changes the color of red Creep to be purple
    ```lua
    mod:AddCallback(ModCallbacks.MC_POST_EFFECT_INIT, function(_, effect)
      if effect.Variant == EffectVariant.CREEP_RED then
        local color = Color(1, 1, 1, 1, 0, 0, 0)
        color:SetColorize(4, 0, 4, 1)
        local sprite = effect:GetSprite()
        sprite.Color = color
      end
    end)
    ```

___

### Set·Offset () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetOffset ( float RedOffset, float GreenOffset, float BlueOffset ) {: .copyable aria-label='Functions' }

Offset is a color that gets added to the sprite after the Tint was applied.
___

### Set·Tint () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetTint ( float RedTint, float GreenTint, float BlueTint, float AlphaTint ) {: .copyable aria-label='Functions' }

Tint acts like a color multiplicator.
___
## Variables

### A {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float A  {: .copyable aria-label='Variables' }
Alpha value of the color, where 0 is fully transparent, 1 is fully opaque.
___

### B {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float B  {: .copyable aria-label='Variables' }
Blue value of the color. Number between 0 and 1.
___

### BO {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float BO  {: .copyable aria-label='Variables' }
Blue-Offset value of the color. Number can be positive or negative.

___

### G {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float G  {: .copyable aria-label='Variables' }
Green value of the color. Number between 0 and 1.

___

### GO {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float GO  {: .copyable aria-label='Variables' }
Green-Offset value of the color. Number can be positive or negative.

___

### R {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float R  {: .copyable aria-label='Variables' }
Red value of the color. Number between 0 and 1.

___

### RO {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float RO  {: .copyable aria-label='Variables' }
Red-Offset value of the color. Number can be positive or negative.

<div class="rgon-only" markdown="1">

### GetColorize () {: aria-label='Functions' }
#### table GetColorize ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个表格，其中包含颜色当前的 Colorize 值：`{R, G, B, A}`

___

### GetOffset () {: aria-label='Functions' }
#### table GetOffset ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个表格，其中包含颜色当前的 Offset 值：`{R, G, B}`
虽然 [Color](https://wofsauge.github.io/IsaacDocs/rep/Color.html) 类已提供用于此目的的 [.RO](https://wofsauge.github.io/IsaacDocs/rep/Color.html#ro)、[.GO](https://wofsauge.github.io/IsaacDocs/rep/Color.html#go) 和 [.BO](https://wofsauge.github.io/IsaacDocs/rep/Color.html#bo) 变量，但在需要访问全部三个值时，实测 GetOffset() 的速度快约 30%，因此建议在这种情况下使用它。访问两个变量时，性能几乎相同；访问一个变量时，性能反而更差。只需一个或两个偏移值时，请继续使用这些变量。

___

### GetTint () {: aria-label='Functions' }
#### table GetTint ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回一个表格，其中包含颜色当前的 Tint 值：`{R, G, B, A}`

___

### Print () {: aria-label='Functions' }
#### string Print ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
返回颜色对象的字符串表示形式。

___

### __tostring () {: aria-label='Functions' }
#### string __tostring ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Operators' }
创建颜色对象的字符串表示形式，因此可以直接使用 `print(myColorObj)` 打印对象。

___
## Constants

### 译者注
下方常量用于将实体、激光或泪弹修改为相应道具的颜色。

例如，`Color.LaserAlmond` 是拥有道具“杏仁奶”时激光所使用的颜色。

如需查找其他颜色，请先前往[以撒 Wiki](https://isaac.huijiwiki.com/wiki/) 查询道具的英文名称，再在本页面搜索。

___

### Color.EmberFade {: aria-label='Constants' }
#### [Color](Color.md) EmberFade [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for enemies like Crackles and Coal Spiders. This color has a hardcoded special property; gibs start orange and fade into grey.

???- info "Info"

    Color of (0, 0, 0, 1.1)

    Colorize of (0, 0, 0, 0)

    Offset of (1, 0.514, 0.004)

___

### Color.LaserAlmond {: aria-label='Constants' }
#### [Color](Color.md) LaserAlmond [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for lasers with the Almond Milk effect.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (5.6, 5.2, 3.8, 1)

    Offset of (0, 0, 0)

___

### Color.LaserChocolate {: aria-label='Constants' }
#### [Color](Color.md) LaserChocolate [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for lasers with the Chocolate Milk effect.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (3, 1.7, 1.7, 1)

    Offset of (0, 0, 0)

___

### Color.LaserCoal {: aria-label='Constants' }
#### [Color](Color.md) LaserCoal [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for lasers with the A Lump of Coal effect.

???- info "Info"

    Color of (3, 3, 3, 1)

    Colorize of (1.3, 1.2, 1.2, 1)

    Offset of (-0.5, -0.5, -0.5)

___

### Color.LaserFireMind {: aria-label='Constants' }
#### [Color](Color.md) LaserFireMind [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for lasers fired by players with Fire Mind.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (5, 3, 1, 1)

    Offset of (0, 0, 0)

___

### Color.LaserHoming {: aria-label='Constants' }
#### [Color](Color.md) LaserHoming [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for homing lasers.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (3, 1, 3.5, 0)

    Offset of (0, 0, 0)

___

### Color.LaserIpecac {: aria-label='Constants' }
#### [Color](Color.md) LaserIpecac [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for lasers with the Ipecac effect.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (1.8, 3, 1, 1)

    Offset of (0, 0, 0)

___

### Color.LaserMother {: aria-label='Constants' }
#### [Color](Color.md) LaserMother [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for Mother's mega laser.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (2, 2.2, 1, 1)

    Offset of (0, 0, 0)

___

### Color.LaserNumberOne {: aria-label='Constants' }
#### [Color](Color.md) LaserNumberOne [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for lasers fired by players with Number One.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (5, 4.9, 1, 1)

    Offset of (0, 0, 0)

___

### Color.LaserSoy {: aria-label='Constants' }
#### [Color](Color.md) LaserSoy [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for lasers with the Soy Milk effect.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (5.6, 5, 4.2, 1)

    Offset of (0, 0, 0)

___

### Color.LaserPoison {: aria-label='Constants' }
#### [Color](Color.md) LaserPoison [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for poisonous lasers fired by players with items like Scorpio or Common Cold.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (1.8, 4, 1, 1)

    Offset of (0, 0, 0)

___

### Color.ProjectileCageBlue {: aria-label='Constants' }
#### [Color](Color.md) ProjectileCageBlue [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for `ProjectileVariant.PROJECTILE_PUKE`s fired by The Cage.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0.8, 1, 0.85, 1)

    Offset of (0, 0, 0)

___

### Color.ProjectileCorpseClusterDark {: aria-label='Constants' }
#### [Color](Color.md) ProjectileCorpseClusterDark [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for clustered `ProjectileVariant.PROJECTILE_NORMAL`s fired in Corpse by enemies like Mother.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0.63, 0.85, 0.32, 0)

    Offset of (0, 0, 0)

___

### Color.ProjectileCorpseClusterLight {: aria-label='Constants' }
#### [Color](Color.md) ProjectileCorpseClusterLight [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for clustered `ProjectileVariant.PROJECTILE_NORMAL`s fired in Corpse by enemies like Mother.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0.63, 0.85, 0.32, 0)

    Offset of (0, 0, 0)

___

### Color.ProjectileCorpseGreen {: aria-label='Constants' }
#### [Color](Color.md) ProjectileCorpseGreen [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for green `ProjectileVariant.PROJECTILE_NORMAL`s fired in Corpse by enemies like Mother.

Also used for the green laser fired by Chimera.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (1.5, 2, 1, 1)

    Offset of (0, 0, 0)

___

### Color.ProjectileCorpsePink {: aria-label='Constants' }
#### [Color](Color.md) ProjectileCorpsePink [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for pink-ish white-ish `ProjectileVariant.PROJECTILE_NORMAL`s fired in Corpse by enemies like Mother.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (4, 3.5, 3.2, 1)

    Offset of (0, 0, 0)

___

### Color.ProjectileCorpseWhite {: aria-label='Constants' }
#### [Color](Color.md) ProjectileCorpseWhite [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for white-ish grey-ish `ProjectileVariant.PROJECTILE_NORMAL`s fired in Corpse by enemies like Mother.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (2.7, 3, 2, 1)

    Offset of (0, 0, 0)

___

### Color.ProjectileCorpseYellow {: aria-label='Constants' }
#### [Color](Color.md) ProjectileCorpseYellow [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for yellow `ProjectileVariant.PROJECTILE_NORMAL`s fired in Corpse by enemies like The Scourge.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (3.5, 2.5, 1, 1)

    Offset of (0, 0, 0)

___

### Color.ProjectileFireWave {: aria-label='Constants' }
#### [Color](Color.md) ProjectileFireWave [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for fire-pillar-wave-spawning `ProjectileVariant.PROJECTILE_NORMAL`s fired by enemies like Crackle.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (1, 0.3, 0)

___

### Color.ProjectileHoming {: aria-label='Constants' }
#### [Color](Color.md) ProjectileHoming [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for homing `ProjectileVariant.PROJECTILE_NORMAL`s fired by enemies like Psychic Maw.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0.8, 0.15, 1, 1)

    Offset of (0.26, 0.05, 0.4)

___

### Color.ProjectileHushBlue {: aria-label='Constants' }
#### [Color](Color.md) ProjectileHushBlue [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for blue `ProjectileVariant.PROJECTILE_HUSH`s fired by Hush.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0, 0.2, 0.4)

___

### Color.ProjectileHushGreen {: aria-label='Constants' }
#### [Color](Color.md) ProjectileHushGreen [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for blue `ProjectileVariant.PROJECTILE_HUSH`s fired by Hush.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0.2, 0.2, 0)

___

### Color.ProjectileHushYellow {: aria-label='Constants' }
#### [Color](Color.md) ProjectileHushYellow [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for blue `ProjectileVariant.PROJECTILE_HUSH`s fired by Hush.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0.4, 0.2, 0)

___

### Color.ProjectileIpecac {: aria-label='Constants' }
#### [Color](Color.md) ProjectileIpecac [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for explosive `ProjectileVariant.PROJECTILE_NORMAL`s fired by enemies like Gurgles.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0.4, 2, 0.5, 1)

    Offset of (0, 0, 0)

___

### Color.ProjectileMegaSatanBlack {: aria-label='Constants' }
#### [Color](Color.md) ProjectileMegaSatanBlack [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for black `ProjectileVariant.PROJECTILE_NORMAL`s fired by Mega Satan.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0.6, 0.6, 0.6, 1)

    Offset of (0, 0, 0)

___

### Color.ProjectileMegaSatanWhite {: aria-label='Constants' }
#### [Color](Color.md) ProjectileMegaSatanWhite [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for white `ProjectileVariant.PROJECTILE_NORMAL`s fired by Mega Satan.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (2, 2, 2, 1)

    Offset of (0, 0, 0)

___

### Color.ProjectileSoy {: aria-label='Constants' }
#### [Color](Color.md) ProjectileSoy [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for soy `ProjectileVariant.PROJECTILE_NORMAL`s fired by enemies like Soy Creep.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (1, 1, 1, 1)

    Offset of (0.8, 0.7, 0.5)

___

### Color.ProjectileTar {: aria-label='Constants' }
#### [Color](Color.md) ProjectileTar [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for tar `ProjectileVariant.PROJECTILE_NORMAL`s fired by enemies like Clot.

???- info "Info"

    Color of (1, 1, 1, 1)

    Colorize of (0.5, 0.5, 0.5, 1)

    Offset of (0, 0, 0)

___

### Color.TearAlmond {: aria-label='Constants' }
#### [Color](Color.md) TearAlmond [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for tears fired by players with Soy Milk.

???- info "Info"

    Color of (1.8, 1.7, 1, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0, 0, 0)

___

### Color.TearChocolate {: aria-label='Constants' }
#### [Color](Color.md) TearChocolate [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for tears fired by players with Chocolate Milk.

???- info "Info"

    Color of (0.33, 0.18, 0.18, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0.258824, 0.156863, 0.156863)

___

### Color.TearCoal {: aria-label='Constants' }
#### [Color](Color.md) TearCoal [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for tears fired by players with A Lump of Coal.

???- info "Info"

    Color of (0.2, 0.09, 0.065, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0, 0, 0)

___

### Color.TearCommonCold {: aria-label='Constants' }
#### [Color](Color.md) TearCommonCold [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for poison tears fired by players with Common Cold.

???- info "Info"

    Color of (0.4, 0.97, 0.5, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0, 0, 0)

___

### Color.TearHoming {: aria-label='Constants' }
#### [Color](Color.md) TearHoming [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for homing tears fired by players with Spoon Bender.

???- info "Info"

    Color of (0.4, 0.15, 0.38, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0.278431, 0, 0.454902)

___

### Color.TearIpecac {: aria-label='Constants' }
#### [Color](Color.md) TearIpecac [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for explosive tears fired by players with Ipecac.

???- info "Info"

    Color of (0.5, 0.9, 0.4, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0, 0, 0)

___

### Color.TearNumberOne {: aria-label='Constants' }
#### [Color](Color.md) TearNumberOne [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for tears fired by players with Number One.

???- info "Info"

    Color of (1, 1, 0, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0.176471, 0.0588235, 0)

___

### Color.TearScorpio {: aria-label='Constants' }
#### [Color](Color.md) TearScorpio [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for poison tears fired by players with Scorpio.

???- info "Info"

    Color of (0.196078, 1, 0.196078, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0, 0, 0)

___

### Color.TearSerpentsKiss {: aria-label='Constants' }
#### [Color](Color.md) TearSerpentsKiss [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for poison tears fired by players with Serpent's Kiss.

???- info "Info"

    Color of (0.5, 0.97, 0.5, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0, 0, 0)

___

### Color.TearSoy {: aria-label='Constants' }
#### [Color](Color.md) TearSoy [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for tears fired by players with Soy Milk.

???- info "Info"

    Color of (1.5, 2, 2, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (0, 0, 0)

___

### Color.TearTar {: aria-label='Constants' }
#### [Color](Color.md) TearTar [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Constants' }
Used for tar tears fired by familiars like Little Gish.

???- info "Info"

    Color of (0.95, 0.8, 0.6, 1)

    Colorize of (0, 0, 0, 0)

    Offset of (-0.588235, -0.588235, -0.588235)

___
> 文档说明已由受约束的语言模型统一润色；API 事实与签名仍保留上游来源。

</div>
