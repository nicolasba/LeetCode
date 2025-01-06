from typing import List
    
def mapFizzBuzz(n: int) -> List[str]:
    
    ret = str(n)

    if n % 3 == 0 and n % 5 == 0:
        ret = "FizzBuzz"
    elif n % 3 == 0:
        ret = "Fizz"
    elif n % 5 == 0:
        ret = "Buzz"

    return ret   

def fizzBuzz(n: int) -> List[str]:
    return map(mapFizzBuzz, range(1, n + 1))
    
if __name__ == '__main__':
    for s in fizzBuzz(5):
        print(s)

