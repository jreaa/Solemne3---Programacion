#Programacion Basica
#Solenme 3
#Jose Era, Seccion 1

CONSTANTE ="="*70
#lista =[]

def addCredit(sueldoEmpleado):
    lista =[]
    tecla = "s"
    while tecla == "s":
        total = {}
        print(CONSTANTE)
        print("NOTA: EL credito a ingresar no debe superar tres veces su sueldo base")
        credito = int(input("Por favor ingrese el credito que desea: "))
        print(CONSTANTE)

        while(credito > (sueldoEmpleado ** 3) ):
            print(CONSTANTE)
            print("EL credito ingresado supera tres veces su sueldo")
            credito = int(input("Por favor ingrese un credito que no supere el maximo: "))
            print(CONSTANTE)

        total['Monto Solicitado'] = credito
        #lista.append(credito)
        opciones = 4
        if(opciones == 4):
            print("Cuantas cuotas desea agregar")
            print("2 - 12 cuotas = 5% interes")
            print("13 - 24 cuotas = 7% interes")
            print("25 - 36 cuotas = 9% interes")
            print("37 - 48 cuotas = 10% interes")
            cuotas = int(input("Cuotas: "))
            total["Cantidad de cuotas: "] = cuotas
            #lista.append(cuotas)
            if(cuotas >= 2 and cuotas <= 12):
                i=credito*0.5/100
                valorCuota = (credito+i)/cuotas
                print(valorCuota)
            if(cuotas >= 13 and cuotas <=24):
                i=credito*0.7/100
                valorCuota = (credito+i)/cuotas
                print(valorCuota)
            if(cuotas >=25 and cuotas <=36):
                i=credito*0.9/100
                valorCuota = (credito+i)/cuotas
                print(valorCuota)
            if(cuotas >= 37 and cuotas<=48):
                i=credito*0.10/100
                valorCuota = (credito+i)/cuotas
                print(valorCuota)
            print(CONSTANTE)
            #lista.append(valorCuota)
            total["Valor Cuotas"] = valorCuota

            lista.append(total)
            tecla = input("Desea agregar otro credito: Pulse 's' si desea continuar de lo contrario pulse cualquier otra tecla ")

    print(CONSTANTE)
    print(lista)
    


SUELDO_MIN = 300000
#El sueldo minimo de la perspona tiene que ser de $ 300.000
print(CONSTANTE)
sueldoEmpleado = input("Por favor ingrese su sueldo: ")
sueldoEmpleado = int(sueldoEmpleado)

while(sueldoEmpleado <= SUELDO_MIN):
    sueldoEmpleado = input("Por favor ingrese un sueldo mayor a 300.000: ")
    sueldoEmpleado = int(sueldoEmpleado)

addCredit(sueldoEmpleado)

