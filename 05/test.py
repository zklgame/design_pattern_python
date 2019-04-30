import unittest
from singleton import Singleton


class TestSingleton(unittest.TestCase):

    def test_Singleton(self):

        s = Singleton()
        self.assertEqual(s.cid, None)
        s.set_id(1)
        self.assertEqual(s.cid, 1)

        s2 = Singleton()
        self.assertEqual(s2.cid, 1)

        s2.set_id(2)
        self.assertEqual(s.cid, 2)


if __name__ == '__main__':
    unittest.main()
