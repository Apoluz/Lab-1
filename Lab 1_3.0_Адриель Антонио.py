def funcion(x):
    return x / 3 
def graficar():
   
    for y in range(4, -5, -1):
        linea = ""    
      
        for x in range(-10, 11):
           
            if round(funcion(x)) == y:
                linea += "#"  
            else:
                linea += " " 
        
        print(linea)  

graficar()
