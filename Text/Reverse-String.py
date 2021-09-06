def reverseString(mayRepeat: bool = False, repeatCount: int = 2) -> str:
    '''Hyprid. Return a Reversed String
    Takes in a boolean to allow repetition and repetition count as parameters. Takes string as input.
    '''
    stringInput = input("String to reverse: ") or "Type something"
    reversedString = ""

    for index, _ in enumerate(stringInput):
        reversedString += stringInput[(len(stringInput) - 1) - index]

    if mayRepeat:
        for i in range(repeatCount):
            print(reversedString)
    return reversedString


reverseString(True)
