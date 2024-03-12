import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.imc import evaluar

class TestIMC(unittest.TestCase):
    def testBajo(self):
        valor_esperado = "bajo"
        valor_actual = evaluar(50, 1.8,   20)
        self.assertEqual(valor_esperado, valor_actual)
    
   
    def testNormal(self):
        valor_esperado = "normal"
        valor_actual = evaluar(70, 1.8, 30)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testSobrepeso(self):
        valor_esperado = "sobrepeso"
        valor_actual = evaluar(85, 1.8, 45)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testObesidad(self):
        valor_esperado = "obesidad"
        valor_actual = evaluar(100, 1.8, 60)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
