import "fmt"
func longestCommonPrefix(A []string )  (string) {
  if len(A)==1{
    return A[0]
  }


 prefix := findPrefix(A[0],A[1])
 fmt.Println(">>", prefix)
  for i:=2; i<len(A); i++{
     prefix = findPrefix(prefix,A[i])
     fmt.Println("&",prefix)
  }

  return prefix
}


func findPrefix(A, B string) string{
fmt.Println("44", A, B)
  i:=0
  for i< len(A) && i<len(B){
    if A[i] != B[i]{
        break
    }
    i++
  }

  if i==0 {return ""}
  return A[:i]
}
