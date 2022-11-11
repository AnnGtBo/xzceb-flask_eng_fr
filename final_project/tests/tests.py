import unittest

from machinetranslation.translator import englishToFrench, frenchToEnglish

class Test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench(5), "")
        self.assertEqual(englishToFrench(""), "")


class Test_fr_To_en(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(frenchToEnglish(5), "")
        self.assertEqual(frenchToEnglish(""), "")
