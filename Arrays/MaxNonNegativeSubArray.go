func maxset(A []int )  ([]int) {
     Max:=0; sp:=0;ep:=0; flag:=false
     for i:=0;i<len(A);i++ {
       cSp := i; cSum :=0
       for i<len(A) && A[i]>=0 {
          flag = true
          cSum+=A[i]
          i++
       }

       if cSum > Max{
          Max = cSum
          sp = cSp; ep = i-1
       }

       if cSum == Max{
          if (i-1)-cSp > ep-sp {
             Max = cSum
             sp = cSp; ep = i-1
          }

          if (i-1)-cSp == ep-sp{
             if cSp < sp {
               Max = cSum
               sp = cSp; ep = i-1
             }
          }
       }
     }

     if flag{
        return A[sp:ep+1]
     }
        return nil

}
