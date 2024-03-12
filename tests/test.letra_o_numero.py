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

class TestLetraONumero(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es número"
        valor_actual = evaluar('c')
        self.assertEqual(valor_esperado, valor_actual)
    
   def test_es_numero(self):
        valor_esperado = "Es número"
        valor_actual = evaluar('5')
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_caracter_especial(self):
        valor_esperado = "Es caracter especial"
        valor_actual = evaluar('*')
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_espacio(self):
        valor_esperado = "Es espacio en blanco"
        valor_actual = evaluar(' ')
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
