# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import random

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:

        matchesGrid = [[getNumberMatches(w1,w2) for w1 in words] for w2 in words]
        possibleSecretIdxSet = set(range(len(words)))
        nbMatches = 0
        r = random.choice(list(possibleSecretIdxSet))

        # print(matchesGrid)

        while len(possibleSecretIdxSet) > 1:
            
            # print("r= " + str(r))
            word = words[r]
            nbMatches = master.guess(word)
            # print("nbMatches= " + str(nbMatches))

            newPossibleSecretIdxSet = getMatchIdxSet(matchesGrid[r], nbMatches)
            # print("newPossible= " + str(newPossibleSecretIdxSet))
            possibleSecretIdxSet = possibleSecretIdxSet.intersection(newPossibleSecretIdxSet)
            print("possibleSecret= " + str(possibleSecretIdxSet))

            r = random.choice(list(possibleSecretIdxSet))

        lastWord = words[possibleSecretIdxSet.pop()]
        master.guess(lastWord)

# Return a list of indexes that match the element
def getMatchIdxSet(l, elem):
    return {i for i, item in enumerate(l) if item == elem}

def getNumberMatches(w1, w2):
    return sum([1 if w1[i] == w2[i] else 0 for i in range(6)])