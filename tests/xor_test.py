import unittest
from cryptokit import xor_cipher


class TestSum(unittest.TestCase):

    def test_convert_key_to_array_shorter_key(self):
        self.assertEqual(xor_cipher.adjust_key_length("AZBzzAe", 9),
                         "AZBzzAeAZ",
                         "Should be AZBzzAeAZ")

    def test_encrypt_normal_example_abcd(self):
        self.assertEqual(xor_cipher.encrypt("abcdZ", "KEYKE"),
                         "Kic6Lx8=",
                         "Should be Kic6Lx8=")

    def test_decrypt_normal_example_abcd(self):
        self.assertEqual(xor_cipher.decrypt("Kic6Lx8=", "KEYKE"),
                         "abcdZ",
                         "Should be abcdZ")


if __name__ == "__main_":
    unittest.main()