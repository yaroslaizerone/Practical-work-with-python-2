try:
    while True:
        print("Введите название файла : ") #take values
        true: bool = True
        word: str = input()
        if word.isalpha() and len(word) > 3: #check
            file: str = f"F:\\PyP\\{word}.txt" #create path
            with open(file, "w"): #create file
                print("Успешное создание файла")
        else:
            print("Введите корректно данные")
except Exception:
    print("Произошла ошибка")
except KeyboardInterrupt:
    print("Заверешение работы")
