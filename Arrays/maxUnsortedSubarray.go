func subUnsort(A []int )  ([]int) {
   if len(A) <=1 {
       return []int{-1}
   }

   left:=0;
   right:= len(A)-1
   for i:=1;i< len(A);i++{
     if A[i] < A[i-1] {
     left = i-1; break
     }
   }


   for i:= len(A)-2; i>=0 ;i--{
     if A[i] > A[i+1] {
       right = i+1; break
     }
   }

   if left ==0 && right == len(A)-1{
      return []int{-1}
   }


   min:=A[left+1]; max:=A[left+1]
   for i:=left+1;i<=right;i++{
      if A[i] < min { min = A[i] }
      if A[i] > max { max = A[i] }
   }

   answerLeft := left
   answerRight := right
   for (left>=0 && min < A[left]) || (right<len(A)&&max > A[right]) {
        if left ==-1 && right>len(A) {break}
        if (left>=0 && min >= A[left]) && (right<len(A) &&max <= A[right]) {break}
        if left>=0 &&  min < A[left] {
             answerLeft = left
             if A[left] > max {max = A[left]}
             left--;
        }

        if right<len(A)&& max > A[right] {
            answerRight = right
            if A[right] < min {min = A[right]}
            right++
        }
   }

   return []int{answerLeft,answerRight}
}
