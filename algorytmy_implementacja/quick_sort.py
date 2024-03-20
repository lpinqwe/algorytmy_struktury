#https://ru.wikipedia.org/wiki/Быстрая_сортировка
def quicksort(Arr, p, r):
    if (p < r):
        q = partition(Arr, p, r)
        quicksort(Arr, p, q - 1)
        quicksort(Arr, q + 1, r)
    # return arr


def partition(Arr, p, r):
    piwot = Arr[r]
    i = p - 1
    for j in range(p, r):
        if (Arr[j] <= piwot):
            i = i + 1
            print(f"({Arr[i]},{Arr[j]})", end=' ')
            Arr[i], Arr[j] = Arr[j], Arr[i]
    print(f"({Arr[i + 1]},{Arr[r]})", end=' ')
    Arr[i + 1], Arr[r] = Arr[r], Arr[i + 1]

    return i + 1