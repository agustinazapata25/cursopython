nombre= input("-bienvenido, ingresá tu nombre") 
print("Hola", nombre, "elige una de las siguientes opciones")
print("1-Detectar mayor de 3 numeros\n 2-Identificar un horario \n 3-Decir si suma de cifras es par o impar \n 4-Descomponer un numero de 5 digitos y mostrarlas invertidas")
opc=int(input("ingrese tu selección.."))
if (opc==1):
    print("ingrese tres números enteros. Vamos a detectar cual es mayor")
    numA=int(input("ingrese primer numero"))
    numB=int(input("ingrese segundo numero"))
    numC=int(input("ingrese tercer numero"))
    if(numA>=numB and numA>=numC):
        print("El numero mayor es", numA)
    elif(numB>=numA and numB>=numC):
        print("El numero mayor es", numB)
    else:
        print("el numero mayor es",numC)
#elif(opc==2):
   # hora= str(input("ingrese un horario"))
  


elif(opc==3):
    print("opcion elegida es 3")

else:
    numero= int(input("ingrese un numero de 5 cifras"))
    numero= str(numero)
    numero= list(numero)
    numero[0]= int(numero[0])
    numero[1]= int(numero[1])
    numero[2]= int(numero[2])
    numero[3]= int(numero[3])
    numero[4]= int(numero[4])
    lNueva=[]
    if (numero[0]%2==0):
        lNueva.append(numero[0])
    if (numero[1]%2==0):
        lNueva.append(numero[1])
    if (numero[2]%2==0):
        lNueva.append(numero[2])
    if (numero[3]%2==0):
        lNueva.append(numero[3])
    if (numero[4]%2==0):
        lNueva.append(numero[4])
    print(lNueva[::-1])



