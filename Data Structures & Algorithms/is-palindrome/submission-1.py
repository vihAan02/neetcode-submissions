class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        left = 0
        right = -1 
        for i in range(len(s) // 2):
            if (s[left] == s[right]):
                
                left += 1
                right -= 1
            else:
                return False
        return True