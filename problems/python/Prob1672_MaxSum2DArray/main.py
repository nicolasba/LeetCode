from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
    return max([sum(i) for i in accounts])

if __name__ == '__main__':
    print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))