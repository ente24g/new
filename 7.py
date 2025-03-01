print("Доброго дня сьогодні тобі треба відповісти на питання по грі Geometry Dash")
while True:
    questions = input ("питання 1 що треба тобі там робити?")
    if questions == "паркурити":
        print(f"правельно проходи далі!")
        break
    elif questions == "не знаю":
        print("не правельно")
    else:
        print("нет")