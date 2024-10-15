from colorama import Back, init

def task4(): 
    init(autoreset=True)  
    p = 0
    file_path = 'sequence.txt'

    with open(file_path, 'r') as g:
        file = g.readlines()
        
    for number in file:
        if (float(number.strip()) >= -3) and (float(number.strip()) <= 3):
            p += 1
    
    percent = int(p / len(file) * 100)
    
   
    for i in range(percent):
        print(Back.RED + ' ', end="")
    print(Back.BLACK + ' Числа от -3 до 3 занимают ', percent, "%")
    
    
    for i in range(100 - percent):
        print(Back.GREEN + ' ', end="")
    print(Back.BLACK + ' Остальные числа занимают ', 100 - percent, "%")
    
    print()

task4()
