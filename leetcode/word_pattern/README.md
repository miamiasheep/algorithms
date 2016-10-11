# Word Pattern

### Problem Description:
https://leetcode.com/problems/word-pattern/

### Description
When the str meets the word pattern:
1. The corresponding pattern characters must be the same if the corresponding words are the same
2. There won't be any new word if and only if the pattern has new character

For the first part, we construct a save dictionary to check whether the condition is true.
For the second part, we create an exist set to check whether the condition is true.