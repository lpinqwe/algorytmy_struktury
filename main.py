#HarelikauValadar11.03.2024
def read_std_in():
    buf = input()
    buf=buf.split(" ")
    return buf

def reverce_arr(arr):
    if(len(arr)==1):
        return arr
    return arr[::-1]
if __name__ == '__main__':

    arr=read_std_in()
    arr=reverce_arr(arr)
    print(*arr)