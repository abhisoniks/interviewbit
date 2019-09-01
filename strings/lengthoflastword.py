class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        A.rstrip()
        p=A.split(" ")
        return len(p[-1])
