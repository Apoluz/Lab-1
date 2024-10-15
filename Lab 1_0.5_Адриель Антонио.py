import os
import time

def clear():
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def task5():
    print("Для запуска анимации введите любой символ в консоли/To start the animation, enter any symbol in the console")
    f = input()
    
    while True:
        print("This") 
        time.sleep(1)
        clear()
        
        print("is a ")  
        time.sleep(1)
        clear()
        
        print("test ") 
        time.sleep(1)
        clear()

        print("animation ") 
        time.sleep(1)
        clear()

task5()
