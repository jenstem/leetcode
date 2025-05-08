# Write a Python script to implement bubble sort with 
# an early exit optimization when no swaps are made.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(sample_array)
    print("Sorted array:", sorted_array)