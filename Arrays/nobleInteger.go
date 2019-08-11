import "sort"

func solve(A []int )  (int) {
   sort.Ints(A)
   for i, val := range A{
     if val == len(A)-i-1 {
       if i+1<len(A) && A[i+1] == val{
       continue
       }
       return 1
     }
   }
   return -1
}
