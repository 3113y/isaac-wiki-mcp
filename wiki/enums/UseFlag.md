---
tags:
  - Enum
---
# Enum "UseFlag"

???+ tip "Bitset Calculator"
    [](#)

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|1 << 0 |USE_NOANIM  | Don't play use animations |
|[ ](#)|1 << 1 |USE_NOCOSTUME  | Don't add costume |
|[ ](#)|1 << 2 |USE_OWNED  | Effect was triggered by an active item owned by the player |
|[ ](#)|1 << 3 |USE_ALLOWNONMAIN  | Allow the effect to trigger on non-main players (i.e. coop babies) |
|[ ](#)|1 << 4 |USE_REMOVEACTIVE  | D4 only: Reroll the player's active item |
|[ ](#)|1 << 5 |USE_CARBATTERY  | Effect was triggered a second time by Car Battery (or Tarot Cloth for cards) |
|[ ](#)|1 << 6 |USE_VOID  | Effect was triggered by Void |
|[ ](#)|1 << 7 |USE_MIMIC  | Effect was mimicked by an active item (Blank Card, Placebo) |
|[ ](#)|1 << 8 |USE_NOANNOUNCER  | Never play announcer voice |
|[ ](#)|1 << 9 |USE_ALLOWWISPSPAWN  | This allows an item to spawn wisps when called from another item usage as the wisps generator checks for NOANIM, so usually you want to use this with NOANIM call |
|[ ](#)|1 << 10 |USE_CUSTOMVARDATA  | If set, forces UseActiveItem to use the CustomVarData argument instead of the active item's stored VarData |
|[ ](#)|1 << 11 |USE_NOHUD  | Don't display text in the HUD (this is currently only used by Echo Chamber) |
