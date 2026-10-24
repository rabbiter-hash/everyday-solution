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