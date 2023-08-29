def insertion(arr, n):
    for i in range(1, n):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
        for l in range(5):
            print(arr[l], end=" ")
        print()
    print()

def main():
    arr = [9, 4, 1, 5, 2]
    insertion(arr, 5)
    for i in range(5):
        print(arr[i], end=" ")

if __name__ == "__main__":
    main()
