# Favorite Songs

Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

- Each object will have a `"title"` property (string), and a `"plays"` property (integer).

## 一、题解和思路

### 1.1、题解

### 1.2、思路

循环、按降序排列、取前两个

## 二、Returns

1. `favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ])` should return `["Sync or Swim", "Earbud Blues"]`.
2. `favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ])` should return `["Clickwheel Love", "99 Downloads"]`.
3. `favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ])` should return `["Song B", "Song C"]`.

## 三、Python Solution(s)

### 3.1、循环、降序

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/10/24 10:24
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: idx.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def favorite_songs(playlist):

    # 1. 排序
    sorted_songs = sorted(playlist, key=lambda song:song["plays"], reverse=True)
    print(sorted_songs)

    # 2. 取前两格
    return [song["title"] for song in sorted_songs[:2]]

favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ])
```

## 四、JavaScript Solution(s)

### 4.1、循环、降序

```js
function favoriteSongs(playlist) {

    // 1. 拷贝数组
    const songCopy = playlist.slice();
    console.log(songCopy);
    // 2. 排序
    const sortedCopy = songCopy.sort((a, b) => b.plays - a.plays);
    console.log(sortedCopy);
    // 3. 取值
    const maxTwo = sortedCopy.slice(0, 2);
    console.log(maxTwo);

    // 4. 提取标题
    const songTitles = maxTwo.map(song => song.title)
    console.log(songTitles);

    return playlist.slice()
      .sort((a, b) => b.plays - a.plays)
      .slice(0, 2)
      .map(song => song.title)
}

favoriteSongs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ])
```

