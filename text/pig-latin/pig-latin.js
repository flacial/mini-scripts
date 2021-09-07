/*
1. Does start with:
    Consonant
    Consonant Cluster
    Vowel
If Consonant:
    Put the consonant letter before the "ay" and the vowels at the beginning.
    Example: banana -> [anana](b)"ay"
If Consonant Cluster:
    Put the consonant Cluster before the suffix "ay" and the vowels at the beginning
    Example: string -> [ing](str)"ay"
If Vowel:
    Leave the word as it's and just add "ay" to it
    Example: apple -> [apple]"ay"
*/
import * as readline from "readline";
var suffix = "ay";
var PigLatinUtils = /** @class */ (function () {
    function PigLatinUtils() {
    }
    var _a;
    _a = PigLatinUtils;
    PigLatinUtils.isVowelLetter = function (letter) {
        return ["A", "E", "I", "O", "U", "Y", "W"].includes(letter.toUpperCase());
    };
    PigLatinUtils.isConsonant = function (letter) { return !_a.isVowelLetter(letter); };
    PigLatinUtils.joinConsonants = function (word, i, consonants) {
        if (i === void 0) { i = 0; }
        if (consonants === void 0) { consonants = ""; }
        if (i === word.length)
            return "You're sure this is a valid word? -> ";
        if (PigLatinUtils.isConsonant(word[i])) {
            consonants += word[i];
            return _a.joinConsonants(word, i + 1, consonants);
        }
        var lettersAfterVowel = word.slice(i);
        return lettersAfterVowel + consonants;
    };
    return PigLatinUtils;
}());
var pigLatin = function (word) {
    if (!word) {
        return "Please provide a word.";
    }
    word = word.trim();
    var _b = [
        PigLatinUtils.isConsonant(word[0]),
        PigLatinUtils.isConsonant(word[1]),
    ], isTheFirstLetterConsonant = _b[0], isTheSecondLetterConsonant = _b[1];
    if (isTheFirstLetterConsonant) {
        if (isTheSecondLetterConsonant) {
            var clusterPigLatinWord = PigLatinUtils.joinConsonants(word);
            return clusterPigLatinWord + suffix;
        }
        var restOfLetters = word.slice(1);
        var consonantLetter = word[0];
        return restOfLetters + consonantLetter + suffix;
    }
    return word + suffix;
};
var pigLatinWithInput = function () {
    var rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
        prompt: "Word to turn into Pig Latin: "
    });
    rl.prompt();
    rl.on("line", function (line) {
        !line && (line = "Type a word");
        console.log("\nPig Latin: " + pigLatin(line));
        rl.close();
    });
};
// Uncomment to use Parameter mode
// console.log(pigLatin("word"));
// Uncomment to use Input mode
// pigLatinWithInput();
export { pigLatin };
