# Song Mood Finder

Given a genre string and a BPM number for a song, determine the mood using the following table:

|   Mood    |     Genre      | BPM Range |
| :-------: | :------------: | :-------: |
| `"focus"` | `"classical"`  |  60–109   |
| `"focus"` | `"electronic"` |   60–89   |
| `"happy"` |    `"pop"`     |  60–180   |
| `"happy"` | `"classical"`  |  110–180  |
| `"happy"` |    `"rock"`    |  60–129   |
| `"happy"` | `"electronic"` |  90–134   |
| `"hype"`  |    `"rock"`    |  130–180  |
| `"hype"`  | `"electronic"` |  135–180  |

## 一、题解和思路

### 1.1、题解

根据给出的【音乐风格（genre】和【BPM（每分钟节拍数）】这两个信息，从一个规则表中进行查找，判断这首歌的【情绪（mood）】是什么。

### 1.2、思路

本质是条件匹配/查表的逻辑。

**建立一个映射表（字典/查找表）**，把“风格”和“BPM范围”作为联合条件，映射到对应的“情绪”。

## 二、Returns

## 三、Python Solution(s)

## 四、JavaScript Solution(s)