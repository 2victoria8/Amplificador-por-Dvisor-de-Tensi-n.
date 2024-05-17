import sys

def salir():
    print("¡Hasta luego!")
    sys.exit()
    


while True:
    print(".....Amplificador por Divisor de Tensión.....")
    print("¿Qué Desea Calcular?")
    print("1. Calcular Ib")
    print("2. Calcular Ic")
    print("3. Calcular Vb")
    print("4. Calcular Vc")
    print("5. Calcular Vce")
    print("6. Calcular Ve")
    print("7. Calcular Ie")
    print("8. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        import LogicaIb
    elif opcion == "2":
        import logicaIc
    elif opcion == "3":
        import LogicaVb
    elif opcion == "4":
        import LogicaVc
    elif opcion == "5":
        import LogicaVce
    elif opcion == "6":
        import LogicaVe 
    elif opcion == "7": 
        import LogicaIe      
    elif opcion == "8":
        salir()
        
    else:

        print("Opción inválida. Intente nuevamente.")
