import unittest
from unittest.mock import patch

from password_generator import create_password


class PasswordGeneratorTests(unittest.TestCase):
    def test_length_and_selected_alphabet(self):
        for length in (8, 16, 128):
            with self.subTest(length=length):
                password = create_password(length, "ab12!ä")
                self.assertEqual(len(password), length)
                self.assertLessEqual(set(password), set("ab12!ä"))

    def test_invalid_lengths_are_rejected(self):
        for length in (-1, 0, 7, 129, 10**9):
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    create_password(length, "abc")

    def test_empty_alphabet_is_rejected(self):
        with self.assertRaises(ValueError):
            create_password(16, "")

    def test_uses_secure_source_and_deduplicates_alphabet(self):
        with patch("password_generator.secrets.choice", return_value="a") as choice:
            self.assertEqual(create_password(8, "aaba"), "a" * 8)
            self.assertEqual(choice.call_count, 8)
            choice.assert_called_with("ab")


if __name__ == "__main__":
    unittest.main()
