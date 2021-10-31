words = input('Введите слова разделеные пробелом ').split()
latin = set('zaqxswcdevfrbgtnhymjukilop')


def int_func(words):
    for element in words:
        if not set(element).difference(latin):
            print(element.capitalize())


int_func(words)
