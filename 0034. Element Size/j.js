/* ==========================================
    第一种解法：常规清晰解法
 ========================================== */
function getElementSize(windowSize, elementVw, elementVh){
    let [w, h] = windowSize.split(" x ").map(Number);

    let vw = parseInt(elementVw.slice(0, -2));
    let vh = parseInt(elementVh.slice(0, -2));

    let elementWidth = w * vw / 100;
    let elementHeight = h * vh / 100;

    return `${elementWidth} x ${elementHeight}`;

}
getElementSize("1200 x 800", "50vw", "50vh")

/* ==========================================
    第二种解法：使用replace
 ========================================== */
function getElementSizeWithReplace(windowSize, elementVw, elementVh){
    let [w, h] = windowSize.split(" x ").map(Number);

    let vw = Number(elementVw.replace("vw", ""));
    let vh = Number(elementVh.replace("vh", ""));

    return `${w * vw / 100} x ${h * vh / 100}`;
}

/* ==========================================
    第二种解法：使用正则提取
 ========================================== */
function getElementSizeWithRegrex(windowSize, elementVw, elementVh){
    let [w, h] = windowSize.match(/\d+/g).map(Number);

    let vw = Number(elementVw.match(/\d+/g));
    let vh = Number(elementVh.match(/\d+/g));

    return `${w * vw / 100} x ${h * vh / 100}`;
}