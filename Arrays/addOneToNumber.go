func plusOne(A []int )  ([]int) {
  size := len(A)
  p := size-1
  for p>=0 &&  A[p] == 9{
    A[p] = 0
    p--
  }

  if p != -1{
    A[p] = A[p]+1
    nonZero := 0
    for i := 0; i<p ; i++{
      if A[i] !=0 {
        break
      } else {
        nonZero++
       }
    }
    if nonZero >0 {
    A = A[nonZero:]
    }
    return A
  }


 b := make([]int,size+1)
 b[0] = 1
 for i:=0; i<size;i++ {
       b[i+1] = A[i]
 }
 return b
}
