---
tags:
  - Enum
---
# Enum "TearFlags"

Tearflag is defined as:
```lua
local function TEARFLAG(x)
	return x >= 64 and BitSet128(0,1<<(x-64)) or BitSet128(1<<x,0)
end
```

???+ tip "Bitset Calculator"
    [](#)

|DLC|Value|Enumerator|Ingame Color|Comment|
|:--|:--|:--|:--|:--|
|[ ](#)| [BitSet128](../BitSet128.md)(0,0) |TEAR_NORMAL  | `Color(1, 1, 1, 1, 0, 0, 0)`<br> Range 0-255: <br>`Color(255, 255, 255, 255, 0, 0, 0)` | Default tear (no special effects) |
|[ ](#)| TEARFLAG(0) |TEAR_SPECTRAL  | `Color(1.5, 2, 2, 0.5, 0, 0, 0)`<br> Range 0-255: <br>`Color(382, 510, 510, 127, 0, 0, 0)` | Ouija board type tear (goes thru obstacles) |
|[ ](#)| TEARFLAG(1) |TEAR_PIERCING  | No changes | Cupid's arrow type tear (goes thru enemy) |
|[ ](#)| TEARFLAG(2) |TEAR_HOMING  | `Color(0.4, 0.15, 0.38, 1, 0.27843, 0, 0.4549)` <br> Range 0-255: <br>`Color(102, 38, 97, 255, 71, 0, 116)` | Spoon bender type tear (homes to enemy) |
|[ ](#)| TEARFLAG(3) |TEAR_SLOW  | `Color(2, 2, 2, 1, 0.196, 0.196, 0.196)` <br> Range 0-255: <br>`Color(510, 510, 510, 255, 50, 50, 50)` | Spider bite type tear (slows on contact) |
|[ ](#)| TEARFLAG(4) |TEAR_POISON  | `Color(0.4, 0.97, 0.5, 1, 0, 0, 0)`<br> Range 0-255: <br>`Color(102, 247, 127, 255, 0, 0, 0)` | Common cold type tear (poisons on contact) |
|[ ](#)| TEARFLAG(5) |TEAR_FREEZE  | `Color(1.25, 0.05, 0.15, 1, 0, 0, 0)`<br> Range 0-255: <br>`Color(318, 13, 38, 255, 0, 0, 0)` | Mom's contact type tear (freezes on contact) |
|[ ](#)| TEARFLAG(6) |TEAR_SPLIT  | `Color(0.9, 0.3, 0.08, 1, 0, 0, 0)`<br> Range 0-255: <br>`Color(229, 76, 20, 255, 0, 0, 0)` | Parasite type tear (splits on collision) |
|[ ](#)| TEARFLAG(7) |TEAR_GROW  | `Color(0.2, 0.09, 0.06, 1, 0, 0, 0)`<br> Range 0-255: <br>`Color(51, 23, 17, 255, 0, 0, 0)` | Lump of coal type tear (grows by range) |
|[ ](#)| TEARFLAG(8) |TEAR_BOOMERANG  | No changes | My reflection type tear (returns back) <br> (ab+: TearFlags.TEAR_BOMBERANG) |
|[ ](#)| TEARFLAG(9) |TEAR_PERSISTENT  | No changes | Polyphemus type tear (Damages the entity and if the damage is more then enemy hp it continues with less damage) |
|[ ](#)| TEARFLAG(10) |TEAR_WIGGLE  | No changes | Wiggle worm type tear (wiggles) |
|[ ](#)| TEARFLAG(11) |TEAR_MULLIGAN  | No changes | Mulligan type tear (creates fly on hit) <br> (ab+: TearFlags.TEAR_MIGAN) |
|[ ](#)| TEARFLAG(12) |TEAR_EXPLOSIVE  | `Color(0.5, 0.9, 0.4, 1, 0, 0, 0)`<br> Range 0-255: <br>`Color(127, 229, 102, 255, 0, 0, 0)` | IPECAC type tear (explodes on hit) |
|[ ](#)| TEARFLAG(13) |TEAR_CHARM  | `Color(1, 0, 1, 1, 0.196, 0, 0)`<br> Range 0-255: <br>`Color(255, 0, 255, 255, 50, 0, 0)` | Mom's Eyeshadow tear |
|[ ](#)| TEARFLAG(14) |TEAR_CONFUSION  | `Color(0.5, 0.5, 0.5, 1, 0, 0, 0)`<br> Range 0-255: <br>`Color(127, 127, 127, 255, 0, 0, 0)` | Iron Bar tear |
|[ ](#)| TEARFLAG(15) |TEAR_HP_DROP  | No changes | These tears cause enemy to drop hearts if killed (33% chance). |
|[ ](#)| TEARFLAG(16) |TEAR_ORBIT  | No changes | Used for Tiny Planet (orbit arounds the player) |
|[ ](#)| TEARFLAG(17) |TEAR_WAIT  | No changes | Anti gravity type tear (floats in place for some time before finally moving) (unset after first update) |
|[ ](#)| TEARFLAG(18) |TEAR_QUADSPLIT  | No changes | Cricket's Body type tear. Splits into 4 smaller tears if it hits the ground |
|[ ](#)| TEARFLAG(19) |TEAR_BOUNCE  | `Color(1, 1, 0.8, 1, 0.1, 0.1, 0.1)`<br> Range 0-255: <br>`Color(255, 255, 204, 255, 25, 25, 25)` | Bounce off of enemies, walls, rocks (Higher priority than PERSISTENT & PIERCING) |
|[ ](#)| TEARFLAG(20) |TEAR_FEAR  | `Color(1, 1, 0.455, 1, 0.169, 0.145, 0)`<br> Range 0-255: <br>`Color(255, 255, 116, 255, 43, 37, 0)` | Mom's Perfume type tear of fear (fear on contact) |
|[ ](#)| TEARFLAG(21) |TEAR_SHRINK  | No changes | Proptosis tears start large and shrink |
|[ ](#)| TEARFLAG(22) |TEAR_BURN  | `Color(1, 1, 1, 1, 0.3, 0, 0)`<br> Range 0-255: <br>`Color(255, 255, 255, 255, 76, 0, 0)` | Fire Mind tears cause Burn effect on enemies |
|[ ](#)| TEARFLAG(23) |TEAR_ATTRACTOR  | No changes | Attracts enemies and pickups |
|[ ](#)| TEARFLAG(24) |TEAR_KNOCKBACK  | No changes | Tear impact pushes enemies back further |
|[ ](#)| TEARFLAG(25) |TEAR_PULSE  | No changes | Makes the tear pulse |
|[ ](#)| TEARFLAG(26) |TEAR_SPIRAL  | No changes | Makes the tear path spiral |
|[ ](#)| TEARFLAG(27) |TEAR_FLAT  | No changes | Makes the tear oval in the direction of travel |
|[ ](#)| TEARFLAG(28) |TEAR_SAD_BOMB  | No changes | Used by Bombs (Sad Bomb) |
|[ ](#)| TEARFLAG(29) |TEAR_BUTT_BOMB  | No changes | Used by Bombs (Butt Bomb) |
|[ ](#)| TEARFLAG(30) |TEAR_SQUARE  | No changes | Used for Hook Worm |
|[ ](#)| TEARFLAG(31) |TEAR_GLOW  | No changes | Used for GodHead (they will have a glow around them) |
|[ ](#)| TEARFLAG(32) |TEAR_GISH  | `Color(0.15, 0.15, 0.15, 1, 0, 0, 0)`<br> Range 0-255: <br>`Color(38, 38, 38, 255, 0, 0, 0)` | Used for Gish player tears (to color enemy black on slowing) |
|[ ](#)| TEARFLAG(33) |TEAR_MYSTERIOUS_LIQUID_CREEP  | `Color(1, 1, 1, 1, 0, 0.2, 0)`<br> Range 0-255: <br>`Color(255, 255, 255, 255, 0, 51, 0)` | Mysterious Liquid tears spawn damaging green creep when hit |
|[ ](#)| TEARFLAG(34) |TEAR_SHIELDED  | No changes | Lost Contact tears, block enemy projectiles |
|[ ](#)| TEARFLAG(35) |TEAR_GLITTER_BOMB  | No changes | Used by Bombs (Glitter Bomb) |
|[ ](#)| TEARFLAG(36) |TEAR_SCATTER_BOMB  | No changes | Used for Scatter bombs |
|[ ](#)| TEARFLAG(37) |TEAR_STICKY  | No changes | Used for Sticky bombs and Explosivo tears |
|[ ](#)| TEARFLAG(38) |TEAR_CONTINUUM  | Initializes with either <br>`Color(1, 1, 1, 1, 0, 0, 0)`<br>or<br>`Color(0, 0, 0, 1, 0, 0, 0)`<br> the purple color is handled on the fly by the game | Tears loop around the screen |
|[ ](#)| TEARFLAG(39) |TEAR_LIGHT_FROM_HEAVEN  | No changes | Create damaging light beam on hit |
|[ ](#)| TEARFLAG(40) |TEAR_COIN_DROP  | No changes | Used by Bumbo, spawns a coin when tear hits |
|[ ](#)| TEARFLAG(41) |TEAR_BLACK_HP_DROP  | No changes | Enemy drops a black hp when dies |
|[ ](#)| TEARFLAG(42) |TEAR_TRACTOR_BEAM  | No changes | Tear with this flag will follow parent player's beam |
|[ ](#)| TEARFLAG(43) |TEAR_GODS_FLESH  | No changes | God's flesh flag to minimize enemies |
|[ ](#)| TEARFLAG(44) |TEAR_GREED_COIN  | No changes | Greed coin tears that has a chance to generate a coin when hit |
|[ ](#)| TEARFLAG(45) |TEAR_CROSS_BOMB  | No changes | Bomber Boy |
|[ ](#)| TEARFLAG(46) |TEAR_BIG_SPIRAL  | No changes | Ouroboros Worm, big radius oscilating tears |
|[ ](#)| TEARFLAG(47) |TEAR_PERMANENT_CONFUSION  | No changes | Glaucoma tears, permanently confuses enemies |
|[ ](#)| TEARFLAG(48) |TEAR_BOOGER  | No changes | Booger tears, stick and do damage over time |
|[ ](#)| TEARFLAG(49) |TEAR_EGG  | No changes | Egg tears, leave creep and spawns spiders or flies |
|[ ](#)| TEARFLAG(50) |TEAR_ACID  | No changes | Sulfuric Acid tears, can break grid entities |
|[ ](#)| TEARFLAG(51) |TEAR_BONE  | No changes | Bone tears, splits in 2 |
|[ ](#)| TEARFLAG(52) |TEAR_BELIAL  | No changes | Belial tears, piecing tears gets double damage + homing |
|[ ](#)| TEARFLAG(53) |TEAR_MIDAS  | No changes | Midas touch tears |
|[ ](#)| TEARFLAG(54) |TEAR_NEEDLE  | No changes | Needle tears |
|[ ](#)| TEARFLAG(55) |TEAR_JACOBS  | No changes | Jacobs ladder tears |
|[ ](#)| TEARFLAG(56) |TEAR_HORN  | `Color(0, 0, 0, 1, 0, 0, 0)`<br> Range 0-255: <br>`Color(0, 0, 0, 255, 0, 0, 0)` | Little Horn tears |
|[ ](#)| TEARFLAG(57) |TEAR_LASER  | No changes | Technology Zero |
|[ ](#)| TEARFLAG(58) |TEAR_POP  | No changes | Pop! |
|[ ](#)| TEARFLAG(59) |TEAR_ABSORB  | No changes | Lachryphagy like tears. Hungry Tears |
|[ ](#)| TEARFLAG(60) |TEAR_LASERSHOT  | No changes | Trisagion, generates a laser on top of the tear |
|[ ](#)| TEARFLAG(61) |TEAR_HYDROBOUNCE  | No changes | Flat Stone |
|[ ](#)| TEARFLAG(62) |TEAR_BURSTSPLIT  | No changes | Haemolacria |
|[ ](#)| TEARFLAG(63) |TEAR_CREEP_TRAIL  | No changes | Bob's Bladder |
|[ ](#)| TEARFLAG(64) |TEAR_PUNCH  | No changes | Knockout Drops |
|[ ](#)| TEARFLAG(65) |TEAR_ICE  | No changes | Uranus |
|[ ](#)| TEARFLAG(66) |TEAR_MAGNETIZE  | No changes | Lodestone |
|[ ](#)| TEARFLAG(67) |TEAR_BAIT  | `Color(0.7, 0.14, 0.1, 1, 0.3, 0, 0)`<br> Range 0-255: <br>`Color(178, 35, 25, 255, 76, 0, 0)` | Rotten Tomato |
|[ ](#)| TEARFLAG(68) |TEAR_OCCULT  | No changes | Eye of the Occult |
|[ ](#)| TEARFLAG(69) |TEAR_ORBIT_ADVANCED  | No changes | Orbiting tears with a more narrow and stable orbit (used by Saturnus and Immaculate Heart) |
|[ ](#)| TEARFLAG(70) |TEAR_ROCK  | No changes | Rock tears, chance to break rocks, deal extra damage to rock type enemies |
|[ ](#)| TEARFLAG(71) |TEAR_TURN_HORIZONTAL  | No changes | Brain Worm, tears turn and go horizontally when moving past an enemy |
|[ ](#)| TEARFLAG(72) |TEAR_BLOOD_BOMB  | No changes | Blood Bombs, leave blood creep on the ground |
|[ ](#)| TEARFLAG(73) |TEAR_ECOLI  | No changes | E. Coli tears, turn enemies into poop |
|[ ](#)| TEARFLAG(74) |TEAR_COIN_DROP_DEATH  | No changes | Killed enemies have a chance to drop a random coin (Reverse Hanged Man) |
|[ ](#)| TEARFLAG(75) |TEAR_BRIMSTONE_BOMB  | No changes | Brimstone Bombs, explosion creates a brimstone cross |
|[ ](#)| TEARFLAG(76) |TEAR_RIFT  | `Color(0, 0, 0, 1, 0, 0, 0)`<br> Range 0-255: <br>`Color(0, 0, 0, 255, 0, 0, 0)` | Rift tears, creates a black hole on impact |
|[ ](#)| TEARFLAG(77) |TEAR_SPORE  | No changes | Spore tears, stick to enemies and multiply on enemy death |
|[ ](#)| TEARFLAG(78) |TEAR_GHOST_BOMB  | No changes | Ghost bombs |
|[ ](#)| TEARFLAG(79) |TEAR_CARD_DROP_DEATH  | No changes | Killed enemies will drop a random tarot card |
|[ ](#)| TEARFLAG(80) |TEAR_RUNE_DROP_DEATH  | No changes | Killed enemies will drop a random rune |
|[ ](#)| TEARFLAG(81) |TEAR_TELEPORT  | No changes | Hit enemies will teleport to a different part of the room |
|[ ](#)| TEARFLAG(82) |TEAR_DECELERATE  | No changes | Decelerate over time |
|[ ](#)| TEARFLAG(83) |TEAR_ACCELERATE  | No changes | Accelerate over time |
|[ ](#)| 84 |TEAR_EFFECT_COUNT  | No changes |  |


The following flags are reserved at the top end of the bitset, and cannot be selected randomly by any items that may attempt to do so.

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)| TEARFLAG(104) | TEAR_BOUNCE_WALLSONLY  | Similar to TEAR_BOUNCE but only bounces off walls, not enemies |
|[ ](#)| TEARFLAG(105) | TEAR_NO_GRID_DAMAGE  | Cannot deal damage to grid entities (used by Saturnus to prevent unfair damage in some rooms) |
|[ ](#)| TEARFLAG(106) | TEAR_BACKSTAB  | Deals extra damage from behind and inflicts bleeding |
|[ ](#)| TEARFLAG(107) | TEAR_FETUS_SWORD  | Fetuses whack their target with a sword and perform spin attacks |
|[ ](#)| TEARFLAG(108) | TEAR_FETUS_BONE  | Fetuses whack their target with a bone club instead of ramming into them |
|[ ](#)| TEARFLAG(109) | TEAR_FETUS_KNIFE  | Fetuses carry a knife |
|[ ](#)| TEARFLAG(110) | TEAR_FETUS_TECHX  | Fetuses have a Tech X ring around them |
|[ ](#)| TEARFLAG(111) | TEAR_FETUS_TECH  | Fetuses keep their distance and occasionally shoot tech lasers at their target |
|[ ](#)| TEARFLAG(112) | TEAR_FETUS_BRIMSTONE  | Fetuses shoot a brimstone beam at the first enemy they hit |
|[ ](#)| TEARFLAG(113) | TEAR_FETUS_BOMBER  | Fetuses drop a bomb on their first impact with an enemy |
|[ ](#)| TEARFLAG(114) | TEAR_FETUS  | Base flag for C Section fetuses |
|[ ](#)| TEARFLAG(115) | TEAR_REROLL_ROCK_WISP  |  |
|[ ](#)| TEARFLAG(116) | TEAR_MOM_STOMP_WISP  |  |
|[ ](#)| TEARFLAG(117) | TEAR_ENEMY_TO_WISP  |  |
|[ ](#)| TEARFLAG(118) | TEAR_REROLL_ENEMY  | D10 Wisps, chance to reroll enemy on hit |
|[ ](#)| TEARFLAG(119) | TEAR_GIGA_BOMB  | Causes giant explosions that create holes in the ground (for Giga Bombs) |
|[ ](#)| TEARFLAG(120) | TEAR_EXTRA_GORE  | Causes enemies to explode into more gibs on death (for Donkey Jawbone) |
|[ ](#)| TEARFLAG(121) | TEAR_RAINBOW  | Causes lasers to visually cycle between rainbow colors |
|[ ](#)| TEARFLAG(122) | TEAR_DETONATE  | Can be detonated by Remote Detonator |
|[ ](#)| TEARFLAG(123) | TEAR_CHAIN  | Akeldama tears, stick to each other and form a chain that can be swung around |
|[ ](#)| TEARFLAG(124) | TEAR_DARK_MATTER  | Used to identify Dark Matter tears |
|[ ](#)| TEARFLAG(125) | TEAR_GOLDEN_BOMB  | Used to identify bombs dropped while having a golden bomb |
|[ ](#)| TEARFLAG(126) | TEAR_FAST_BOMB  | Used to identify bombs dropped while having Fast Bombs |
|[ ](#)| TEARFLAG(127) | TEAR_LUDOVICO  | Used as a weapon for Ludovico Technique |
