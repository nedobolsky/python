class Warehouse:
    equipment_dict = {}

    def __init__(self, length, width):
        self.length = length
        self.width = width


class OfficeEquipment:
    def __init__(self, model, page, color):
        self.model = model
        self.page = page
        self.color = color


class AppendEquipment(Warehouse):
    @classmethod
    def append_element(cls):
        while True:
            x = input('Нажмите q для выхода, или Enter для ввода данных ')
            if x == 'q':
                break
            else:
                # ниже словарь сделал для примера
                try:
                    cls.equipment_dict['model'] = input('Введите наименование устройства - ')
                    cls.equipment_dict['quantity'] = int(input('Введите кол-во - '))
                    cls.equipment_dict['price'] = int(input('Введите цену - '))
                except ValueError:
                    print('Вы ввели некоректные данные')

        print(cls.equipment_dict)


class Printer(OfficeEquipment):
    def prints_minute(self):
        return f'Принтер печатает {self.page} страниц в минуту'


class Scanner(OfficeEquipment):
    def scan_prints_minute(self):
        return f'Сканер сканирует {self.page} страниц в минуту'


class Xerox(OfficeEquipment):
    def photocopy_prints_minute(self):
        return f'Ксерокс копирует {self.page} страниц в минуту'


printer_model = Printer('принтер', 20, 30)
scan_model = Scanner('сканер', 30, 10)
xerox_model = Xerox('ксерокс', 7, 21)
print(printer_model.prints_minute())
AppendEquipment.append_element()
