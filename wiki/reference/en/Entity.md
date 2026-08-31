---
tags:
  - Class
---
# Class "Entity"

???+ info
    First, see [the tutorial on entities](entities/Overview.md).

    You can get this class by using the following function:

    ???- info "List of all functions that return 'Entity' objects"
        * [EntityList.Get()](CppContainer_EntityList.md#get)
        * [Entity.GetLastChild()](Entity.md#getlastchild)
        * [Entity.GetLastParent()](Entity.md#getlastparent)
        * [Entity.Child](Entity.md#child)
        * [Entity.Parent](Entity.md#parent)
        * [Entity.SpawnerEntity](Entity.md#spawnerentity)
        * [Entity.Target](Entity.md#target)
        * [EntityLaser.BounceLaser()](EntityLaser.md#bouncelaser)
        * [EntityNPC.GetPlayerTarget()](EntityNPC.md#getplayertarget)
        * [EntityNPC.EntityRef](EntityNPC.md#entityref)
        * [EntityPlayer.AddBlueFlies](EntityPlayer.md#addblueflies)
        * [EntityPlayer.AddBlueSpider](EntityPlayer.md#addbluespider)
        * [EntityPlayer.GetActiveWeaponEntity](EntityPlayer.md#getactiveweaponentity)
        * [EntityPlayer.GetNPCTarget](EntityPlayer.md#getnpctarget)
        * [EntityPlayer.GetTractorBeam](EntityPlayer.md#gettractorbeam)
        * [EntityPlayer.ThrowBlueSpider](EntityPlayer.md#throwbluespider)
        * [EntityPlayer.ThrowHeldEntity](EntityPlayer.md#throwheldentity)
        * [EntityPtr](EntityPtr.md#ref)
        * [EntityRef.Entity](EntityRef.md#entity)
        * [EntityTear.StickTarget](EntityTear.md#sticktarget)
        * [Game.Spawn()](Game.md#spawn)
        * [Isaac.Spawn()](Game.md#spawn)

    ???+ example "Example Code"
        `local entity = Isaac.Spawn(EntityType.ENTITY_PICKUP, PickupVariant.PICKUP_COLLECTIBLE, 0, Vector(320,280), Vector(0,0), nil)`

## Class Diagram
--8<-- "en/snippets/EntityClassDiagram.md"

## Functions

### Add·Burn () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### void AddBurn ( [EntityRef](EntityRef.md) Source, int Duration, float Damage ) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void AddBurn ( [EntityRef](EntityRef.md) Source, int Duration, float Damage, boolean IgnoreBosses ) {: .copyable aria-label='Functions' }

Adds a burn effect to an enemy. `Duration` is in number of frames. `Damage` is the damage taken per frame.

???- info "Duration Information"
    `Duration` must be a minimum of 3 frames to deal damage. Every consecutive damage tick is 20 frames apart.

    - 2 damage ticks = 23 frames
    - 3 damage ticks = 43 frames
    - 4 damage ticks = 63 frames

    `Duration` has an upper limit. For an EntityPlayer, its maximum is one interval. For a normal entity, the maximum is 6 intervals.

???- example "Example Code"
    This code damages every entity in the room for 1 second with the damage source set to the player. The total damage dealt is 1.

    ```lua
    local player = Isaac.GetPlayer()
    local entities = Isaac.GetRoomEntities()
    for i, entity in ipairs(entities) do
    	entity:AddBurn(EntityRef(player), 30, 1)
    end
    ```

___

### Add·Charmed () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### void AddCharmed ( [EntityRef](EntityRef.md) sourceEntity, int Duration ) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void AddCharmed ( [EntityRef](EntityRef.md) sourceEntity, int Duration, boolean IgnoreBosses ) {: .copyable aria-label='Functions' }

Adds a charmed-effect to an enemy. Duration is in Number of Frames. Charmed enemies are friendly towards Isaac and attack other enemies.

`:::lua Duration = -1` makes the effect permanent and the enemy will follow you even to different rooms.

???- example "Example Code"
    This code charms every entity in the room for 1 second.

    ```lua
    local player = Isaac.GetPlayer()
    local entities = Isaac.GetRoomEntities()
    for i, entity in ipairs() do
    	entity:AddCharmed(EntityRef(player), 30)
    end
    ```

___

### Add·Confusion () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddConfusion ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses ) {: .copyable aria-label='Functions' }

Adds a confusion effect to an entity.

???- info "Duration infos"
    The Duration has a maximum of 5 seconds

???- example "Example Code"
    This code confuses every entity in the room for 1 second while ignoring bosses.

    ```lua
    local player = Isaac.GetPlayer()
    local entities = Isaac.GetRoomEntities()
    for i, entity in ipairs(entities) do
    	entity:AddConfusion(EntityRef(player), 30, true)
    end
    ```

___

### Add·Entity·Flags () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddEntityFlags ( int Flags ) {: .copyable aria-label='Functions' }

Add [EntityFlags](enums/EntityFlag.md) to the entity. Flags are used to add specific effects like being friendly or being immune from spike damage. You can add multiple flags at the same time by bitwise-concatenating them.

???- example "Example Code"
    This code adds slowing and confusion to the entity.

    ```lua
    local player = Isaac.GetPlayer()
    local entities = Isaac.GetRoomEntities()
    for i, entity in ipairs(entities) do
    	entity:AddEntityFlags(EntityFlag.FLAG_SLOW | EntityFlag.FLAG_CONFUSION)
    end
    ```
___

### Add·Fear () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### void AddFear ( [EntityRef](EntityRef.md) Source, int Duration ) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void AddFear ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses ) {: .copyable aria-label='Functions' }

Adds a fear-effect to an entity.

???- info "Duration infos"
    The Duration has a maximum of 5 seconds

???- example "Example Code"
    This code frightens every entity in the room for 1 second.

    ```lua
    local player = Isaac.GetPlayer()
    local entities = Isaac.GetRoomEntities()
    for i, entity in ipairs(entities) do
    	entity:AddFear(EntityRef(player), 30)
    end
    ```

___

### Add·Freeze () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### void AddFreeze ( [EntityRef](EntityRef.md) Source, int Duration ) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void AddFreeze ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses ) {: .copyable aria-label='Functions' }

Freezes an entity, making it unable to move and attack.

???- info "Duration infos"
    The Duration has a maximum of 5 seconds

???- example "Example Code"
    This code freezes every entity in the room for 1 second.

    ```lua
    local player = Isaac.GetPlayer()
    local entities = Isaac.GetRoomEntities()
    for i, entity in ipairs(entities) do
    	entity:AddFreeze(EntityRef(player), 30)
    end
    ```

___

### Add·Health () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void AddHealth ( float HitPoints ) {: .copyable aria-label='Functions' }
Heals an entity.
___

### Add·Midas·Freeze () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### void AddMidasFreeze ( [EntityRef](EntityRef.md) Source, int Duration ) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void AddMidasFreeze ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses ) {: .copyable aria-label='Functions' }
Turns the entity into a gold statue (can't move, can't attack, drops coins when killed)

???- info "Duration infos"
    The Duration has a maximum of 5 seconds

???+ bug
    The golden color applied to the entity will stay for the full duration passed into the function, despite the freeze effect only lasting for a maximum of 5 seconds.

???- example "Example Code"
    This code turns every entity in the room into gold for 1 second.

    ```lua
    local player = Isaac.GetPlayer()
    local entities = Isaac.GetRoomEntities()
    for i, entity in ipairs(entities) do
    	entity:AddMidasFreeze(EntityRef(player), 30)
    end
    ```
___

### Add·Poison () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### void AddPoison ( [EntityRef](EntityRef.md) Source, int Duration, float Damage ) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void AddPoison ( [EntityRef](EntityRef.md) Source, int Duration, float Damage, boolean IgnoreBosses ) {: .copyable aria-label='Functions' }

Adds a poison effect to the entity.

???- info "Duration infos"
    The Duration must be a minimum of 3 frames to deal damage. Every consecutive damage tick is 20 frames apart.

    ```
    2 Damage-ticks = 23 frames
    3 = 43
    4 = 63
    ...
    ```

???+ bug
    The Duration value seems to have an upper limit. For a PlayerEntity, it's only lasting for the duration of one damage interval. For Entities it's up to 6 damage-intervals.

???- example "Example Code"
    This code applies a poison effect to every entity in the room for 1 second.

    ```lua
    local player = Isaac.GetPlayer()
    local entities = Isaac.GetRoomEntities()
    for i, entity in ipairs(entities) do
    	entity:AddPoison(EntityRef(player), 30, 1)
    end
    ```
___

### Add·Shrink () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### void AddShrink ( [EntityRef](EntityRef.md) Source, int Duration ) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void AddShrink ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses ) {: .copyable aria-label='Functions' }

Adds a shrink effect to the entity.

???- info "Duration infos"
    The Duration has a maximum of 5 seconds

???- example "Example Code"
    This code shrinks every entity in the room for 1 second.

    ```lua
    local player = Isaac.GetPlayer()
    local entities = Isaac.GetRoomEntities()
    for i, entity in ipairs(entities) do
    	entity:AddShrink(EntityRef(player), 30)
    end
    ```
___

### Add·Slowing () {: aria-label='Functions' }
[ ](#){: .abrep .tooltip .badge }
#### void AddSlowing ( [EntityRef](EntityRef.md) Source, int Duration, float SlowValue, [Color](Color.md) SlowColor ) {: .copyable aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void AddSlowing ( [EntityRef](EntityRef.md) Source, int Duration, float SlowValue, [Color](Color.md) SlowColor, boolean IgnoreBosses ) {: .copyable aria-label='Functions' }
Makes the friction higher, effectively slowing down the entity.

???- example "Example Code"
    This code slows every entity in the room for 1 second with 0.5 original speed and applies a red color to it.

    ```lua
    local player = Isaac.GetPlayer()
    local slowColor = Color(1, 0, 0, 1, 0, 0, 0)
    local entities = Isaac.GetRoomEntities()
    for i, entity in ipairs(entities) do
    	entity:AddSlowing(EntityRef(player), 30, 0.5, slowColor)
    end
    ```
___

### Add·Velocity () {: aria-label='Functions' }
[ ](#){: .abp .tooltip .badge }
#### void AddVelocity ( [Vector](Vector.md) Velocity ) {: .copyable aria-label='Functions' }
[ ](#){: .reporplus .tooltip .badge }
#### void AddVelocity ( [Vector](Vector.md) Velocity, boolean IgnoreTimeScale = false ) {: .copyable aria-label='Functions' }

Adds velocity to the entity. This can be used to move him in a certain direction (for example as a result of collision)

- **IgnoreTimeScale** - if true, TimeScale is treated as if it were 1.0, ignoring effects that would otherwise slow down or speed up the entity (e.g. Stopwatch)
___

### Blood·Explode () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void BloodExplode ( ) {: .copyable aria-label='Functions' }
Explodes with gibs and blood.
___

### Can·Shut·Doors () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CanShutDoors ( ) {: .copyable aria-label='Functions' }
Enemies keep the doors shut.
___

### Clear·Entity·Flags () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void ClearEntityFlags ( int Flags ) {: .copyable aria-label='Functions' }

Removes all of the provided [EntityFlags](enums/EntityFlag.md) from the entity.
___

### Collides·With·Grid () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean CollidesWithGrid ( ) {: .copyable aria-label='Functions' }

Returns true if the entity is currently colliding with a valid GridEntity, as dictated by its `Entity.GridCollisionClass`.
___

### Die () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Die ( ) {: .copyable aria-label='Functions' }

Kills the entity and triggers its death animation.
___

### Exists () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean Exists ( ) {: .copyable aria-label='Functions' }

Checks whether the entity is still spawned in the current room.

This is mostly useful in situations where you are unwrapping an `EntityPtr` and the corresponding entity may or may not have been killed in the interim period.

___

### Get·Boss·ID () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetBossID ( ) {: .copyable aria-label='Functions' }
If the entity is a boss, it returns its specific boss id. If it isn't a boss it will return 0.

A boss ID is **NOT** equal to the entity Type, but is defined as a separate value in the entities2.xml file inside the "bossID" attribute.

For Delirium, this function returns the boss id Delirium is currently transformed into.
___

### Get·Color () {: aria-label='Functions' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Color](Color.md) GetColor ( ) {: .copyable aria-label='Functions' }

Returns the Color object associated with this entity.
___

### Get·Data () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### table GetData ( ) {: .copyable aria-label='Functions' }

Returns a Lua table that contains mod-related data associated with the entity. Initially, this will always be an empty table. Any values stored in the table by mods will persist until the entity is despawned.

GetData is typically used by smaller mods as a quick way to store information about an entity without having to create a dedicated data structure.

???- example "Example Code"
    This code adds custom data to an entity or prints it in the console if it exists.

    ```lua
    function checkAndSetData(entity)
      local data = entity:GetData()
      if data.foo == nil then -- Keys of data should be strings
        data.foo = "bar" -- Values of data can be any data type
        print("Assigned an initial key of: foo --> bar")
      else
        print("Key foo already exists: " .. tostring(data.foo))
      end
    end
    ```

There are three main problems with `GetData`:

1. Data is not unique per mod, which means that using `GetData` is essentially the same thing as using a global variable. Using global variables is bad for two main reasons. First, other mods can overwrite or mess with your data, so it isn't safe to use them. Second, the scope of global variables makes it difficult to determine where the variable is used when reading the code, and makes it harder to track down bugs, especially in larger programs.

2. Most entities will despawn when leaving the room. For example, even though heart pickups are persisted by the game, they will be despawned and respawned each time the room is left and reentered, respectively. Thus, most entities will have their data deleted upon leaving the room. The exceptions to this are players, familiars, and entities with [`EntityFlag.FLAG_PERSISTENT`](./enums/EntityFlag.md).

3. Even for entities that don't despawn when you leave a room, `GetData` is still not a suitable storage mechanism because it will be deleted when exiting to the menu or restarting/finishing a run. Well-programmed mods should never lose state when end-users save and quit the game, so instead of programming a `GetData` conversion + serialization routine, it's much simpler to just avoid using it to begin with.

Modders should consider using data structures that are local to their own mod in order to avoid conflicts and any of the other issues previously presented. The index for such data structures is usually the pointer hash, which can be retrieved for any entity by using the [`GetPtrHash`](./GlobalFunctions.md#getptrhash) function.
___

### Get·Drop·RNG () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [RNG](RNG.md) GetDropRNG ( ) {: .copyable aria-label='Functions' }

Returns the assigned RNG object for the entity. This RNG is used to determine the items that are dropped on the entity's death.
___

### Get·Entity·Flags () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetEntityFlags ( ) {: .copyable aria-label='Functions' }

Get the [EntityFlags](enums/EntityFlag.md)of the entity. This will be a number which acts like a bitmask.

???- example "Example Code"
    This code prints something in the console, if the entity has a specific [EntityFlags](enums/EntityFlag.md).

    ```lua
    if entity:GetEntityFlags() & EntityFlag.FLAG_CONFUSION == EntityFlag.FLAG_CONFUSION then
        print("This entity is confused!")
    end
    ```
___

### Get·Last·Child () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) GetLastChild ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

Returns the last child of this entity. This is useful for certain segmented enemies so you can go all the way to the bottom "tail" entity in one method call.

???+ note "Return behavior"
    If no child is found, this function returns `nil`.
___

### Get·Last·Parent () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) GetLastParent ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }

Returns the last parent of this entity. This is useful for certain segmented enemies so you can go all the way to the top "head" entity in one method call.

???+ note "Return behavior"
    If no parent is found, this function returns `nil`.
___

### Get·Sprite () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [Sprite](Sprite.md) GetSprite ( ) {: .copyable aria-label='Functions' }

Return the sprite object of the entity.
___

### Has·Common·Parent·With·Entity () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasCommonParentWithEntity ( [Entity](Entity.md) Other ) {: .copyable aria-label='Functions' }

___

### Has·Entity·Flags () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasEntityFlags ( int Flags ) {: .copyable aria-label='Functions' }

Returns true if the entity has all named [EntityFlags](enums/EntityFlag.md) set.

???- example "Example Code"
    This code prints something in the console, if the entity has a specific [EntityFlags](enums/EntityFlag.md).

    ```lua
    if entity:HasEntityFlags(EntityFlag.FLAG_CONFUSION) then
        print("This entity is confused!")
    end
    ```
___

### Has·Full·Health () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasFullHealth ( ) {: .copyable aria-label='Functions' }

___

### Has·Mortal·Damage () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean HasMortalDamage ( ) {: .copyable aria-label='Functions' }


???- note "Notes"
    The game adds taken damage to a damage buffer, which gets applied in the next frame. HasMortalDamage() returns true if the buffered damage is enough to kill the entity.
    HasMortalDamage() will be updated additionally after TakeDamage() is called.
___

### Is·Active·Enemy () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsActiveEnemy ( boolean includeDead ) {: .copyable aria-label='Functions' }
return true for non background NPCs (ex: every enemy except fire and shopkeepers)
___

### Is·Boss () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsBoss ( ) {: .copyable aria-label='Functions' }
bosses display health bar
___

### Is·Dead () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsDead ( ) {: .copyable aria-label='Functions' }

___

### Is·Enemy () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsEnemy ( ) {: .copyable aria-label='Functions' }
return true for NPCs that are not controlled by the player
___

### Is·Flying () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsFlying ( ) {: .copyable aria-label='Functions' }

___

### Is·Frame () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsFrame ( int Frame, int Offset ) {: .copyable aria-label='Functions' }
true every X frames
___

### Is·Invincible () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsInvincible ( ) {: .copyable aria-label='Functions' }

___

### Is·Visible () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsVisible ( ) {: .copyable aria-label='Functions' }

___

### Is·Vulnerable·Enemy () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean IsVulnerableEnemy ( ) {: .copyable aria-label='Functions' }
return true for enemies that can be damaged
___

### Kill () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Kill ( ) {: .copyable aria-label='Functions' }
Kills the entity and makes a blood splat or gibs.
___

### Kill·With·Source () {: aria-label='Functions' }
[ ](#){: .repplus .tooltip .badge }
#### void KillWithSource ( [EntityRef](EntityRef.md) Source ) {: .copyable aria-label='Functions' }
___

### Multiply·Friction () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void MultiplyFriction ( float Value ) {: .copyable aria-label='Functions' }

___

### Post·Render () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void PostRender ( ) {: .copyable aria-label='Functions' }

___

### Remove () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Remove ( ) {: .copyable aria-label='Functions' }
Remove the entity from the game instantly, without doing any additional effects/animations.
___

### Remove·Status·Effects () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void RemoveStatusEffects ( ) {: .copyable aria-label='Functions' }

Removes all Status Effects from the entity.
___

### Render () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Render ( [Vector](Vector.md) Offset ) {: .copyable aria-label='Functions' }
Render the current sprite of the Entity at the current entity position + offset.
___

### Render·Shadow·Layer () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean RenderShadowLayer ( [Vector](Vector.md) Offset ) {: .copyable aria-label='Functions' }

Render the shadow / shadow layer again.
___

### Set·Color () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetColor ( [Color](Color.md) Color, int Duration, int Priority, boolean Fadeout, boolean Share ) {: .copyable aria-label='Functions' }

Set the colormask for the entity. This can be used to tint the sprites in different colors.

``Share`` boolean will apply color to child entitiy.

???- example "Example Code"
    This code changes the color of the sprite to a fully white sprite for 15 frames.

    ```lua
    entity:SetColor(Color(1, 1, 1, 1, 255, 255, 255), 15, 1, false, false)
    ```

___

### Set·Size () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetSize ( float Size, [Vector](Vector.md) SizeMulti, int NumGridCollisionPoints ) {: .copyable aria-label='Functions' }

Set the size of the entity.
___

### Set·Sprite·Frame () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetSpriteFrame ( string AnimationName, int FrameNum ) {: .copyable aria-label='Functions' }

___

### Set·Sprite·Overlay·Frame () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetSpriteOverlayFrame ( string AnimationName, int FrameNum ) {: .copyable aria-label='Functions' }

___

### Take·Damage () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean TakeDamage ( float Damage, [DamageFlag](enums/DamageFlag.md) Flags, [EntityRef](EntityRef.md) Source, int DamageCountdown ) {: .copyable aria-label='Functions' }


???- note "Notes"
    The game adds taken damage to a damage buffer, which gets applied in the next frame. Therefore, TakeDamage() will not decrement the entities HP immediately upon calling the function. Rather, it is only updated on the frame afterwards.
___

### To·Bomb () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityBomb](EntityBomb.md) ToBomb ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
Used to cast an [Entity](Entity.md) object to an [EntityBomb](EntityBomb.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.
___

### To·Effect () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityEffect](EntityEffect.md) ToEffect ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
Used to cast an [Entity](Entity.md) object to an [EntityEffect](EntityEffect.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.

___

### To·Familiar () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityFamiliar](EntityFamiliar.md) ToFamiliar ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
Used to cast an [Entity](Entity.md) object to an [EntityFamiliar](EntityFamiliar.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.

___

### To·Knife () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityKnife](EntityKnife.md) ToKnife ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
Used to cast an [Entity](Entity.md) object to an [EntityKnife](EntityKnife.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.

___

### To·Laser () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityLaser](EntityLaser.md) ToLaser ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
Used to cast an [Entity](Entity.md) object to an [EntityLaser](EntityLaser.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.

___

### To·NPC () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityNPC](EntityNPC.md) ToNPC ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
Used to cast an [Entity](Entity.md) object to an [EntityNPC](EntityNPC.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.

___

### To·Pickup () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityPickup](EntityPickup.md) ToPickup ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
Used to cast an [Entity](Entity.md) object to an [EntityPickup](EntityPickup.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.

___

### To·Player () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityPlayer](EntityPlayer.md) ToPlayer ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
Used to cast an [Entity](Entity.md) object to an [EntityPlayer](EntityPlayer.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.

___

### To·Projectile () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityProjectile](EntityProjectile.md) ToProjectile ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
Used to cast an [Entity](Entity.md) object to an [EntityProjectile](EntityProjectile.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.

___

### To·Tear () {: aria-label='Functions' data-altreturn='nil' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityTear](EntityTear.md) ToTear ( ) {: .copyable aria-label='Functions' }
Used to cast an [Entity](Entity.md) object to an [EntityTear](EntityTear.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.

___

### Update () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void Update ( ) {: .copyable aria-label='Functions' }

Runs the post-update logic for the entity for a single frame, which will cause the associated callback to fire. Mods usually never need to call this function, as it can cause bugs when post-update logic is run more than once a frame.

___
## Variables

### Child {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) Child {: .copyable aria-label='Variables' }

???- warning "Warning"
    Sisters Vis bosses do have their counterpart entity as their Child. But none of them have a Parent entity set.
___

### Collision·Damage {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float CollisionDamage  {: .copyable aria-label='Variables' }

___

### Color {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Color](Color.md) Color  {: .copyable aria-label='Variables' }

___

### Depth·Offset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float DepthOffset  {: .copyable aria-label='Variables' }

Get/Set the depth-offset of the entity. This value is added to the Y Position of the entity, which is then used to determine the rendering order of each entity. Default is 0 for all entities.

???- example "Example Code"
    This code explains how this variable works.

    ```lua
    entity1.Position.Y -- => 50
    entity2.Position.Y -- => 45
    -- Entity1 is rendered in front of Entity2

    entity1.DepthOffset = -10
    -- new Entity1 renderYPosition => 40
    -- Entity2 is rendered in front of Entity1
    ```

___

### Drop·Seed {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const int DropSeed  {: .copyable aria-label='Variables' }

Get the Seed of the Drop RNG.
___

### Entity·Collision·Class {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityCollisionClass](enums/EntityCollisionClass.md) EntityCollisionClass {: .copyable aria-label='Variables' }

___

### FlipX {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean FlipX  {: .copyable aria-label='Variables' }

___

### Frame·Count {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const int FrameCount  {: .copyable aria-label='Variables' }

___

### Friction {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Friction  {: .copyable aria-label='Variables' }
loaded from entity config
___

### Grid·Collision·Class {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityGridCollisionClass](enums/EntityGridCollisionClass.md) GridCollisionClass {: .copyable aria-label='Variables' }


???- note "Notes"
    EntityPlayers can only use GRIDCOLL_NONE, GRIDCOLL_WALLS, and GRIDCOLL_GROUND. All other enums will behave like GRIDCOLL_WALLS.
___

### Hit·Points {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float HitPoints  {: .copyable aria-label='Variables' }


???- note "Notes"
    The HitPoints value is not decremented immediately upon taking damage like you would expect. Rather, it is only updated on the frame after the entity takes damage.
___

### Index {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const int Index  {: .copyable aria-label='Variables' }

___

### Init·Seed {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const int InitSeed  {: .copyable aria-label='Variables' }

___

### Mass {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Mass  {: .copyable aria-label='Variables' }
???+ note "Notes"
    Stationary enemies have a Mass of 100. This does not apply to some stationary non-enemies, like slots.
___

### Max·Hit·Points {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float MaxHitPoints  {: .copyable aria-label='Variables' }

___

### Parent {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) Parent  {: .copyable aria-label='Variables' data-altreturn='nil' }

This is a reference to the "parent" entity. For most entities, this field will be nil. This field is used in multi-segment entities to refer back to which segment is the "main" entity, like the head.

___

### Position {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) Position  {: .copyable aria-label='Variables' }

___

### Position·Offset {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [Vector](Vector.md) PositionOffset  {: .copyable aria-label='Variables' }

___

### Render·ZOffset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int RenderZOffset  {: .copyable aria-label='Variables' }


???+ bug "Bugs"
    This variable doesn't seem to do anything useful. Use DepthOffset instead.
___

### Size {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float Size  {: .copyable aria-label='Variables' }
Returns the size of the hitbox of an entity.

___

### Size·Multi {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) SizeMulti  {: .copyable aria-label='Variables' }

"Hitboxes" in Isaac aren't boxes at all, but are actually capsules (circles). This determines the shape of the circle, with a higher X value making the circle wider, a higher Y value making the circle taller, and vice versa.

___

### Sorting·Layer {: aria-label='Variables' }
[ ](#){: .reporplus .tooltip .badge }
#### [SortingLayer](enums/SortingLayer.md) SortingLayer  {: .copyable aria-label='Variables' }

Determines when the entity should render over other entities.

___

### Spawner·Entity {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) SpawnerEntity  {: .copyable aria-label='Variables' data-altreturn='nil' }

___

### Spawner·Type {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [EntityType](enums/EntityType.md) SpawnerType  {: .copyable aria-label='Variables' }

___

### Spawner·Variant {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int SpawnerVariant  {: .copyable aria-label='Variables' }

___

### Spawn·Grid·Index {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const int SpawnGridIndex  {: .copyable aria-label='Variables' }

This is the grid index with which the entity spawned upon room generation.

Rerolled item pedestals, or entities spawned after the initial room generation will have a value of -1

___

### Splat·Color {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Color](Color.md) SplatColor  {: .copyable aria-label='Variables' }

The color of the gibs when an entity dies.

The Color of this property is read only, so if you want to change it, you have to replace the entire thing with a new Color object.

___

### Sprite·Offset {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) SpriteOffset  {: .copyable aria-label='Variables' }

___

### Sprite·Rotation {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### float SpriteRotation  {: .copyable aria-label='Variables' }

___

### Sprite·Scale {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) SpriteScale  {: .copyable aria-label='Variables' }
Get/set the scale of the enemy sprite. This can be used to also scale the shadow of the entity.

Also used as a Player stat - Change this in a callback to MC_EVALUATE_CACHE using the CacheFlag.CACHE_SIZE flag.  **This is equal to the Size stat.**

Most items that apply a Size Up (Magic Mushroom, Pill Larger...) do so by multiplying the SpriteScale by 1.2500623464584 (this is speculated to be 1.25 with a floating number error, you may choose to use 1.25 for future proofing instead).

Most items that apply a Size Down (Mini Mushroom, Binky, Pill Smaller...) do so by multiplying the SpriteScale by 0.79996013641357 (this is speculated to be 0.8 with a floating number error, you may choose to use 0.8 for future proofing instead).

Pluto uses its own multiplier of 0.5.

___

### Sub·Type {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int SubType  {: .copyable aria-label='Variables' }

___

### Target {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Entity](Entity.md) Target  {: .copyable aria-label='Variables' }

___

### Target·Position {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) TargetPosition  {: .copyable aria-label='Variables' }

___

### Type {: aria-label='Variables' }
[ ](#){: .const .tooltip .badge } [ ](#){: .alldlc .tooltip .badge }
#### const [EntityType](enums/EntityType.md) Type  {: .copyable aria-label='Variables' }

___

### Variant {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### int Variant  {: .copyable aria-label='Variables' }

___

### Velocity {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### [Vector](Vector.md) Velocity  {: .copyable aria-label='Variables' }

___

### Visible {: aria-label='Variables' }
[ ](#){: .alldlc .tooltip .badge }
#### boolean Visible  {: .copyable aria-label='Variables' }

___

<div class="rgon-only" markdown="1">

### AddBaited () {: aria-label='Functions' }
#### void AddBaited ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "Duration info"
    The Duration has a maximum of 10 seconds.

___

### AddBleeding () {: aria-label='Functions' }
#### void AddBleeding ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "Duration info"
    The Duration has a maximum of 4 seconds.

___

### AddBrimstoneMark () {: aria-label='Functions' }
#### void AddBrimstoneMark ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "Duration info"
    The Duration has a maximum of 10 seconds.

___

### AddIce () {: aria-label='Functions' }
#### void AddIce ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "Duration info"
    The Duration has a maximum of 10 seconds.

___

### AddKnockback () {: aria-label='Functions' }
#### void AddKnockback ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, [Vector](Vector.md) PushDirection, int Duration, boolean TakeImpactDamage ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "Duration info"
    The Duration has a maximum of 0.5 seconds / 15 frames.

___

### AddMagnetized () {: aria-label='Functions' }
#### void AddMagnetized ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "Duration info"
    The Duration has a maximum of 10 seconds.

___

### AddWeakness () {: aria-label='Functions' }
#### void AddWeakness ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ info "Duration info"
    The Duration has a maximum of 10 seconds.

___

### CanDevolve () {: aria-label='Functions' }
#### boolean CanDevolve ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ClearHitList () {: aria-label='Functions' }
#### void ClearHitList ( ) [ ](#){: .rgon .tooltip .badge } {: .copyable aria-label='Functions' }
清除泪弹的命中列表，使其能够再次命中之前命中过的敌人。

___

### ComputeStatusEffectDuration () {: aria-label='Functions' }
#### int ComputeStatusEffectDuration ( int InitialLength, [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
If the source entity originates from a player with Second Hand, returns the duration multiplied by `(2 × Second Hand multiplier)`, otherwise returns the original duration.

___

### CopyStatusEffects () {: aria-label='Functions' }
#### void CopyStatusEffects ( [Entity](Entity.md) Target, boolean Overwrite = false ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
If `Target` is left unspecified, this will recursively copy status effects to all [Child](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#child) Entities. `Overwrite` will additionally remove all other status effects from the target and set the properties of existing effects to match the entity.

___

### ForceCollide () {: aria-label='Functions' }
#### boolean ForceCollide ( [Entity](Entity.md) Entity, boolean Force ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

Returns true if the rest of the collision logic should be **skipped**; either because the entities did not collide in the first place (if `Force` is false),
or because one of the entities' internal collision logic decided so (which can be influenced by one of the `PRE_COLLISION` callbacks).

If `Force` is set to false, then the game will check if the entities' [EntityCollisionClass](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#entitycollisionclass) values are
compatible and if both entities are not [Dead](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#isdead) before triggering the collision.

???- warning "Collision Logic Changes"
    The collision logic for some entity types changes when forced.<br>
    For example: Slots do not make the player pay the regular prize for activation.

___

### GetBaitedCountdown () {: aria-label='Functions' }
#### int GetBaitedCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBleedingCountdown () {: aria-label='Functions' }
#### int GetBleedingCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBossStatusEffectCooldown () {: aria-label='Functions' }
#### int GetBossStatusEffectCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBrimstoneMarkCountdown () {: aria-label='Functions' }
#### int GetBrimstoneMarkCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBurnCountdown () {: aria-label='Functions' }
#### int GetBurnCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetBurnDamageTimer () {: aria-label='Functions' }
#### int GetBurnDamageTimer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCharmedCountdown () {: aria-label='Functions' }
#### int GetCharmedCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetCollisionCapsule () {: aria-label='Functions' }
#### [Capsule](Capsule.md) GetCollisionCapsule ( [Vector](Vector.md) Vector ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetColorParams () {: aria-label='Functions' }
#### [ColorParams](ColorParams.md)[] GetColorParams ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a table of all colors currently queued by `SetColor` alongside their parameters.

___

### GetConfusionCountdown () {: aria-label='Functions' }
#### int GetConfusionCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetDamageCountdown () {: aria-label='Functions' }
#### int GetDamageCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
If the entity recently took damage with the DAMAGE_COUNTDOWN [DamageFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html), this returns how many more frames must pass before they can take damage with the DAMAGE_COUNTDOWN [DamageFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) again.

Note that this is NOT the same as the player's invincibility frames (`EntityPlayer:GetDamageCooldown()`). The DAMAGE_COUNTDOWN [DamageFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) and its associated countdown are typically used to control how rapidly an enemy will take damage from the few sources that use that flag, such as the collision damage effects from "My Little Unicorn", "The Nail", and "The Gamekid".

___

### GetDebugShape () {: aria-label='Functions' }
#### [Shape](renderer/Shape.md) GetDebugShape ( boolean Unknown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetEntityConfigEntity () {: aria-label='Functions' }
#### [EntityConfigEntity](EntityConfigEntity.md) GetEntityConfigEntity ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the corresponding [EntityConfig](EntityConfig.md) entry for this entity.

___

### GetFearCountdown () {: aria-label='Functions' }
#### int GetFearCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetFireDamageCooldown () {: aria-label='Functions' }
#### int GetFireDamageCooldown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetFreezeCountdown () {: aria-label='Functions' }
#### int GetFreezeCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetHitListIndex () {: aria-label='Functions' }
#### int GetHitListIndex ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns an array of hit entities using their [Index](https://wofsauge.github.io/IsaacDocs/rep/Entity.html#index) field.

___

### GetIceCountdown () {: aria-label='Functions' }
#### int GetIceCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetKnockbackCountdown () {: aria-label='Functions' }
#### int GetKnockbackCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetKnockbackDirection () {: aria-label='Functions' }
#### [Vector](Vector.md) GetKnockbackDirection ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMagnetizedCountdown () {: aria-label='Functions' }
#### int GetMagnetizedCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMidasFreezeCountdown () {: aria-label='Functions' }
#### int GetMidasFreezeCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetMinecart () {: aria-label='Functions' }
#### [EntityNPC](EntityNPC.md) GetMinecart ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the minecart the entity is riding.

???+ note "Return behavior"
    If the entity is not riding a minecart, this function returns `nil`.

___

### GetNullCapsule () {: aria-label='Functions' }
#### [Capsule](Capsule.md) GetNullCapsule ( string NullLayerName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetNullOffset () {: aria-label='Functions' }
#### [Vector](Vector.md) GetNullOffset ( string NullLayerName ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns the position of the null layer mark. Alternatively, returns `Vector.Zero` if the layer is not visible, has no frame available for the current animation, or for other unknown reasons.

___

### GetPauseTime () {: aria-label='Functions' }
#### int GetPauseTime ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPoisonCountdown () {: aria-label='Functions' }
#### int GetPoisonCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPoisonDamageTimer () {: aria-label='Functions' }
#### int GetPoisonDamageTimer ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetPosVel () {: aria-label='Functions' }
#### [PosVel](https://wofsauge.github.io/IsaacDocs/rep/PlayerTypes_PosVel.html) GetPosVel ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns two values, both Vectors: the entity's Position first, followed by its Velocity.

___

### GetPredictedTargetPosition () {: aria-label='Functions' }
#### [Vector](Vector.md) GetPredictedTargetPosition ( [Entity](Entity.md) Target, float Delay ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
The prediction is the target's current position plus their velocity multiplied by the distance between this and the target.
`Delay` acts as a multiplier for how far ahead the prediction should be. For example, `1.0` would predict where the target's velocity would place them on the next update.

___

### GetShadowSize () {: aria-label='Functions' }
#### float GetShadowSize ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetShrinkCountdown () {: aria-label='Functions' }
#### int GetShrinkCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSlowingCountdown () {: aria-label='Functions' }
#### int GetSlowingCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetSpeedMultiplier () {: aria-label='Functions' }
#### float GetSpeedMultiplier ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ warning "Depreciation notice"
    This variable is actually the Entity's time scale. A properly named replacement function will be added in a future version.

___

### GetType () {: aria-label='Functions' }
#### [EntityType](https://wofsauge.github.io/IsaacDocs/rep/enums/EntityType.html) GetType ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GetWaterClipFlags () {: aria-label='Functions' }
#### [WaterClipFlag](enums/WaterClipFlag.md) GetWaterClipFlags ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Gets a bitset that informs some of how this entity interacts with water, primarily rendering related (reflections, etc).

___

### GetWeaknessCountdown () {: aria-label='Functions' }
#### int GetWeaknessCountdown ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### GiveMinecart () {: aria-label='Functions' }
#### [EntityNPC](EntityNPC.md) GiveMinecart ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### IgnoreEffectFromFriendly () {: aria-label='Functions' }
#### boolean IgnoreEffectFromFriendly ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used to determine if this entity should ignore any status effect coming from `Source`.

___

### MakeBloodPoof () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) MakeBloodPoof ( [Vector](Vector.md) Position = self.Position, [Color](Color.md) Color = default, float Scale = 1.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
This function spawns two blood poof effects of subtypes 3 and 4; the second will be the Child of the returned effect.

___

### MakeGroundPoof () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) MakeGroundPoof ( [Vector](Vector.md) Position = self.Position, [Color](Color.md) Color = default, float Scale = 1.0 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
This function spawns two dust poof effects of subtypes 1 and 2; the second will be the Child of the returned effect.

___

### ResetWaterClipFlags () {: aria-label='Functions' }
#### void ResetWaterClipFlags ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Restores water rendering to the default vanilla state. See `SetWaterClipFlags()`.

___

### SetBaitedCountdown () {: aria-label='Functions' }
#### void SetBaitedCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBleedingCountdown () {: aria-label='Functions' }
#### void SetBleedingCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBossStatusEffectCooldown () {: aria-label='Functions' }
#### void SetBossStatusEffectCooldown ( int Cooldown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBrimstoneMarkCountdown () {: aria-label='Functions' }
#### void SetBrimstoneMarkCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBurnCountdown () {: aria-label='Functions' }
#### void SetBurnCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetBurnDamageTimer () {: aria-label='Functions' }
#### void SetBurnDamageTimer ( int Timer ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetCharmedCountdown () {: aria-label='Functions' }
#### void SetCharmedCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetColorParams () {: aria-label='Functions' }
#### void SetColorParams ( [ColorParams](ColorParams.md)[] Params ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets colors to be used alongside their parameters.

___

### SetConfusionCountdown () {: aria-label='Functions' }
#### void SetConfusionCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetDamageCountdown () {: aria-label='Functions' }
#### void SetDamageCountdown ( int countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Sets how many frames must pass before the entity can take damage with the DAMAGE_COUNTDOWN [DamageFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html).

Note that this is NOT the same as the player's invincibility frames (`EntityPlayer:GetDamageCooldown()`). The DAMAGE_COUNTDOWN [DamageFlag](https://wofsauge.github.io/IsaacDocs/rep/enums/DamageFlag.html) and its associated countdown are typically used to control how rapidly an enemy takes damage from the few sources that use this flag, such as the collision damage effects from "My Little Unicorn", "The Nail", and "The Gamekid".

___

### SetDead () {: aria-label='Functions' }
#### void SetDead ( boolean IsDead ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetFearCountdown () {: aria-label='Functions' }
#### void SetFearCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetFireDamageCooldown () {: aria-label='Functions' }
#### void SetFireDamageCooldown ( int Cooldown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetFreezeCountdown () {: aria-label='Functions' }
#### void SetFreezeCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetIceCountdown () {: aria-label='Functions' }
#### void SetIceCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetInvincible () {: aria-label='Functions' }
#### void SetInvincible ( boolean IsInvincible ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetKnockbackCountdown () {: aria-label='Functions' }
#### void SetKnockbackCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetKnockbackDirection () {: aria-label='Functions' }
#### void SetKnockbackDirection ( [Vector](Vector.md) Direction ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetMagnetizedCountdown () {: aria-label='Functions' }
#### void SetMagnetizedCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetMidasFreezeCountdown () {: aria-label='Functions' }
#### void SetMidasFreezeCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetPauseTime () {: aria-label='Functions' }
#### void SetPauseTime ( int Duration ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetPoisonCountdown () {: aria-label='Functions' }
#### void SetPoisonCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetPoisonDamageTimer () {: aria-label='Functions' }
#### void SetPoisonDamageTimer ( int Timer ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetShadowSize () {: aria-label='Functions' }
#### float SetShadowSize ( float Size ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetShrinkCountdown () {: aria-label='Functions' }
#### void SetShrinkCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetSlowingCountdown () {: aria-label='Functions' }
#### void SetSlowingCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SetSpeedMultiplier () {: aria-label='Functions' }
#### void SetSpeedMultiplier ( float Amount ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
???+ warning "Deprecation notice"
    This variable is actually the Entity's time scale. A properly named replacement function will be added in a future version.

___

### SetWaterClipFlags () {: aria-label='Functions' }
#### void SetWaterClipFlags ( [WaterClipFlag](enums/WaterClipFlag.md) Flags ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Allows modification of how this entity interacts with water, primarily rendering-related behaviour such as reflections.

Note that this will also override/disable any natural vanilla changes to these flags, such as the player losing their reflection with Charm of the Vampire.

Vanilla state can be restored with `ResetWaterClipFlags()`.

___

### SetWeaknessCountdown () {: aria-label='Functions' }
#### void SetWeaknessCountdown ( int Countdown ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SpawnBloodEffect () {: aria-label='Functions' }
#### [EntityEffect](EntityEffect.md) SpawnBloodEffect ( int SubType = 0, [Vector](Vector.md) position = self.Position, [Vector](Vector.md) Offset = Vector.Zero, [Color](Color.md) Color = Default, [Vector](Vector.md) Velocity = Vector.Zero ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### SpawnWaterImpactEffects () {: aria-label='Functions' }
#### void SpawnWaterImpactEffects ( [Vector](Vector.md) Position, [Vector](Vector.md) Velocity = Vector.Zero, float Strength ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

???+ warning "Warning"
    This function only spawns effects if the Room's [water amount](Room.md#getwateramount) is greater than or equal to `0.2`.

___

### TeleportToRandomPosition () {: aria-label='Functions' }
#### void TeleportToRandomPosition ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### ToDelirium () {: aria-label='Functions' }
#### [EntityDelirium](EntityDelirium.md) ToDelirium ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Convert an [Entity](Entity.md) userdata to an [EntityDelirium](EntityDelirium.md) userdata.
The conversion will only succeed if the source entity is an instance of Delirium (in its normal form or in a transformed form).

???+ note "Return behavior"
    If the conversion fails, this function returns `nil`.

___

### ToSlot () {: aria-label='Functions' }
#### [EntitySlot](EntitySlot.md) ToSlot ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Used to cast an [Entity](Entity.md) object to an [EntitySlot](EntitySlot.md) object.

???+ note "Return behavior"
    If the conversion is not successful, this function returns `nil`.

___

### TryThrow () {: aria-label='Functions' }
#### boolean TryThrow ( [EntityRef](https://wofsauge.github.io/IsaacDocs/rep/EntityRef.html) Source, [Vector](Vector.md) Velocity, float Height ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Has different effects based on the entity it was used on.

[EntityPlayer](https://repentogon.com/EntityPlayer.html) Players:
Throws the player into the air, respects grid collision.
Throw won't be applied if the player is airborne or has flight, unless the source is a player.

[EntityPickup](https://repentogon.com/EntityPickup.html) Pickups:
Only works on Chests, throws it into the air, respects grid collision.
When the Chest lands it will always open, no matter the unlock condition.

[EntityNPC](https://repentogon.com/EntityNPC.html) NPCs:
Only works on poop entities, throws it into the air, ignores grid collision.
At a certain velocity, the poop will play the `SoundEffect.SOUND_POOPITEM_THROW` sound effect when thrown.

[EntityFamiliar](https://repentogon.com/EntityFamiliar.html) Familiars:
Only works on Dip familiars and Cube Baby, throws it into the air, ignores grid collision.
Cube baby will leave creep when thrown, similar to throwing it with Mom's Ring.

___

</div>
