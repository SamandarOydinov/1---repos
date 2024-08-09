class Solution:
    def romanToInt(self, s: str) -> int:
            son = 0
            i = 0
            while i < len(s):
                if s[i] == 'I':
                    if i + 1 < len(s) and s[i + 1] == 'V':
                        son += 4
                        i += 1
                    elif i + 1 < len(s) and s[i + 1] == 'X':
                        son += 9
                        i += 1
                    else:
                        son += 1
                elif s[i] == 'V':
                    son += 5
                elif s[i] == 'X':
                    if i + 1 < len(s) and s[i + 1] == 'L':
                        son += 40
                        i += 1
                    elif i + 1 < len(s) and s[i + 1] == 'C':
                        son += 90
                        i += 1
                    else:
                        son += 10
                elif s[i] == 'L':
                    son += 50
                elif s[i] == 'C':
                    if i + 1 < len(s) and s[i + 1] == 'D':
                        son += 400
                        i += 1
                    elif i + 1 < len(s) and s[i + 1] == 'M':
                        son += 900
                        i += 1
                    else:
                        son += 100
                elif s[i] == 'D':
                    son += 500
                elif s[i] == 'M':
                    son += 1000
                i += 1
            return son
