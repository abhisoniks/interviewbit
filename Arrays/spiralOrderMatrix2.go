//import "fmt"
func generateMatrix(A int )  ([][]int) {
  B := make([][]int, A)
  for i:=0;i<A;i++{
   B[i] = make([]int, A)
  }
  ele :=0
  for i:=0;i<A-i;i++{
     j:=i

     for j<A-i{
        ele++
        B[i][j] = ele
        j++
     }

     p := i+1
     for p<A-i{
        ele++
        B[p][j-1] = ele
        p++
     }

     k := j-2
     for k>=i{
        ele++
        B[p-1][k] =  ele
        k--
     }
 //    fmt.Println(k, i)
     k++

     for t := A-2-k; t>i ; t--{
        ele++
        B[t][i] =  ele
     }
  }

 // fmt.Println(B)
  return B
}
