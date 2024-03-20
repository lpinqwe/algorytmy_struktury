def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Przykładowa lista liczb do posortowania
arr = [2, 11,12, 13, 5, 6]
print("Przed sortowaniem przez wstawianie:", arr)

insertion_sort(arr)

print("Po sortowaniu przez wstawianie:", arr)
