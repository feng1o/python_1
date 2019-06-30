#!/usr/bin/env python3


def twoSum(arr, tartGet):
    mp = {} 
    for i  in range(len(arr)):
        print("-----i = ", i)
        complent = tartGet - arr[i]
        if complent in mp:
            return (i, mp[complent])
        else :
            mp[complent] = i


print(twoSum([1,2,6,2,1,6,23],12))