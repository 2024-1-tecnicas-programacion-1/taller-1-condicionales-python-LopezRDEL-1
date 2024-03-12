def evaluar(caracter):
    if caracter.isalpha():
        return "El caracter ingresado es una letra."
    elif caracter.isdigit():
        return "El caracter ingresado es un número."
    else:
        return "El caracter ingresado no es ni una letra ni un número."

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
