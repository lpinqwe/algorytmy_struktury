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


def make_money_for_me_bae(arr):
    try:
        min = arr[0]
        for i in arr:
            if (i < min):
                min=i

        arr = reverce_arr(arr)
        arr = arr[:arr.index(min)]
        max = arr[0]
        for i in arr:
            if(i>max):
                max=i
        return (max-min)
    except:
        return 0

if __name__ == '__main__':
    arr = read_std_in()
    print(make_money_for_me_bae(arr))
    #print(f"ur cash is {make_money_for_me_bae(arr)}$$$")
    # arr=reverce_arr(arr)
    # print(*arr)
    # print(palindome_check(arr))
