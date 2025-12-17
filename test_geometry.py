import unittest
import math
import square
import rectangle
import circle
import triangle


class GeometryTestCase(unittest.TestCase):

    def test_square_area_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_square_area_positive(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_square_area_decimal(self):
        res = square.area(2.5)
        self.assertEqual(res, 6.25)

    def test_square_perimeter_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_positive(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_square_perimeter_decimal(self):
        res = square.perimeter(2.5)
        self.assertEqual(res, 10)

    def test_square_area_negative(self):
        res = square.area(-5)
        self.assertEqual(res, 25)

    def test_square_perimeter_negative(self):
        res = square.perimeter(-5)
        self.assertEqual(res, -20)

    def test_rectangle_area_zero(self):
        res = rectangle.area(0, 5)
        self.assertEqual(res, 0)
        res = rectangle.area(5, 0)
        self.assertEqual(res, 0)
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_rectangle_area_positive(self):
        res = rectangle.area(10, 5)
        self.assertEqual(res, 50)

    def test_rectangle_area_decimal(self):
        res = rectangle.area(2.5, 4.0)
        self.assertEqual(res, 10.0)


    def test_rectangle_perimeter_zero(self):
        res = rectangle.perimeter(0, 5)
        self.assertEqual(res, 10)
        res = rectangle.perimeter(5, 0)
        self.assertEqual(res, 10)
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_rectangle_perimeter_positive(self):
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_rectangle_perimeter_decimal(self):
        res = rectangle.perimeter(2.5, 4.0)
        self.assertEqual(res, 13.0)

    def test_rectangle_area_negative(self):
        res = rectangle.area(-10, 5)
        self.assertEqual(res, -50)
        res = rectangle.area(10, -5)
        self.assertEqual(res, -50)

    def test_rectangle_perimeter_negative(self):
        res = rectangle.perimeter(-10, 5)
        self.assertEqual(res, -10)

    def test_circle_area_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_circle_area_positive(self):
        res = circle.area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(res, expected, places=7)

    def test_circle_area_decimal(self):
        res = circle.area(2.5)
        expected = math.pi * 6.25
        self.assertAlmostEqual(res, expected, places=7)

    def test_circle_perimeter_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_positive(self):
        res = circle.perimeter(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(res, expected, places=7)

    def test_circle_perimeter_decimal(self):
        res = circle.perimeter(2.5)
        expected = 2 * math.pi * 2.5
        self.assertAlmostEqual(res, expected, places=7)

    def test_circle_area_negative(self):
        res = circle.area(-5)
        expected = math.pi * 25
        self.assertAlmostEqual(res, expected, places=7)

    def test_circle_perimeter_negative(self):
        res = circle.perimeter(-5)
        expected = 2 * math.pi * -5
        self.assertAlmostEqual(res, expected, places=7)

    def test_triangle_area_zero(self):
        res = triangle.area(0, 10)
        self.assertEqual(res, 0)
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_triangle_area_positive(self):
        res = triangle.area(10, 5)
        self.assertEqual(res, 25)

    def test_triangle_area_decimal(self):
        res = triangle.area(2.5, 4.0)
        self.assertEqual(res, 5.0)

    def test_triangle_perimeter_zero(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
        res = triangle.perimeter(0, 5, 7)
        self.assertEqual(res, 12)

    def test_triangle_perimeter_positive(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_triangle_perimeter_decimal(self):
        res = triangle.perimeter(2.5, 3.5, 4.0)
        self.assertEqual(res, 10.0)

    def test_triangle_area_negative(self):
        res = triangle.area(-10, 5)
        self.assertEqual(res, -25)
        res = triangle.area(10, -5)
        self.assertEqual(res, -25)

    def test_triangle_perimeter_negative(self):
        res = triangle.perimeter(-3, 4, 5)
        self.assertEqual(res, 6)
        res = triangle.perimeter(-3, -4, -5)
        self.assertEqual(res, -12)

    def test_square_large_numbers(self):
        res = square.area(1000)
        self.assertEqual(res, 1000000)

    def test_rectangle_square_case(self):
        res = rectangle.area(5, 5)
        self.assertEqual(res, 25)
        res = rectangle.perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_circle_unit_radius(self):
        res = circle.area(1)
        self.assertAlmostEqual(res, math.pi, places=7)
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi, places=7)

    def test_triangle_equilateral(self):
        res = triangle.perimeter(5, 5, 5)
        self.assertEqual(res, 15)


if __name__ == '__main__':
    unittest.main(verbosity=2)