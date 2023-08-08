a = int(input('введите а'))
b = int(input('ведите б'))
c = int(input('введите с'))
if a > b > c or a < b < c:
    print('b среднее')
if c > a > b or c < a < b:
    print('a среднее')
if a > c > b or a < c < b:
    print('c средее')
if a > b > c or a > c > b:
    print('a максимальное')
if b > c > a or b > a > c:
    print('b максимальное')
if c > a > b or c > b > a:
    print('c максимальное')
if a < c < b or a < b < c:
    print('a минимальное')
if b < a < c or b < c < a:
    print('b минимальное')
if c < a < b or c < b < a:
    print('с минимальное')


