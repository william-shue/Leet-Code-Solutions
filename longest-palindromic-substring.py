#source: https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        longest = 0
        resultStart = 0
        resultEnd = 0

        for i in range(0, len(s)-1): #for every value in the string
            start, end = expand(s, i) #call the expand method
            if end - start > longest:
                resultStart = start
                resultEnd = end
                longest = end - start #if a longer value has been found, update tracking values
        return s[resultStart:resultEnd+1] #return splice of the result


def expand(s, center):
  start = center
  end = center

  #first while loop handles cases where there are repeating values from the center
  #for example, "aaa", "aaaa", "abbba", "aaabbbaaa|a"
  while start >= 0 and end < len(s):
    if end+1 < len(s) and s[center] == s[end+1]:
        end += 1
    else:
        break

    if start-1 >= 0 and s[center] == s[start-1]:
        start -= 1
    else:
        break
 #end of first while loop

  #after the above while loop, the comparison is made between the start and end indecies
  #this is where the 'expand' from the center concept comes into play, if start == end then expand
  while start-1 >= 0 and end+1 < len(s) and s[start-1] == s[end+1]:
    start -= 1
    end += 1

  return start, end
