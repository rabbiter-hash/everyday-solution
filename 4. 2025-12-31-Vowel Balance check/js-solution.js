function is_balanced(s){
    const vowels = new Set('aeiouAEIOU'.split(''));
    const len = s.length;

    // 左半部分
    const left_c = s.slice(0, len / 2);
    console.log(left_c);
    // 右半部分
    const right_c = s.slice(-(len/2));
    console.log(right_c);

    const count = str => [...str].reduce((acc, c) => vowels.has(c) ? acc+1 :acc, 0);
    /*
        # 以上代码拆解
        const count = function(str){
            const arr = [...str];
            let acc = 0;

            for(const c of arr){
                if(vowels.has(c)){
                    acc = acc + 1;
                }
            }
            return acc;
        };
     */
    return count(left_c) === count(right_c);
}

