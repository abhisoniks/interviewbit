import "fmt"
func repeatedNumber(A []int )  ([]int) {
    m:=0
    r:=0
    sumActual,sumExpected := calculateSum(A)
    diff := sumActual - sumExpected
    fmt.Println("*",diff)
    //r-m = diff
    SSActual, SSExpected := calcualteSumSquare(A)
    diff2 := SSActual - SSExpected
    fmt.Println(">",diff2)
    // (r - m)(r + m) = diff2


    temp := diff2/diff  // (r+m) = temp
    fmt.Println(">",temp)
    temp2 := temp+diff     // 2*r = diff +temp
    r = temp2/2       // r =

    m = r+diff
    return []int{r, m}
    
