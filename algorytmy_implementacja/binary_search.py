#https://en.wikipedia.org/wiki/Binary_search_algorithm
def binary_search(arr):
    target = arr[0]
    arr_bin = arr[1:]
    index_buf = 0
    while True:
        index_middle_elem = int(len(arr_bin) / 2)
        middle_elem = arr_bin[index_middle_elem]
        if((len(arr_bin)==1 or len(arr_bin)==0) and middle_elem!=target):
            break
        if (middle_elem == target):
            return (index_buf + index_middle_elem)
        if (middle_elem < target):
            index_buf = index_buf + index_middle_elem
            arr_bin = arr_bin[index_middle_elem:]
            continue
        if (middle_elem > target):
            arr_bin = arr_bin[:index_middle_elem]
            continue

    return -1
