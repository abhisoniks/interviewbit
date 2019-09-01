class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        carry=0
        diff = abs(len(A)-len(B))
        p=["0" for i in range(diff)]
        difStr="".join(p)
        if len(A)>len(B):
            B=difStr+B
        if len(A)<len(B):
            A=difStr+A
        res=""
        i=len(A)-1
        j=len(B)-1
        while(i>=0 and j>=0):
            print("params=",A[i],B[j])
            p=int(A[i]) ^ int(B[j])
            print("p=",p)
            p=p ^ carry
            print("p=",p," carry=",carry)
            res=str(p)+res
            print("res",res)
            if A[i]==B[j] and A[i]=="1":
                print("res>>",res)
                carry=1
            elif p==1 and carry==1:
                print("##>>",res)
                carry=1
            elif p==0:
                print("##")
                carry=0

            i-=1
            j-=1
        if carry!=0:
            return str(carry)+res
        return res
