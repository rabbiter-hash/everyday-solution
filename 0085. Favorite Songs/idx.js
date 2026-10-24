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