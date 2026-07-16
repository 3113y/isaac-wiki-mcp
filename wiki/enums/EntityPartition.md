---
tags:
  - Enum
---
# Enum "EntityPartition"

???+ tip "Bitset Calculator"
    [](#)

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|1 << 0 |FAMILIAR  |  |
|[ ](#)|1 << 1 |BULLET  |  |
|[ ](#)|1 << 2 |TEAR  |  |
|[ ](#)|1 << 3 |ENEMY  |  |
|[ ](#)|1 << 4 |PICKUP  |  |
|[ ](#)|1 << 5 |PLAYER  |  |
|[ ](#)|1 << 6 |EFFECT  | Effects are only returned by [Isaac.FindInRadius](../Isaac.md#findinradius) if its [EntityCollisionClass](./EntityCollisionClass.md) is NOT set to `ENTCOLL_NONE`! |
