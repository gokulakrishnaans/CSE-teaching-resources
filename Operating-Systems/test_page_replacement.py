
import unittest

from page_replacement import fifo, lru, optimal


class TestPageReplacement(unittest.TestCase):
    def setUp(self):
        self.pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
        self.capacity = 3

    def test_fifo_page_faults(self):
        faults, history = fifo(self.pages, self.capacity)
        self.assertEqual(faults, 10)
        self.assertEqual(len(history), len(self.pages))

    def test_lru_page_faults(self):
        faults, history = lru(self.pages, self.capacity)
        self.assertEqual(faults, 9)
        self.assertEqual(len(history), len(self.pages))

    def test_optimal_page_faults(self):
        faults, history = optimal(self.pages, self.capacity)
        self.assertEqual(faults, 7)
        self.assertEqual(len(history), len(self.pages))

    def test_hits_and_faults_add_up(self):
        for algorithm in (fifo, lru, optimal):
            faults, history = algorithm(self.pages, self.capacity)
            hits = sum(result == "HIT" for _, _, result in history)
            self.assertEqual(faults + hits, len(self.pages))

    def test_empty_reference_string(self):
        for algorithm in (fifo, lru, optimal):
            faults, history = algorithm([], self.capacity)
            self.assertEqual(faults, 0)
            self.assertEqual(history, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
