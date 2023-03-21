Plan for Aplication for v.1.0

Dane:
Imie
Nazwisko
Płeć
Data urodzenia
PESEL



Użykownik wchodzi na stornę Główną:
	losuj nowe dane:
	Otrzymuję info losowego użytkownika displej w tabelce:
	moze pobrać dane użytkownika w csv, xml, json
	Informacje w jaki sposób skorzystać z API
Użytkownik wchodzi na url API:
	Wyświetla dane dotyczące jednego użytkownika
	
generate Adres:
	post-code, City, ulica, musza byc zgodne -> csv 
	numer domu/mieszkania

Stworzyć django projekt
strona startowa, strona wyswietljaca wygenerowane dane 

aplikacja do importu danych danych z csv.
każda tabela importowana w osobnej funkcji
przed importowaniem, czyszczenie tabeli

wykonanie import za pomocą komendy(wszystkie tabele naraz)
	import danych na widoku -> dodać tabelę przechowującą informację o importcie
w modelach dodać tabele :

address (id, post-code, city, street, street_number, flat_number)
random person (id, first_name, last_name, gender, birth_date, pesel, id_card, phone, zip-code, city, street, street_number, flat_number)
	różne tryby tworzenia FakePerson
	