from Lesson3.Adress import Adress
from Lesson3.Mailing import Mailing

# Создание адресов
to_address = Adress("190000", "Санкт-Петербург", "Невский проспект", "д 50", "кв 100") # noqa:  E501.
from_address = Adress("105005", "Москва", "Тверская улица", "д 15", "кв 28")


# Создание отправления
mailing = Mailing(to_address, from_address, 150, '1234567890')


# Вывод информации об отправлении
part1 = f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment}" # noqa:  E501.
part2 = f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей." # noqa:  E501.
print(part1)
print(part2)
