class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack = []
        return canBeValid(s, locked, stack)


def canBeValid(s: str, locked: str, stack: List[str]) -> bool:
    if not s:
        return not stack
    
    c = s[0]
    char_locked = locked[0]
    left = c == '('

    if not stack:
        if left or char_locked == '0':
            stack.append('(')
            return canBeValid(s[1:], locked[1:], stack)
        else:
            return False

    if left:
        # Attempt with ')' first
        orig_stack = stack[:]
        if char_locked == '0':
            stack.pop()
            if canBeValid(s[1:], locked[1:], stack):
                return True
        # If first attempt did not work, attempt with '('
        orig_stack.append(c)
        return canBeValid(s[1:], locked[1:], orig_stack)
    else:
        # Attempt with ')' first
        orig_stack = stack[:]
        stack.pop()
        if canBeValid(s[1:], locked[1:], stack):
            return True
        # If first attempt did not work, attempt with '('
        if char_locked == '0':
            orig_stack.append('(')
            return canBeValid(s[1:], locked[1:], orig_stack)

    return False