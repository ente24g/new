def calculator():
    while True:
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            operation = input("Введіть операцію (+, -, *, /) або 'exit' для виходу: ")

            if operation == 'exit':
                print("Калькулятор завершив роботу.")
                break

            if operation == '+':
                print(f"Результат: {a + b}")
            elif operation == '-':
                print(f"Результат: {a - b}")
            elif operation == '*':
                print(f"Результат: {a * b}")
            elif operation == '/':
                if b != 0:
                    print(f"Результат: {a / b}")
                else:
                    print("Помилка: ділення на нуль")
            else:
                print("Помилка: невідома операція")
        except ValueError:
            print("Помилка: введіть коректні числа")


# Запуск калькулятора
calculator()
