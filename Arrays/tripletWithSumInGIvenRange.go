import "strconv"
 //import "fmt"
func solve(A []string )  (int) {
  if len(A)<3{
      return 0
  }


  first_number, _ := strconv.ParseFloat(A[0], 64)
  min := first_number
  max := first_number
  middle := first_number

  second_number, _ := strconv.ParseFloat(A[1], 64)
  if second_number < first_number {
    min = second_number
  } else {
    max = second_number
  }

 // fmt.Println(min, max)

  third_number, _ := strconv.ParseFloat(A[2], 64)
  if third_number < min {
     middle = min
     min = third_number
  } else if third_number > max {
     middle = max
     max = third_number
  } else{ middle = third_number }

  //fmt.Println(min, max, middle)


  sum:=min + max + middle
  if sum > 1 && sum<2 {
       return 1
  }

  for i := 3;i<len(A);i++ {
    number, _ := strconv.ParseFloat(A[i], 64)
    if sum > 2{
       if number < min {
          max = middle
          middle = min
          min = number
       } else if number > min && number < middle{
          max = middle
          middle = number
       } else if number > middle {
          max = number
       }
    }

    if sum < 1{
        if number < min { continue }
        if number > max{
          min = middle
          middle = max
          max = number
        } else if number > middle && number < max {
          min = middle
          middle = number
        } else if number > min{
          min = number
        }
    }

    //fmt.Println(min+middle+max)
    if min + max + middle >1 && min+max+ middle <2{
   //    fmt.Println(min+middle+max)
    //   fmt.Println(min, ">", middle, ">", max)
       return 1
    }
  }

  return 0
}
