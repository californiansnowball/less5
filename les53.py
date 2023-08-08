from random import randint
import time
life = 1
score = 0
while life == 1:
    Z = randint(1,5)
    print('перед вмаи 5 дверей ...')
    time.sleep(2)
    print('за одной из низ гость из местного военкомата')
    time.sleep(2)
    print('выбери дверь через которую ты сбежишь')


    door = int(input(''))
    if door == Z   :
        print('тебя Zабрали')
        life = 0
    else:
        print('а теперь снова развилка, выбирай куда побежишь')
        score = score+1
time.sleep(2)
print()
print('ваши очки:', score)