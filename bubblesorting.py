def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    arr = [9, 4, 1, 5, 2]
    bubble_sort(arr)
    for i in range(len(arr)):
        print(arr[i], end=" ")
