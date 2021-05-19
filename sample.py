from random import seed
from random import randint


def generator(length, max_range):
    # zeby dane byly losowe nalezy pozostawic nawiasy puste, jezeli podamy liczbe, dane beda zawsze takie same
    seed()
    # Otwieramy plik przy uzyciu with, w trybie zapisywania
    with open('teststrony.txt', 'w', encoding='utf-8') as file:
        # dodajemy dodatkowa zmienna, zapisujaca w ktorej serii jest proces, sluzy to tylko czytelnosci pliku z danymi
        series_count = 0
        # Pierwsza linia jest, tabelka pokazujaca ktora dana sluzy do czego
        file.write('Page index' + '\t' + 'page number' + '\n')
        # Tworzy tyle danych ile podamy w funkcji
        for index in range(length):
            # numer ciagu
            if index % 100 == 0:
                series_count += 1
            # indeksowanie numerow stron, P nazwa indexu a po '_' numer ciagu numerowania stron
            file.write('P' + str((index % 100)+1) + '_' + str(series_count))
            # specjalny warunek, poniewaz tabulatory sie rozjedzaja na 10 000 linijce
            # te warunki tylko sluza kosmetyce pliku z danymi
            if index >= 9999:
                file.write(2*'\t')  # Spacing
            else:
                file.write(3*'\t')  # Spacing
            # Tworzymy czas przybycia zalezny od podanego parametru w funkcji generator
            file.write(str(randint(0, max_range)))
            # kosmetyka
            file.write('\n')

