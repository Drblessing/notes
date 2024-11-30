""" 
An overview of sorting algorithms.
"""


def insertion_sort(arr):
    """Insertion sort is a simple sorting algorithm that builds
    the final sorted array one item at a time.

    It is much less efficient on large lists than more advanced algorithms

    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Example usage:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array is:", arr)


def merge_sort(arr):
    """Merge sort is a divide and conquer algorithm that divides the input
    array into two halves, calls itself for the two halves, and then merges
    the two sorted halves.

    Time complexity: O(n log n)
    Space complexity: O(n)
    """

    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        # while i < len(L):
        #     arr[k] = L[i]
        #     i += 1
        #     k += 1

        # while j < len(R):
        #     arr[k] = R[j]
        #     j += 1
        #     k += 1
        # After the main merge loop
        arr[k:] = L[i:] + R[j:]


# Example usage:
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array is:", arr)
