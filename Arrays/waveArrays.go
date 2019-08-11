import (
  "sort"
  "fmt"
  )
func wave(A []int )  ([]int) {
    if len(A) <=1 {return A}
    sort.Ints(A)
    fmt.Println(A)
    i:=0
    for i<len(A)-1{
      temp := A[i];
      A[i] = A[i+1]; A[i+1] = temp;
      i+=2
    }

    return A
}
