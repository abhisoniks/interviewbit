class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        seq = [1]
        p = 1
        while(p<A):
            p+=1
            c = 1
            num = seq[0]
            l = []
            for i in range(1,len(seq)):
                if num==seq[i]:
                    c+=1
                else:
                    l.append(c)
                    l.append(num)
                    num = seq[i]
                    c = 1
            l.append(c)
            l.append(num)
            seq.clear()
            seq.extend(l)

        return ''.join(list(map(str,seq)))
