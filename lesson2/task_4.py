user_phrase = input('Введите фразу ')
data = user_phrase.split()

for i, element in enumerate(data, 1):
    print(i, element[:10])
