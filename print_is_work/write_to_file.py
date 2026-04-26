with open("журнал_событий.txt", "a", encoding="utf-8") as flight_file:
    print("10:00 - Начало регистрации на рейс SU123", file=flight_file)
    print("10:15 - Открыт выход 15", file=flight_file)  