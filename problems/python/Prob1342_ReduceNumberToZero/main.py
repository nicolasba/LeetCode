def numberOfSteps(num: int) -> int:
    
    total = 0

    while num != 0:

        if num % 2 == 0:
            num /= 2 
        else:
            num -= 1
        total += 1

    return total

if __name__ == '__main__':
    print(numberOfSteps(10))

