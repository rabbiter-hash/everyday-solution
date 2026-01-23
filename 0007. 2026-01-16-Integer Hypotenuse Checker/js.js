
function isIntegerHypotenuse(a, b) {
    let c = Math.sqrt(a*a + b*b);
    return Number.isInteger(c);
}