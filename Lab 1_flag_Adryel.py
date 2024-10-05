def print_bandera_Suiza():
    #ANSI codes 
    white = '\033[47m'
    red = '\033[41m'
    reset = '\033[0m'
    
    flag = [
        f"{red}{5*' '}{reset}",
        f"{red}  {white} {red}  {reset}",
        f"{red} {white}   {red} {reset}",
        f"{red}  {white} {red}  {reset}",
        f"{red}{5*' '}{reset}",
        
    ]
    for row in flag:
        print(row)   
        
print_bandera_Suiza()
