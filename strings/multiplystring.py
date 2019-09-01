class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
       # return str(int(A)*int(B))
        if B=="0" or A=="0":
            return str(0)
        if len(A)<len(B):
            temp=A
            A=B
            B=A
        aInt=int(A)
        res=0
        for i in range(len(B)-1,-1,-1):
            bInt=int(B[i])
            bResult=bInt*aInt
            q=str(bResult)
            p=""
            if bResult!=0:
                p=["0" for j in range(len(B)-1-i)]
            else:
                p=["0" for j in range(len(A)+len(B)-i-2)]
            str1 = q+(''.join(p))
            #print(">>",str1)
            res=res+int(str1)
           # print(">>res",res)
        return str(res)
