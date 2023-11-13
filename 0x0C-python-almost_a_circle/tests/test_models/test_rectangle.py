#!/usr/bin/python3
"""define unittest for rectangle"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """test instances"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangle_width(unittest.TestCase):
    """test widht init"""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """test init"""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")


class TestRectangle_area(unittest.TestCase):
    """test area method"""

    def test_area_small(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """test the display methods"""

    @staticmethod
    def capture_stdout(rect, method):
        """return text printed to stdout

        Args:
            rect (Rectangle): rectangle to print
            method (str): method to run on rectangle
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """update_args method test"""

    # Test args
    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """test update_kwargs method"""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")


class TestRectangle_to_dictionary(unittest.TestCase):
    """test to_dictionary method."""

    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
