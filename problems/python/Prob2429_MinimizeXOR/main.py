class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count_ones = num2_ones = getNumberSetBits(num2)
        num1_bstr = format(num1, 'b')
        ret = ""

        # Keep first n occurences of "1" in num1 if available
        for i, b in enumerate(num1_bstr):
            if count_ones > 0:
                if b == "1":
                    ret += "1"
                    count_ones -= 1
                else:
                    ret += "0"
            else:
                ret += "0" * (len(num1_bstr) - i)
                break

        # If there are not enough "1"s, start replacing 0s with 1s from the right
        for i in reversed(range(len(ret))):
            if count_ones > 0:
                if ret[i] == "0":
                    ret = ret[:i] + "1" + ret[i+1:]
                    count_ones -= 1
            else:
                break

        # If there are not enough 1s still (despite ret being composed of only 1s)
        # Append as many 1s as expected
        if len(ret) < num2_ones:
            ret = "1" * (num2_ones - len(ret)) + ret

        return int(ret, 2)

def getNumberSetBits(n: int) -> int:
    b_str = format(n, 'b')
    return Counter(b_str)["1"]