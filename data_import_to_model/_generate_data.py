import random
import string
import datetime
from FakePersonGenerator import settings
from data_import_to_model.models import *
from abc import ABC, abstractmethod

import csv


class BasicPersonGenerator(ABC):
    @abstractmethod
    def __init__(self, gender=0):
        self.gender = generate_gender(gender)

    @abstractmethod
    def jsonify(self):
        pass

    @abstractmethod
    def xmlify(self):
        pass


class FullNamePersonGenerator(BasicPersonGenerator):
    def __init__(self, gender=0):
        super().__init__(gender)
        self.first_name = generate_first_name(self.gender)
        self.last_name = generate_last_name(self.gender)

    def jsonify(self):
        pass

    def xmlify(self):
        pass


class PeselPersonGenerator(FullNamePersonGenerator):
    def __init__(self, gender=0):
        super().__init__(gender)
        self.birth_date = generate_birth_date()
        self.pesel = generate_pesel(self.gender, self.birth_date)


class FullPersonGenerator(PeselPersonGenerator):
    def __init__(self, gender=0):
        super().__init__(gender)
        self.id_card = generate_id_card()
        self.phone_number = generate_fake_phone_number()
        self.address = generate_address() #baza danych


class FakePersonGenerator():
    def __init__(self):
        self.gender = generate_gender()
        self.first_name = generate_first_name(self.gender)#baza danych
        self.last_name = generate_last_name(self.gender)#baza danych
        self.birth_date = generate_birth_date()
        self.pesel = generate_pesel(self.gender, self.birth_date)
        self.id_card = generate_id_card()
        self.address = generate_address() #baza danych
        self.phone_number = generate_fake_phone_number()
    # Dodanie kilku konfiguracji tworzenia danych



# TO DO convert to class
def generate_fake_phone_number():
    number = ''
    first_number = random.choice([5, 6, 7, 8])
    number += str(first_number)
    for i in range(8):
        number += str(random.randint(1, 9))
    return number


# TO DO convert to class input
def generate_birth_date():
    _min_date = datetime.date(1930,1,1)
    _max_date = datetime.date(2008,12,31)
    _min_date_ordinar = datetime.date(1920,1,1).toordinal()
    _max_date_ordinar = datetime.date(2008,12,31).toordinal()
    date_range = _max_date_ordinar - _min_date_ordinar
    random_date_ordinar = _min_date_ordinar + random.randint(1, date_range)
    random_date = datetime.date.fromordinal(random_date_ordinar)

    return str(random_date)


def generate_gender(gender):
    if gender == 1:
        return 'M'
    elif gender == 2:
        return 'K'
    elif gender == 0:
        return random.choice(['M', 'K'])
    else:
        raise Exception('It can be 1=Male or 2=Female or 0=random gender')


def generate_pesel(gender, birth_date):
    pesel = ''
    year, month, day = birth_date.split('-')
    pesel += year[-2:]
    if year[0] == '2':
        pesel += str(int(month) + 20)
    else:
        pesel += month
    pesel += day
    for i in range(3):
        pesel += str(random.randint(0, 9))
    if gender == 'K':
        pesel += str(random.choice([0, 2, 4, 6, 8]))
    if gender == 'M':
        pesel += str(random.choice([1, 3, 5, 7, 9]))

    numbers_of_weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum = 0
    for i in range(len(pesel)):
        tmp_number = int(pesel[i]) * numbers_of_weight[i]
        tmp_number = int(str(tmp_number)[-1])
        sum += tmp_number
    sum = int(str(sum)[-1])
    if sum == 0:
        pesel += '0'
    else:
        pesel += str(10 - sum)

    return pesel


def generate_id_card():
    number_of_weights = [7, 3, 1, 7, 3, 1, 7, 3]
    card_series = random.choices(string.ascii_uppercase, k=3)
    series_converted = [string.ascii_uppercase.index(letter) + 10 for letter in card_series]
    card_number = random.choices(string.digits, k=5)
    card_id = series_converted + card_number
    control_number = [str(sum(int(number_of_weights[i]) * int(card_id[i])  for i in range(len(number_of_weights))) % 10)]
    return ''.join((card_series + control_number + card_number))


def generate_first_name(gender='M'):
    if gender == 'M':
        cls = MaleName
    else:
        cls = FemaleName
    print(cls.__name__)
    # wielkośc danych należy zapiać w oddzielnej tabeli dotyczącej importów
    table_size = cls.objects.all().count()
    random_id = randint(1, table_size)
    random_obj = cls.objects.get(id=random_id)
    return random_obj.name


def generate_last_name(gender='M'):
    if gender == 'M':
        cls = MaleSurname
    else:
        cls = FemaleSurname
    print(cls.__name__)
    # wielkośc danych należy zapiać w oddzielnej tabeli dotyczącej importów
    table_size = cls.objects.all().count()
    random_id = randint(1, table_size)
    random_obj = cls.objects.get(id=random_id)
    return random_obj.name


def generate_address():
    with open(DATA_CSV / 'kody-pocztowe.csv') as csv_file:
        address = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_csv_reader = [i for i in csv_reader]
        rows_count = (len(list_csv_reader))
        random_row = random.randint(1, rows_count)
        street_number = str(random.randint(1, 100))
        flat = str(random.randint(1, 100))
        for row in list_csv_reader:
            if row[0] == str(random_row):
                return [row[1], row[2].capitalize(), row[4], street_number, flat]




