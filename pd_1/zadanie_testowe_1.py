#HarelikauValadar11.03.2024
def read_std_in():
    buf = input().strip()
    buf=buf.split(" ")
    buf = [int(elem) for elem in buf]

    return buf

def reverce_arr(arr):
    if(len(arr)==1):
        return arr
    return arr[::-1]

def palindome_check(arr):
    len_arr=len(arr)
    if(len_arr==1):return 1
    for i in range(int(len_arr/2)):
        if(arr[len_arr-1-i]!=arr[i]):
            return 0
    return 1



if __name__ == '__main__':

    arr=read_std_in()
    #arr=reverce_arr(arr)
    #print(*arr)
    print(palindome_check(arr))