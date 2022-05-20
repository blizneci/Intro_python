"""
Упражнения главы 7
"""

import re
import unicodedata
import binascii
import struct
from pprint import pprint


# 1.
print("# 1")
mystery = '\U0001f4a9'
mystery_name = unicodedata.name(mystery)
print("mystery is: ", mystery)
print("mystery name is: ", mystery_name)

# 2.
# Кодируем mystery с использованием UTF-8
print("# 2")
pop_bytes = mystery.encode('utf-8')
print("mystery in bytes in 'utf-8' is: ", pop_bytes)

# 3.
# Декодируем, используя UTF-8 в pop_string
# Должно совпадать с mystery
print("# 3")
pop_string = pop_bytes.decode('utf-8')
print("pop_string is: ", pop_string)
print("pop_string == mystery is: ", pop_string == mystery)

# 4.
# Старый стиль форматирования.
# Подставить "roast beef", "ham", "head", "clam"
print("# 4")
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
print("# 5")
letter = """Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your {room}.
Please note that it should never be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling. We will send you another {product} that,
in our tests, is {percent}% less likely to have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""
print("letter without formatting is: ", letter, sep='\n')

# 6.
# Вывод в новом стиле форматирования.
print("# 6")
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
print("Форматированный текст письма со значениями словаря response: ")
pprint(response)
print()
print(letter.format(**response))

# 7.
# Регулярные выражения.
print("# 7")
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
print("mammoth is: ", mammoth)

# 8.
# import re  в начале файла
# Все слова, которые начинаются с буквы "с".
print("# 8")
print("Все слова, которые начинаются с буквы 'c':")
pat = r'\bc\w*'
print("Search pattern is: ", pat)
print(re.findall(pat, mammoth))

# 9.
# Все четырехбуквенные слова, которые начинаются с буквы "с".
print("# 9")
print("Все четырехбуквенные слова, которые начинаются с буквы 'c':")
pat = r'\bc\w{3}\b'
print("Search pattern is: ", pat)
print(re.findall(pat, mammoth))

# 10.
# Все слова, которые кончаются на букву "r".
print("# 10")
print("Все слова, которые кончаются на букву 'r':")
pat = r'\w*r\b'
print("Search pattern is: ", pat)
print(re.findall(pat, mammoth))
print("Все слова, которые кончаются на букву 'l':")
pat = r'[\w\']*l\b'
pat2 = r"\b[\w']*l\b"
# Симол ' нужно экранировать для поиска так: \'
# Или окружить строку шаблона двойными кавычками r"[\w']*l\b"
print("Search pattern is: ", pat)
print(re.findall(pat, mammoth))
print("Search second pattern is: ", pat2)
print(re.findall(pat2, mammoth))

# 11.
# Все слова, которые содержат три гласные подряд.
print("# 11")
print("Все слова, которые содержат три гласные подряд:")
pat = r'\w*[aeiou]{3}\w*'
print("Search pattern is: ", pat)
print(re.findall(pat, mammoth))
pat2 = r"\b\w*[aeiou]{3}[^aeiou\s]*\w*\b"
print("Search pattern is: ", pat2)
print(re.findall(pat2, mammoth))

# 12.
print("Исполюзуя unhexlify для преобразования шестнадцатеричной строки в переменную bytes с именем gif")
hex_str = '47494638396101000100800000000000ffffff21f9' + \
'0401000000002c000000000100010000020144003b'
print("hex_str is: ", hex_str)
gif = binascii.unhexlify(hex_str)
print("gif is: ", gif)
print("len of gif is: ", len(gif))

# 13.
# Байты в переменной gif определяют однопиксельный прозрачный GIF-файл.
# Корректный файл начинается со строки GIF89a.
correct_gif = b'GIF89a'
print("correct_gif head is: ", correct_gif)
print("correct_gif == gif[:6] is: ", correct_gif == gif[:6])

# 14.
print("Ширина файла - 16 битное число с прямым(в книге, возможно, ошибка) порядком со смещением 6 байт")
print("Высота - такое же число со смещением 8 байт")
width, height = struct.unpack('<HH', gif[6:10])
print("width and height is: ", width, height)
