//import "fmt"
func flip(A string )  ([]int) {
  B:= make([]int,len(A))
  for i:=0;i<len(A);i++{
     B[i] =int(A[i])-48
    if B[i] == 0 {
      B[i] = 1
    }else {
      B[i] = -1
    }
  }

  sp, ep := calculateMaxSum(B)
  if sp ==-1{
  return nil
  }

  return []int{sp,ep}
}

func calculateMaxSum(B []int) (int,int){
  // fmt.Println(B)
   size:= len(B)
   max:= make([]int, len(B)); max[size-1]=B[size-1]
   ep := make([]int, len(B)); ep[size-1] = size-1
   sp := size-1; EndP := size-1; MaxTill := B[size-1]
   for i:=len(B)-2;i>=0;i--{
      if max[i+1] > 0 {
         max[i] = B[i] + max[i+1]
         ep[i] = ep[i+1]

      }else{
        max[i] = B[i];
        ep[i] = i
      }

      if max[i]>=MaxTill{
             EndP=ep[i];sp=i
             MaxTill = max[i]
       }
      // fmt.Println(i, sp, EndP, MaxTill)
   }

   if MaxTill == -1{
   return -1,-1}

   return sp+1,EndP+1
  }
