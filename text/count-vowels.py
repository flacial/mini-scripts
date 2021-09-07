def countVowels() -> int:
    word: str = input("Type a Word: ")
    count: int = 0
    vowels: list = ["A", "E", "I", "O", "U", "Y", "W"]

    for letter in word:
        if letter.upper() in vowels:
            count += 1

    return count


result = countVowels()
print(f'\nThe word has: {result} vowel{"s" if result > 1 else ""}')
