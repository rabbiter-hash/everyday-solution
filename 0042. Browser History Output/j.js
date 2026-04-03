
function getBrowerHistory(commands){
    const history = [];
    let currentIndex = -1;

    for (const command of commands) {
        if (command === "Back") {
            // 后退：如果不在开头就往前移动
            if (currentIndex > 0) {
                currentIndex--;
            }
        }
        else if (command === "Forward") {
            // 前进：如果不在末尾就往后移动
            if (currentIndex < history.length - 1) {
                currentIndex++;
            }
        }
        else {
            // URL 命令：添加新页面
            // 丢弃当前位置之后的所有历史
            if (currentIndex < history.length - 1) {
                history.splice(currentIndex + 1);
            }
            // 添加新 URL
            history.push(command);
            currentIndex++;
        }
    }

    return [history, currentIndex];
}

const result = getBrowerHistory([
    "freecodecamp.org",
    "freecodecamp.org/learn",
    "Back"
]);
console.log(result); // [["freecodecamp.org", "freecodecamp.org/learn"], 0]