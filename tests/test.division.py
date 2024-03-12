import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.division import evaluar

class TestDivision(unittest.TestCase):
    def testDivisionExacta(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 2\n" \
                         "Residuo: 4"
        valor_actual = evaluar(14, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
     def testDivisionInexacta(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: 2\n" \
                         "Residuo: 1"
        valor_actual = evaluar(5, 2)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDivisionPorCero(self):
        valor_esperado = "No se puede dividir por cero."
        valor_actual = evaluar(10, 0)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testNumerosNegativos(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: -3\n" \
                         "Residuo: 0"
        valor_actual = evaluar(-15, -5)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testDividendoNegativo(self):
        valor_esperado = "La división no es exacta. \n" \
                         "Cociente: -2\n" \
                         "Residuo: 1"
        valor_actual = evaluar(-5, 2)
        self.assertEqual(valor_esperado, valor_actual)

    

if __name__ == '__main__':
    unittest.main()
