---
title: Vector
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 25
---

# Vector

## Summary

Vector 类表示二维向量，提供构造、基本算术运算（加减乘除、取反）、长度与方向计算、线性插值、归范化、旋转、限制以及静态工厂方法等，是位置、速度、方向等建模的核心工具。

## Key Methods

- [[#Vector|Vector]]
- [[#__mul|__mul]]
- [[#Length|Length]]

## Methods

### Constructors

### Vector {#Vector}

```
Vector Vector ( float , float )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

构造函数，创建一个具有指定 X 和 Y 分量的向量。

**Use Cases:**

- 创建自定义向量
- 初始化位置

**See also:** 
[[#X|X]], [[#Y|Y]]


---

### Operators

### __div {#__div}

```
Vector __div ( float Modifier )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

除法运算符，将向量各分量除以一个标量，返回缩放后的新向量。

Defines the Division of a Vector object and a float divisor(Modifier) using the `/` operator.

**Use Cases:**

- 精细缩放
- 平均速度

**See also:** 
[[#__mul|__mul]], [[#Resized|Resized]]


---

### __mul {#__mul}

```
Vector __mul ( float Modifier )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

乘法运算符（标量版），将向量各分量乘以一个浮点数，返回缩放后的新向量。

[ ](#){: .alldlc .tooltip .badge }

**Use Cases:**

- 速度缩放
- 距离延伸

**See also:** 
[[#__div|__div]], [[#Resized|Resized]]


---

### __unm {#__unm}

```
Vector __unm ( Vector Right )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

取反运算符，返回各分量取负的新向量。

Defines the inversion of a Vector object using the `-` operator.

**Use Cases:**

- 反向移动
- 镜像方向

**See also:** 
[[#__mul|__mul]], [[#Rotated|Rotated]]


---

### __tostring {#__tostring}

```
void __tostring ( )
```

*DLC: AB+, REP, REP+*

[Vector](Vector.md) objects can be cast to a string object, which returns information about this object in the following format:

[Vector](Vector.md) objects can be cast to a string object, which returns information about this object in the following format:

**Use Cases:**

- 调用 __tostring 完成对应 API 操作

**See also:** 



---

### Functions

### Vector.Zero {#Vector.Zero}

```
Vector __add ( Vector Right )
```

*DLC: REP, REP+ | Modifiers: const*

加法运算符，返回两个向量对应分量相加的新向量。

Defines the Addition of two Vector objects using the `+` operator.

**Use Cases:**

- 位移叠加
- 合成速度

**See also:** 
[[#__add|__add]], [[#__sub|__sub]], [[#__mul|__mul]]


---

### [Vector](Vector.md) __mul ( [Vector](Vector.md) Modifier ) {#[Vector](Vector.md) __mul ( [Vector](Vector.md) Modifier )}

```
Vector __sub ( Vector Right )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

减法运算符，返回两个向量对应分量相减的新向量。

Defines the Subtraction of two Vector objects using the `-` operator.

**Use Cases:**

- 计算相对位移
- 方向向量

**See also:** 
[[#__sub|__sub]], [[#__add|__add]], [[#Distance|Distance]]


---

### Clamp {#Clamp}

```
void Clamp ( float MinX, float MinY, float MaxX, float MaxY )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将自身分量限制在指定矩形范围内（破坏性修改），不保持原方向。

Clamps the vector based on left, top, right, bottom boundings. Doesn't keep direction

**Use Cases:**

- 边界约束
- 防止越界

**See also:** 
[[#Clamped|Clamped]], [[#Resize|Resize]]


---

### Clamped {#Clamped}

```
Vector Clamped ( float MinX, float MinY, float MaxX, float MaxY )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回一个分量被限制在指定矩形范围内的新向量，原向量不变。

Returns a clamped version of the vector.

**Use Cases:**

- 安全获取受限位置
- 路径约束

**See also:** 
[[#Clamp|Clamp]], [[#Normalized|Normalized]]


---

### Cross {#Cross}

```
float Cross ( Vector second )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

计算与另一向量的叉积（二维行列式），表示垂直向量的大小与方向。

Cross product this is the 2x2 matrix determinant or the resulting z value for their 3D versions with z=0

**Use Cases:**

- 判断相对方位
- 面积计算

**See also:** 
[[#Dot|Dot]], [[#GetAngleDegrees|GetAngleDegrees]]


---

### Distance {#Distance}

```
float Distance ( Vector first, Vector second )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回与另一向量的欧几里得距离。

Returns distance between two vectors

**Use Cases:**

- 碰撞检测
- 距离判断

**See also:** 
[[#DistanceSquared|DistanceSquared]], [[#Length|Length]]


---

### DistanceSquared {#DistanceSquared}

```
float DistanceSquared ( Vector first, Vector second )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回与另一向量距离的平方，避免开方运算，适合比较大小。

Returns squared distance between two vectors

**Use Cases:**

- 性能优化的距离比较
- 范围检测

**See also:** 
[[#Distance|Distance]], [[#LengthSquared|LengthSquared]]


---

### Dot {#Dot}

```
float Dot ( Vector second )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

计算与另一向量的点积，反映投影和夹角余弦。

Dot product

**Use Cases:**

- 判断朝向相似度
- 投影长度

**See also:** 
[[#Cross|Cross]], [[#GetAngleDegrees|GetAngleDegrees]]


---

### FromAngle {#FromAngle}

```
static Vector FromAngle ( float AngleDegrees )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

静态工厂方法，根据角度（度）创建一个归一化的方向向量。

Build a [Vector](Vector.md) from an angle, returns a normalized vector. Angle 0 will result in (1, 0). Angle 90 will result in (0, 1).

**Use Cases:**

- 生成指向
- 弹幕发射

**See also:** 
[[#Rotated|Rotated]], [[#GetAngleDegrees|GetAngleDegrees]]


---

### GetAngleDegrees {#GetAngleDegrees}

```
float GetAngleDegrees ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回该向量在游戏坐标系下的方向角度（度）。

**Use Cases:**

- 获取朝向
- 角度差计算

**See also:** 
[[#FromAngle|FromAngle]], [[#Rotated|Rotated]]


---

### Length {#Length}

```
float Length ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回向量长度（模）。

Returns the length of the vector

**Use Cases:**

- 速度大小
- 距离获取

**See also:** 
[[#LengthSquared|LengthSquared]], [[#Normalize|Normalize]]


---

### LengthSquared {#LengthSquared}

```
float LengthSquared ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回长度平方，避免开方，用于性能敏感的比较。

Returns the length squared of the vector

**Use Cases:**

- 快速长度比较
- 阈值检测

**See also:** 
[[#Length|Length]], [[#DistanceSquared|DistanceSquared]]


---

### Lerp {#Lerp}

```
Vector Lerp ( Vector first, Vector second, float t )
```

*DLC: AB+, REP, REP+*

在两个向量之间按比例 t 进行线性插值，返回插值后的新向量。

**Use Cases:**

- 平滑移动
- 位置过渡

**See also:** 
[[#__add|__add]], [[#__mul|__mul]]


---

### Normalize {#Normalize}

```
void Normalize ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将自身归一化（长度变为1），破坏性修改。

Normalizes this vector, effectively making its length equal 1.

**Use Cases:**

- 直接转向单位向量
- 方向标准化

**See also:** 
[[#Normalized|Normalized]], [[#Resize|Resize]]


---

### Normalized {#Normalized}

```
Vector Normalized ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

返回一个方向相同但长度为1的新向量，原向量不变。

Returns a normalized version of this vector, effectively making its length equal 1.

**Use Cases:**

- 获取方向单位向量
- 方向标准化

**See also:** 
[[#Normalize|Normalize]], [[#Resized|Resized]]


---

### Resize {#Resize}

```
void Resize ( float NewLength )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Resizes the vector length.

Resizes the vector length.

**Use Cases:**

- 调用 Resize 完成对应 API 操作

**See also:** 



---

### Resized {#Resized}

```
Vector Resized ( float NewLength )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns a resized version of the vector.

Returns a resized version of the vector.

**Use Cases:**

- 调用 Resized 完成对应 API 操作

**See also:** 



---

### Rotated {#Rotated}

```
Vector Rotated ( float AngleDegrees )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Returns a rotated version of the vector by AngleDegrees

Returns a rotated version of the vector by AngleDegrees

**Use Cases:**

- 调用 Rotated 完成对应 API 操作

**See also:** 



---

### X {#X}

```
float X
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Components of vector.

Components of vector.

**Use Cases:**

- 调用 X 完成对应 API 操作

**See also:** 



---

### Y {#Y}

```
float Y
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Y 完成对应 API 操作

**See also:** 



---

## See Also

- [[Vector]]
