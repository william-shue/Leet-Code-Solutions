#from: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hmap = {}
        longest = 0
        sliderStart = 0

        for index, val in enumerate(s): #iterate through ALL values
            if val in hmap: #if dup. is found
                shiftVal = hmap[val] #find the slider shift value
                for i in range(sliderStart, shiftVal+1): #from slider start to shift val.
                    hmap.pop(s[i], None) #remove vals. from hash map
                    sliderStart += 1 #shift the slider by 1 each time
                hmap[val] = index #add new instance of duplicate.

            else:
                hmap[val] = index #add unique value
                if len(hmap) > longest:
                    longest = len(hmap) #update longest if applicable

        return longest
