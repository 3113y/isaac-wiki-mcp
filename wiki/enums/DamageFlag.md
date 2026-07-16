---
tags:
  - Enum
---
# Enum "DamageFlag"

???+ tip "Bitset Calculator"
    [](#)

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|1 << 0 |DAMAGE_NOKILL  | Damage can not kill the receiver <br> |
|[ ](#)|1 << 1 |DAMAGE_FIRE  | Source is some sort of fire (ie. fireplace) <br> |
|[ ](#)|1 << 2 |DAMAGE_EXPLOSION  | Damage comes from an explosion <br> |
|[ ](#)|1 << 3 |DAMAGE_LASER  | Damage comes from laser <br> |
|[ ](#)|1 << 4 |DAMAGE_ACID  | Damage comes from acid, e.g. blood acid <br> |
|[ ](#)|1 << 5 |DAMAGE_RED_HEARTS  | Damage affects only red hearts if > 1 (ex: razor) <br> |
|[ ](#)|1 << 6 |DAMAGE_COUNTDOWN  | Damage from unicorn horn, the nail, game kid that has cooldown <br> |
|[ ](#)|1 << 7 |DAMAGE_SPIKES  | Damage from spikes <br> |
|[ ](#)|1 << 8 |DAMAGE_CLONES  | Damage is done by clones when they took damage, avoid infinite loops <br> |
|[ ](#)|1 << 9 |DAMAGE_POOP  | Damage from red poop <br> |
|[ ](#)|1 << 10 |DAMAGE_DEVIL  | Damage comes from devil room deal <br> |
|[ ](#)|1 << 11 |DAMAGE_ISSAC_HEART  | Indicates the damage has been redirected from Isaac's Heart familiar <br> |
|[ ](#)|1 << 12 |DAMAGE_TNT  | Damage comes from a TNT barrel <br> |
|[ ](#)|1 << 13 |DAMAGE_INVINCIBLE  | Damages even if invincible (currently only for player). Used on IV Bag. <br> |
|[ ](#)|1 << 14 |DAMAGE_SPAWN_FLY  | Creates a fly when damage is applied <br> |
|[ ](#)|1 << 15 |DAMAGE_POISON_BURN  | Damage comes from POISON/BURN flags <br> |
|[ ](#)|1 << 16 |DAMAGE_CURSED_DOOR  | Damage comes from a cursed door <br> |
|[ ](#)|1 << 17 |DAMAGE_TIMER  | Damage comes from the passage of time (used for player damage by time limited special seeds) <br> |
|[ ](#)|1 << 18 |DAMAGE_IV_BAG  | Damage from using the IV Bag <br> |
|[ ](#)|1 << 19 |DAMAGE_PITFALL  | Damage comes from pitfalls (such as ones spawned by Little Horn) <br> |
|[ ](#)|1 << 20 |DAMAGE_CHEST  | Damage comes from spiked chest <br> |
|[ ](#)|1 << 21 |DAMAGE_FAKE  | Fake damage that should trigger player's damage effects. <br> |
|[ ](#)|1 << 22 |DAMAGE_BOOGER  | Damage from booger tear <br> |
|[ ](#)|1 << 23 |DAMAGE_SPAWN_BLACK_HEART  | Should drop a black heart if damage is lethal <br> |
|[ ](#)|1 << 24 |DAMAGE_CRUSH  | Damage comes from a strong impact, can damage Tuff Twins or The Shells' stony exteriors (like Mom's foot, shockwaves, rock tears) <br> |
|[ ](#)|1 << 25 |DAMAGE_NO_MODIFIERS  | Ignore damage modifiers (such as doubled damage from the Womb and later floors or reduced damage from the Wafer) <br> |
|[ ](#)|1 << 26 |DAMAGE_SPAWN_RED_HEART  | Should drop a red heart if damage is lethal <br> |
|[ ](#)|1 << 27 |DAMAGE_SPAWN_COIN  | Should drop a coin if damage is lethal <br> |
|[ ](#)|1 << 28 |DAMAGE_NO_PENALTIES  | Damage shouldn't apply any penalties (such as devil deal chance) <br> |
|[ ](#)|1 << 29 |DAMAGE_SPAWN_TEMP_HEART  | Should drop a half red heart that quickly despawns if damage is lethal <br> |
|[ ](#)|1 << 30 |DAMAGE_IGNORE_ARMOR  | Damage ignores boss armor <br> |
|[ ](#)|1 << 31 |DAMAGE_SPAWN_CARD  | Should drop a card if damage is lethal <br> |
|[ ](#)|1 << 32 |DAMAGE_SPAWN_RUNE  | Should drop a rune if damage is lethal <br> |
