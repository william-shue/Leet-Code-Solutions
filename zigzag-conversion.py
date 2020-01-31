#from: https://leetcode.com/problems/zigzag-conversion

class Solution(object):
    def convert(self, s, numRows):
        result = ""
        n = numRows

        if n < 2:
            return s

        for i in range(n):
          j = i
          alt = False
          while j <= len(s)-1:#len(s): #for end rows
            if i == 0 or i == n-1:
              result += s[j]
              j += ((n-1) * 2)
            elif i % 2 != 1 and i == i // 2: #for middle row
              result += s[j]
              j += ((n-1) * 2) - (2*i)
            else: # for rows in between

              if alt == False:
                result += s[j]
                j += abs(((n-1) * 2) - (2*i))
                alt = True
              else:
                result += s[j]
                j += abs((((n-1) * 2) - (2*i)) - ((n-1) * 2))
                alt = False
        return result
