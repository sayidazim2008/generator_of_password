import random
import string
import subprocess
import time

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
while True:
    while True:
        try:
            dlina=int(input('ведите длину пароля: '))
            i=''
            g=0
            p=0
            while dlina != g:
                if random.randint(0,1)==1:
                    p = str(p)
                    p=random.choice(string.ascii_letters)
                else:
                    p = random.randint(0, 9)
                p = str(p)
                i=str(i)+p
                dlina=dlina-1

            print(i)
            d=input('Копировать?(y-да,n-нет): ')
            try:
                if d=='y' or d=='н':
                    copy2clip(i)
                    print('скопировано!')
                else:
                    print('пошел нахуй')
                break
            except:
                print('пошел нахуй я заебался')
        except:
            try:
                print('пиши цыфру')
            except:
                print('пошел нахуй я заебался')
    print('продолжить?')
    ha=input()
    if ha == 'y' or d == 'н' or d == 'yes' or d == 'да'or d == 'Да':
        continue
    else:
        print('пошел нахуй')
        time.sleep(2)
    break