from typing import List


def letterCombinations(digits: str) -> List[str]:
    l = []

    if len(digits) == 0:
        return l

    appendLetter(l, digits, "")
    return l



letterDigitDict = {2: ["a", "b", "c"],
                    3: ["d", "e", "f"],
                    4: ["g", "h", "i"],
                    5: ["j", "k", "l"],
                    6: ["m", "n", "o"],
                    7: ["p", "q", "r", "s"],
                    8: ["t", "u", "v"],
                    9: ["w", "x", "y", "z"]
                    }

def appendLetter(l, s, cumul):
    
    if len(s) == 0:
        l.append(cumul)
        return

    digit = int(s[0])

    for letter in letterDigitDict[digit]:
        appendLetter(l, s[1:], cumul + letter)
        
print(letterCombinations("23"))