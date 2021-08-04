from unittest import TestCase
from testcalc import Calc


class TestSum(TestCase):

    def test_001(self):
        self.assertEqual(Calc.sum(1, 2), 3)
        self.assertEqual(Calc.sum(-2, 2), 0)

    def test_002(self):
        self.assertIsInstance(Calc.sum(1, 2), int)
        self.assertIsInstance(Calc.sum(1, 2.0), float)
        self.assertIsInstance(Calc.sum(1.0, 2.0), float)
        self.assertIsInstance(Calc.sum(1.0, 2), float)

    def test_003(self):
        with self.assertRaises(TypeError):
            Calc.sum("1", 2)


class TestMinus(TestCase):

    def test_101(self):
        with self.assertRaises(TypeError):
            Calc.minus("1", 2)

    def test_102(self):
        self.assertIsInstance(Calc.minus(4, 2), int)
        self.assertIsInstance(Calc.minus(1, 2.0), float)

    def test_103(self):
        self.assertEqual(Calc.minus(1, 2), -1)
        self.assertEqual(Calc.minus(-2, 2), -4)


class TestMul(TestCase):

    def test_201(self):
        with self.assertRaises(TypeError):
            Calc.mul("1", 2)

    def test_202(self):
        self.assertIsInstance(Calc.mul(4, 2), int)
        self.assertIsInstance(Calc.mul(1, 2.0), float)

    def test_203(self):
        self.assertEqual(Calc.mul(1, 2), 2)
        self.assertEqual(Calc.mul(-2, 2), -4)


class TestDiv(TestCase):
    def test_301(self):
        with self.assertRaises(ZeroDivisionError):
            Calc.div(1, 0)

    def test_302(self):
        with self.assertRaises(TypeError):
            Calc.div("1", 2)

    def test_303(self):
        self.assertIsInstance(Calc.div(4, 2), float)
        self.assertIsInstance(Calc.div(1, 2.0), float)

    def test_304(self):
        self.assertEqual(Calc.div(1, 2), 0.5)
        self.assertEqual(Calc.div(-2, 2), -1)

class TestPercent(TestCase):

    def test_401(self):
        with self.assertRaises(TypeError):
            Calc.minus("1", 2)

    def test_402(self):
        self.assertIsInstance(Calc.percent(10, 100), float)
        self.assertIsInstance(Calc.percent(1, 2), float)

    def test_403(self):
        self.assertEqual(Calc.percent(10, 100), 10)
        self.assertEqual(Calc.percent(5, 200), 10)


class TestPow(TestCase):

    def test_501(self):
        with self.assertRaises(TypeError):
            Calc.pow("1", 2)

    def test_502(self):
        self.assertIsInstance(Calc.pow(10, 10), int)
        self.assertIsInstance(Calc.pow(1.0, 2), float)

    def test_503(self):
        self.assertEqual(Calc.pow(10, 2), 100)
        self.assertEqual(Calc.pow(5, 2), 25)


class TestSqrt(TestCase):

    def test_601(self):
        with self.assertRaises(TypeError):
            Calc.sqrt("1")

    def test_602(self):
        self.assertIsInstance(Calc.sqrt(10), float)
        self.assertIsInstance(Calc.sqrt(1.0), float)

    def test_603(self):
        self.assertEqual(Calc.sqrt(25), 5)

    def test_601(self):
        with self.assertRaises(ValueError):
            Calc.sqrt(-25)


