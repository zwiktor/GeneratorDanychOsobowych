from django.shortcuts import render, HttpResponse,redirect
from .models import FemaleName, FemaleSurname, MaleName, MaleSurname
from ._generate_data import FullNamePersonGenerator, PeselPersonGenerator
from FakePersonGenerator import settings
import csv


# możliwość ładowania danych wyłącznie przez admina (Sesja lub ciasteczka)
# dodanie dwoch oddzielnych importów do danych osobowych oraz adresowych
# możliwosć parametryzacji a przy defaulcie wartośc np. 100
# widoki do czyszczenia bazy danych wraz z indeksami
# Stworzenie dekoratora do zapisywania zmian ilościowych baz danych dla dodawanai i usuwania
def load_data(request):
    data_in_files = {
        FemaleName: 'Imiona_damskie.csv',
        FemaleSurname: 'Nazwiska_Damskie.csv',
        MaleName: 'Imiona_Meskie.csv',
        MaleSurname: 'Nazwiska_Meskie.csv'
    }
    for cls, file in data_in_files.items():
        path = settings.DATA_CSV / file
        with open(path, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for i in range(5):
                name = next(csv_reader)[0]
                obj = cls.objects.create(name=name)
                obj.save()
        csv_file.close()


    return HttpResponse('ladowanie zakonczone')


def home(request):
    random_male = FullNamePersonGenerator(1).gender
    random_female = FullNamePersonGenerator(2).__dict__
    random_gender = PeselPersonGenerator().__dict__

    text_response = f'''
        {random_male} ----- {random_female}----------{random_gender}
    '''
    return HttpResponse(text_response)
# Create your views here.
