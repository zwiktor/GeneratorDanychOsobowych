import unittest
import _generate_data
import datetime
import string


class TestPhoneNumberGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.phone_number = _generate_data.generate_fake_phone_number()

    def test_lenght_number(self):
        phone_number_len = len(self.phone_number)
        self.assertEqual(phone_number_len, 9)

    def test_first_number(self):
        self.assertIn(self.phone_number[0], ['5', '6', '7', '8'])


class TestBirthDateGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.birth_date = _generate_data.generate_birth_date()

    def test_date_is_string(self):
        self.assertEqual(self.birth_date, str(self.birth_date))

    def test_format_birth_date(self):
        self.assertRegex(self.birth_date, '\d\d\d\d-\d\d-\d\d')
        year, month, day = self.birth_date.split('-')
        self.assertEqual(len(year), 4)
        self.assertLessEqual(len(month), 2)
        self.assertLessEqual(len(day), 2)

    def test_range_of_birth_date(self):
        # between 1 and 100 year
        year, month, day = self.birth_date.split('-')
        self.assertTrue(datetime.date(1900,1,1) <= datetime.date(int(year), int(month), int(day)) <= datetime.date(2020,12,31))

    def test_month_number(self):
        month = self.birth_date.split('-')[1]
        self.assertIn(int(month), range(1, 13))

    def test_day_number(self):
        day = self.birth_date.split('-')[2]
        self.assertIn(int(day), range(1, 32))

class TestGenderGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.gender = _generate_data.generate_gender()

    def test_gender(self):
        self.assertIn(self.gender, ['M', 'K'])


class TestPeselGenerator(unittest.TestCase):

    def setUp(self) -> None:
        self.gender = _generate_data.generate_gender()
        self.birth_date = _generate_data.generate_birth_date()
        self.pesel = _generate_data.generate_pesel(self.gender, self.birth_date)
        # self.gender = 'M'
        # self.birth_date = '2096-07-21'
        # self.pesel = '96072101471'

    def text_pesel_lenght(self):
        self.assertEqual(len(self.pesel), 11)

    def test_pesel_control_number(self):
        contorl_number = int(self.pesel[10])
        numbers_of_weight = [1,3,7,9,1,3,7,9,1,3]
        sum = 0
        for i in range(len(self.pesel[:-1])):
            tmp_number = int(self.pesel[i]) * numbers_of_weight[i]
            tmp_number = int(str(tmp_number)[-1])
            sum += tmp_number
        sum = int(str(sum)[-1]) #modulo !!!!
        if sum == 0:
            result_number = 0
        else:
            result_number = 10 - sum
        self.assertEqual(int(contorl_number), result_number)

    def test_birth_year_after_2000(self):
        month = self.pesel[2:4]
        year = self.birth_date[:4]
        if int(year) >= 2000:
            self.assertGreaterEqual(int(month), 20)
        else:
            self.assertLessEqual(int(month), 12)


    def test_gender_nuber(self):
        gender_number = int(self.pesel[9])
        if self.gender == 'M':
            self.assertIn(gender_number, [1,3,5,7,9])
        if self.gender == 'K':
            self.assertIn(gender_number, [2,4,6,8,0])

class TestIdCardGenerator(unittest.TestCase):

    def setUp(self) -> None:
        self.card = _generate_data.generate_id_card()

    def test_id_card_series(self):
        for letter in self.card[0:3]:
            self.assertIn(letter, string.ascii_uppercase)

    def test_id_card_number(self):
        for number in self.card[3:]:
            self.assertIn(number, string.digits)

    def test_id_card_control_number(self):
        number_of_weights = [7, 3, 1, 7, 3, 1, 7, 3]
        ascii_letter = string.ascii_uppercase
        series_converted = [ascii_letter.index(letter) + 10 for letter in self.card[0:3]]
        card_numbers = series_converted + [int(number) for number in self.card[4:]]
        control_result = 0
        for i in range(len(number_of_weights)):
            control_result += (card_numbers[i] * number_of_weights[i])
        control_number = int(self.card[3])
        modulo_results = control_result % 10
        self.assertEqual(control_number, modulo_results)


class TestFirstNameGenerator(unittest.TestCase):

    def setUp(self):
        self.gender = _generate_data.generate_gender()
        self.first_name = _generate_data.generate_first_name(self.gender)

    def test_name_lenght(self):
        self.assertGreater(len(self.first_name), 2, 'first name is too short')

    def test_whitespaces(self):
        for letter in self.first_name:
            self.assertNotIn(letter, string.whitespace, 'first name contain whitespaces')

    def test_digits(self):
        for letter in self.first_name:
            self.assertNotIn(letter, string.digits, 'first name contain digits')

    def test_name_punctation(self):
        for letter in self.first_name:
            self.assertNotIn(letter, string.punctuation, 'first name contain puntactions')

    def test_name_capitalize(self):
        name_capital = self.first_name.capitalize()
        self.assertEqual(self.first_name, name_capital, 'Name is not Capitalized')


class TestLastNameGenerator(unittest.TestCase):

    def setUp(self):
        self.gender = _generate_data.generate_gender()
        self.last_name = _generate_data.generate_last_name(self.gender)

    def test_name_lenght(self):
        self.assertGreater(len(self.last_name), 2, 'first name is too short')

    def test_whitespaces(self):
        for letter in self.last_name:
            self.assertNotIn(letter, string.whitespace, 'first name contain whitespaces')

    def test_digits(self):
        for letter in self.last_name:
            self.assertNotIn(letter, string.digits, 'first name contain digits')

    def test_name_punctation(self):
        for letter in self.last_name:
            self.assertNotIn(letter, string.punctuation, 'first name contain puntactions')

    def test_name_capitalize(self):
        name_capital = self.last_name.capitalize()
        self.assertEqual(self.last_name, name_capital, 'Name is not Capitalized')

class TestLastAdresGenerator(unittest.TestCase):

    def setUp(self) -> None:
        address = _generate_data.generate_address()
        self.post_code = address[0]
        self.city = address[1]
        self.street = address[2]
        self.streetNo = address[3]
        self.flat = address[4]

    def test_post_code_letters(self):
        for elem in self.post_code:
            self.assertNotIn(elem, string.ascii_letters)

    def test_post_code_format(self):
        self.assertRegex(self.post_code, '\d\d-\d\d\d')

    def test_post_code_len(self):
        self.assertEqual(len(self.post_code), 6)

    def test_city_capitalized(self):
        text_cap = self.city.capitalize()
        self.assertEqual(self.city, text_cap)

    def test_city_len(self):
        self.assertLess(len(self.city), 128)

    def test_street_capitalized(self):
        text_cap = self.street.capitalize()
        self.assertEqual(self.street, text_cap)

    def test_street_len(self):
        self.assertLess(len(self.street), 128)

    def test_street_number(self):
        self.assertRegex(self.streetNo, '\d')

    def test_flat_number(self):
        for number in self.flat:
            self.assertIn(number, string.digits)

    def test_flat_number_len(self):
        if self.flat:
            self.assertGreaterEqual(len(self.flat), 1)
            self.assertLessEqual(len(self.flat), 4)


if __name__ == '__main__':
    unittest.main()