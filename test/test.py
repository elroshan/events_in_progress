import unittest
from src.overlap_determiner import max_overlap


class Test(unittest.TestCase):

    def test_max_overlap_when_empty_list(self):
        self.assertEqual(max_overlap([]), 0)

    def test_max_overlap_when_one_pair(self):
        m = max_overlap([{"startTime": "2022‑09‑01 17:45:30.005", "endTime": "2022‑09‑01 18:15:30.005"}])
        self.assertEqual(m, 1)

    def test_max_overlap_when_neighbours(self):
        m = max_overlap([{"startTime": "2022‑09‑01 17:45:30.005", "endTime": "2022‑09‑01 18:15:30.005"},
                        {"startTime": "2022‑09‑01 18:15:30.005", "endTime": "2022‑09‑01 18:45:30.005"}])
        self.assertEqual(m, 1)


if __name__ == '__main__':
    unittest.main()
