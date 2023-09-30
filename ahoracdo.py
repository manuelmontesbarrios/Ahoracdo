from os import system
system ("cls")
import random
ahorcado=[]
c=0
while True:
    print("MENU")
    print("1. AHORCADO")
    print("2. ADIVINAR")
    print("3. AHORCADO")
    print("4. SALIR")
    opcion=int(input("Ingrese la opcion: "))
    if opcion == 4:
        exit()
    match opcion:
        case 1:
            while True:
                print("MENU AHORCADO")
                print("1. Ahorcado")
                print("2. Insertar")
                print("3. Modificar")
                print("4. Salir")
                opcion=int(input("Ingrese la opcion: "))
                match opcion:
                    case 1:
                        x=len(ahorcado)
                        if x ==0:
                            print("No hay palabras para adivinar")
                        else:
                            a=random.choice(ahorcado)
                            print(a)
                            for i in a:
                                c+=1
                            print(c)
                    case 2:
                        c_palabras=int(input("Ingrese la cantidad de palabras: "))
                        for i in range(c_palabras):
                            palabra=str(input(f"Ingrese la palabra {i+1}: "))
                            ahorcado.append(palabra)
                        print(ahorcado)
                    case 3:
                        print(ahorcado)
                    case 4:
                        break
        case 2:
            pass
        case 3:
            pass
        case 4:
            exit()