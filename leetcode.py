# Write a Python program to modify bubble sort to sort a list 
# of strings in alphabetical order.

def bubble_sort_strings(string_list):
    n = len(string_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if string_list[j] > string_list[j+1]:
                string_list[j], string_list[j+1] = string_list[j+1], string_list[j]
    return string_list


strings = ["banana", "apple", "cherry", "date"]
sorted_strings = bubble_sort_strings(strings)
print(sorted_strings)