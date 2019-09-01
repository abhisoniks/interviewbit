class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        i=len(A)-1
        l=len(A)-1
        end=i
        for i in range(l,-1,-1):
            asci = ord(A[i])
            if asci<=47 or asci>=58:
                if i==0 and (A[i]=="+" or A[i]=="-"):
                    break
                end=i-1
        if end<0:
            return 0
        number=0
        flag=False
        for j in range(end,-1,-1):
            if j==0 and A[j]=="-":
                if number==0:
                    return 0
                else:
                    flag=True
                    break
            if j==0 and A[j]=="+":
                break
            p=ord(A[j])-48
            number+=(p*pow(10,end-j))
        if number>2147483647:
            if flag:
                return "-"+str(2147483648)
            else:
                return 2147483647
        else:
            if flag:
                return "-"+str(number)
            return number
