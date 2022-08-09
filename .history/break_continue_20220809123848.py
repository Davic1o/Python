#este es el codigo que debe funcionar desntro del main 
def run():
    
    
    # for i in range(10000):
    #     print(i)
    # #condicionamos hasta que numero va a recorrer el lazo 
    #     if i == 5678:
    #         break
#buena practica antes de iniciar el codigo definir es como el main en potros lenguajes


    for contador in range(10):
        if contador % 2 != 0:
            continue
    # el continue permite que el codigo se ejecute siempre, si hay una condicion ejecuta solo lo que muestra la condicion    
        print(contador)
if __name__ == '__main__':
    run()