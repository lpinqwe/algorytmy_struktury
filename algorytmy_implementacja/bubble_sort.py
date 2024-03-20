def bubble_sort(arr):
    #https://en.wikipedia.org/wiki/Bubble_sort
    n = len(arr)
    # Iterujemy po wszystkich elementach listy
    for i in range(n):
        # Ostatnie i elementów jest już na swojej miejscu
        # Dlatego nie musimy ich porównywać
        for j in range(0, n-i-1):
            # Zamieniamy elementy, jeśli są w złej kolejności
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Przykładowa lista liczb do posortowania
arr = [64, 34, 25, 12, 22, 11, 90]
print("Przed sortowaniem bąbelkowym:", arr)

bubble_sort(arr)

print("Po sortowaniu bąbelkowym:", arr)
