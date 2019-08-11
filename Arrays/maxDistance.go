func maximumGap(A []int )  (int) {
  minArray := make([]int, len(A))
  maxArray := make([]int, len(A))

  min, max := A[0], A[len(A)-1]

  for i:=0; i<len(A); i++ {
     if A[i]<min {
          min = A[i]
     }

     minArray[i] = min
  }

  for i:=len(A)-1;i >= 0;i-- {
     if A[i]>max {max = A[i]}
     maxArray[i] = max
  }

  i, j := 0, 0; sol:=-1
    for j < len(A) && i < len(A) {
        if minArray[i] <= maxArray[j] {
            sol = mx(sol, j-i)
            j = j + 1
        } else {
            i = i + 1
        }
    }
    return sol
}

func mx(a,b int) int {
    if a > b {
        return a
    }
    return b
}
