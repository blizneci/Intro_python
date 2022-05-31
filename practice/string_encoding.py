'''
Encode "aabbbccd" to "a2b3c2d1"
'''
strings = ('aabbbccd', '', ' ', '123', 123, ['aabb', 'aa'], 1.2)

def encode_string(a_string: str) -> str:
    if not isinstance(a_string, str):
        print('This is not a string: ', a_string)
        return
    elif not a_string.isalpha():
        print('This is not a valid string: ', a_string)
        return

    result_string = ''

    while a_string:
        len_a_string = len(a_string)
        first_letter = a_string[0]
        a_string = a_string.lstrip(first_letter)
        result_string = ''.join((result_string, first_letter, str(len_a_string - len(a_string))))
        #result_string += first_letter + str(len_a_string - len(a_string))
    return result_string

def encode_string_2(a_string: str) -> str:
    if a_string == '':
        print('string is empty')
        return a_string
    result_string = ''
    count = 1
    for i in range(len(a_string) - 1):
        if a_string[i] == a_string[i + 1]:
            count += 1
            continue
        else:
            result_string += a_string[i] + str(count)
            count = 1
    result_string += a_string[-1] + str(count)
    return result_string

def encode_string_3(a_string: str) -> str:
    if a_string == '':
        print('string is empty')
        return a_string
    result_string = ''
    while a_string:
       result_string += a_string[0] + str(len(a_string) - len(a_string.lstrip(a_string[0]))) 
       a_string = a_string.lstrip(a_string[0])
    return result_string

if __name__ == '__main__':
    for string in strings:
        print(encode_string(string))

