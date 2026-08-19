class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_A = len(s1)
        for _ in range(len(s2) - length_A + 1):
            test = "".join(s2[_ : _ + length_A])
            if sorted(test) == sorted(s1):
                return True

        return False
