def evaluar(numero1, numero2, numero3, numero4):
    numeros = [numero1, numero2, numero3, numero4]
    
    numeros_ordenados = sorted(numeros)

    numeros_str = ", ".join(str(num) for num in numeros_ordenados)
    
    return "Los números ordenados de forma ascendente son: " + numeros_str

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
