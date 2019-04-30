# Standard-library imports
import itertools
import string


LOWER_CHARS = set(string.ascii_lowercase)
UPPER_CHARS = set(string.ascii_uppercase)
SPECIAL_SIGNS = set(string.punctuation)
DIGITS = set(string.digits)
ALL_CHARS = itertools.chain(LOWER_CHARS, UPPER_CHARS, SPECIAL_SIGNS, DIGITS)


class PasswordGenerator:

    def __init__(self, min_chars=5, max_chars=15, max_upper_chars = 3, max_special_signs=2, max_digits=4):
        self.min_chars = min_chars
        self.max_chars = max_chars
        self.max_upper_chars = max_upper_chars
        self.max_special_signs = max_special_signs
        self.max_digits = max_digits

    def password_generator(self):
        for pass_length in range(self.min_chars, self.max_chars):
            for product in itertools.product(ALL_CHARS, repeat=pass_length):
                special_signs_count = sum(x in SPECIAL_SIGNS for x in product)
                digits_count = sum(x in DIGITS for x in product)
                upper_chars_count = sum(x in UPPER_CHARS for x in product)
                if (special_signs_count <= self.max_special_signs and digits_count <= self.max_digits and
                        upper_chars_count <= self.max_upper_chars):
                    password = ''.join(product)
                    yield password
