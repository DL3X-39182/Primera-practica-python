#Se declara una variable
calificación = input("Introduce la calificaión de la certificación AZ-900: ")
#Se le da valor entero a la variable y se recalca a la variable
calificación = int(calificación)
#Se hace un if else
#Si la califiacion es reprobatoria se da este mensaje
if calificación < 700 :
    print("Lero lero, por no estudiar")
else :#Si no se cumple con el if anterior pasa a esta condición
    print("Felicidades perrillo, ahora a conseguir jale")
if calificación >= 1000 :
    print("No sea mentiroso viejo teibolero")

#Verificador de mayoria de edad
edad=input("Porfavor introduce tu edad: ")
edad=int(edad)

if edad >= 18 and edad <=100:
    print("Bienvenido a la vida adulta, pagale al SAT")
elif edad > 100 :
    print("Nomanche carnal, ya jubilise, huele a dinosaurio")
elif edad < 0 :
    print("Que pedo, tu ni has nacido")
else :
    print("Tas chiquito, vete a dormir, es tarde")