'''
Необходимо создать класс Human с атрибутами:

name
surname
age
phone
address
Атрибуты должны заполняться в методе __init__

Так-же нужно написать методы:

get_info() - который возвращает словарь в котором находится информация о человеке
call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
Нужно создать 3 обьекта класса Human и вызвать у них метод get_info
'''


class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        a = {'name': f'{self.name}', 'surname': f'{self.surname}', 'age': f'{self.age}', 'phone': f'{self.phone}', 'addres': f'{self.address}'}
        return a

    def call(self, phone_number):
        print(f'{self.phone} calls {phone_number}')


person1 = Human('Alexandra', 'Stepanova', '19', '+380961234567', 'Korolenko st, 33, Dnipro')
person2 = Human('Vitalii', 'Kuznecov', '21', '+380991234567', 'Robocha st, 26, Dnipro')
person3 = Human('Olga', 'Morozova', '29', '+380931234567', 'Bakha st, 52, Dnipro')

print(person1.get_info())
print(person2.get_info())
print(person3.get_info())


