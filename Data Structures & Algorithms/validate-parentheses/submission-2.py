class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {")":"(","}":"{","]":"["}
        for i in s:
            if i in char_map.values():
                stack.append(i)
            elif i in char_map.keys():
                print(stack)
                if not stack or stack.pop()!=char_map[i]:
                    return False
        if len(stack)==0:
            return True
        return False
            