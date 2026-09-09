class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(len(s))
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        else:
            left = 0 
            right = 0
            chara = set()
            longest = 0 
            curr_longest = 0 
            while right < len(s): 
                if s[right] in chara: 
                    while s[right] in chara:
                        chara.remove(s[left])
                        left += 1
                    chara.add(s[right])
                    right += 1
                else: 
                    chara.add(s[right])
                    curr_longest = len(chara)
                    if curr_longest > longest:
                        longest = curr_longest
                    right += 1
                    # print(chara)
                # print(longest)
            return longest