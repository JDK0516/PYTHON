#3El Centro de Industria y Construcción del Sena regional Tolima, 
#quiere implementar un sistema de control de ingreso que permita contar los estudiantes que ingresan 
#durante los  seis días a la semana como también el número de estudiantes por formación. 
#Para el ejemplo vamos a tener en cuenta las siguientes formaciones: ADSO, producción multimedia, 
#Desarrollo de videojuegos, Sistemas El algoritmo debe indicar el total de estudiantes clasificados 
#por cada programa, por día.
#Y al finalizar la semana debe generar un reporte con la cantidad de estudiantes que ingresaron al 
#centro de formación.

#variables
ingreso=0
dia=0
adso=0
produccion_multimedia=0
desarrollo_videojuegos=0
estudiantes=1

while estudiantes==1:
    ingreso=int(input("¿De que formacion es el estudiante?/n1.ADSO/n2.PRODUCCION MULTIMEDIA/n3.DESARROLLO DE VIDEOJUEGOS"))
    if ingreso==1:
        adso +=1
    elif ingreso==2:
        produccion_multimedia +=1
    elif ingreso==3:
        desarrollo_videojuegos +=1
    estudiantes=int(input("Ingreso otro estudiantes:1.'si'/2.'no' "))
    
print("Los ingresads de Adso son ", adso," los ingresados de produccion multimedia son ",produccion_multimedia," y los ingresados de desarrollo de videojuegos son ",desarrollo_videojuegos)



      


