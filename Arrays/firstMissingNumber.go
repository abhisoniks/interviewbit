func firstMissingPositive(A []int )  (int) {
      p, max := findMin(A)
      min := A[p]
      if max <=0 || min >1 {return 1}

      if min==max && min!=1{ return 1 }
      if min==max && min==1{ return 2}

      max = min + len(A)-1

      i :=0
      for i<len(A) {
          if A[i] >= min && A[i] <= max {
              index := A[i]-min
              if index==i {
                  i++;
                  continue
              }

              temp := A[i]; A[i] = A[index]; A[index] = temp
              continue
          }
          i++
      }

      for i:=1;i< len(A);i++{
        if A[i-1]>=0 && A[i]!=min+i && min+i>0{
           return min+i
        }
      }

      q :=A[len(A)-1]+1

      if q<=0 {
          return 1
      }
        return A[len(A)-1]+1

}



func findMin( A []int) (int,int) {
    min := A[0]; max:=A[0]; index:=0
    for i:=1; i< len(A);i++{
        if A[i] < min{
             index=i; min = A[i]
        }

        if A[i]>max{
             max=A[i]
        }
    }

    return index,max
}
