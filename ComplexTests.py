import unittest
import ComplexNumbers

class TestComplex(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(ComplexNumbers.suma((1,1), (1,1)), "2 + 2i")
        self.assertEqual(ComplexNumbers.suma((7, 1), (2, 2)), "9 + 3i")

    def test_producto(self):
        self.assertEqual(ComplexNumbers.producto((3, -2), (1, 2)), "7 + 4i")
        self.assertEqual(ComplexNumbers.producto((-3, -1), (1, -2)), "-5 + 5i")

    def test_resta(self):
        self.assertEqual(ComplexNumbers.resta((1, 1), (1, 1)), "0 + 0i")
        self.assertEqual(ComplexNumbers.resta((5, 5), (3, 2)), "2 + 3i")

    def test_division(self):
         self.assertEqual(ComplexNumbers.division((-2, 1), (1, 2)), "0.0 + 1.0i")

    def test_modulo(self):
         self.assertEqual(ComplexNumbers.modulo((3, 4)), 5)

    def test_conjugado(self):
         self.assertEqual(ComplexNumbers.conjugado((1,2)), "1 - 2i")
         self.assertEqual(ComplexNumbers.conjugado((2, -2)), "2 + 2i")

    def test_cAP(self):
         self.assertEqual(ComplexNumbers.cartesianoAPolares((1, 1)), (1.4142135623730951, 0.7853981633974483))

    def test_PAC(self):
         self.assertEqual(ComplexNumbers.polarACartesiano((1.4142135623730951, 0.7853981633974483)), "1.0000000000000002 + 1.0000000000000002i")
    #
    def test_fase(self):
         self.assertEqual(ComplexNumbers.fase((1, 1)), 0.7853981633974483)



if __name__ == '__main__':
    unittest.main()