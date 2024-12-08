#записать и запомнить

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'a+', encoding='utf-8')
    file.seek(0)
    lines = len(file.readlines())
    start_line = lines + 1
    start_byte = file.tell()

    for i in strings:
        file.write(f'{i}\n')
        strings_positions[(start_line, start_byte)] = i
        start_line += 1
        start_byte = file.tell()

    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)


