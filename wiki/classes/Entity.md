---
title: Entity
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 100
---

# Entity

## Summary

Entity 是所有实体的基类，提供生命/伤害管理、状态效果施加（燃烧、魅惑、混乱等）、属性修改、父子链查询、渲染控制、类型转换及大量可读写属性。

- Subclasses:
  - [[EntityBomb]]
  - [[EntityEffect]]
  - [[EntityFamiliar]]
  - [[EntityKnife]]
  - [[EntityLaser]]
  - [[EntityNPC]]
  - [[EntityPickup]]
  - [[EntityPlayer]]
  - [[EntityProjectile]]
  - [[EntityTear]]

## Related Types

- [[Color]]
- [[EntityBomb]]
- [[EntityEffect]]
- [[EntityFamiliar]]
- [[EntityKnife]]
- [[EntityLaser]]
- [[EntityNPC]]
- [[EntityPickup]]
- [[EntityPlayer]]
- [[EntityProjectile]]
- [[EntityRef]]
- [[EntityTear]]
- [[RNG]]
- [[Sprite]]
- [[Vector]]

## Key Methods

- [[#AddBurn|AddBurn]]
- [[#Die|Die]]
- [[#GetData|GetData]]
- [[#TakeDamage|TakeDamage]]

## Methods

### Functions

### AddBurn {#AddBurn}

```
void AddBurn ( EntityRef Source, int Duration, float Damage )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为实体添加燃烧效果，指定伤害来源、持续帧数和每帧伤害。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 对全房间敌人造成持续火焰伤害
- 配合 IgnoreBosses 控制是否影响首领

**See also:** 
[[#AddPoison|AddPoison]], [[#AddFreeze|AddFreeze]], [[#AddMidasFreeze|AddMidasFreeze]]


---

### void AddBurn ( [EntityRef](EntityRef.md) Source, int Duration, float Damage, boolean IgnoreBosses ) {#void AddBurn ( [EntityRef](EntityRef.md) Source, int Duration, float Damage, boolean IgnoreBosses )}

```
void AddCharmed ( EntityRef sourceEntity, int Duration )
```

*DLC: REP, REP+ | Modifiers: const*

为实体添加燃烧效果，并可指定是否忽略首领。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 对非首领敌人施加燃烧
- 控制状态效果对首领的豁免

**See also:** 
[[#AddBurn|AddBurn]], [[#AddPoison|AddPoison]], [[#AddCharmed|AddCharmed]], [[#AddFear|AddFear]]


---

### void AddCharmed ( [EntityRef](EntityRef.md) sourceEntity, int Duration, boolean IgnoreBosses ) {#void AddCharmed ( [EntityRef](EntityRef.md) sourceEntity, int Duration, boolean IgnoreBosses )}

```
void AddConfusion ( EntityRef Source, int Duration, boolean IgnoreBosses )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为实体添加魅惑效果，指定持续帧数并可忽略首领。

**Use Cases:**

- 让敌人暂时帮助玩家战斗
- 永久魅惑（Duration=-1）让敌人跟随换房

**See also:** 
[[#AddCharmed|AddCharmed]], [[#AddConfusion|AddConfusion]], [[#AddFear|AddFear]], [[#Die|Die]]


---

### AddEntityFlags {#AddEntityFlags}

```
void AddEntityFlags ( int Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为实体添加实体标记（按位拼接），用于附加如友好、免伤等特殊效果。

**Use Cases:**

- 给实体加 FLAG_SLOW | FLAG_CONFUSION
- 实现自定义状态效果组合

**See also:** 
[[#ClearEntityFlags|ClearEntityFlags]], [[#GetEntityFlags|GetEntityFlags]], [[#HasEntityFlags|HasEntityFlags]]


---

### AddFear {#AddFear}

```
void AddFear ( EntityRef Source, int Duration )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为实体添加恐惧效果，指定持续帧数。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 使敌人逃跑
- 短暂控制敌人行动

**See also:** 
[[#AddCharmed|AddCharmed]], [[#AddFreeze|AddFreeze]], [[#AddConfusion|AddConfusion]]


---

### void AddFear ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses ) {#void AddFear ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses )}

```
void AddFreeze ( EntityRef Source, int Duration )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

为实体添加恐惧效果，并可指定是否忽略首领。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 仅恐惧普通敌人
- 组合其他状态效果

**See also:** 
[[#AddFear|AddFear]], [[#AddBurn|AddBurn]], [[#AddSlowing|AddSlowing]]


---

### void AddFreeze ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses ) {#void AddFreeze ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses )}

```
void AddHealth ( float HitPoints )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为实体恢复生命值。

为实体恢复生命值.

**Use Cases:**

- 治疗玩家或随从
- 修改敌人生命值以实现特殊机制

**See also:** 
[[#AddHealth|AddHealth]], [[#HitPoints|HitPoints]], [[#MaxHitPoints|MaxHitPoints]], [[#HasFullHealth|HasFullHealth]]


---

### AddMidasFreeze {#AddMidasFreeze}

```
void AddMidasFreeze ( EntityRef Source, int Duration )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将实体变为黄金雕像（无法行动，死亡掉落硬币），指定持续帧数。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 控场并获取金币
- 对高威胁敌人临时冻结并制造资源

**See also:** 
[[#AddFreeze|AddFreeze]], [[#AddBurn|AddBurn]], [[#RemoveStatusEffects|RemoveStatusEffects]]


---

### void AddMidasFreeze ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses ) {#void AddMidasFreeze ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses )}

```
void AddPoison ( EntityRef Source, int Duration, float Damage )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将实体变为黄金雕像，并可指定是否忽略首领。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 只冻结普通敌人转化为黄金
- 创造金币掉落时机

**See also:** 
[[#AddMidasFreeze|AddMidasFreeze]], [[#AddCharmed|AddCharmed]], [[#AddPoison|AddPoison]]


---

### void AddPoison ( [EntityRef](EntityRef.md) Source, int Duration, float Damage, boolean IgnoreBosses ) {#void AddPoison ( [EntityRef](EntityRef.md) Source, int Duration, float Damage, boolean IgnoreBosses )}

```
void AddShrink ( EntityRef Source, int Duration )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为实体添加中毒效果，指定伤害来源、持续帧数和每帧伤害。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 造成持续毒素伤害
- 结合 IgnoreBosses 控制伤害对象

**See also:** 
[[#AddPoison|AddPoison]], [[#AddBurn|AddBurn]], [[#AddFreeze|AddFreeze]], [[#TakeDamage|TakeDamage]]


---

### void AddShrink ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses ) {#void AddShrink ( [EntityRef](EntityRef.md) Source, int Duration, boolean IgnoreBosses )}

```
void AddSlowing ( EntityRef Source, int Duration, float SlowValue, Color SlowColor )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为实体添加缩小效果，指定持续帧数。

[ ](#){: .repplus .tooltip .badge }

**Use Cases:**

- 缩小敌人体积便于躲避或击杀
- 触发缩小特效的视觉反馈

**See also:** 
[[#AddShrink|AddShrink]], [[#SetSize|SetSize]], [[#Size|Size]], [[#AddSlowing|AddSlowing]]


---

### void AddSlowing ( [EntityRef](EntityRef.md) Source, int Duration, float SlowValue, [Color](Color.md) SlowColor, boolean IgnoreBosses ) {#void AddSlowing ( [EntityRef](EntityRef.md) Source, int Duration, float SlowValue, [Color](Color.md) SlowColor, boolean IgnoreBosses )}

```
void AddVelocity ( Vector Velocity )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为实体添加缩小效果，并可指定是否忽略首领。

[ ](#){: .reporplus .tooltip .badge }

**Use Cases:**

- 仅缩小非首领敌人
- 配合其他控制效果

**See also:** 
[[#AddShrink|AddShrink]], [[#AddFreeze|AddFreeze]], [[#AddFear|AddFear]]


---

### void AddVelocity ( [Vector](Vector.md) Velocity, boolean IgnoreTimeScale = false ) {#void AddVelocity ( [Vector](Vector.md) Velocity, boolean IgnoreTimeScale = false )}

```
void BloodExplode ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

为实体添加减速效果，指定摩擦力倍率、变色和是否忽略首领。

使实体伴随碎块和血液爆炸.

**Use Cases:**

- 通过减速控制敌人速度
- 利用颜色变化提示减速状态

**See also:** 
[[#AddSlowing|AddSlowing]], [[#MultiplyFriction|MultiplyFriction]], [[#SetColor|SetColor]], [[#AddFreeze|AddFreeze]]


---

### CanShutDoors {#CanShutDoors}

```
boolean CanShutDoors ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

为实体添加速度向量，可选择忽略时间缩放。

判断敌人是否会保持门关闭状态。返回布尔值

**Use Cases:**

- 击退实体
- 实现自定义移动逻辑

**See also:** 
[[#AddVelocity|AddVelocity]], [[#Velocity|Velocity]], [[#Position|Position]], [[#CollidesWithGrid|CollidesWithGrid]]


---

### ClearEntityFlags {#ClearEntityFlags}

```
void ClearEntityFlags ( int Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

使实体伴随血液和碎块爆炸。

**Use Cases:**

- 为死亡效果增加血腥表现
- 实现自定义爆炸技能

**See also:** 
[[#BloodExplode|BloodExplode]], [[#Die|Die]], [[#Kill|Kill]], [[#Remove|Remove]]


---

### CollidesWithGrid {#CollidesWithGrid}

```
boolean CollidesWithGrid ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

判断该实体是否会使房门保持关闭（通常敌人为 true）。

**Use Cases:**

- 检查房间是否需要清怪才开门
- 筛选关闭房门的敌人

**See also:** 
[[#IsDoorCloser|IsDoorCloser]], [[#IsBoss|IsBoss]], [[#IsEnemy|IsEnemy]]


---

### Die {#Die}

```
void Die ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Die 完成对应 API 操作

**See also:** 



---

### Exists {#Exists}

```
boolean Exists ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Exists 完成对应 API 操作

**See also:** 



---

### GetBossID {#GetBossID}

```
int GetBossID ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

若实体是 Boss，返回其特定的 Boss ID；若不是 Boss，返回 0.

若实体是 Boss，返回其特定的 Boss ID；若不是 Boss，返回 0.

**Use Cases:**

- 调用 GetBossID 完成对应 API 操作

**See also:** 



---

### GetColor {#GetColor}

```
const Color GetColor ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 GetColor 完成对应 API 操作

**See also:** 



---

### GetData {#GetData}

```
table GetData ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetData 完成对应 API 操作

**See also:** 



---

### GetDropRNG {#GetDropRNG}

```
RNG GetDropRNG ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 GetDropRNG 完成对应 API 操作

**See also:** 



---

### GetEntityFlags {#GetEntityFlags}

```
int GetEntityFlags ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GetEntityFlags 完成对应 API 操作

**See also:** 



---

### GetLastChild {#GetLastChild}

```
Entity GetLastChild ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 GetLastChild 完成对应 API 操作

**See also:** 



---

### GetLastParent {#GetLastParent}

```
Entity GetLastParent ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 GetLastParent 完成对应 API 操作

**See also:** 



---

### GetSprite {#GetSprite}

```
Sprite GetSprite ( )
```

*DLC: AB+, REP | Modifiers: const*

**Use Cases:**

- 调用 GetSprite 完成对应 API 操作

**See also:** 



---

### HasCommonParentWithEntity {#HasCommonParentWithEntity}

```
boolean HasCommonParentWithEntity ( Entity Other )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

**Use Cases:**

- 调用 HasCommonParentWithEntity 完成对应 API 操作

**See also:** 



---

### HasEntityFlags {#HasEntityFlags}

```
boolean HasEntityFlags ( int Flags )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 HasEntityFlags 完成对应 API 操作

**See also:** 



---

### HasFullHealth {#HasFullHealth}

```
boolean HasFullHealth ( )
```

*DLC: REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 HasFullHealth 完成对应 API 操作

**See also:** 



---

### HasMortalDamage {#HasMortalDamage}

```
boolean HasMortalDamage ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 HasMortalDamage 完成对应 API 操作

**See also:** 



---

### IsActiveEnemy {#IsActiveEnemy}

```
boolean IsActiveEnemy ( boolean includeDead )
```

*DLC: AB+, REP, REP+*

如果实体是非背景 NPC（例如，除了火焰和店主之外的所有敌人），则返回 true

如果实体是非背景 NPC（例如，除了火焰和店主之外的所有敌人），则返回 true

**Use Cases:**

- 调用 IsActiveEnemy 完成对应 API 操作

**See also:** 



---

### IsBoss {#IsBoss}

```
boolean IsBoss ( )
```

*DLC: AB+, REP, REP+*

如果实体是首领（显示生命值条），则返回 true

如果实体是首领（显示生命值条），则返回 true

**Use Cases:**

- 调用 IsBoss 完成对应 API 操作

**See also:** 



---

### IsDead {#IsDead}

```
boolean IsDead ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 IsDead 完成对应 API 操作

**See also:** 



---

### IsEnemy {#IsEnemy}

```
boolean IsEnemy ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 IsEnemy 完成对应 API 操作

**See also:** 



---

### IsFlying {#IsFlying}

```
boolean IsFlying ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 IsFlying 完成对应 API 操作

**See also:** 



---

### IsFrame {#IsFrame}

```
boolean IsFrame ( int Frame, int Offset )
```

*DLC: AB+, REP, REP+*

每 X 帧返回 true

每 X 帧返回 true

**Use Cases:**

- 调用 IsFrame 完成对应 API 操作

**See also:** 



---

### IsInvincible {#IsInvincible}

```
boolean IsInvincible ( )
```

*DLC: AB+, REP, REP+*

检查实体是否无敌

检查实体是否无敌

**Use Cases:**

- 调用 IsInvincible 完成对应 API 操作

**See also:** 



---

### IsVisible {#IsVisible}

```
boolean IsVisible ( )
```

*DLC: AB+, REP, REP+*

检查实体是否可见

检查实体是否可见

**Use Cases:**

- 调用 IsVisible 完成对应 API 操作

**See also:** 



---

### IsVulnerableEnemy {#IsVulnerableEnemy}

```
boolean IsVulnerableEnemy ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 IsVulnerableEnemy 完成对应 API 操作

**See also:** 



---

### Kill {#Kill}

```
void Kill ( )
```

*DLC: AB+, REP, REP+*

杀死实体并产生血溅或碎块效果.

杀死实体并产生血溅或碎块效果.

**Use Cases:**

- 调用 Kill 完成对应 API 操作

**See also:** 



---

### KillWithSource {#KillWithSource}

```
void KillWithSource ( EntityRef Source )
```

*DLC: AB+, REP, REP+*

___

___

**Use Cases:**

- 调用 KillWithSource 完成对应 API 操作

**See also:** 



---

### MultiplyFriction {#MultiplyFriction}

```
void MultiplyFriction ( float Value )
```

*DLC: AB+, REP, REP+*

将实体的摩擦力乘以指定的值

将实体的摩擦力乘以指定的值

**Use Cases:**

- 调用 MultiplyFriction 完成对应 API 操作

**See also:** 



---

### PostRender {#PostRender}

```
void PostRender ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 PostRender 完成对应 API 操作

**See also:** 



---

### Remove {#Remove}

```
void Remove ( )
```

*DLC: AB+, REP, REP+*

立即从游戏中移除实体，不执行任何额外的效果或动画.

立即从游戏中移除实体，不执行任何额外的效果或动画.

**Use Cases:**

- 调用 Remove 完成对应 API 操作

**See also:** 



---

### RemoveStatusEffects {#RemoveStatusEffects}

```
void RemoveStatusEffects ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RemoveStatusEffects 完成对应 API 操作

**See also:** 



---

### Render {#Render}

```
void Render ( Vector Offset )
```

*DLC: AB+, REP, REP+*

在当前实体位置加上偏移量的位置渲染实体的当前精灵.

在当前实体位置加上偏移量的位置渲染实体的当前精灵.

**Use Cases:**

- 调用 Render 完成对应 API 操作

**See also:** 



---

### RenderShadowLayer {#RenderShadowLayer}

```
boolean RenderShadowLayer ( Vector Offset )
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 RenderShadowLayer 完成对应 API 操作

**See also:** 



---

### SetColor {#SetColor}

```
void SetColor ( Color Color, int Duration, int Priority, boolean Fadeout, boolean Share )
```

*DLC: REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SetColor 完成对应 API 操作

**See also:** 



---

### SetSize {#SetSize}

```
void SetSize ( float Size, Vector SizeMulti, int NumGridCollisionPoints )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SetSize 完成对应 API 操作

**See also:** 



---

### SetSpriteFrame {#SetSpriteFrame}

```
void SetSpriteFrame ( string AnimationName, int FrameNum )
```

*DLC: AB+, REP, REP+*

设置实体精灵的指定动画的帧

设置实体精灵的指定动画的帧

**Use Cases:**

- 调用 SetSpriteFrame 完成对应 API 操作

**See also:** 



---

### SetSpriteOverlayFrame {#SetSpriteOverlayFrame}

```
void SetSpriteOverlayFrame ( string AnimationName, int FrameNum )
```

*DLC: AB+, REP, REP+*

设置实体精灵覆盖层的指定动画的帧号

设置实体精灵覆盖层的指定动画的帧号

**Use Cases:**

- 调用 SetSpriteOverlayFrame 完成对应 API 操作

**See also:** 



---

### TakeDamage {#TakeDamage}

```
boolean TakeDamage ( float Damage, DamageFlag Flags, EntityRef Source, int DamageCountdown )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 TakeDamage 完成对应 API 操作

**See also:** 



---

### ToBomb {#ToBomb}

```
EntityBomb ToBomb ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

用于将[Entity](Entity.md) 对象转换为 [EntityBomb](EntityBomb.md) 对象.

用于将[Entity](Entity.md) 对象转换为 [EntityBomb](EntityBomb.md) 对象.

**Use Cases:**

- 调用 ToBomb 完成对应 API 操作

**See also:** 



---

### ToEffect {#ToEffect}

```
EntityEffect ToEffect ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

用于将 [Entity](Entity.md) 对象转换为 [EntityEffect](EntityEffect.md) 对象.

用于将 [Entity](Entity.md) 对象转换为 [EntityEffect](EntityEffect.md) 对象.

**Use Cases:**

- 调用 ToEffect 完成对应 API 操作

**See also:** 



---

### ToFamiliar {#ToFamiliar}

```
EntityFamiliar ToFamiliar ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

用于将 [Entity](Entity.md) 对象转换为 [EntityFamiliar](EntityFamiliar.md) 对象.

用于将 [Entity](Entity.md) 对象转换为 [EntityFamiliar](EntityFamiliar.md) 对象.

**Use Cases:**

- 调用 ToFamiliar 完成对应 API 操作

**See also:** 



---

### ToKnife {#ToKnife}

```
EntityKnife ToKnife ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

用于将 [Entity](Entity.md) 对象转换为 [EntityKnife](EntityKnife.md) 对象.

用于将 [Entity](Entity.md) 对象转换为 [EntityKnife](EntityKnife.md) 对象.

**Use Cases:**

- 调用 ToKnife 完成对应 API 操作

**See also:** 



---

### ToLaser {#ToLaser}

```
EntityLaser ToLaser ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

用于将 [Entity](Entity.md) 对象转换为 [EntityLaser](EntityLaser.md) 对象.

用于将 [Entity](Entity.md) 对象转换为 [EntityLaser](EntityLaser.md) 对象.

**Use Cases:**

- 调用 ToLaser 完成对应 API 操作

**See also:** 



---

### ToNPC {#ToNPC}

```
EntityNPC ToNPC ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

用于将 [Entity](Entity.md) 对象转换为 [EntityNPC](EntityNPC.md) 对象.

用于将 [Entity](Entity.md) 对象转换为 [EntityNPC](EntityNPC.md) 对象.

**Use Cases:**

- 调用 ToNPC 完成对应 API 操作

**See also:** 



---

### ToPickup {#ToPickup}

```
EntityPickup ToPickup ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: REP, REP+*

用于将 [Entity](Entity.md) 对象转换为 [EntityPickup](EntityPickup.md) 对象.

用于将 [Entity](Entity.md) 对象转换为 [EntityPickup](EntityPickup.md) 对象.

**Use Cases:**

- 调用 ToPickup 完成对应 API 操作

**See also:** 



---

### ToPlayer {#ToPlayer}

```
EntityPlayer ToPlayer ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: REP, REP+*

用于将 [Entity](Entity.md) 对象转换为 [EntityPlayer](EntityPlayer.md) 对象.

用于将 [Entity](Entity.md) 对象转换为 [EntityPlayer](EntityPlayer.md) 对象.

**Use Cases:**

- 调用 ToPlayer 完成对应 API 操作

**See also:** 



---

### ToProjectile {#ToProjectile}

```
EntityProjectile ToProjectile ( ) {: .copyable aria-label='Functions' data-altreturn='nil' }
```

*DLC: REP, REP+*

用于将 [Entity](Entity.md) 对象转换为 [EntityProjectile](EntityProjectile.md) 对象.

用于将 [Entity](Entity.md) 对象转换为 [EntityProjectile](EntityProjectile.md) 对象.

**Use Cases:**

- 调用 ToProjectile 完成对应 API 操作

**See also:** 



---

### ToTear {#ToTear}

```
EntityTear ToTear ( )
```

*DLC: AB+, REP, REP+*

用于将 [Entity](Entity.md) 对象转换为 [EntityTear](EntityTear.md) object.

用于将 [Entity](Entity.md) 对象转换为 [EntityTear](EntityTear.md) object.

**Use Cases:**

- 调用 ToTear 完成对应 API 操作

**See also:** 



---

### Update {#Update}

```
void Update ( )
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Update 完成对应 API 操作

**See also:** 



---

### Child {#Child}

```
Entity Child
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Child 完成对应 API 操作

**See also:** 



---

### CollisionDamage {#CollisionDamage}

```
float CollisionDamage
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 CollisionDamage 完成对应 API 操作

**See also:** 



---

### Color {#Color}

```
Color Color
```

*DLC: REP, REP+*

**Use Cases:**

- 调用 Color 完成对应 API 操作

**See also:** 



---

### DepthOffset {#DepthOffset}

```
float DepthOffset
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 DepthOffset 完成对应 API 操作

**See also:** 



---

### DropSeed {#DropSeed}

```
const int DropSeed
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 DropSeed 完成对应 API 操作

**See also:** 



---

### EntityCollisionClass {#EntityCollisionClass}

```
EntityCollisionClass EntityCollisionClass
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 EntityCollisionClass 完成对应 API 操作

**See also:** 



---

### FlipX {#FlipX}

```
boolean FlipX
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 FlipX 完成对应 API 操作

**See also:** 



---

### FrameCount {#FrameCount}

```
const int FrameCount
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 FrameCount 完成对应 API 操作

**See also:** 



---

### Friction {#Friction}

```
float Friction
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Friction 完成对应 API 操作

**See also:** 



---

### GridCollisionClass {#GridCollisionClass}

```
EntityGridCollisionClass GridCollisionClass
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 GridCollisionClass 完成对应 API 操作

**See also:** 



---

### HitPoints {#HitPoints}

```
float HitPoints
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 HitPoints 完成对应 API 操作

**See also:** 



---

### Index {#Index}

```
const int Index
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Index 完成对应 API 操作

**See also:** 



---

### InitSeed {#InitSeed}

```
const int InitSeed
```

*DLC: REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 InitSeed 完成对应 API 操作

**See also:** 



---

### Mass {#Mass}

```
float Mass
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Mass 完成对应 API 操作

**See also:** 



---

### MaxHitPoints {#MaxHitPoints}

```
float MaxHitPoints
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 MaxHitPoints 完成对应 API 操作

**See also:** 



---

### Parent {#Parent}

```
Entity Parent {: .copyable aria-label='Variables' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Parent 完成对应 API 操作

**See also:** 



---

### Position {#Position}

```
Vector Position
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Position 完成对应 API 操作

**See also:** 



---

### PositionOffset {#PositionOffset}

```
const Vector PositionOffset
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 PositionOffset 完成对应 API 操作

**See also:** 



---

### RenderZOffset {#RenderZOffset}

```
int RenderZOffset
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 RenderZOffset 完成对应 API 操作

**See also:** 



---

### Size {#Size}

```
float Size
```

*DLC: AB+, REP, REP+*

实体 hitbox（阴影/碰撞箱） 的大小.

实体 hitbox（阴影/碰撞箱） 的大小.

**Use Cases:**

- 调用 Size 完成对应 API 操作

**See also:** 



---

### SizeMulti {#SizeMulti}

```
Vector SizeMulti
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SizeMulti 完成对应 API 操作

**See also:** 



---

### SortingLayer {#SortingLayer}

```
SortingLayer SortingLayer
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SortingLayer 完成对应 API 操作

**See also:** 



---

### SpawnerEntity {#SpawnerEntity}

```
Entity SpawnerEntity {: .copyable aria-label='Variables' data-altreturn='nil' }
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SpawnerEntity 完成对应 API 操作

**See also:** 



---

### SpawnerType {#SpawnerType}

```
EntityType SpawnerType
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SpawnerType 完成对应 API 操作

**See also:** 



---

### SpawnerVariant {#SpawnerVariant}

```
int SpawnerVariant
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SpawnerVariant 完成对应 API 操作

**See also:** 



---

### SpawnGridIndex {#SpawnGridIndex}

```
const int SpawnGridIndex
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SpawnGridIndex 完成对应 API 操作

**See also:** 



---

### SplatColor {#SplatColor}

```
Color SplatColor
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 SplatColor 完成对应 API 操作

**See also:** 



---

### SpriteOffset {#SpriteOffset}

```
Vector SpriteOffset
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SpriteOffset 完成对应 API 操作

**See also:** 



---

### SpriteRotation {#SpriteRotation}

```
float SpriteRotation
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SpriteRotation 完成对应 API 操作

**See also:** 



---

### SpriteScale {#SpriteScale}

```
Vector SpriteScale
```

*DLC: AB+, REP, REP+*

获取 / 设置敌人精灵的缩放比例，也可用于缩放实体的阴影。它还作为玩家属性，可在 MC_EVALUATE_CACHE 回调中使用 CacheFlag.CACHE_SIZE 标记更改，**等同于大小（Size）属性**

获取 / 设置敌人精灵的缩放比例，也可用于缩放实体的阴影。它还作为玩家属性，可在 MC_EVALUATE_CACHE 回调中使用 CacheFlag.CACHE_SIZE 标记更改，**等同于大小（Size）属性**

**Use Cases:**

- 调用 SpriteScale 完成对应 API 操作

**See also:** 



---

### SubType {#SubType}

```
int SubType
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 SubType 完成对应 API 操作

**See also:** 



---

### Target {#Target}

```
Entity Target
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Target 完成对应 API 操作

**See also:** 



---

### TargetPosition {#TargetPosition}

```
Vector TargetPosition
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 TargetPosition 完成对应 API 操作

**See also:** 



---

### Type {#Type}

```
const EntityType Type
```

*DLC: AB+, REP, REP+ | Modifiers: const*

**Use Cases:**

- 调用 Type 完成对应 API 操作

**See also:** 



---

### Variant {#Variant}

```
int Variant
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Variant 完成对应 API 操作

**See also:** 



---

### Velocity {#Velocity}

```
Vector Velocity
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Velocity 完成对应 API 操作

**See also:** 



---

### Visible {#Visible}

```
boolean Visible
```

*DLC: AB+, REP, REP+*

**Use Cases:**

- 调用 Visible 完成对应 API 操作

**See also:** 



---

## See Also

- [[Color]]
- [[Entity]]
- [[EntityBomb]]
- [[EntityEffect]]
- [[EntityFamiliar]]
- [[EntityKnife]]
- [[EntityLaser]]
- [[EntityNPC]]
- [[EntityPickup]]
- [[EntityPlayer]]
- [[EntityProjectile]]
- [[EntityRef]]
- [[EntityTear]]
- [[RNG]]
- [[Sprite]]
- [[Vector]]
