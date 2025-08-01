def evaluar_num(numero):
    if numero == 10:
        return "es 10 NUMERO PAR"
    elif numero == 7:
        return "es 7 un COMODIN"
    if numero % 2 == 0:
            return "NUMERO PAR"
    else:
            return "NUMERO IMPAR"
def main():
    num = int(input("Ingrese un numero: "))
    resultado = evaluar_num(num)
    print(resultado)
if __name__ == "__main__":
    main()
