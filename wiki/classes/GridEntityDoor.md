---
title: GridEntityDoor
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 30
---

# GridEntityDoor

## Summary

表示游戏中的门网格实体，负责管理门的开闭、锁定、动画、目标房间类型以及与钥匙、炸弹的交互。

## Inheritance

- Inherits from: [[GridEntity]]

## Related Types

- [[Entity]]
- [[EntityPlayer]]
- [[Room]]
- [[Sprite]]
- [[Vector]]

## Key Methods

- [[#Open|Open]]
- [[#Close|Close]]
- [[#TryUnlock|TryUnlock]]
- [[#TryBlowOpen|TryBlowOpen]]
- [[#SetLocked|SetLocked]]

## Methods

### Functions

### Bar {#Bar}

```
void Bar ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Bar 完成对应 API 操作

**See also:** 



---

### CanBlowOpen {#CanBlowOpen}

```
boolean CanBlowOpen ( )
```

*DLC: REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 CanBlowOpen 完成对应 API 操作

**See also:** 



---

### Close {#Close}

```
void Close ( boolean Force )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Close 完成对应 API 操作

**See also:** 



---

### GetSpriteOffset {#GetSpriteOffset}

```
const Vector GetSpriteOffset ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetSpriteOffset 完成对应 API 操作

**See also:** 



---

### IsBusted {#IsBusted}

```
boolean IsBusted ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 IsBusted 完成对应 API 操作

**See also:** 



---

### IsKeyFamiliarTarget {#IsKeyFamiliarTarget}

```
boolean IsKeyFamiliarTarget ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 IsKeyFamiliarTarget 完成对应 API 操作

**See also:** 



---

### IsLocked {#IsLocked}

```
boolean IsLocked ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 IsLocked 完成对应 API 操作

**See also:** 



---

### IsOpen {#IsOpen}

```
boolean IsOpen ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 IsOpen 完成对应 API 操作

**See also:** 



---

### IsRoomType {#IsRoomType}

```
boolean IsRoomType ( RoomType Type )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 IsRoomType 完成对应 API 操作

**See also:** 



---

### IsTargetRoomArcade {#IsTargetRoomArcade}

```
boolean IsTargetRoomArcade ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 IsTargetRoomArcade 完成对应 API 操作

**See also:** 



---

### Open {#Open}

```
void Open ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Open 完成对应 API 操作

**See also:** 



---

### SetLocked {#SetLocked}

```
void SetLocked ( boolean Locked )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SetLocked 完成对应 API 操作

**See also:** 



---

### SetRoomTypes {#SetRoomTypes}

```
void SetRoomTypes ( RoomType CurrentRoomType, RoomType TargetRoomType )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 SetRoomTypes 完成对应 API 操作

**See also:** 



---

### SpawnDust {#SpawnDust}

```
void SpawnDust ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SpawnDust 完成对应 API 操作

**See also:** 



---

### TryBlowOpen {#TryBlowOpen}

```
boolean TryBlowOpen ( boolean FromExplosion, Entity source )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

try to open the door by explosive force, true for success

try to open the door by explosive force, true for success

**Use Cases:**

- 调用 TryBlowOpen 完成对应 API 操作

**See also:** 



---

### TryUnlock {#TryUnlock}

```
boolean TryUnlock (EntityPlayer player, boolean Force )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

try to unlock the door using a key, true for success

try to unlock the door using a key, true for success

**Use Cases:**

- 调用 TryUnlock 完成对应 API 操作

**See also:** 



---

### Busted {#Busted}

```
boolean Busted
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Busted 完成对应 API 操作

**See also:** 



---

### CloseAnimation {#CloseAnimation}

```
string CloseAnimation
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 CloseAnimation 完成对应 API 操作

**See also:** 



---

### CurrentRoomType {#CurrentRoomType}

```
RoomType CurrentRoomType
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 CurrentRoomType 完成对应 API 操作

**See also:** 



---

### Direction {#Direction}

```
Direction Direction
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Direction 完成对应 API 操作

**See also:** 



---

### ExtraSprite {#ExtraSprite}

```
Sprite ExtraSprite
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Additional sprite used for the door. Examples for extra sprites are: bars, chains, wooden boards, etc.

Additional sprite used for the door. Examples for extra sprites are: bars, chains, wooden boards, etc.

**Use Cases:**

- 调用 ExtraSprite 完成对应 API 操作

**See also:** 



---

### ExtraVisible {#ExtraVisible}

```
boolean ExtraVisible
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Toggles the visibility of the extra sprite. Examples for extra sprites are: bars, chains, wooden boards, etc.

Toggles the visibility of the extra sprite. Examples for extra sprites are: bars, chains, wooden boards, etc.

**Use Cases:**

- 调用 ExtraVisible 完成对应 API 操作

**See also:** 



---

### LockedAnimation {#LockedAnimation}

```
string LockedAnimation
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 LockedAnimation 完成对应 API 操作

**See also:** 



---

### OpenAnimation {#OpenAnimation}

```
string OpenAnimation
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 OpenAnimation 完成对应 API 操作

**See also:** 



---

### OpenLockedAnimation {#OpenLockedAnimation}

```
string OpenLockedAnimation
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 OpenLockedAnimation 完成对应 API 操作

**See also:** 



---

### PreviousState {#PreviousState}

```
int PreviousState
```

*DLC: AB+, REP | Modifiers: const*

???+ bug "Bug"

???+ bug "Bug"

**Use Cases:**

- 调用 PreviousState 完成对应 API 操作

**See also:** 



---

### PreviousVariant {#PreviousVariant}

```
int PreviousVariant
```

*DLC: AB+, REP, REP+ | Modifiers: static*

???+ bug "Bug"

???+ bug "Bug"

**Use Cases:**

- 调用 PreviousVariant 完成对应 API 操作

**See also:** 



---

### Slot {#Slot}

```
DoorSlot Slot
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Slot 完成对应 API 操作

**See also:** 



---

### TargetRoomIndex {#TargetRoomIndex}

```
int TargetRoomIndex
```

*DLC: REP, REP+ | Modifiers: const*

Note: this value only affects the room transition animation and does not actually change the target room.

Note: this value only affects the room transition animation and does not actually change the target room.

**Use Cases:**

- 调用 TargetRoomIndex 完成对应 API 操作

**See also:** 



---

### TargetRoomType {#TargetRoomType}

```
RoomType TargetRoomType
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 TargetRoomType 完成对应 API 操作

**See also:** 



---

## See Also

- [[Entity]]
- [[EntityPlayer]]
- [[GridEntity]]
- [[Room]]
- [[Sprite]]
- [[Vector]]
