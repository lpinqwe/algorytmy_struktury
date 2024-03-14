# HarelikauValadar12.03.2024
def read_std_in():
    buf = input().strip()
    buf = buf.split(" ")
    buf = [int(elem) for elem in buf]
    return buf


def reverce_arr(arr):
    if (len(arr) == 1):
        return arr
    return arr[::-1]


def palindome_check(arr):
    len_arr = len(arr)
    if (len_arr == 1): return 1
    for i in range(int(len_arr / 2)):
        if (arr[len_arr - 1 - i] != arr[i]):
            return 0
    return 1


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


if __name__ == '__main__':
    arr = read_std_in()
    print(f"{binary_search(arr)}")
    # arr=reverce_arr(arr)
    # print(*arr)
    # print(palindome_check(arr))
