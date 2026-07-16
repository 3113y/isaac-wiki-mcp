---
tags:
  - Enum
---
# Enum "ItemConfig"

The "ItemConfig" Class has separate Enums that are used for special information handling.

Even though they have different prefixes, all enums on this page are part of the "**ItemConfig**" enum.

???+ example "Example usage:"

    ```lua
    local sadOnionConfig = Isaac.GetItemConfig():GetCollectible(1)
    if sadOnionConfig.Tags & ItemConfig.TAG_SUMMONABLE == ItemConfig.TAG_SUMMONABLE then
        print("This item has the tag 'summonable'")
    end
    ```

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|0 |CHARGE_NORMAL  |  |
|[ ](#)|1 |CHARGE_TIMED  |  |
|[ ](#)|2 |CHARGE_SPECIAL  |  |

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|0 |CARDTYPE_TAROT  | Tarot cards |
|[ ](#)|1 |CARDTYPE_SUIT  | Standard playing cards (twos, aces and Joker, does not include Suicide King, Rules Card or Queen of Hearts) |
|[ ](#)|2 |CARDTYPE_RUNE  | Runes |
|[ ](#)|3 |CARDTYPE_SPECIAL  | Special cards (anything that doesn't fall in the above categories excludes non-cards such as Dice Shard, see below) |
|[ ](#)|4 |CARDTYPE_SPECIAL_OBJECT  | Special pocket items that do not qualify as "cards" |
|[ ](#)|5 |CARDTYPE_TAROT_REVERSE  | Reversed tarot cards |

|DLC|Value|Enumerator|Comment|
|:--|:--|:--|:--|
|[ ](#)|1 << 0 |TAG_DEAD  | Dead things (for the Parasite unlock) |
|[ ](#)|1 << 1 |TAG_SYRINGE  | Syringes (for Little Baggy and the Spun! transformation) |
|[ ](#)|1 << 2 |TAG_MOM  | Mom's things (for Mom's Contact and the Yes Mother? transformation) |
|[ ](#)|1 << 3 |TAG_TECH  | Technology items (for the Technology Zero unlock) |
|[ ](#)|1 << 4 |TAG_BATTERY  | Battery items (for the Jumper Cables unlock) |
|[ ](#)|1 << 5 |TAG_GUPPY  | Guppy items (Guppy transformation) |
|[ ](#)|1 << 6 |TAG_FLY  | Fly items (Beelzebub transformation) |
|[ ](#)|1 << 7 |TAG_BOB  | Bob items (Bob transformation) |
|[ ](#)|1 << 8 |TAG_MUSHROOM  | Mushroom items (Fun Guy transformation) |
|[ ](#)|1 << 9 |TAG_BABY  | Baby items (Conjoined transformation) |
|[ ](#)|1 << 10 |TAG_ANGEL  | Angel items (Seraphim transformation) |
|[ ](#)|1 << 11 |TAG_DEVIL  | Devil items (Leviathan transformation) |
|[ ](#)|1 << 12 |TAG_POOP  | Poop items (Oh Shit transformation) |
|[ ](#)|1 << 13 |TAG_BOOK  | Book items (Book Worm transformation) |
|[ ](#)|1 << 14 |TAG_SPIDER  | Spider items (Spider Baby transformation) |
|[ ](#)|1 << 15 |TAG_QUEST  | Quest item (cannot be rerolled or randomly obtained) |
|[ ](#)|1 << 16 |TAG_MONSTER_MANUAL  | Can be spawned by Monster Manual |
|[ ](#)|1 << 17 |TAG_NO_GREED  | Cannot appear in Greed Mode |
|[ ](#)|1 << 18 |TAG_FOOD  | Food item (for Binge Eater) |
|[ ](#)|1 << 19 |TAG_TEARS_UP  | Tears up item (for Lachryphagy unlock detection) |
|[ ](#)|1 << 20 |TAG_OFFENSIVE  | Whitelisted item for Lost B |
|[ ](#)|1 << 21 |TAG_NO_KEEPER  | Blacklisted item for Keeper/Keeper B |
|[ ](#)|1 << 22 |TAG_NO_LOST_BR  | Blacklisted item for Lost's Birthright |
|[ ](#)|1 << 23 |TAG_STARS  | Star themed items (for the Planetarium unlock) |
|[ ](#)|1 << 24 |TAG_SUMMONABLE  | Summonable items (for Bethany B) |
|[ ](#)|1 << 25 |TAG_NO_CANTRIP  | Can't be obtained in Cantripped challenge |
|[ ](#)|1 << 26 |TAG_WISP  | Active items that have wisps attached to them (automatically set) |
|[ ](#)|1 << 27 |TAG_UNIQUE_FAMILIAR  | Unique familiars that cannot be duplicated |
|[ ](#)|1 << 28 |TAG_NO_CHALLENGE  | Items that shouldn't be obtainable in challenges |
|[ ](#)|1 << 29 |TAG_NO_DAILY  | Items that shouldn't be obtainable in daily runs |
|[ ](#)|1 << 30 |TAG_LAZ_SHARED  | Items that should be shared between Tainted Lazarus' forms |
|[ ](#)|1 << 31 |TAG_LAZ_SHARED_GLOBAL  | Items that should be shared between Tainted Lazarus' forms but only through global checks (such as PlayerManager::HasCollectible) |
|[ ](#)|1 << 32 |TAG_NO_EDEN  | Items that can't be randomly rolled |
