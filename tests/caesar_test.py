import unittest
from cryptokit import caesar


class TestSum(unittest.TestCase):

    def test_encrypt_normal_example_abcd_key_3(self):
        self.assertEqual(caesar.encrypt("abcd", 3),
                         "defg",
                         "Should be defg")

    def test_encrypt_non_alpha_characters(self):
        self.assertEqual(caesar.encrypt("}zzAA-~~", 5),
                         "#  FF2$$",
                         "Should be #  FF2$$")

    def test_decrypt_normal_example_abcd_key_3(self):
        self.assertEqual(caesar.decrypt("defg", 3),
                         "abcd",
                         "Should be abcd")

    def test_decrypt_non_alpha_characters(self):
        self.assertEqual(caesar.decrypt("#  FF2$$", 5),
                         "}zzAA-~~",
                         "Should be }zzAA-~~")

if __name__ == "__main_":
    unittest.main()