function elevatorStops(currentFloor, stops) {
    // 1. 去重所有要停靠的楼层
    const allStops = new Set(stops);
    console.log(allStops);

    // 2. 分离向上和向下请求
    const above = stops
        .filter(f => f > currentFloor)
        .sort((a, b) => a - b);
    console.log(above);
    const below = stops
        .filter(f => f < currentFloor)
        .sort((a, b) => b - a);
    console.log(below);

    // 3. 如果不存在上下请求
    if(above.length === 0 && below.length === 0) return null;
    if(above.length === 0) return below;
    if(below.length === 0) return above;

    // 4. 找出最近的向下和向上的请求以供比较
    const nearestUp = above[0]; // 升序排列，直接取第一个
    const nearestDown = below[0]; // 降序排列，直接取第一个
    // 5. 决定先下还是先上
    const distUp = nearestUp - currentFloor;
    const distDown = currentFloor - nearestDown;
    // 如果向下的距离小于或者等于向上的距离，优先向下
    if(distDown <= distUp) {
        return [...below, ...above];
    }
    return [...above, ...below];
}

elevatorStops(5, [2, 8, 3, 9]);
elevatorStops(6, [2, 10, 8, 3, 1, 9]);
elevatorStops(1, [4, 8, 3, 6, 9]);
elevatorStops(12, [6, 10, 7, 3, 1, 4]);