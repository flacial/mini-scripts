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

const suffix: string = "ay";

class PigLatinUtils {
  static isVowelLetter = (letter: string): boolean =>
    ["A", "E", "I", "O", "U", "Y", "W"].includes(letter.toUpperCase());

  static isConsonant = (letter: string): boolean => !this.isVowelLetter(letter);

  static joinConsonants = (
    word: string,
    i: number = 0,
    consonants: string = ""
  ): string => {
    if (i === word.length) return "You're sure this is a valid word? -> ";

    if (PigLatinUtils.isConsonant(word[i])) {
      consonants += word[i];
      return this.joinConsonants(word, i + 1, consonants);
    }

    const lettersAfterVowel = word.slice(i);
    return lettersAfterVowel + consonants;
  };
}

const pigLatin = (word: string): string => {
  if (!word) {
    return "Please provide a word.";
  }

  word = word.trim();

  const [isTheFirstLetterConsonant, isTheSecondLetterConsonant] = [
    PigLatinUtils.isConsonant(word[0]),
    PigLatinUtils.isConsonant(word[1]),
  ];

  if (isTheFirstLetterConsonant) {
    if (isTheSecondLetterConsonant) {
      const clusterPigLatinWord: string = PigLatinUtils.joinConsonants(word);
      return clusterPigLatinWord + suffix;
    }

    const restOfLetters = word.slice(1);
    const consonantLetter = word[0];

    return restOfLetters + consonantLetter + suffix;
  }

  return word + suffix;
};

const pigLatinWithInput = (): void => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: "Word to turn into Pig Latin: ",
  });

  rl.prompt();

  rl.on("line", (line: string) => {
    !line && (line = "Type a word");

    console.log(`\nPig Latin: ${pigLatin(line)}`);

    rl.close();
  });
};

// Uncomment to use Parameter mode
// console.log(pigLatin("word"));

// Uncomment to use Input mode
// pigLatinWithInput();

export { pigLatin };
