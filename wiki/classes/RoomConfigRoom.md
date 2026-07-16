---
title: RoomConfigRoom
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 16
---

# RoomConfigRoom

## Summary

RoomConfigRoom provides read-only access to a room's configuration as defined in the room editor, including dimensions, door placements, spawn points, type identifiers, and weighting for procedural generation.

## Related Types

- [[RoomConfigSpawns]]

## Key Methods

- [[#Type|Type]]
- [[#Variant|Variant]]
- [[#Subtype|Subtype]]
- [[#Doors|Doors]]
- [[#Spawns|Spawns]]

## Methods

### Functions

### Difficulty {#Difficulty}

```
const int Difficulty
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the room's difficulty level, typically 5, 10, 15, or 20 for special rooms; 0 means the room cannot appear naturally.

The difficulty of the room, as defined in the room editor. Typically either 5, 10, 15, or 20 for Void rooms, although mods can add rooms with any difficulty. Difficulty 0 means this room cannot show up naturally.

**Use Cases:**

- Filtering rooms by difficulty in custom generation
- Assigning difficulty-based rewards
- Ensuring only challenging rooms appear in end-game floors

**See also:** 
[[#Weight|Weight]], [[#StageID|StageID]], [[#Type|Type]]


---

### Doors {#Doors}

```
const int Doors
```

*DLC: REP, REP+ | Modifiers: const*

Returns a bitmask of valid door positions using the DoorSlotFlag enum, indicating which walls can have doors.

Returns a bit mask of the positions of valid door positions in this room. It is  a combination of bit flags of the DoorSlotFlag enum, which is defined as follows:

**Use Cases:**

- Determining which sides of a room can connect to adjacent rooms
- Preventing invalid door placements in modded rooms
- Custom room shape and connectivity detection

**See also:** 
[[#Shape|Shape]], [[#Width|Width]], [[#Height|Height]]


---

### Height {#Height}

```
const int Height
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Height 完成对应 API 操作

**See also:** 



---

### InitialWeight {#InitialWeight}

```
const float InitialWeight
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 InitialWeight 完成对应 API 操作

**See also:** 



---

### Mode {#Mode}

```
const userdata Mode
```

*DLC: AB+, REP, REP+ | Modifiers: const*

???+ bug "Bug"

???+ bug "Bug"

**Use Cases:**

- 调用 Mode 完成对应 API 操作

**See also:** 



---

### Name {#Name}

```
const string Name
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Name 完成对应 API 操作

**See also:** 



---

### OriginalVariant {#OriginalVariant}

```
int OriginalVariant
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 OriginalVariant 完成对应 API 操作

**See also:** 



---

### Shape {#Shape}

```
const RoomShape Shape
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Shape 完成对应 API 操作

**See also:** 



---

### SpawnCount {#SpawnCount}

```
const int SpawnCount
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SpawnCount 完成对应 API 操作

**See also:** 



---

### Spawns {#Spawns}

```
const RoomConfigSpawns Spawns
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Spawns 完成对应 API 操作

**See also:** 



---

### StageID {#StageID}

```
const int StageID
```

*DLC: AB+, REP, REP+ | Modifiers: const*

The ID of the stage the room was designed for.

The ID of the stage the room was designed for.

**Use Cases:**

- 调用 StageID 完成对应 API 操作

**See also:** 



---

### Subtype {#Subtype}

```
const int Subtype
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Subtype 完成对应 API 操作

**See also:** 



---

### Type {#Type}

```
const RoomType Type
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Type 完成对应 API 操作

**See also:** 



---

### Variant {#Variant}

```
const int Variant
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Variant 完成对应 API 操作

**See also:** 



---

### Weight {#Weight}

```
const float Weight
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 Weight 完成对应 API 操作

**See also:** 



---

### Width {#Width}

```
const int Width
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Width 完成对应 API 操作

**See also:** 



---

## See Also

- [[RoomConfigSpawns]]
