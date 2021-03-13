import random
import string
import datetime
from pathlib import Path
import csv

DATA_CSV = Path.cwd() / 'data_csv'

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

def generate_gender():
    return random.choice(['M', 'K'])

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

def generate_first_name(gender):
    if gender == 'M':
        with open(DATA_CSV / 'Imiona_Meskie.csv') as csv_file:
            random_first_name = ''
            csv_reader = csv.reader(csv_file, delimiter=',')
            list_csv_reader = [i for i in csv_reader]
            rows_count = (len(list_csv_reader))
            random_row = random.randint(1, rows_count)
            for index, row in enumerate(list_csv_reader):
                if index == random_row:
                    random_first_name = row[0]
                    if ([i for i in random_first_name if i in string.whitespace]):
                        random_first_name = row[0].split()[0]
                    return random_first_name.capitalize()

    elif gender == 'K':
        with open(DATA_CSV / 'Imiona_damskie.csv') as csv_file:
            random_first_name = ''
            csv_reader = csv.reader(csv_file, delimiter=',')
            list_csv_reader = [i for i in csv_reader]
            rows_count = (len(list_csv_reader))
            random_row = random.randint(1, rows_count)
            for index, row in enumerate(list_csv_reader):
                if index == random_row:
                    random_first_name = row[0]
                    if ([i for i in random_first_name if i in string.whitespace]):
                        random_first_name = row[0].split()[0]
                    return random_first_name.capitalize()


def generate_last_name(gender):
    if gender == 'M':
        with open(DATA_CSV / 'Nazwiska_Meskie.csv') as csv_file:
            random_last_name = ''
            csv_reader = csv.reader(csv_file, delimiter=',')
            list_csv_reader = [i for i in csv_reader]
            rows_count = (len(list_csv_reader))
            random_row = random.randint(1, rows_count)
            for index, row in enumerate(list_csv_reader):
                if index == random_row:
                    random_last_name = row[0]
                    if ([i for i in random_last_name if i in string.whitespace]):
                        random_last_name = row[0].split()[0]
                    return random_last_name.capitalize()

    elif gender == 'K':
        with open(DATA_CSV / 'Nazwiska_Damskie.csv') as csv_file:
            random_last_name = ''
            csv_reader = csv.reader(csv_file, delimiter=',')
            list_csv_reader = [i for i in csv_reader]
            rows_count = (len(list_csv_reader))
            random_row = random.randint(1, rows_count)
            for index, row in enumerate(list_csv_reader):
                if index == random_row:
                    random_last_name = row[0]
                    if ([i for i in random_last_name if i in string.whitespace]):
                        random_last_name = row[0].split()[0]
                    return random_last_name.capitalize()


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

def create_random_person():
    gender = generate_gender()
    birth_date = generate_birth_date()
    return  generate_first_name(gender), \
            generate_last_name(gender), \
            birth_date, \
            generate_id_card(), \
            generate_pesel(gender, birth_date), \
            generate_fake_phone_number(), \
            *generate_address()



print(create_random_person())

