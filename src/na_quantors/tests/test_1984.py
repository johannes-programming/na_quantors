import unittest
from typing import Self

from na_quantors.core import isna


class Test1984(unittest.TestCase):
    def test_1984(self: Self) -> None:
        self.assertTrue(isna(None, float("nan")))
        self.assertFalse(isna(4.2, 9000, "hello"))
        with self.assertRaises(Exception):
            isna(None, float("nan"), 4.2, 9000, "hello")


if __name__ == "__main__":
    unittest.main()
