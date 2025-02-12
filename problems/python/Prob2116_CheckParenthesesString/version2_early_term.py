class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        left = []
        optional = []

        if len(s) % 2 == 1:
            return False
        
        if (locked[0] == "1" and s[0] == ")") or (locked[-1] == "1" and s[-1] == "("):
            return False

        # Do a pass through s and check if any locked '(' canceled with locked ')'.
        # Also cancel locked ')' with locked or optional '('
        for i, (c, l) in enumerate(list(zip(s, locked))):
            if l == '1':
                if c == '(':
                    left.append(i)
                else:
                    if left:
                        left.pop()
                    elif optional:
                        optional.pop()
                    else:
                        return False
            elif l == '0':
                optional.append(i)

        # Do another pass through the locked '(' that could not be canceled
        # and check if they can be canceled with an optional ')'
        for l_idx in left[::-1]:
            if not optional:
                return False
            opt_idx = optional.pop()
            if opt_idx < l_idx:
                return False
    
        return len(optional) % 2 == 0