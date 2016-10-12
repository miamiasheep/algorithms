class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        exist = set()
        s_to_t = {}
        
        if len(s) != len(t):
            return False
        
        for i, v in enumerate(s):
            if v not in s_to_t:
                if t[i] in exist:
                    return False
                s_to_t[v] = t[i]
            else:
                if s_to_t[v] != t[i]:
                    return False
            exist.add(t[i])
        return True
    
class Solution_ref(object):
    def isIsomorphic(self, s, t):
        return [s.find(i) for i in s] == [t.find(j) for j in t]
            
        
if __name__ == '__main__':
    pass