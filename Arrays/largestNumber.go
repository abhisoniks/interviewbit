import "fmt"
import "sort"
import "strconv"
func largestNumber(A []int )  (string) {
  sort.Slice(A, func(x, y int) bool {
    result, _ := strconv.Atoi(fmt.Sprintf("%d%d", A[x], A[y]))
    result2, _ := strconv.Atoi(fmt.Sprintf("%d%d", A[y], A[x]))
    return result>result2
})

 res:=""
for i:=0;i< len(A);i++{
  p := strconv.Itoa(A[i])
  res = res+p
}

if result, _ := strconv.Atoi(res);result==0{
return "0"
}

return res
}
