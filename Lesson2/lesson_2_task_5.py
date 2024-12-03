def month_to_season(month):
    if 3 <= month <=5:
        return 'Весна'
    elif 6 <= month <= 8:
        return 'Лето'
    elif 9 <= month <= 11:
        return 'Осень'
    elif month == 12 or 1 <= month <= 2:
        return 'Зима'
    else:
        return 'Неверный месяц'


month = 0
print(month_to_season(month))
