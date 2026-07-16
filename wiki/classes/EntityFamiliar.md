---
title: EntityFamiliar
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 39
---

# EntityFamiliar

## Summary

Represents a familiar entity that can follow the player, orbit, shoot tears, collect pickups, and be managed as part of follower/delayed/orbit groups. Provides controls for movement, targeting, animation, and state.

## Inheritance

- Inherits from: [[Entity]]

## Related Types

- [[EntityPlayer]]
- [[EntityTear]]
- [[Vector]]

## Key Methods

- [[#Shoot|Shoot]]
- [[#AddToOrbit|AddToOrbit]]
- [[#AddToFollowers|AddToFollowers]]
- [[#FireProjectile|FireProjectile]]
- [[#PickEnemyTarget|PickEnemyTarget]]

## Methods

### Functions

### AddCoins {#AddCoins}

```
void AddCoins ( int Value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Increases the familiar's coin count.

**Use Cases:**

- Accumulating coins for coin-based familiars
- Custom pickup management

**See also:** 
[[#Coins|Coins]]


---

### AddHearts {#AddHearts}

```
void AddHearts ( int Hearts )
```

*DLC: REP, REP+ | Modifiers: const*

Increases the familiar's heart count.

**Use Cases:**

- Healing or health-based familiar mechanics
- Custom health pickup simulation

**See also:** 
[[#Hearts|Hearts]]


---

### AddKeys {#AddKeys}

```
void AddKeys ( int Keys )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Increases the familiar's key count.

**Use Cases:**

- Key-based familiar behaviors
- Simulating key collection

**See also:** 
[[#Keys|Keys]]


---

### AddToDelayed {#AddToDelayed}

```
void AddToDelayed ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Adds the familiar to the delayed movement set without removing other flags, enabling delayed follow behavior.

Adds to delayed. This doesn't remove other flags!

**Use Cases:**

- Enabling delayed movement like Tractor Beam effect
- Layering movement states

**See also:** 
[[#RemoveFromDelayed|RemoveFromDelayed]], [[#MoveDelayed|MoveDelayed]], [[#IsDelayed|IsDelayed]]


---

### AddToFollowers {#AddToFollowers}

```
void AddToFollowers ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Adds the familiar to the followers group, making it a normal follower without clearing other flags.

Adds to followers. This doesn't remove other flags!

**Use Cases:**

- Setting a familiar as a standard follower
- Re‑enabling follower status after orbital or delayed use

**See also:** 
[[#RemoveFromFollowers|RemoveFromFollowers]], [[#IsFollower|IsFollower]], [[#FollowParent|FollowParent]]


---

### AddToOrbit {#AddToOrbit}

```
void AddToOrbit ( int Layer )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Adds the familiar to an orbital layer, setting it to orbit the player without removing other flags.

Adds to orbitals. This doesn't remove other flags!

**Use Cases:**

- Converting a familiar into an orbital
- Stacking orbitals in specific layers

**See also:** 
[[#RemoveFromOrbit|RemoveFromOrbit]], [[#OrbitLayer|OrbitLayer]], [[#GetOrbitPosition|GetOrbitPosition]], [[#RecalculateOrbitOffset|RecalculateOrbitOffset]]


---

### FireProjectile {#FireProjectile}

```
EntityTear FireProjectile ( Vector Dir )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Shoots a regular tear from the familiar's center in the given direction. Returns the leftmost projectile; does not play shoot animation or use special attacks.

**Use Cases:**

- Custom projectile attacks
- Testing basic tear firing without side effects

**See also:** 
[[#Shoot|Shoot]], [[#PlayShootAnim|PlayShootAnim]]


---

### FollowParent {#FollowParent}

```
void FollowParent ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Makes the familiar follow its parent (player) like a default follower.

**Use Cases:**

- Restoring normal following behavior
- Initializing follower movement

**See also:** 
[[#FollowPosition|FollowPosition]], [[#AddToFollowers|AddToFollowers]]


---

### FollowPosition {#FollowPosition}

```
void FollowPosition ( Vector Pos )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Moves the familiar towards a specific world position.

**Use Cases:**

- Custom movement patterns
- Teleporting or repositioning a familiar

**See also:** 
[[#FollowParent|FollowParent]], [[#MoveDiagonally|MoveDiagonally]]


---

### GetOrbitDistance {#GetOrbitDistance}

```
static Vector GetOrbitDistance ( int Layer )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Static method returning the default orbit distance vector for a given orbital layer.

**Use Cases:**

- Getting baseline orbit dimensions
- Orbit calculations without an instance

**See also:** 
[[#OrbitDistance|OrbitDistance]], [[#AddToOrbit|AddToOrbit]], [[#GetOrbitPosition|GetOrbitPosition]]


---

### GetOrbitPosition {#GetOrbitPosition}

```
Vector GetOrbitPosition ( Vector Pos )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns the world position of an orbiting familiar relative to the player, with an offset.

**Use Cases:**

- Drawing custom orbital effects
- Precise orbital targeting

**See also:** 
[[#AddToOrbit|AddToOrbit]], [[#OrbitDistance|OrbitDistance]]


---

### MoveDelayed {#MoveDelayed}

```
void MoveDelayed ( int NumFrames )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Incrementally moves the familiar in its delayed state over a number of frames.

**Use Cases:**

- Smooth delayed repositioning
- Controlling Tractor Beam-like movement

**See also:** 
[[#AddToDelayed|AddToDelayed]], [[#RemoveFromDelayed|RemoveFromDelayed]]


---

### MoveDiagonally {#MoveDiagonally}

```
void MoveDiagonally ( float Speed )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Moves the familiar diagonally at a given speed.

**Use Cases:**

- Custom movement patterns
- Evasive or attack maneuvers

**See also:** 
[[#FollowPosition|FollowPosition]], [[#FollowParent|FollowParent]]


---

### PickEnemyTarget {#PickEnemyTarget}

```
void PickEnemyTarget ( float MaxDistance, int FrameInterval = 13, int Flags = 0, Vector ConeDir = Vector.Zero, float ConeAngle = 15 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Selects an enemy target based on distance, interval, and optional flags/cone constraints. Can prioritize switching, HP, or owner proximity.

**Flags**: A combination of the following flags (none of these are set by default)

**Use Cases:**

- Advanced familiar AI targeting
- Cone‑based attack logic

**See also:** 
[[#FireProjectile|FireProjectile]], [[#Shoot|Shoot]]


---

### PlayChargeAnim {#PlayChargeAnim}

```
void PlayChargeAnim ( Direction Dir )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Plays the charge animation in the specified direction.

**Use Cases:**

- Custom charging attack visuals
- Synchronizing animation with mechanics

**See also:** 
[[#PlayShootAnim|PlayShootAnim]], [[#Shoot|Shoot]]


---

### PlayFloatAnim {#PlayFloatAnim}

```
void PlayFloatAnim ( Direction Dir )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Plays the float (idle/movement) animation in the specified direction.

**Use Cases:**

- Custom idle or floating animations
- State‑based visual feedback

**See also:** 
[[#PlayChargeAnim|PlayChargeAnim]], [[#PlayShootAnim|PlayShootAnim]]


---

### PlayShootAnim {#PlayShootAnim}

```
void PlayShootAnim ( Direction Dir )
```

*DLC: AB+, REP, REP+*

Plays the shoot animation in the specified direction.

**Use Cases:**

- Triggering shoot visuals manually
- Cosmetic familiar customization

**See also:** 
[[#Shoot|Shoot]], [[#FireProjectile|FireProjectile]]


---

### RecalculateOrbitOffset {#RecalculateOrbitOffset}

```
int RecalculateOrbitOffset ( int Layer, boolean Add )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Recalculates the orbital offset for a given layer, optionally adding the familiar to it. Returns the total number of familiars in that layer.

Returns the number of familiars in that layer.

**Use Cases:**

- Adjusting orbital spacing dynamically
- Managing layered orbital groups

**See also:** 
[[#AddToOrbit|AddToOrbit]], [[#RemoveFromOrbit|RemoveFromOrbit]], [[#OrbitLayer|OrbitLayer]]


---

### RemoveFromDelayed {#RemoveFromDelayed}

```
void RemoveFromDelayed ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Removes the familiar from the delayed movement set.

**Use Cases:**

- Disabling delayed behavior
- Switching movement modes

**See also:** 
[[#AddToDelayed|AddToDelayed]], [[#IsDelayed|IsDelayed]]


---

### RemoveFromFollowers {#RemoveFromFollowers}

```
void RemoveFromFollowers ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Removes the familiar from the followers list.

**Use Cases:**

- Temporarily detaching a follower
- Switching to orbital or other state

**See also:** 
[[#AddToFollowers|AddToFollowers]], [[#IsFollower|IsFollower]]


---

### RemoveFromOrbit {#RemoveFromOrbit}

```
void RemoveFromOrbit ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Removes the familiar from its orbital layer.

**Use Cases:**

- Taking an orbital out of orbit
- Switching to follower mode

**See also:** 
[[#AddToOrbit|AddToOrbit]], [[#OrbitLayer|OrbitLayer]]


---

### Shoot {#Shoot}

```
void Shoot ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Handles the complete shooting routine for a basic shooting familiar: animations, tear firing, and synergy processing. Recommended for custom familiars in POST_FAMILIAR_UPDATE.

When called in POST_FAMILIAR_UPDATE on a custom familiar, appears to handle everything for a basic shooting familiar. This includes handling animations, firing tears, and synergies.

**Use Cases:**

- Implementing a standard shooting familiar
- Centralizing shoot logic with automatic synergy support

**See also:** 
[[#FireProjectile|FireProjectile]], [[#PlayShootAnim|PlayShootAnim]], [[#FireCooldown|FireCooldown]]


---

### Coins {#Coins}

```
int Coins
```

*DLC: AB+, REP, REP+*

Variable: Current coin count of the familiar.

**Use Cases:**

- Reading/modifying coin amount for coin-based familiar logic
- Custom pickup display

**See also:** 
[[#AddCoins|AddCoins]]


---

### FireCooldown {#FireCooldown}

```
int FireCooldown
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Variable: Cooldown timer before the familiar can shoot again.

**Use Cases:**

- Adjusting fire rate
- Synchronizing custom shoot logic

**See also:** 
[[#Shoot|Shoot]], [[#FireProjectile|FireProjectile]]


---

### HeadFrameDelay {#HeadFrameDelay}

```
int HeadFrameDelay
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Variable: Frame delay for the familiar's head animation.

**Use Cases:**

- Custom animation timing
- Head‑based familiar behavior

**See also:** 



---

### Hearts {#Hearts}

```
int Hearts
```

*DLC: AB+, REP | Modifiers: const*

Variable: Current heart count of the familiar.

**Use Cases:**

- Health‑based familiar mechanics
- Custom heart pickup tracking

**See also:** 
[[#AddHearts|AddHearts]]


---

### IsDelayed {#IsDelayed}

```
boolean IsDelayed
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Variable: Whether the familiar is in the delayed movement set.

**Use Cases:**

- Checking movement state
- Conditional behavior based on delayed status

**See also:** 
[[#AddToDelayed|AddToDelayed]], [[#RemoveFromDelayed|RemoveFromDelayed]]


---

### IsFollower {#IsFollower}

```
boolean IsFollower
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Variable: Whether the familiar is currently registered as a follower.

**Use Cases:**

- State queries for follower‑only logic
- Determining if the familiar follows the player

**See also:** 
[[#AddToFollowers|AddToFollowers]], [[#RemoveFromFollowers|RemoveFromFollowers]]


---

### Keys {#Keys}

```
int Keys
```

*DLC: REP, REP+ | Modifiers: const*

Variable: Current key count of the familiar.

**Use Cases:**

- Key‑based familiar interactions
- Tracking key pickups

**See also:** 
[[#AddKeys|AddKeys]]


---

### LastDirection {#LastDirection}

```
Direction LastDirection
```

*DLC: AB+, REP, REP+*

Variable: The last movement direction of the familiar.

**Use Cases:**

- Storing previous direction for animation or AI
- Detecting direction changes

**See also:** 
[[#MoveDirection|MoveDirection]]


---

### MoveDirection {#MoveDirection}

```
Direction MoveDirection
```

*DLC: AB+, REP, REP+*

Variable: The current movement direction of the familiar.

**Use Cases:**

- Reading active movement vector
- Custom controller input mapping

**See also:** 
[[#LastDirection|LastDirection]]


---

### OrbitAngleOffset {#OrbitAngleOffset}

```
float OrbitAngleOffset
```

*DLC: AB+, REP, REP+*

Variable: Angular offset for the familiar on its orbit, allowing manual repositioning along the orbital path.

**Use Cases:**

- Creating tight orbital walls
- Custom orbital arrangements

**See also:** 
[[#AddToOrbit|AddToOrbit]], [[#GetOrbitPosition|GetOrbitPosition]]


---

### OrbitDistance {#OrbitDistance}

```
Vector OrbitDistance
```

*DLC: AB+, REP, REP+*

Variable: Defines the orbit dimensions as a Vector (width, height) when the familiar is an orbital.

**Use Cases:**

- Setting custom orbital shapes
- Dynamic orbit resizing

**See also:** 
[[#AddToOrbit|AddToOrbit]], [[#GetOrbitDistance|GetOrbitDistance]]


---

### OrbitLayer {#OrbitLayer}

```
int OrbitLayer
```

*DLC: AB+, REP, REP+*

Variable: The orbital layer index (‑1 if not an orbital). Set by AddToOrbit.

**Use Cases:**

- Identifying orbital layer
- Layer‑based filtering

**See also:** 
[[#AddToOrbit|AddToOrbit]], [[#RemoveFromOrbit|RemoveFromOrbit]], [[#RecalculateOrbitOffset|RecalculateOrbitOffset]]


---

### OrbitSpeed {#OrbitSpeed}

```
float OrbitSpeed
```

*DLC: AB+, REP, REP+*

Variable: Speed at which the familiar moves along its orbit.

**Use Cases:**

- Adjusting orbital rotation speed
- Creating custom orbit dynamics

**See also:** 
[[#AddToOrbit|AddToOrbit]]


---

### Player {#Player}

```
EntityPlayer Player
```

*DLC: AB+, REP, REP+*

Variable: Reference to the EntityPlayer that owns this familiar.

**Use Cases:**

- Accessing player stats for familiar syncing
- Checking owner properties

**See also:** 
[[#FollowParent|FollowParent]]


---

### RoomClearCount {#RoomClearCount}

```
int RoomClearCount
```

*DLC: AB+, REP, REP+*

Variable: Tracks the number of room clears, possibly related to familiar progression.

**Use Cases:**

- Unlocking behaviors after certain clears
- Room‑clear‑dependent logic

**See also:** 



---

### ShootDirection {#ShootDirection}

```
Direction ShootDirection
```

*DLC: AB+, REP, REP+*

Variable: The direction in which the familiar is shooting.

**Use Cases:**

- Reading current shoot aim
- Aligning visual effects with shoot direction

**See also:** 
[[#Shoot|Shoot]], [[#FireProjectile|FireProjectile]]


---

### State {#State}

```
int State
```

*DLC: AB+, REP, REP+*

Variable: The AI state integer, used to control familiar behavior stages.

**Use Cases:**

- Custom state machines for familiars
- Synchronizing behavior with state

**See also:** 
[[#Shoot|Shoot]]


---

## See Also

- [[Entity]]
- [[EntityPlayer]]
- [[EntityTear]]
- [[Vector]]
