import math
def task_integer19():
    try:  # проверка на ошибки
        N = int(input("N (seconds) = "))
    except ValueError:  # если ошибка
        print("N must be an INTEGER !!!")
        input("Press enter for exit ...")
    else:  # если нет ошибки
        minutes = N // 60
        print("Full minutes since the start of the day:", minutes)

# Вызовем функцию для выполнения
task_integer19()
