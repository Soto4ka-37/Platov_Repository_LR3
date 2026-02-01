# - ввести натуральное число X
# - ввести цифру A
# - верно ли, что в числе X нет данной цифры А
# - верно ли, что в числе X цифра А встречается более двух раз
def zadanie_1(X: int, A: int):
    if str(A) in str(X):
        return False
    return True

def zadanie_2(X: int, A: int):
    pass
def vernoNenverno(a: bool):
    return "-----------------------------\n" + ("Верно" if a else "Неверно") + "\n-----------------------------"

X = int(input("Перед запуском программы введите число X -> "))

while True:
    A = input("Перед запуском программы введите цифру A -> ")
    if len(A.strip()) != 1:
        print("Должна быть введена одна цифра")
        continue
    A = int(A)
    break

while True:
    print(
        (
            "Меню\n"
            "1) Верно ли, что в числе X нет данной цифры А\n"
            "2) Верно ли, что в числе X цифра А встречается более двух раз\n"
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