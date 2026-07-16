---
tags:
  - Enum
---
# Enum "EntityFlag"

???+ tip "Bitset Calculator"
    [](#)

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|1 << 0|FLAG_NO_STATUS_EFFECTS  | Prevents status effects from applying to the entity (e.g. freeze, poison, slow, charm, confusion, fear, burn, etc.). |
|[ ](#)|1 << 1 |FLAG_NO_INTERPOLATE  | Do not interpolate the position. |
|[ ](#)|1 << 2 |FLAG_APPEAR  | The "Appear" animation will be played after the entity is initialized. |
|[ ](#)|1 << 3 |FLAG_RENDER_FLOOR  | Meant for entities that have a sprite loaded that represent a floor texture. Entities with this flag will be removed after their first render. (Removing the entity is desirable because we would not want it to override other things that render to the floor, like bomb explosions.) You can use `EntityFlag.NO_REMOVE_ON_TEX_RENDER` to disable this behavior. |
|[ ](#)|1 << 4 |FLAG_NO_TARGET  | Will not be a target of NPCs or familiars. |
|[ ](#)|1 << 5 |FLAG_FREEZE  | |
|[ ](#)|1 << 6 |FLAG_POISON  | |
|[ ](#)|1 << 7 |FLAG_SLOW  | |
|[ ](#)|1 << 8 |FLAG_CHARM  | |
|[ ](#)|1 << 9 |FLAG_CONFUSION  | |
|[ ](#)|1 << 10 |FLAG_MIDAS_FREEZE  | |
|[ ](#)|1 << 11 |FLAG_FEAR  | Fleeing in fear (from e.g. Mom's Pad). |
|[ ](#)|1 << 12 |FLAG_BURN  | Caused by Fire Mind tears. Works like poison except with a red color effect. |
|[ ](#)|1 << 13 |FLAG_RENDER_WALL  | Meant for entities that have a sprite loaded that represent a wall texture. Entities with this flag will be removed after their first render. (Removing the entity is desirable because we would not want it to override other things that render to the wall, like bomb explosions.) You can use `EntityFlag.NO_REMOVE_ON_TEX_RENDER` to disable this behavior. |
|[ ](#)|1 << 14 |FLAG_INTERPOLATION_UPDATE  | The entity is updating at 60 frames per second and this is an odd frame. |
|[ ](#)|1 << 15 |FLAG_APPLY_GRAVITY  | Indicates that the entity is in a side-scrolling room and is within a gravity zone. |
|[ ](#)|1 << 16 |FLAG_NO_BLOOD_SPLASH  | |
|[ ](#)|1 << 17 |FLAG_NO_REMOVE_ON_TEX_RENDER  | See `EntityFlag.FLAG_RENDER_FLOOR` and `EntityFlag.FLAG_RENDER_WALL`. |
|[ ](#)|1 << 18 |FLAG_NO_DEATH_TRIGGER  | |
|[ ](#)|1 << 19 |FLAG_NO_SPIKE_DAMAGE  | |
|[ ](#)|1 << 19 |FLAG_LASER_POP  | EntityTear: Pop tear fired by a laser, should decelerate very quickly for the first few frames |
|[ ](#)|1 << 19 |FLAG_ITEM_SHOULD_DUPLICATE  | EntityPickup: item pedestal affected by Damocles, will be duplicated at the end of the current frame |
|[ ](#)|1 << 20 |FLAG_BOSSDEATH_TRIGGERED  | Some bosses (Lamb/Mother) can die but they'll still appear to be active in the room (IsActiveEnemy). You can check this flag in those cases. |
|[ ](#)|1 << 21 |FLAG_DONT_OVERWRITE  | Used in entityfactory to not remove this entity if there is no space left for new entity |
|[ ](#)|1 << 22 |FLAG_SPAWN_STICKY_SPIDERS  | Used by Sticky bombs to generate spiders on death |
|[ ](#)|1 << 23 |FLAG_SPAWN_BLACK_HP  | Used by black hp drop tear flag to drop a black hp on enemy death |
|[ ](#)|1 << 24 |FLAG_SHRINK  | God's flesh effect |
|[ ](#)|1 << 25 |FLAG_NO_FLASH_ON_DAMAGE  | Entity will not flash red when damaged |
|[ ](#)|1 << 26 |FLAG_NO_KNOCKBACK  | Bombs and farts have no knockback effects |
|[ ](#)|1 << 27 |FLAG_SLIPPERY_PHYSICS  | Standing on a slippery surface |
|[ ](#)|1 << 28 |FLAG_ADD_JAR_FLY  | Adds a fly to the jar when killed |
|[ ](#)|1 << 29 |FLAG_FRIENDLY  | Charmed and m_CharmCountdown<0 |
|[ ](#)|1 << 30 |FLAG_NO_PHYSICS_KNOCKBACK  | No knockback from general collisions |
|[ ](#)|1 << 31 |FLAG_DONT_COUNT_BOSS_HP  | Do not count boss hp. If all boss entities have this tag, the boss hp bar is hidden |
|[ ](#)|1 << 32 |FLAG_NO_SPRITE_UPDATE  | Do not update sprite animation |
|[ ](#)|1 << 33 |FLAG_CONTAGIOUS  | Used for Contagious item (if the enemy is infected) |
|[ ](#)|1 << 34 |FLAG_BLEED_OUT  | Used for Mom's Razor |
|[ ](#)|1 << 35 |FLAG_HIDE_HP_BAR  | Hides the Spider Mod hp bar of an EntityNPC |
|[ ](#)|1 << 36 |FLAG_NO_DAMAGE_BLINK  | Player was given a short period of invulnerability by something other than damage, don't blink |
|[ ](#)|1 << 37 |FLAG_PERSISTENT  | The entity will persists between rooms. (It will appear in every room, as opposed to the game remembering the specific room that it was spawned in.) |
|[ ](#)|1 << 38 |FLAG_BACKDROP_DETAIL  | Was spawned as a backdrop decoration, should be deleted if the current backdrop changes (due to Delirium) |
|[ ](#)|1 << 39 |FLAG_AMBUSH  | Enemy was spawned by some sort of ambush (Greed Mode, challenge rooms), don't collide with the player for a few frames |
|[ ](#)|1 << 40 |FLAG_GLITCH  | Glitched out, has different effects depending on the entity |
|[ ](#)|1 << 41 |FLAG_SPIN  | Used by Spin to Win, causes a familiar to rapidly spin around its owner |
|[ ](#)|1 << 42 |FLAG_NO_REWARD  | Doesn't spawn any kind of reward on death |
|[ ](#)|1 << 43 |FLAG_REDUCE_GIBS  | Spawn less gibs on death |
|[ ](#)|1 << 44 |FLAG_TRANSITION_UPDATE  | Updates during room/stage transitions |
|[ ](#)|1 << 45 |FLAG_NO_PLAYER_CONTROL  | Cannot be controlled by players |
|[ ](#)|1 << 46 |FLAG_NO_QUERY  | Hide from query results. This can hide entities from things like `Isaac.FindByType` and the `MC_ENTITY_TAKE_DMG` callback. Entities will still be visible to `Isaac.GetRoomEntities` and `_UPDATE` callbacks. |
|[ ](#)|1 << 47 |FLAG_KNOCKED_BACK  | Strong knockback: Forcefy moved in a specified direction for a short duration |
|[ ](#)|1 << 48 |FLAG_APPLY_IMPACT_DAMAGE  | Inflicts damage upon colliding with enemies, takes damage when colliding with walls |
|[ ](#)|1 << 49 |FLAG_ICE_FROZEN  | Frozen solid |
|[ ](#)|1 << 50 |FLAG_ICE  | Flagged to become frozen on death |
|[ ](#)|1 << 51 |FLAG_MAGNETIZED  | Magnetized: Attracts nearby enemies, projectiles and pickups |
|[ ](#)|1 << 52 |FLAG_BAITED  | Baited: Is targeted by nearby enemies |
|[ ](#)|1 << 53 |FLAG_KILLSWITCH  | Killed by a killswitch |
|[ ](#)|1 << 54 |FLAG_WEAKNESS  | Weakness effect from Reverse Strength |
|[ ](#)|1 << 55 |FLAG_EXTRA_GORE  | Spawns more gibs on death |
|[ ](#)|1 << 56 |FLAG_BRIMSTONE_MARKED  | Marked by Tainted Azazel; takes extra damage from Brimstone attacks. |
|[ ](#)|1 << 57 |FLAG_HELD  | Picked up by a player |
|[ ](#)|1 << 58 |FLAG_THROWN  | Thrown by a player |
|[ ](#)|1 << 59 |FLAG_FRIENDLY_BALL  | Used to detect enemies spawned by Friendly Ball |
