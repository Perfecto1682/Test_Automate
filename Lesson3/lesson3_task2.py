from Lesson3.Smartphone import Smartphone

catalog = []

catalog.append(Smartphone('Apple', 'iPhone 12', '+7 (123) 456-7890'))
catalog.append(Smartphone('Samsung', 'Galaxy S21', '+7 (987) 654-3210'))
catalog.append(Smartphone('Huawei', 'P40 Pro', '+7 (555) 555-5555'))
catalog.append(Smartphone('Xiaomi', 'Mi 11', '+7 (888) 888-8888'))
catalog.append(Smartphone('Infinix', 'M21', '+7 (666) 666-6666'))

for phone in catalog:
    print(f'Марка: {phone.brand}, Модель: {phone.model}, Номер телефона: {phone.number}') # noqa:  E501. # Использую игнорирование длины текста для лучшего чтения кода.
