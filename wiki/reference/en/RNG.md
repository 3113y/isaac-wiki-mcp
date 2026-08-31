---
tags:
  - Globals
  - Class
---
# Class "RNG"

???+ info
    The RNG class provides a mechanism to produce seeded random numbers. This is used heavily by both the game and mods.

    This class can be accessed by using its constructor or the following function:

    * [Entity.GetDropRNG()](Entity.md#getdroprng)
    * [EntityPlayer.GetCardRNG()](EntityPlayer.md#getcardrng)
    * [EntityPlayer.GetCollectibleRNG()](EntityPlayer.md#getcollectiblerng)
    * [EntityPlayer.GetPillRNG()](EntityPlayer.md#getpillrng)
    * [EntityPlayer.GetTrinketRNG()](EntityPlayer.md#gettrinketrng)
    * [GridEntity.GetRNG()](GridEntity.md#getrng)
    * [GridEntityPreasurePlate.GreedModeRNG](GridEntityPressurePlate.md#greedmoderng)
    * [Level.GetDevilAngelRoomRNG()](Level.md#getdevilangelroomrng)

    ???+ example "Example Code"
        ```lua
        local myRNG = RNG()
        ```

## Constructors

### RNG () {: aria-label='Constructors' }
[ ](#){: .alldlc .tooltip .badge }
#### [RNG](RNG.md) RNG ( ) {: .copyable aria-label='Constructors' }

New RNG objects are always initialized with a seed of 2853650767. Thus, after invoking the constructor, you must set the seed of the new RNG object to the initial seed that you want. In some cases, this can just be a new random number between 1 and 4294967295. Use the `Random` global function to get a starting seed for these cases, (but check to make sure that values of 0 are not allowed, since that will crash the game). However, in most cases, seeding with a completely random number would be a bug in your mod, because all behavior in Isaac should be deterministic based on the starting seed of the run, or the seed of the level, or the seed of the room, and so on.

When setting the seed, it is recommended to use a shift index of 35, which is what most of the game's internal functions use. Document this number as a constant using SHOUTING_SNAKE_CASE so that you avoid using [magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)) in your program.

???+ example "Example code"
    ```lua
    -- This is the ShiftIdx that Blade recommended after having reviewing the game's internal functions.
    -- Any value between 0 and 80 (inclusive) should work equally well.
    -- https://www.jstatsoft.org/article/view/v008i14/xorshift.pdf
    local RECOMMENDED_SHIFT_IDX = 35

    local game = Game()
    local seeds = game:GetSeeds()
    local startSeed = seeds:GetStartSeed()
    local rng = RNG()
    rng:SetSeed(startSeed, RECOMMENDED_SHIFT_IDX)
    local myRandomNumber = rng:RandomInt(4) -- Will be either 0, 1, 2, or 3.
    ```

___
## Functions

<div class="rgon-extension" markdown="1">

### RNG () {: aria-label='Modified Constructors' }
#### [RNG](RNG.md) RNG ( int seed = 2853650767, int shiftIdx = 35 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Constructors' }
Accepts an optional seed and shiftIdx.
This avoids having to construct the RNG object separately from calling SetSeed.

Both the seed and shift index are validated.

___
## Modified Functions

</div>

### Get·Seed () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int GetSeed ( ) {: .copyable aria-label='Functions' }

Returns the current seed of the RNG object.

???- example "Get shift index example code"
    Isaac's API doesn't provide a way to get the shift index. Repentogon does, but if you don't have access to that then you can use the following function to find the game's default rng shift index values.

    ```lua
    local function getShiftIdx(rng)
      local seed = rng:GetSeed()
      local nexts = {}
      -- 18 seems to be the magic number here so you don't get false positives
      -- at 17, rng with seed=1,shiftIdx=53 returns a false positive of 52
      for i = 1, 18 do
        table.insert(nexts, rng:Next())
      end
      for i = 0, 80 do
        local rng2 = RNG()
        rng2:SetSeed(seed, i)
        for j, v in ipairs(nexts) do
          if v ~= rng2:Next() then
            break
          end
          if j == #nexts then
            -- reset the rng since it was modified with Next
            rng:SetSeed(seed, i)
            return i
          end
        end
      end
    end

    print(getShiftIdx(Game():GetLevel():GetDevilAngelRoomRNG())) -- prints: 2
    ```

___

### Next () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int Next ( ) {: .copyable aria-label='Functions' }

"Iterates" the RNG's seed to the next random number in the psuedo-random sequence. (The internal PRNG algorithm used is [Xorshift](https://en.wikipedia.org/wiki/Xorshift).)

___

### Random·Float () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### float RandomFloat ( ) {: .copyable aria-label='Functions' }
Returns a number between 0 and 1. This is inclusive on the lower end and exclusive on the higher end.

Note that this will automatically call the `RNG.Next` method before retrieving the random number. Since this mutates the RNG object, you should use this method with care.

???+ example "Example code"
    ```lua
    -- This is the ShiftIdx that Blade recommended after having reviewing the game's internal functions.
    -- Any value between 0 and 80 (inclusive) should work equally well.
    -- https://www.jstatsoft.org/article/view/v008i14/xorshift.pdf
    local RECOMMENDED_SHIFT_IDX = 35
    local MY_ENTITY_CHANCE = 0.3 -- 30%

    function shouldEntityDoThing(entity)
      local rng = RNG()
      rng:SetSeed(entity.InitSeed, RECOMMENDED_SHIFT_IDX)
      local randomChance = myRNG:RandomFloat()
      return randomChance < MY_ENTITY_CHANCE
    end
    ```
___

### Random·Int () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### int RandomInt ( int Max ) {: .copyable aria-label='Functions' }
Returns a number between 0 and the max value. It is inclusive on the lower end and exclusive on the higher end.

Note that this will automatically call the `RNG.Next` method before retrieving the random number. Since this mutates the RNG object, you should use this method with care.

???+ example "Example code"
    ```lua
    local RECOMMENDED_SHIFT_IDX = 35

    function getZeroOneTwoOrThree(seed)
      local rng = RNG()
      rng:SetSeed(seed, RECOMMENDED_SHIFT_IDX)
      return rng:RandomInt(4) -- Will generate 0, 1, 2, or 3.
    end
    ```
___

<div class="rgon-extension" markdown="1">

### RandomInt () {: aria-label='Modified Functions' }
#### int RandomInt ( int Min, int Max ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Can emulate `math.random` by accepting a second argument and generating an inclusive value between the two arguments. Negative values are supported in this mode, and the result is correctly bounded by `min` and `max` regardless of their signs.

___

</div>

### Set·Seed () {: aria-label='Functions' }
[ ](#){: .alldlc .tooltip .badge }
#### void SetSeed ( int Seed, int ShiftIdx ) {: .copyable aria-label='Functions' }
Set the seed of a given RNG object. Seed needs to be a positive integer number that is **not** 0. Otherwise it can cause crashes. ShiftIdx must be between 0 and 80 (inclusive) or it can cause crashes.

Shift index table can be found here: https://gist.github.com/bladecoding/17b341ed08ff94d2deb704ebda8ffc5f

???+ bug "Bug"
    If the seed of an RNG object is set to 0, the game will crash after invoking a method like `Next()`, `RandomInt()`, etc.


???+ example "Example code"
    ```lua
    local myRNG = RNG()
    myRNG:SetSeed(Random(), 1)
    ```

___

<div class="rgon-extension" markdown="1">

### SetSeed () {: aria-label='Modified Functions' }
#### void SetSeed ( int Seed, int ShiftIdx = 35 ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Modified Functions' }
Throws an error when Seed is negative.

Throws an error when ShiftIdx is outside the inclusive range 0–80.

ShiftIdx is optional and defaults to 35.

___
## Functions

</div>

<div class="rgon-only" markdown="1">

### GetShiftIdx () {: aria-label='Functions' }
#### int GetShiftIdx ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### PhantomFloat () {: aria-label='Functions' }
#### float PhantomFloat ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Generates a random float from `0` (inclusive) to `1` (exclusive).

Does not advance the RNG object's internal state.

___

### PhantomInt () {: aria-label='Functions' }
#### int PhantomInt ( int Max ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Behaves like RandomInt without advancing the RNG object's internal state.

___

### PhantomNext () {: aria-label='Functions' }
#### int PhantomNext ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### PhantomPrevious () {: aria-label='Functions' }
#### int PhantomPrevious ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### PhantomVector () {: aria-label='Functions' }
#### [Vector](Vector.md) PhantomVector ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a random vector of length `1`; multiply it by a number to obtain a larger random vector.

Does not advance the RNG object's internal state.

___

### Previous () {: aria-label='Functions' }
#### int Previous ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }

___

### RandomVector () {: aria-label='Functions' }
#### [Vector](Vector.md) RandomVector ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable aria-label='Functions' }
Returns a random vector of length `1`; multiply it by a number to obtain a larger random vector.

___

</div>
