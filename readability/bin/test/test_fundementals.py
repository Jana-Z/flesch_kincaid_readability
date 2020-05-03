import unittest

from bin.fundementals import split_words, \
    split_sentences, count_words, count_sentences, \
    count_syllables

class TestFundementals(unittest.TestCase):

    def test_split_words(self):
        expressions = [
            'Hallo, ich bin Jana.',
            'Wie geht es dir? Gut!',
            "Wie geht's?",
            "Alle meine Entchen schwimmen auf dem See, Köpfchen unter's Wasser, Schwänzchen in die Höh."
        ]
        words = [
            ['Hallo', 'ich', 'bin', 'Jana'],
            ['Wie', 'geht', 'es', 'dir', 'Gut'],
            ['Wie', 'geht', 's'],
            ['Alle', 'meine', 'Entchen', 'schwimmen', 'auf', 'dem', 'See', 'Köpfchen', 'unter', 's', 'Wasser', 'Schwänzchen', 'in', 'die', 'Höh']
        ]
        results = [split_words(exp) for exp in expressions]
        self.assertEqual(results, words)

    def test_split_sentences(self):
        expressions = [
            'Hallo, ich bin Jana.',
            'Wie geht es dir? Gut!',
            "Wie geht's?",
            "Alle meine Entchen schwimmen auf dem See, Köpfchen unter's Wasser, Schwänzchen in die Höh."
        ]
        sentences = [
            ['Hallo, ich bin Jana'],
            ['Wie geht es dir', 'Gut'],
            ["Wie geht's"],
            ["Alle meine Entchen schwimmen auf dem See, Köpfchen unter's Wasser, Schwänzchen in die Höh"]
        ]
        results = [split_sentences(exp) for exp in expressions]
        self.assertEqual(results, sentences)

    def test_count_words(self):
        expressions = [
            'Hallo, ich bin Jana.',
            'Wie geht es dir? Gut!',
            "Wie geht's?",
            "Alle meine Entchen schwimmen auf dem See, Köpfchen unter's Wasser, Schwänzchen in die Höh."
        ]
        word_counts = [
            4,
            5,
            3,
            15
        ]
        results = [count_words(exp) for exp in expressions]
        self.assertEqual(results, word_counts)
    
    def test_count_sentences(self):
        expressions = [
            'Hallo, ich bin Jana.',
            'Wie geht es dir? Gut!',
            "Wie geht's?",
            "Alle meine Entchen schwimmen auf dem See, Köpfchen unter's Wasser, Schwänzchen in die Höh",
            "Alle meine Entchen schwimmen auf dem See, Köpfchen unter's Wasser, Schwänzchen in die Höh."
        ]
        sentence_count = [
            1,
            2,
            1,
            1,
            1
        ]
        results = [count_sentences(exp) for exp in expressions]
        self.assertEqual(results, sentence_count)
    
    def test_count_syllables(self):
        expressions = [
            'Hallo, ich bin Jana.',
            'Wie geht es dir? Gut!',
            "Wie geht's?",
            "Alle meine Entchen schwimmen auf dem See, Köpfchen unter's Wasser, Schwänzchen in die Höh."
        ]
        syllable_count = [
            6,
            5,
            2,
            22
        ]
        results = [count_syllables(exp, lang='de') for exp in expressions]
        self.assertEqual(results, syllable_count)

if __name__ == '__main__':
    unittest.main()