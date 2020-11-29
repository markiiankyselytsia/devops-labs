from math import pi


consts = [True, False, pi]

for i, const in enumerate(consts):
    print(f'Константа {i} = {const}')


if 2 <= len(consts) <= 3:
    print('Констант достатньо')
else:
    print('Констант замало або забагато')


invalid_fp = 'file.txt'

try:
    with open(invalid_fp) as fid:
        for line in fid:
            print(line)

except FileNotFoundError:
    print(f'Файлу {invalid_fp} не існує')

else:
    print('Файл прочитано')


arr = [{'a': 3}, {'a': 2}, {'a': 1}]

getter = lambda dict: dict.get('a')

arr.sort(key=getter)    

print('Посортовані словники по ключу а', arr)

