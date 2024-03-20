def selection_sort(arr):
    #https://en.wikipedia.org/wiki/Selection_sort
    n = len(arr)
    for i in range(n):
        # Znajdowanie indeksu najmniejszego elementu w nieposortowanej części listy
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Zamiana miejscami znalezionego najmniejszego elementu z elementem na pozycji i
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Przykładowa lista liczb do posortowania
arr = [64, 25, 12, 22, 11]
print("Przed sortowaniem przez wybieranie:", arr)

selection_sort(arr)

print("Po sortowaniu przez wybieranie:", arr)