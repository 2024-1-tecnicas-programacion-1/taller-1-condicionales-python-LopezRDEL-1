def evaluar(anno):
    annobis = anno % 4
    
    if annobis == 0:
        res = str(anno) + " es bisiesto"
        return res
    else:
        res2 = str(anno) + " no es bisiesto"
        return res2

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)