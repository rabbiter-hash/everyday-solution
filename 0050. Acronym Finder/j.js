
function findOrg(acronym){
    // 1. 将所有organizations存储抽成数组
    let organizations = [
        "National Avocado Storage Authority",
        "Cats Infiltration Agency",
        "Fluffy Beanbag Inspectors",
        "Department Of Jelly",
        "Wild Honey Organization",
        "Eating Pancakes Administration"
    ];

    // 2. 循环遍历
    for(let org of organizations){
        // console.log(org);
        // 3. 初始化存储字符串
        let initials = "";

        // 4. org中的单词列表
        let wordsArr = org.split(" ");
        console.log(wordsArr);
        // 5. 取每个列表中每个元素的首字母进行拼接
        for(let ch of wordsArr){
            console.log(ch);
            initials += ch[0].toUpperCase();
            if(initials === acronym){
                return org;
            }
        }
    }
    return null;
}

findOrg("NASA");