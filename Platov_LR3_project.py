# - ввести натуральное число X
# - ввести цифру A
# - верно ли, что в числе X нет данной цифры А
# - верно ли, что в числе X цифра А встречается более двух раз

def input_x():
    while True:
        try:
            n = int(input('Введите число X -> '))
            return n
        except ValueError:
            continue
            
def zadanie_1(X: int, A: int):
    if str(A) in str(X):
        return False
    return True

def zadanie_2(X: int, A: int):
    n = 0
    for bukva in str(X):
        print(bukva)
        if bukva == str(A):
            n += 1
    if n > 2:
        return True
    return False

def vernoNenverno(a: bool):
    return "-----------------------------\n" + ("Верно" if a else "Неверно") + "\n-----------------------------"


while True:
    A = input("Перед запуском программы введите цифру A -> ")
    if len(A.strip()) != 1:
        print("Должна быть введена одна цифра")
        continue
    A = int(A)
    break

X = input_x()
while True:
    print(
        (
            "Меню\n"
            "1) Верно ли, что в числе X нет данной цифры А\n"
            "2) Верно ли, что в числе X цифра А встречается более двух раз\n"
            "3) Заменить X на новое значание\n"
            "0) Выход"
        )
    )
    i = input('Введите число ->')
    if i == '0':
        break
    elif i == '1':
        print(vernoNenverno(zadanie_1(X,A)))
    elif i == '2':
        print(vernoNenverno(zadanie_2(X,A)))
    elif i == '3':
        X = input_x()