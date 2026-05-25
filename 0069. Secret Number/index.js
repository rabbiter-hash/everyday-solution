function guessNumber(secret, guess) {
    if (guess < secret) {
        return "higher";
    } else if (guess > secret) {
        return "lower";
    } else {
        return "you got it!";
    }
}


function guessNumberIdiomatic(secret, guess){
    if(guess < secret) return "higher";

    if(guess > secret) return "lower";

    return "you got it!";
}