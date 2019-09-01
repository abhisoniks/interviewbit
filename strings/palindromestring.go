import "fmt"

func isPalindrome(A string )  (int) {
first := 0
last := len(A)-1


for first < last {
  front := A[first]
  rear := A[last]
  flag := false
  if front < 48 || (front > 57 && front < 65) || (front >90 && front < 97) || front > 122{
    first++
    flag = true
  }
  if rear < 48 || (rear > 57 && rear < 65) || (rear >90 && rear < 97) || rear > 122{
    last--
    flag = true
  }
  if flag {
      continue
  }

  if rear > 97 {
      rear -= 32
  }

  if front > 97 {
      front -=32
  }

  if front != rear{
      return 0
  }

  fmt.Println(front, rear)


  first++;last--


}

return 1xw
}
