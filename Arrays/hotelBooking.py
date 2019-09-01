class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def myfunc(self,val):
        return int(val[:-1])

    def hotel(self, arrive, depart, K):
        event=[str(i)+"a" for i in arrive]
        event.extend([str(i)+"e" for i in depart])
        event.sort(key = self.myfunc)
        count=0
        i=0
        while i < len(event):
            if event[i][-1]=="e":
                count-=1
                i+=1
                continue
            if count>=K:
                if i<len(event)-1:
                    if event[i+1][-1]=="e" and event[i+1][:-1]==event[i][:-1]:
                        i+=2
                        continue
                return 0
            if event[i][-1]=="a":
                count+=1
            i+=1
        return 1
