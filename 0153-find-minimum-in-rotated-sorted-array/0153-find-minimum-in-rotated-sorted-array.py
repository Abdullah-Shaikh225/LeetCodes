class Solution(object):
    def findMin(self, arr:list[int])->int:
        s = 0
        e = len(arr)-1
        while s<e:
            m = (s+e)//2
            if arr[m]>arr[e]:
                s = m+1
            else:
                e=m
        return arr[s]