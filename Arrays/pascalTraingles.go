import "fmt"
func solve(A int )  ([][]int) {
  B := make([][]int, A)
  fmt.Println(">>")
  B[0][0] = 1
  fmt.Println(">>")
  for i:=1;i<A;i++{
    for j:=0;j<=i;j++{
      if j==0 {
         B[i][0] = B[i-1][0]
         continue
      }

      if i==j {
        B[i][j] = B[i-1][j-1];continue
      }

      B[i][j] = B[i-1][j-1]+ B[i-1][j]
    }
  }

  return B
}
