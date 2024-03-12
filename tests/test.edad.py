import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.edad import evaluar

class TestEdad(unittest.TestCase):
    def test2000Enero1(self):
        valor_esperado = "Usted tiene 24 años"
        valor_actual = evaluar(1, 1, 2024)
        self.assertEqual(valor_esperado, valor_actual)
    
 
    def test1990Julio15(self):
        valor_esperado = "Usted tiene 33 años"
        valor_actual = evaluar(15, 7, 1990)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test2005Diciembre31(self):
        valor_esperado = "Usted tiene 18 años"
        valor_actual = evaluar(31, 12, 2005)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test1999Febrero29(self):
        valor_esperado = "Usted tiene 25 años"
        valor_actual = evaluar(29, 2, 1999)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
