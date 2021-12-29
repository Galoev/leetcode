class Solution:
    def skipSymb(self, s: str, i: int):
        skip_idx = 0
        while i >= 0:
            if s[i] == '#':
                skip_idx += 1
            elif skip_idx > 0:
                skip_idx -= 1
            else:
                break

            i -= 1

        return i
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_pointer = len(s) - 1
        t_pointer = len(t) - 1

        while s_pointer >= 0 or t_pointer >=0:
            s_pointer = self.skipSymb(s, s_pointer)
            t_pointer = self.skipSymb(t, t_pointer)

            if s_pointer < 0 and t_pointer < 0:
                return True
            if s_pointer < 0 or t_pointer < 0:
                return False
            if s[s_pointer] != t[t_pointer]:
                return False
            
            s_pointer -= 1
            t_pointer -= 1
        
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare("ab#c", "ad#c")) #True
    print(s.backspaceCompare("ab##", "c#d#")) #True
    print(s.backspaceCompare("a#c", "b")) #False
    print(s.backspaceCompare("bxj##tw", "bxo#j##tw")) #True
    print(s.backspaceCompare("xywrrmp", "xywrrmu#p")) #True
    print(s.backspaceCompare("bxj##tw", "bxj###tw")) #False
    print(s.backspaceCompare("a##c", "#a#c")) #True
    print(s.backspaceCompare("j##yc##bs#srqpfzantto###########i#mwb", "j##yc##bs#srqpf#zantto###########i#mwb")) #False
    print(s.backspaceCompare("bbbextm", "bbb#extm")) #False