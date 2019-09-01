class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        cr=0
        i=0
        res=[]
        while i<len(A):
        #    print("$$>",i,A[i])
            if A[i] =="{" or A[i]=="[":
                p=""
                for k in range(cr):
                    p+="\t"
                res.append(p+A[i])
                cr+=1
                i+=1
                continue
            if A[i]=="}" or A[i]=="]":
                cr-=1
                p=""
                for k in range(cr):
                    p+="\t"
                p=p+A[i]
                i+=1
                if i<len(A) and A[i]==",":
                    res.append(p+",")
                    i+=1
                    continue
                res.append(p)
                continue
            p=""
            for k in range(cr):
                p+="\t"
            while(i<len(A) and A[i]!=","):
                if A[i]=="}" or A[i]=="{" or A[i]=="[" or A[i]=="]":
                    break
                p=p+A[i]
                i+=1
            if i<len(A) and A[i]=="}" or A[i]=="]":
                res.append(p)
                continue
            if i<len(A) and A[i]=="{" or A[i]=="[":
                res.append(p)
                continue
            res.append(p+",")
            i+=1
        return res
