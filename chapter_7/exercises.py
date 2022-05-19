"""
Упражнения главы 7
"""
import re
from pprint import pprint



# 1.
mystery = '\U0001f4a9'
print(mystery)

# 2.
# Кодируем mystery с использованием UTF-8
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

# 3.
# Декодируем, используя UTF-8 в pop_string
# Должно совпадать с mystery
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(pop_string == mystery)

# 4.
# Старый стиль форматирования.
# Подставить "roast beef", "ham", "head", "clam"
poem = """My kitty cat likes %s.
My kitty cat likes %s.
My kitty cat fell on his %s
And now thinks he's a %s."""
print("Стихотворение без форматирования", poem, sep='\n')
print()
print("Стихотворение с форматированием")
print(poem % ('roast beef', 'ham', 'head', 'clam'), end='\n\n')

# 5.
# Новый стиль форматирования.
letter = """Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your {room}.
Please note that it should never be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling. We will send you another {product} that,
in our tests, is {percent}% less likely to have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""

# 6.
# Вывод в новом стиле форматирования.
response = {
        "salutation": "Colonel",
        "name": "Hackenbush",
        "product": "duck blind",
        "verbed": "imploded",
        "room": "conservatory",
        "animals": "emus",
        "amount": "$1.38",
        "percent": "1",
        "spokesman": "Edgar Schmeltz",
        "job_title": "Licensed Podiatrist"
        }
print("Неформатированный текст письма", letter, sep='\n', end='\n\n')
print("Форматированный текст письма со значениями словаря response: ")
pprint(response)
print()
print(letter.format(**response))

# 7.
# Регулярные выражения.
mammoth = """
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
"""

# 8.
# import re
# Все слова, которые начинаются с буквы "с".
print(re.findall('c\w*', mammoth))
# 9.
# Все четырехбуквенные слова, которые начинаются с буквы "с".
print(re.findall(r'c\w{3}\b', mammoth))
# 10.
# Все слова, которые кончаются на букву "r".
print(re.findall(r'\w*r\b', mammoth))
# 11.
# Все слова, которые содержат три гласные подряд.
print(re.findall(r'\w*[aeiouy]{3}\w*', mammoth))

