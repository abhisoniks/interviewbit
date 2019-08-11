#!/bin/python3

#Without dp, solution wont work.
import os
import sys

def summingPieces(arr):
    return calculate(arr,0,0,0)

def calculate(arr,start,i,sum_):
    if i==len(arr)-1:
        return sum_+cal(arr,start,i)
    p=calculate(arr,i+1,i+1,sum_+cal(arr,start,i))
    e=calculate(arr,start,i+1,sum_)
    return (p+e)%1000000007

def cal(arr,start,i):
    sum_=sum(arr[start:(i+1)])
    return (len(arr[start:(i+1)])*sum_)%1000000007


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = summingPieces(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
