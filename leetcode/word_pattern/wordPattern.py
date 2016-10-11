class Solution(object):
    def wordPattern(self, pattern, str):
        strings = str.split(' ')
        exist = set()
        save = {}

        if len(pattern) != len(strings):
            return False

        for i, v in enumerate(pattern):
            if v not in save:
                if strings[i] in exist:
                    return False
                save[v] = strings[i]
            else:
                if save[v] != strings[i]:
                    return False
            exist.add(strings[i])
        return True

if __name__ == '__main__':
    s = Solution()
    pattern = 'abba'
    str = 'dog dog dog dog'
    assert s.wordPattern(pattern, str) == False
    
    pattern = 'abba'
    str = 'dog cat cat dog'
    assert s.wordPattern(pattern, str) == True
    
    pattern = 'abba'
    str = 'dog cat cat fish'
    assert s.wordPattern(pattern, str) == False
    
    print 'complete!'