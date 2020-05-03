import unittest

from bin.calculator import get_reading_ease, \
    get_reading_level

class TestRedability(unittest.TestCase):

    def test_get_reading_level(self):
        test_cases = [
            "Alle meine Entchen schwimmen auf dem See, Köpfchen unter's Wasser, Schwänzchen in die Höh."
        ]
        scores = [
            7.57
        ]
        results = [round(get_reading_level(case, lang='de'), 2) for case in test_cases]
        self.assertEqual(results, scores)

    def test_get_reading_ease(self):
        test_cases = [
            "Alle meine Entchen schwimmen auf dem See, Köpfchen unter's Wasser, Schwänzchen in die Höh."
        ]
        scores = [
            67.53
        ]
        results = [round(get_reading_ease(case, lang='de'), 2) for case in test_cases]
        self.assertEqual(results, scores)


if __name__ == '__main__':
    unittest.main()