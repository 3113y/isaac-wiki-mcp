---
title: Seeds
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 27
---

# Seeds

## Summary

管理游戏种子的类，提供种子效果、起始种子、种子格式转换与运行类型判断等功能。

## Related Types

- [[Level]]

## Key Methods

- [[#GetStartSeed|GetStartSeed]]
- [[#GetStartSeedString|GetStartSeedString]]
- [[#SetStartSeed|SetStartSeed]]
- [[#AddSeedEffect|AddSeedEffect]]
- [[#IsCustomRun|IsCustomRun]]

## Methods

### Functions

### AddSeedEffect {#AddSeedEffect}

```
void AddSeedEffect ( SeedEffect Value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

向当前运行添加一个种子效果（彩蛋），如 BASE MENT 等。

**Use Cases:**

- 动态启用某个特殊种子规则
- 测试多种种子效果组合

**See also:** 
[[#RemoveSeedEffect|RemoveSeedEffect]], [[#HasSeedEffect|HasSeedEffect]], [[#CanAddSeedEffect|CanAddSeedEffect]], [[#ClearSeedEffects|ClearSeedEffects]]


---

### CanAddSeedEffect {#CanAddSeedEffect}

```
boolean CanAddSeedEffect ( SeedEffect Value )
```

*DLC: REP, REP+ | Modifiers: const*

判断某个种子效果是否可以被添加（已解锁且未禁用组合）。

**Use Cases:**

- 在添加前校验种子效果的可用性
- 防止产生无效或冲突的彩蛋

**See also:** 
[[#AddSeedEffect|AddSeedEffect]], [[#HasSeedEffect|HasSeedEffect]], [[#IsSeedComboBanned|IsSeedComboBanned]]


---

### ClearSeedEffects {#ClearSeedEffects}

```
void ClearSeedEffects ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

移除当前所有已激活的种子效果。

**Use Cases:**

- 快速清空所有彩蛋
- 恢复到无特殊效果的运行

**See also:** 
[[#AddSeedEffect|AddSeedEffect]], [[#RemoveSeedEffect|RemoveSeedEffect]], [[#Reset|Reset]]


---

### ClearStartSeed {#ClearStartSeed}

```
void ClearStartSeed ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

清除当前运行的起始种子，恢复为随机种子。

**Use Cases:**

- 取消一个已设置的固定种子
- 让游戏选择随机起始种子

**See also:** 
[[#SetStartSeed|SetStartSeed]], [[#GetStartSeed|GetStartSeed]]


---

### CountSeedEffects {#CountSeedEffects}

```
int CountSeedEffects ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

返回当前激活的种子效果数量。

**Use Cases:**

- 显示已激活彩蛋的数量
- 检查是否已添加任何种子效果

**See also:** 
[[#AddSeedEffect|AddSeedEffect]], [[#HasSeedEffect|HasSeedEffect]]


---

### CountUnlockedSeedEffects {#CountUnlockedSeedEffects}

```
static int CountUnlockedSeedEffects ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

静态方法，返回所有存档中已解锁的种子效果总数。

**Use Cases:**

- 获取可用的彩蛋总量
- 用于收集进度统计

**See also:** 
[[#GetSeedEffect|GetSeedEffect]]


---

### ForgetStageSeed {#ForgetStageSeed}

```
void ForgetStageSeed ( LevelStage Stage )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

清除指定关卡（LevelStage）对应的关卡种子，使得该关卡重新随机生成。

**Use Cases:**

- 让已访问楼层在下一次进入时变化
- 调试特定楼层生成

**See also:** 
[[#ClearStageSeed|ClearStageSeed]], [[#GetStageSeed|GetStageSeed]]


---

### GetNextSeed {#GetNextSeed}

```
int GetNextSeed ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetNextSeed 完成对应 API 操作

**See also:** 



---

### GetPlayerInitSeed {#GetPlayerInitSeed}

```
int GetPlayerInitSeed ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetPlayerInitSeed 完成对应 API 操作

**See also:** 



---

### GetSeedEffect {#GetSeedEffect}

```
static SeedEffect GetSeedEffect ( string str )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetSeedEffect 完成对应 API 操作

**See also:** 



---

### GetStageSeed {#GetStageSeed}

```
int GetStageSeed ( LevelStage Stage )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetStageSeed 完成对应 API 操作

**See also:** 



---

### GetStartSeed {#GetStartSeed}

```
int GetStartSeed ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

The "start seed" is a number between 1 and (2^32 - 1) that is used to generate the random elements for the current run. The seed displayed in the pause menu is this number represented in string form.

The "start seed" is a number between 1 and (2^32 - 1) that is used to generate the random elements for the current run. The seed displayed in the pause menu is this number represented in string form.

**Use Cases:**

- 调用 GetStartSeed 完成对应 API 操作

**See also:** 



---

### GetStartSeedString {#GetStartSeedString}

```
string GetStartSeedString ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 GetStartSeedString 完成对应 API 操作

**See also:** 



---

### HasSeedEffect {#HasSeedEffect}

```
boolean HasSeedEffect ( SeedEffect Value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 HasSeedEffect 完成对应 API 操作

**See also:** 



---

### InitSeedInfo {#InitSeedInfo}

```
static void InitSeedInfo ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 InitSeedInfo 完成对应 API 操作

**See also:** 



---

### IsCustomRun {#IsCustomRun}

```
boolean IsCustomRun ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Returns true if the player is in a challenge run or a seeded run.

Returns true if the player is in a challenge run or a seeded run.

**Use Cases:**

- 调用 IsCustomRun 完成对应 API 操作

**See also:** 



---

### IsInitialized {#IsInitialized}

```
boolean IsInitialized ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 IsInitialized 完成对应 API 操作

**See also:** 



---

### IsSeedComboBanned {#IsSeedComboBanned}

```
boolean IsSeedComboBanned ( SeedEffect Seed1, SeedEffect Seed2 )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 IsSeedComboBanned 完成对应 API 操作

**See also:** 



---

### IsSpecialSeed {#IsSpecialSeed}

```
static boolean IsSpecialSeed ( string str )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 IsSpecialSeed 完成对应 API 操作

**See also:** 



---

### IsStringValidSeed {#IsStringValidSeed}

```
static boolean IsStringValidSeed ( string str )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 IsStringValidSeed 完成对应 API 操作

**See also:** 



---

### RemoveBlockingSeedEffects {#RemoveBlockingSeedEffects}

```
void RemoveBlockingSeedEffects ( SeedEffect Value )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Removes seeds that are banned in conjunction with the given seed.

Removes seeds that are banned in conjunction with the given seed.

**Use Cases:**

- 调用 RemoveBlockingSeedEffects 完成对应 API 操作

**See also:** 



---

### RemoveSeedEffect {#RemoveSeedEffect}

```
void RemoveSeedEffect ( SeedEffect Value )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 RemoveSeedEffect 完成对应 API 操作

**See also:** 



---

### Reset {#Reset}

```
void Reset ( )
```

*DLC: AB+, REP, REP+*

Removes all seed effects. Only takes effect when the run is restarted.

Removes all seed effects. Only takes effect when the run is restarted.

**Use Cases:**

- 调用 Reset 完成对应 API 操作

**See also:** 



---

### Restart {#Restart}

```
void Restart ( Challenge CurrentChallenge )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

Re-selects a random start seed, but only if the start seed was not custom.

Re-selects a random start seed, but only if the start seed was not custom.

**Use Cases:**

- 调用 Restart 完成对应 API 操作

**See also:** 



---

### Seed2String {#Seed2String}

```
static string Seed2String ( int seed )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

Turns a seed into its String representation as used for any in-game seed display.

Turns a seed into its String representation as used for any in-game seed display.

**Use Cases:**

- 调用 Seed2String 完成对应 API 操作

**See also:** 



---

### SetStartSeed {#SetStartSeed}

```
void SetStartSeed ( string StartSeed )
```

*DLC: AB+, REP | Modifiers: const*

Empty string means we will pick a new random seed.

Empty string means we will pick a new random seed.

**Use Cases:**

- 调用 SetStartSeed 完成对应 API 操作

**See also:** 



---

### String2Seed {#String2Seed}

```
static int String2Seed ( string str )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

___

___

**Use Cases:**

- 调用 String2Seed 完成对应 API 操作

**See also:** 



---

## See Also

- [[Level]]
