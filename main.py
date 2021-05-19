# from sample import generator
from processing import *
from LRU import least_recently_used
from LFU import least_frequently_used

# Generator losowych liczb, pierwszy parametr to ilosc wygenerowanych procesow, drugi to zakres
# generator(10000, 20)

# pusta lista na numery stron
my_page_list = []

# listy z zapisanymi wynikami

value_LRU3 = []
value_LRU5 = []
value_LRU7 = []

value_LFU3 = []
value_LFU5 = []
value_LFU7 = []

# with open otwiera plik i automatycznie zamyka plik, wiec nie musimy sie martwic, o zamykanie go
# plik otwieramy tylko w trybie odczytu, nie potrzebujemy zapisu
with open('teststrony.txt', 'r', encoding='utf-8') as file:
    # Pomijamy pierwsza linie, poniewaz pierwsza linia jest opisowa P_index, Arrival_time i Burst_time
    next(file)
    # definiowanie zmiennych do zliczania count i do sumowania sum od 0
    lines_count = 0
    series_count = 0

    # dzialamy tak dlugo, az nie skoncza sie linie w notatniku
    for line in file:
        # Dodawanie danych do glownej tablicy przechowujacej dane, funkcja from_string rozdziela string na 2 rozne
        # zmienne potrzebne pozniej do obliczen
        my_page_list.append(from_string(line))

        lines_count += 1
        # gdy zczytamy juz 100 linii z pliku, sa wykonywane pierwsze dzialania na zmiennych pobranych z pliku
        if lines_count == 100:

            value_LRU3.append(least_recently_used(my_page_list, 3))
            value_LRU5.append(least_recently_used(my_page_list, 5))
            value_LRU7.append(least_recently_used(my_page_list, 7))

            value_LFU3.append(least_frequently_used(my_page_list, 3))
            value_LFU5.append(least_frequently_used(my_page_list, 5))
            value_LFU7.append(least_frequently_used(my_page_list, 7))

            # zerowanie licznika linii do 0, poniewaz zaczynamy nowy ciag
            lines_count = 0
            # dodajemmy do licznika serii 1, poniewaz przeszlismy w tym momenciu juz jeden ciag po 100 procesow
            series_count += 1
            # Czyscimy liste, zeby moc wypelnic nowa seria, w ten sposob tez oszczedzamy RAM'u nie przydzielajac
            # kolejnej listy
            my_page_list.clear()

# lista z wszystkimi wynikami spietymi
value_LRU = [value_LRU3, value_LRU5, value_LRU7]
value_LFU = [value_LFU3, value_LFU5, value_LFU7]

# Zapisuje wyniki do pliku
save_to_file(value_LRU, value_LFU, 'LRU', 'LFU', series_count)
