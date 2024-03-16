# 16.03.2024 harelikau Valdar
# https://ru.wikipedia.org/wiki/Обратная_польская_запись#Вычисления_на_стеке

arr_data = ['*', '+', '-', '/']


def polish_notation(arr):
    # ["2", "1", "+", "-3", "*"]
    arr.reverse()
    number_stack = []
    while len(arr):
        val = arr.pop()
        if (val in arr_data):
            val_1 = number_stack.pop()

            val_2 = number_stack.pop()
            str_to_eval = val_2 + val + val_1
            number_stack.append(math(str_to_eval))
        else:
            number_stack.append(val)
    return int(float(*number_stack))


def math(arr):
    arr = arr + ".0"

    return str(int(eval(arr)))


def read_std_in():
    buf = input()
    buf = buf.replace("[", '').replace("]", '')
    buf = buf.split(",")
    arr = list(x.replace('"', '') for x in buf)

    return arr


if __name__ == '__main__':
    #arr = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    arr = read_std_in()
    print(polish_notation(arr))
