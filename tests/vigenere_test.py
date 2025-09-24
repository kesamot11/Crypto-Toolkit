import unittest
from cryptokit import vigenere


class TestSum(unittest.TestCase):

    def test_convert_key_to_array_shorter_key(self):
        self.assertEqual(vigenere.convert_to_numbers("AZBzzAe", "Test text"),
                         [0, 25, 1, 25, 25, 0, 4, 0 ,25],
                         "Should be [0, 25, 1, 25, 25, 0, 4, 0 ,25]")

    def test_convert_key_to_array_longer_key(self):
        self.assertEqual(vigenere.convert_to_numbers("AZBzzAe", "Te"),
                         [0, 25],
                         "Should be [0, 25]")

    def test_encrypt_normal_example_abcd(self):
        self.assertEqual(vigenere.encrypt("abcdZ", [0,1,2,25,3]),
                         "ace}]",
                         "Should be ace}")

    def test_decrypt_normal_example_abcd(self):
        self.assertEqual(vigenere.decrypt("ace}]", [0,1,2,25,3]),
                         "abcdZ",
                         "Should be abcd")


if __name__ == "__main_":
    unittest.main()