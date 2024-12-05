def task_boolean28():
    try:
        x = float(input("x = "))
        y = float(input("y = "))
    except ValueError:
        print("Both x and y MUST be numbers !!!")
        input("Press enter for exit ...")
    else:
        res = (x > 0 and y > 0) or (x < 0 and y < 0)
        print("The point lies in the first or third quadrant:", res)

# Вызовем функцию для выполнения
task_boolean28()
