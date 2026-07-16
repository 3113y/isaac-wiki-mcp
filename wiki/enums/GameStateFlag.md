---
tags:
  - Enum
---
# Enum "GameStateFlag"
|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|0 |STATE_FAMINE_SPAWNED  | Repurposed as "angel room spawned" in Rep. This doesn't seem to do anything with Famine anymore. |
|[ ](#)|1 |STATE_PESTILENCE_SPAWNED  | obsolete with Rep |
|[ ](#)|2 |STATE_WAR_SPAWNED  | obsolete with Rep |
|[ ](#)|3 |STATE_DEATH_SPAWNED  | obsolete with Rep |
|[ ](#)|4 |STATE_BOSSPOOL_SWITCHED  | Repurposed as "left from starting room" in Rep. Used to check if the coop player should spawn as a coop baby or normal character. |
|[ ](#)|5 |STATE_DEVILROOM_SPAWNED  | By default, "devil room spawned" is false which gives 100% devil chance on stage 2. When the devil room spawns, "devil room spawned" is set to true. If you visit the devil room then "devil room visited" is set to true and your devil/angel chance will be 50/50 (assuming you don't pick up a devil item). If you don't visit the devil room then "devil room visited" stays false and the next time you'll get a guaranteed angel room. Once that angel room spawns, "angel room spawned" is set to true so angel rooms don't continue to be guaranteed. |
|[ ](#)|6 |STATE_DEVILROOM_VISITED  |  |
|[ ](#)|7 |STATE_BOOK_REVELATIONS_USED  |  |
|[ ](#)|8 |STATE_BOOK_PICKED_UP  |  |
|[ ](#)|9 |STATE_WRATH_SPAWNED  |  |
|[ ](#)|10 |STATE_GLUTTONY_SPAWNED  |  |
|[ ](#)|11 |STATE_LUST_SPAWNED  |  |
|[ ](#)|12 |STATE_SLOTH_SPAWNED  |  |
|[ ](#)|13 |STATE_ENVY_SPAWNED  |  |
|[ ](#)|14 |STATE_PRIDE_SPAWNED  |  |
|[ ](#)|15 |STATE_GREED_SPAWNED  |  |
|[ ](#)|16 |STATE_SUPERGREED_SPAWNED  |  |
|[ ](#)|17 |STATE_DONATION_SLOT_BROKEN  |  |
|[ ](#)|18 |STATE_DONATION_SLOT_JAMMED  |  |
|[ ](#)|19 |STATE_HEAVEN_PATH  | Flips to true when you take a heaven light door in the womb ii (taking you to the cathedral instead of sheol). Does not flip back to false if you replay the womb ii and take a trapdoor. |
|[ ](#)|20 |STATE_REBIRTH_BOSS_SWITCHED  | obsolete with Rep |
|[ ](#)|21 |STATE_HAUNT_SELECTED  | obsolete with Rep |
|[ ](#)|22 |STATE_ADVERSARY_SELECTED  | obsolete with Rep |
|[ ](#)|23 |STATE_MR_FRED_SELECTED  | obsolete with Rep |
|[ ](#)|24 |STATE_MAMA_GURDY_SELECTED  | obsolete with Rep |
|[ ](#)|25 |STATE_URIEL_SPAWNED  |  |
|[ ](#)|26 |STATE_GABRIEL_SPAWNED  |  |
|[ ](#)|27 |STATE_FALLEN_SPAWNED  |  |
|[ ](#)|28 |STATE_HEADLESS_HORSEMAN_SPAWNED  | obsolete with Rep |
|[ ](#)|29 |STATE_KRAMPUS_SPAWNED  |  |
|[ ](#)|30 |STATE_DONATION_SLOT_BLOWN  |  |
|[ ](#)|31 |STATE_SHOPKEEPER_KILLED  |  |
|[ ](#)|32 |STATE_ULTRAPRIDE_SPAWNED  |  |
|[ ](#)|33 |STATE_BOSSRUSH_DONE  |  |
|[ ](#)|34 |STATE_GREED_SLOT_JAMMED  |  |
|[ ](#)|35 |STATE_AFTERBIRTH_BOSS_SWITCHED  | obsolete with Rep |
|[ ](#)|36 |STATE_BROWNIE_SELECTED  | obsolete with Rep |
|[ ](#)|37 |STATE_SUPERBUM_APPEARED  |  |
|[ ](#)|38 |STATE_BOSSRUSH_DOOR_SPAWNED  |  |
|[ ](#)|39 |STATE_BLUEWOMB_DOOR_SPAWNED  |  |
|[ ](#)|40 |STATE_BLUEWOMB_DONE  |  |
|[ ](#)|41 |STATE_HEART_BOMB_COIN_PICKED  |  |
|[ ](#)|42 |STATE_ABPLUS_BOSS_SWITCHED  | obsolete with Rep |
|[ ](#)|43 |STATE_SISTERS_VIS_SELECTED  | obsolete with Rep |
|[ ](#)|43 |STATE_MAX_COINS_OBTAINED  | set when reaching 99 coins, used to check for the Golden Razor achievement |
|[ ](#)|44 |STATE_SECRET_PATH  | set when entering a trapdoor that leads to the alternate path |
|[ ](#)|45 |STATE_PERFECTION_SPAWNED  | set when Perfection has dropped from a boss |
|[ ](#)|46 |STATE_MAUSOLEUM_HEART_KILLED  | set when Mom's Heart has been killed in the Mausoleum |
|[ ](#)|47 |STATE_BACKWARDS_PATH_INIT  | set when entering Mausoleum/Gehenna II through the photo door, causes Dad's Note to spawn instead of the Mom boss room |
|[ ](#)|48 |STATE_BACKWARDS_PATH  | set during the Ascent |
|[ ](#)|49 |NUM_STATE_FLAGS  |  |
|[ ](#)|49 |STATE_MEGA_SATAN_DOOR_OPENED  |  |
|[ ](#)|50 |STATE_URIEL_KILLED  |  |
|[ ](#)|51 |STATE_GABRIEL_KILLED  |  |
|[ ](#)|52 |STATE_MOTHER_HEART_DOOR_OPENED  |  |
|[ ](#)|53 |NUM_STATE_FLAGS  |  |