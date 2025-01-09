class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        l = []
        recConstructIpAddr(s, 1, "", l)
        return l

def recConstructIpAddr(s: str, section: int, acc: str, ret_list: List[str]):
    # Iterate through first, second and third digits
    for i in range(1, 4):
        if len(s) >= i:
            subs = s[:i]
            num = int(subs)
            # Number must be 0 <= n <= 255
            if num >= 0 and num <= 255:
                # No leading zeros
                if len(subs) > 1 and s[0] == "0":
                    continue
                # If we reach section 4, if we take n digits, there must be no remaining digits
                if section == 4 and not s[i:]:
                    ret_list.append(acc + subs)
                else:
                    recConstructIpAddr(s[i:], section + 1, acc + subs + ".", ret_list)