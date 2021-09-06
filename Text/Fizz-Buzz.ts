const fizzBuzz = (logsCount: number, i: number = 0, word: string = ""): void => {
  if (i >= logsCount) return;

  if (i % 3 === 0) word = "Fuzz";
  if (i % 5 === 0) word = "Buzz";
  if (i % 5 === 0 && i % 3 === 0) word = "FuzzBuzz";

  console.log(word);

  return fizzBuzz(logsCount, i + 1, word);
};

fizzBuzz(100)