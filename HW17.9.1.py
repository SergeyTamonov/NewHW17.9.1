import random
def proverka_dannih_1():
    try:
        posledov_bez_prob = posledov.replace(" ", "")

        if not posledov_bez_prob.isdigit():
            raise ValueError("Неправильный ввод данных.")

    except ValueError as error:
        print(error)
        print("ВВЕДИТЕ ЧИСЛА ЧЕРЕЗ ПРОБЕЛ!!!")
        exit()
def proverka_dannih_2():
    try:
        if not chislo_vvod.isdigit():
            raise ValueError("Неправильный ввод данных.")

    except ValueError as error:
        print(error)
        print("ВВЕДИТЕ ЧИСЛО!!!")
        exit()


def qsort_random(spisok, left, right):
    if left >= right:
        return
    else:
        p = random.choice(spisok[left:right + 1])
        i, j = left, right
        while i <= j:
            while spisok[i] < p:
                i += 1
            while spisok[j] > p:
                j -= 1
            if i <= j:

                spisok[i], spisok[j] = spisok[j], spisok[i]
                i += 1
                j -= 1
                qsort_random(spisok, left, j)
                qsort_random(spisok, i, right)


def binary_search(spisok, chislo, less, more):
    global middle
    middle = (less + more) // 2
    if spisok[more] < chislo:
        print("Введенное число больше максимального числа в последовательности")
        exit()
    if chislo < spisok[less]:
        print("Введенное число меньше минимального числа в последовательности")
        exit()
    if spisok[middle] < chislo <= spisok[middle + 1]:
               return middle

    elif chislo < spisok[middle]:

        return binary_search(spisok, chislo, less, middle - 1)
    else:
        return binary_search(spisok, chislo, middle + 1, more)

posledov = input("Введите числа через пробел: ")
chislo_vvod = input("Введите любое число: ")
proverka_dannih_1()
proverka_dannih_2()
spisok = list(map(int, posledov.split()))
chislo = int(chislo_vvod)
qsort_random(spisok, 0, len(spisok)-1)
binary_search(spisok, chislo, 0, len(spisok)-1)


print(spisok)
print(middle, " - номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу")

