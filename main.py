from avanzadas import OperacionesAvanzadas

if __name__ == "__main__":
    op = OperacionesAvanzadas()
    op.leerNumeros()
    raiz= op.raizCuadrada()
    resultado = op.elevarPotencia()
    print(f"El resultado de {op.num1} elevado a {op.num2} es: {resultado}")
    print("La raiz cuadrada del primer numero es: ", raiz)