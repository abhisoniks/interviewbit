class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        if len(A)<3:
            return -1
        if len(A)==3:
            return A[0]*A[1]*A[2]
        if max(A)<0:
            p=[A[0],A[1],A[2]]
            p.sort()
            for i in A[2:]:
          #      print(p)
                if i>p[2]:
                    p[0]=p[1]
                    p[1]=p[2]
                    p[2]=i
                    continue
                if i>p[1]:
                    p[0]=p[1]
                    p[1]=i
                if i>p[0]:
                    p[0]=i

            return p[0]*p[1]*p[2]


        po=[]
        nv=[]
        for i in range(len(A)):
            if A[i]<0:
                if len(nv)<2:
                    nv.append(A[i])
                    nv.sort(reverse=True)
                    continue
                if abs(nv[0])<abs(A[i]):
                    nv[0]=A[i]
                    nv.sort(reverse=True)
                    continue
            else:
                if len(po)<3:
                    po.append(A[i])
                    po.sort()
                    continue
                if A[i]>min(po):
                    po[0]=A[i]
                    po.sort()
                    continue


        if len(nv)<2:
            return po[0]*po[1]*po[2]
        if len(po)<3:
            return po[-1]*nv[0]*nv[1]

        q=po[0]*po[1]*po[2]
        r=po[2]*nv[0]*nv[1]
        return max(q,r)
