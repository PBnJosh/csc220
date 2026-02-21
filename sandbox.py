#!/usr/local/bin/python3

s = "G J D C L B A F I H K E"
arr = s.split()
pivot = arr[len(arr) - 1]
left = 0;
right = len(arr) - 2
	
while (left <= right):
    swap = True
    if (arr[left] < pivot):
        left += 1
        swap = False
    if (arr[right] > pivot):
        right -= 1
        swap = False
    if (swap):
        arr[left], arr[right] = arr[right], arr[left]
arr[left], arr[len(arr) - 1] = arr[len(arr) - 1], arr[left]
print(arr)