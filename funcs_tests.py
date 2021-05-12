import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_f_1(self):
      self.assertEqual(funcs.f(3), 69)
   def test_f_2(self):
      self.assertEqual(funcs.f(10), 720)

   def test_g_1(self):
      self.assertAlmostEqual(funcs.g(3, 2), 1.444444444444)
   def test_g_2(self):
      self.assertRaises(ZeroDivisionError, funcs.g, 0, 3)
      
   def test_h_1(self):
      self.assertEqual(funcs.hypotenuse(3, 4), 5)
   def test_h_2(self):
      self.assertAlmostEqual(funcs.hypotenuse(6.0, 8.0), 10.0)

   def test_is_p1(self):
      self.assertTrue(funcs.is_positive(1), False)
   def test_is_p2(self):
      self.assertFalse(funcs.is_positive(-1), False)
   
   
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
