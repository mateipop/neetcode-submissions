class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        print(s)
        right_index,left_index = len(s)-1,0
        while right_index>left_index:
            while left_index<=right_index and not s[left_index].isalnum():
                left_index+=1
            while right_index >= left_index and not s[right_index].isalnum():                
                right_index-=1
            
            if left_index<=right_index:
                if s[left_index]!=s[right_index]:
                    return False
            left_index+=1
            right_index-=1
        return True  

        