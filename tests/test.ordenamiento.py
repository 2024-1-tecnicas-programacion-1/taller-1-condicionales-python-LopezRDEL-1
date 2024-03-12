import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.ordenamiento import evaluar

class TestOrdenamiento(unittest.TestCase):
     def testNo(self):
        valor_esperado = "0 1 6 7"
        valor_actual = evaluar(7, 0, 6, 1)
        self.assertEqual(valor_esperado, valor_actual)
    
       def testAscendente(self):
        valor_esperado = "1 2 3 4"
        valor_actual = evaluar(1, 2, 3, 4)
        self.assertEqual(valor_esperado, valor_actual)
    
        def testDescendente(self):
        valor_esperado = "4 3 2 1"
        valor_actual = evaluar(4, 3, 2, 1)
        self.assertEqual(valor_esperado, valor_actual)
    
         def testIguales(self):
        valor_esperado = "3 3 3 3"
        valor_actual = evaluar(3, 3, 3, 3)
        self.assertEqual(valor_esperado, valor_actual)


    

if __name__ == '__main__':
    unittest.main()
