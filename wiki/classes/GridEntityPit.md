---
title: GridEntityPit
category: class
dlc_versions: [AB+, REP, REP+]
method_count: 4
---

# GridEntityPit

## Summary

GridEntityPit 表示房间中的坑洞网格实体。它可以被转换为可通过的桥梁，也可以附加梯子供角色攀爬。通过方法可以动态改变坑洞的通行性和外观。

## Inheritance

- Inherits from: [[GridEntity]]

## Related Types

- [[Entity]]

## Key Methods

- [[#MakeBridge|MakeBridge]]
- [[#SetLadder|SetLadder]]
- [[#UpdateCollision|UpdateCollision]]
- [[#HasLadder|HasLadder]]

## Methods

### Functions

### MakeBridge {#MakeBridge}

```
void MakeBridge ( GridEntity parentEntity)
```

*DLC: AB+, REP, REP+ | Modifiers: const*

在坑洞上创建一个桥梁，使其变为可通行。如果 parentEntity 为 nil，则使用默认桥梁纹理。

parentEntity can be `nil` to use the default texture as the bridge

**Use Cases:**

- 将不可通行的坑洞转换为可通行的桥梁
- 使用特定实体的外观作为桥梁纹理

**See also:** 
[[#UpdateCollision|UpdateCollision]]


---

### SetLadder {#SetLadder}

```
void SetLadder ( boolean Value )
```

*DLC: REP, REP+ | Modifiers: const*

设置坑洞是否拥有梯子，控制角色是否能通过攀爬方式越过该坑洞。

**Use Cases:**

- 允许或禁止角色使用梯子越过坑洞
- 根据游戏逻辑动态显示或隐藏梯子

**See also:** 
[[#HasLadder|HasLadder]], [[#UpdateCollision|UpdateCollision]]


---

### UpdateCollision {#UpdateCollision}

```
void UpdateCollision ( )
```

*DLC: AB+, REP, REP+ | Modifiers: const*

更新坑洞的碰撞体，通常在改变坑洞状态（如添加桥梁或梯子）后调用，以确保碰撞与视觉效果一致。

**Use Cases:**

- 在 MakeBridge 或 SetLadder 后同步碰撞数据
- 确保实体与坑洞的交互结果正确

**See also:** 
[[#MakeBridge|MakeBridge]], [[#SetLadder|SetLadder]]


---

### HasLadder {#HasLadder}

```
boolean HasLadder
```

*DLC: AB+, REP, REP+ | Modifiers: const*

只读布尔变量，指示坑洞当前是否拥有梯子。

**Use Cases:**

- 检查坑洞的梯子状态以决定角色行为
- 作为条件判断是否允许攀爬操作

**See also:** 
[[#SetLadder|SetLadder]]


---

## See Also

- [[Entity]]
- [[GridEntity]]
