def evaluar(peso, estatura, edad):
  
    imc = peso / (estatura ** 2)
    
    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc < 25:
        categoria = "Peso normal"
    elif 25 <= imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
    
    return "Tu Índice de Masa Corporal es {:.2f}, lo que indica: {}".format(imc, categoria)

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
