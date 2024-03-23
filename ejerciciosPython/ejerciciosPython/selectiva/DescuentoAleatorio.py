#Ejercicio descuento según el color de la balota.

valorBase=50000
valorCompra =int(input("Por favor inserte el valor de la compra: "))
roja =valorCompra*0.1
verde=valorCompra*0.15
azul=valorCompra*0.2
amarilla=valorCompra*0.5
negra=valorCompra*1

if valorCompra>=valorBase:
    print("El valor de la compra es: ", valorCompra)
    colorBalota=input("Ingrese el color de la balota: ")
if colorBalota == "roja":
    print(f"Su descuento es: {roja}")
    print(f"El valor final es: ", valorCompra-roja)
elif colorBalota == "verde":
    print(f"Su descuento es {verde}")
    print(f"El valor final es: ", valorCompra-verde)
elif colorBalota == "azul":
    print(f"Su descuento es {azul}")
    print(f"El valor final es: ", valorCompra-azul)
elif colorBalota == "amarilla":
    print(f"Su descuento es {amarilla}")
    print(f"El valor final es: ", valorCompra-amarilla)
elif colorBalota == "negra":
    print(f"Su descuento es {negra}")
    print(f"El valor final es: ", valorCompra-negra)