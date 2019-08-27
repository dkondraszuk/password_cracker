import itertools
import string
import time


LOWER_CHARS = set(string.ascii_lowercase)
UPPER_CHARS = set(string.ascii_uppercase)
SPECIAL_SIGNS = set(string.punctuation)
DIGITS = set(string.digits)
ALL_CHARS = string.ascii_letters + string.digits + string.punctuation


class PasswordGenerator:

    def __init__(self, min_chars=2, max_chars=4, max_upper_chars=0, max_special_signs=0, max_digits=0):
        self._min_chars = min_chars
        self._max_chars = max_chars
        self._max_upper_chars = max_upper_chars
        self._max_special_signs = max_special_signs
        self._max_digits = max_digits
        self._batch_size = 1_000
        self._batch = []

    def password_generator(self):
        for pass_length in range(self._min_chars, self._max_chars + 1):
            iter_product = itertools.product(ALL_CHARS, repeat=pass_length)
            for product in iter_product:
                special_signs_count = sum(x in SPECIAL_SIGNS for x in product)
                digits_count = sum(x in DIGITS for x in product)
                upper_chars_count = sum(x in UPPER_CHARS for x in product)
                if (special_signs_count <= self._max_special_signs and digits_count <= self._max_digits and
                        upper_chars_count <= self._max_upper_chars):
                    password = ''.join(product)
                    yield password

    def generate_passwords_to_file(self):
        pw_generator = self.password_generator()
        t_start = time.perf_counter()
        t_print = time.perf_counter()
        counter = 0
        print('Generating passwords in progress ...', end='')
        with open('passwords.txt', 'w') as f:
            while True:
                try:
                    self._batch.extend((next(pw_generator), '\n'))
                except StopIteration:
                    f.writelines(self._batch)
                    break
                if len(self._batch) == self._batch_size:
                    f.writelines(self._batch)
                    self._batch = []
                counter += 1
                if time.perf_counter() - t_print > 5:
                    print('.', end='')
                    t_print = time.perf_counter()
        t_stop = time.perf_counter()
        print()
        print('****************************************************')
        print('Generated passwords count: {}'.format(counter))
        print('Total password generation time: {}'.format(t_stop - t_start))
        print('****************************************************')


if __name__ == '__main__':
    pw_gen = PasswordGenerator()
    pw_gen.generate_passwords_to_file()
