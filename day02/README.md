# Day 02

## 今天学了什么
累加、while 循环、break/continue 的几种对比写法

## 卡点
- range 是左闭右开的，取不到最后那个数
- break 和 continue 通常和 if 一起用于判断，它们在这里的结构区别是：
  - 先算后判断（累加写在 if 前面）→ 会包含这个元素
  - 先判断后算（if 写在累加前面）→ 不会包含这个元素

例如：

```python
total = 0
for n in [200, 180, 220, 90, 150, 300]:
    if n < 100:
        break
    total += n
print(total)
# 不会加上 90，输出 600
```

```python
total = 0
for n in [5, 2, 8]:
    total += n
    if n < 3:
        break
print(total)
# 会执行到 2，输出是 7
```
