# Write a Python function to perform bubble sort on a list of 
# integers and print the list after each full pass.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        print(f"Pass {i+1}: {arr}")
        if not swapped:
            break


numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)