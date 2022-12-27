import logging
import time
import urllib.request
import urllib.error
from student import Student


logging.basicConfig(level=logging.INFO, filename="my_log.log", filemode="w")

def decor_log(arg):
    def wrapper():
        arg()
        logging.info("not type")
    return wrapper
    
def decor_time(arg):
    def wrapper():
        tic = time.perf_counter()
        arg()
        toc = time.perf_counter()
        print(f'время выполнение функции {toc - tic:0.4f} секунд')
    return wrapper



def sleep(arg):
    def wrapper():
        arg()
        time.sleep(10)
        print(f'Сон на 10 секунд')
        
    return wrapper


@decor_log
@sleep
@decor_time
def sravnenie():
    dz_Sem = 0
    dz_Bob = 0

   

    Sem = Student('type1', 'subtype', 'clacc', 'всеяден', 23, 65, 2, 2, 'male', 'Sem', 110, 'русский', 'учусь', dz_Sem)
    Bob = Student('type1', 'subtype', 'clacc', 'всеяден', 23, 65, 2, 2, 'male', 'Bob', 110, 'русский', 'учусь', dz_Bob)

    check = False
    while not check:
        try:
            Sem.say()
            dz_Sem = int(input('Ведите количество сданных ДЗ у Sem: '))
            Bob.say()
            dz_Bob = int(input('Ведите количество сданных ДЗ у Bob: '))
            check = True
        except ValueError:
            print('неверное значение')
            # logging.info("not type")
            check = False

    if Sem == Bob:
        print('количество сданных ДЗ у студентов равное')
    else:
        print('количество сданных ДЗ у студентов разное')

sravnenie()