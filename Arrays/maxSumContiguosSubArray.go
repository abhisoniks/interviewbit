// import "fmt"
func maxSubArray(A []int )  (int) {
  overAllMax := A[len(A)-1]
  pMax := A[len(A)-1]
  for i:=len(A)-2; i>0; i-- {
    if pMax > 0 {
      pMax +=A[i]
    } else {
      pMax = A[i]
    }

    if pMax > overAllMax {
       overAllMax = pMax
    }

    // fmt.Println(pMax, overAllMax)
  }

  return overAllMax
 }
