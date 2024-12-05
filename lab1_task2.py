import math
def task_expression():
    try:
        x = float(input("Enter x = "))
    except ValueError:
        print("x must be a NUMBER !!!")
        return
    
    try:
        numerator = math.tan(abs(3 * x ** 3 + 6 * x - 31.15) + math.log(abs(x - 2.5), 5))
        denominator = (math.sin(x ** 2) + (1 / 4) * math.log(abs(x ** 2 - 2.5), 5)) ** (1 / 3)
        y = numerator / denominator
    except Exception as e:
        print("Calculation error !!!", e)
    else:
        print("y = ", y)

# Вызовем функцию для выполнения
task_expression()
