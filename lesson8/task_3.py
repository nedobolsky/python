class MyList:
    my_list = []

    @classmethod
    def examination(cls):
        print('Для выхода из программы нажмите q')
        while True:
            try:
                num = input('Введите число - ')
                if num == 'q':
                    break
                else:
                    num = int(num)
                cls.my_list.append(num)
            except:
                print('Ошибка. Неверный тип данных')
        print(cls.my_list)


data = MyList()
data.examination()
