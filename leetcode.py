# Write a Python program to sort a list using bubble sort 
# and count the number of swaps performed.

def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return arr, swap_count

# Example usage
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list, swaps = bubble_sort(sample_list)
    print("Sorted List:", sorted_list)
    print("Number of swaps:", swaps)