def romanToInt(s: str) -> int:
    roman_letter_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    prev = ""

    for c in s:
        to_add = roman_letter_to_int[c]
        to_subtract = 0

        if prev == "I":
            if c == "V":
                to_subtract = 1
                to_add = 4

            if c == "X":
                to_subtract = 1
                to_add = 9

        if prev == "X":
            if c == "L":
                to_subtract = 10
                to_add = 40
            if c == "C":
                to_subtract = 10
                to_add = 90

        if prev == "C":
            if c == "D":
                to_subtract = 100
                to_add = 400
            if c == "M":
                to_subtract = 100
                to_add = 900

        total += to_add
        total -= to_subtract
        prev = c

    return total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(romanToInt("MCMXCIV"))

