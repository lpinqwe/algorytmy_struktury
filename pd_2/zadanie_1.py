"""Napisz funkcję przyjmującą ciąg znaków zawierający trzy typy nawiasów: "(", ")", "[", "]", "{","}".
Funkcja powinna zwracać 1 w przypadku poprawnego nawiasowania lub 0 w przypadku błędnego.
 Nawiasowanie uznajemy za poprawne jeżeli spełnione są wszystkie poniższe warunki:
• nawiasy otwierające są zamykane przez nawiasy tego samego typu,
• nawiasy otwierające są zamykane w odpowiedniej kolejności,
• każdy nawias zamykający ma odpowiadający mu nawias otwierający tego samego typu.
"""


def counter_wthere_no_matter_sequence_of_brackets(string):
    type1, type2, type3 = 0, 0, 0
    type11, type22, type33 = 0, 0, 0
    for i in range(len(string)):
        if (i == "("):
            type1 = type1 + 1
        if (i == "["):
            type2 = type2 + 1
        if (i == "{"):
            type3 = type3 + 1
        if (i == ")"):
            type11 = type11 + 1
        if (i == "]"):
            type22 = type22 + 1
        if (i == "}"):
            type33 = type33 + 1
    if (type1 == type11 and type2 == type22 and type3 == type33):
        return 1
    return 0


def counter_with_sequence(string):
    try:
        now_is_open_stack = []
        for i in range(len(string)):
            if (string[i] == "("):
                now_is_open_stack.append("(")
            if (string[i] == "["):
                now_is_open_stack.append("[")
            if (string[i] == "{"):
                now_is_open_stack.append("{")
            if (string[i] == "}" and now_is_open_stack.pop() != "{") or (
                    string[i] == ")" and now_is_open_stack.pop() != "(") or (
                    string[i] == "]" and now_is_open_stack.pop() != "["):
                return 0
        if (len(now_is_open_stack) != 0):
            return 0
        return 1
    except:
        return 0


def read_std_in():
    buf = input()
    # buf=buf.split("")
    return buf


if __name__ == '__main__':
    arr = read_std_in()
    print(counter_with_sequence(arr))
