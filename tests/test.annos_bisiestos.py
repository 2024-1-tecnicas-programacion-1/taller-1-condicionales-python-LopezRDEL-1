import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.annos_bisiestos import evaluar

class TestAnnosBisiestos(unittest.TestCase):
    def test_1988(self):
        valor_esperado = "1988 es bisiesto"
        valor_actual = evaluar(1988)
        self.assertEqual(valor_esperado, valor_actual)
    
  def test_2000(self):
        valor_esperado = "2000 es bisiesto"
        valor_actual = evaluar(2000)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_1900(self):
        valor_esperado = "1900 no es bisiesto"
        valor_actual = evaluar(1900)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_2021(self):
        valor_esperado = "2021 no es bisiesto"
        valor_actual = evaluar(2021)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
