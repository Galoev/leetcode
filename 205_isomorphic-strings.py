class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters_f = dict()

        for s_c, t_c in zip(s, t):
            if s_c in letters_f :
                if letters_f.get(s_c) != t_c:
                    return False
            elif t_c in letters_f.values():
                return False
            else:
                letters_f[s_c] = t_c
        
        return True
            