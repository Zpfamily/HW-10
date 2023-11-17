from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.value = value
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Phone should be 10 digits and only numbers')
        else:
            return None
   
        


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)
        

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone
        else:
            raise ValueError('Old phone not found')
        

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError('Phone not found')


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if record.name.value in self.data:
            raise ValueError('Record already exists')
        else:
            self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)
   

    def delete(self, name: str):
        self.data.pop(name, None)
        
          

book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)


   # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)


    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

     # Видалення запису Jane
book.delete("Jane")
