---
title: EntityPtr
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 3
---

# EntityPtr

## Summary

A safe wrapper for holding a reference to an Entity that automatically becomes nil when the entity is destroyed, preventing crashes and unexpected behavior from dangling pointers.

## Related Types

- [[Entity]]

## Key Methods

- [[#EntityPtr|EntityPtr]]
- [[#SetReference|SetReference]]
- [[#Ref|Ref]]

## Methods

### Constructors

### EntityPtr {#EntityPtr}

```
const EntityPtr EntityPtr ( Entity )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Constructs a new EntityPtr that safely references the given Entity. The Ref property will be nil when the entity no longer exists.

**Use Cases:**

- Creating a persistent reference to a player for later use
- Storing an NPC reference in a global table
- Initializing a pointer in a component that may outlive the entity

**See also:** 
[[#SetReference|SetReference]], [[#Ref|Ref]]


---

### Functions

### SetReference {#SetReference}

```
void SetReference ( Entity ref )
```

*DLC: REP, REP+ | Modifiers: const*

Reassigns the EntityPtr to point to a different Entity, or to nil to release the reference. Automatically handles cleanup of the previous entity watch.

**Use Cases:**

- Updating a pointer when a new entity of interest spawns
- Resetting a cached entity reference
- Reusing a single EntityPtr across different game stages

**See also:** 
[[#EntityPtr|EntityPtr]], [[#Ref|Ref]]


---

### Ref {#Ref}

```
Entity Ref
```

*DLC: AB+, REP, REP+ | Modifiers: const*

The currently referenced Entity, or nil if the original entity was destroyed. This property is automatically managed by the engine for safety.

**Use Cases:**

- Checking if a stored entity still exists
- Calling methods on the referenced entity after verifying it’s not nil
- Accessing an entity in a delayed event like a timer callback

**See also:** 
[[#EntityPtr|EntityPtr]], [[#SetReference|SetReference]]


---

## See Also

- [[Entity]]
- [[EntityPtr]]
