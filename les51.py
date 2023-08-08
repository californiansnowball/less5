from random import randint
import time
life = 1
score = 0
while life == 1:
    ghost = randint(1,3)
    print('перед вмаи 3 двери ...')
    time.sleep(2)
    print('за одной из низ приведение....')
    time.sleep(2)
    print('тебе осталось угадать за какой нет...')


    door = int(input('1..2.. или 3...?'))
    if door == ghost   :
        print('оо неет, за дверью призрак')
        life = 0
    else:
        print('призрака нет, идем дальше')
        score = score+1
time.sleep(2)
print()
print('ваши очки:', score)