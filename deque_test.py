import unittest
from deque import Deque, DequeException


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.my_deque = Deque(5)

    def test_add_first_full(self):
        for i in range(5):
            self.my_deque.add_first(1)
        with self.assertRaises(DequeException):
            self.my_deque.add_first(0)

    def test_add_first_1st(self):
        self.my_deque.add_first(1)
        self.assertEqual(len(self.my_deque), 1)

    def test_add_first_generic(self):
        self.my_deque.add_first(1)
        self.assertEqual(self.my_deque.first(), 1)

    def test_add_first_last(self):
        self.my_deque.add_first(1)
        self.my_deque.add_last(5)
        self.my_deque.add_last(6)
        self.assertEqual(self.my_deque.first(), 1)

    def test_add_last_full(self):
        for i in range(5):
            self.my_deque.add_last(1)
        with self.assertRaises(DequeException):
            self.my_deque.add_last(0)

    def test_add_last_1st(self):
        self.my_deque.add_last(1)
        self.assertEqual(len(self.my_deque), 1)

    def test_add_last_generic(self):
        self.my_deque.add_last(1)
        self.assertEqual(self.my_deque.last(), 1)

    def test_add_last_first(self):
        self.my_deque.add_last(2)
        self.my_deque.add_first(3)
        self.my_deque.add_first(7)
        self.assertEqual(self.my_deque.last(), 2)

    def test_delete_first_len(self):
        self.my_deque.add_first(1)
        self.my_deque.delete_first()
        self.assertEqual(len(self.my_deque), 0)

    def test_delete_first_first_1(self):
        self.my_deque.add_first(1)
        self.assertEqual(self.my_deque.delete_first(), 1)

    def test_delete_first_last_1(self):
        self.my_deque.add_last(1)
        self.assertEqual(self.my_deque.delete_first(), 1)

    def test_delete_first_1(self):
        self.my_deque.add_last(3)
        self.my_deque.add_first(2)
        self.my_deque.delete_first()
        self.assertEqual(self.my_deque.first(), 3)

    def test_delete_first_2(self):
        self.my_deque.add_first(2)
        self.my_deque.add_first(3)
        self.my_deque.add_first(4)
        self.assertEqual(self.my_deque.delete_first(), 4)

    def test_delete_last_len(self):
        self.my_deque.add_last(1)
        self.my_deque.delete_last()
        self.assertEqual(len(self.my_deque), 0)

    def test_delete_last_last_1(self):
        self.my_deque.add_last(1)
        self.assertEqual(self.my_deque.delete_last(), 1)

    def test_delete_last_first_1(self):
        self.my_deque.add_first(1)
        self.assertEqual(self.my_deque.delete_last(), 1)

    def test_delete_last_1(self):
        self.my_deque.add_last(4)
        self.my_deque.add_first(3)
        self.my_deque.delete_last()
        self.assertEqual(self.my_deque.last(), 3)

    def test_delete_last_2(self):
        self.my_deque.add_last(2)
        self.my_deque.add_last(56)
        self.my_deque.add_last(4)
        self.assertEqual(self.my_deque.delete_last(), 4)

    def test_add_and_delete(self):
        self.my_deque.add_first(1)
        self.my_deque.add_last(2)
        self.my_deque.add_first(0)
        self.my_deque.delete_first()
        self.my_deque.delete_last()
        self.assertEqual(len(self.my_deque), 1)
        self.assertEqual(self.my_deque.first(), 1)

    def test_empty_deque(self):
        self.assertEqual(len(self.my_deque), 0)
        with self.assertRaises(DequeException):
            self.my_deque.last()
        with self.assertRaises(DequeException):
            self.my_deque.first()
        with self.assertRaises(DequeException):
            self.my_deque.delete_first()
        with self.assertRaises(DequeException):
            self.my_deque.delete_last()

    def test_add_and_delete_many(self):
        for i in range(5):
            self.my_deque.add_first(i)
        self.assertEqual(len(self.my_deque), 5)
        for i in range(5):
            self.my_deque.delete_last()
        self.assertEqual(len(self.my_deque), 0)

    def test_is_empty_1(self):
        self.assertTrue(self.my_deque.is_empty())

    def test_is_empty_2(self):
        self.my_deque.add_first(1)
        self.my_deque.add_last(2)
        self.my_deque.delete_last()
        self.my_deque.delete_first()
        self.assertTrue(self.my_deque.is_empty(), 0)


if __name__ == '__main__':
    unittest.main()
