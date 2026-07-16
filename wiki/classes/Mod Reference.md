---
title: Mod Reference
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 8
---

# Mod Reference

## Summary

Mod Reference 类代表通过 RegisterMod 注册的 mod 实例，提供回调注册、优先级控制与跨存档/跨游戏流程的持久化数据保存与加载功能。

## Key Methods

- [[#AddCallback|AddCallback]]
- [[#AddPriorityCallback|AddPriorityCallback]]
- [[#SaveData|SaveData]]
- [[#LoadData|LoadData]]

## Methods

### Functions

### AddCallback {#AddCallback}

```
void AddCallback ( ModCallbacks callbackId, function callbackFn, int entityId )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

向指定回调 ID 添加一个常规回调函数，可限定特定实体 ID，用于响应游戏事件。

___

**Use Cases:**

- 在游戏启动或特定事件发生时执行自定义逻辑
- 为特定实体类型添加自定义行为

**See also:** 
[[#AddPriorityCallback|AddPriorityCallback]], [[#RemoveCallback|RemoveCallback]]


---

### AddPriorityCallback {#AddPriorityCallback}

```
void AddPriorityCallback ( ModCallbacks callbackId, CallbackPriority priority, function callbackFn, int entityId )
```

*DLC: REP, REP+ | Modifiers: const*

添加一个带有执行优先级的回调函数，允许 mod 指定该回调相对于其他同回调列表函数执行的先后顺序。

**Use Cases:**

- 需要确保自己的逻辑在其他 mod 之前或之后运行时
- 解决多个 mod 修改同一数据时的执行顺序冲突

**See also:** 
[[#AddCallback|AddCallback]], [[#RemoveCallback|RemoveCallback]]


---

### HasData {#HasData}

```
boolean HasData ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

检查当前 mod 是否已有通过 SaveData 保存的存档文件（saveX.dat），返回布尔值。

**Use Cases:**

- 在加载数据前判断是否需要执行加载逻辑
- 防止 LoadData 返回空字符串导致解析错误

**See also:** 
[[#SaveData|SaveData]], [[#LoadData|LoadData]], [[#RemoveData|RemoveData]]


---

### LoadData {#LoadData}

```
string LoadData ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

加载并返回之前由 SaveData 存储的字符串数据，若无存档文件则返回空字符串，通常配合 JSON 反序列化使用。

**Use Cases:**

- 恢复 mod 的持久化配置或进度
- 配合 JSON 库将字符串还原为 Lua 表

**See also:** 
[[#HasData|HasData]], [[#SaveData|SaveData]]


---

### RemoveCallback {#RemoveCallback}

```
void RemoveCallback ( int callbackId, function callbackFn )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

移除先前通过 AddCallback 或 AddPriorityCallback 添加的指定回调函数，停止其响应对应事件。

**Use Cases:**

- 暂时或永久停用某个 mod 行为
- 防止重复注册或进行回调清理

**See also:** 
[[#AddCallback|AddCallback]], [[#AddPriorityCallback|AddPriorityCallback]]


---

### RemoveData {#RemoveData}

```
void RemoveData ( )
```

*DLC: AB+, REP, REP+ | Modifiers: static*

删除当前存档对应的持久化数据文件（saveX.dat），彻底清除已保存的 mod 数据。

**Use Cases:**

- 重置 mod 的存档数据
- 在 mod 卸载或初始化时清理旧数据

**See also:** 
[[#SaveData|SaveData]], [[#HasData|HasData]]


---

### SaveData {#SaveData}

```
void SaveData ( string data )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

将一个字符串保存到对应存档文件的 saveX.dat 中，数据持久化且跨游戏进程存在，建议先将要保存的内容转换为 JSON 字符串。

**Use Cases:**

- 保存玩家的 mod 进度或配置
- 在游戏退出前或其他关键时刻持久化数据

**See also:** 
[[#LoadData|LoadData]], [[#HasData|HasData]], [[#RemoveData|RemoveData]]


---

### Name {#Name}

```
string Name
```

*DLC: AB+, REP, REP+ | Modifiers: const*

获取本 mod 实例的名称，通常是在 RegisterMod 时指定的名字。

**Use Cases:**

- 日志输出或调试时识别当前 mod
- 用于构建基于 mod 名的唯一标识

**See also:** 



---
