class Page:
    # glowny pojemnik na dane, posiadamy w nim wszystkie potrzebne informacje o numerze stron
    def __init__(self):
        self.p_index = None
        self.p_number = None


def from_string(line):
    # Tworzymy nowa instacje klasy 'Page'
    page = Page()
    # Rozdziela wszystkie dane oddzielone spacja(dowolna iloscia) do listy data[]
    data = line.split()
    # uzupelniammy kazdy atrybut klasy danymi z ciagu z plikow
    page.p_index = data[0]
    page.p_number = int(data[1])
    # zwracamy instancje klasy, adres na klase
    return page


def make_list_copy(process_list):
    # Tworzymy pusta liste
    copied_list = []
    for i in range(0, len(process_list)):
        # Tworzymy nowa instacje klasy 'page'
        page = Page()
        # dodajemy do listy nowa pusta instancje klasy
        copied_list.append(page)
        # atrybuty klasy uzupelniamy danymi podanymi w parametrze
        copied_list[i].p_index = process_list[i].p_index
        copied_list[i].p_number = process_list[i].p_number
    return copied_list

# funkcja do obliczania sredniej
def average(value_list, number,  series_count):
    list_sum = 0
    for item in value_list:
        list_sum += item[number]
    return list_sum/series_count


def save_to_file(value_list1, value_list2, name1, name2, series_count):

    # otwieramy plik w trybie zapisu, with open, nie musimy sie martwic o zamykanie pliku
    with open('wyniki' + name1 + name2 + '.txt', 'w', encoding='utf-8') as file:
        # Pierwsza linia jest, tabelka pokazujaca ktora dana sluzy do czego
        file.write('\t' + name1 + '1' + '\t\t\t' + name1 + '2' + '\t\t\t' + name1 + '3' + '\t\t\t')
        file.write('\t' + name2 + '1' + '\t\t\t' + name2 + '2' + '\t\t\t' + name2 + '3' + '\n')
        # druga to linia kosmetyczna mowiaca, ze kolejna linia to srednia
        file.write('average' + '1' + '\t\t' + 'average' + '2' + '\t\t' + 'average' + '3' + '\t\t\t')
        file.write('average' + '1' + '\t\t' + 'average' + '2' + '\t\t' + 'average' + '3' + '\n')

        # obliczania jest srednia i umieszczana w odpowiednie miejsca
        file.write(str(average(value_list1[0], 0, series_count))
                   + '\t' + str(average(value_list1[0], 1, series_count)) + '\t')
        file.write(str(average(value_list1[1], 0, series_count))
                   + '\t' + str(average(value_list1[1], 1, series_count)) + '\t')
        file.write(str(average(value_list1[2], 0, series_count))
                   + '\t' + str(average(value_list1[2], 1, series_count)) + '\t\t')

        file.write(str(average(value_list2[0], 0, series_count))
                   + '\t' + str(average(value_list2[0], 1, series_count)) + '\t')
        file.write(str(average(value_list2[1], 0, series_count))
                   + '\t' + str(average(value_list2[1], 1, series_count)) + '\t')
        file.write(str(average(value_list2[2], 0, series_count))
                   + '\t' + str(average(value_list2[2], 1, series_count)) + '\n')

        # linia kosmetyczna, mowiaca ile jest trafien ile zastapien
        file.write('fault' + '\t' + 'hit' + '\t\t' + 'fault' + '\t' + 'hit' + '\t\t' + 'fault' + '\t' + 'hit'
                   + 3 * '\t')
        file.write('fault' + '\t' + 'hit' + '\t\t' + 'fault' + '\t' + 'hit' + '\t\t' + 'fault' + '\t' + 'hit' + '\n')
        # petla wypisujaca dane z listy
        for i in range(0, len(value_list1[0])):
            file.write(str(value_list1[0][i][0]) + '\t\t' + str(value_list1[0][i][1]) + '\t\t')
            file.write(str(value_list1[1][i][0]) + '\t\t' + str(value_list1[1][i][1]) + '\t\t')
            file.write(str(value_list1[2][i][0]) + '\t\t' + str(value_list1[2][i][1]) + '\t\t\t')

            file.write(str(value_list2[0][i][0]) + '\t\t' + str(value_list2[0][i][1]) + '\t\t')
            file.write(str(value_list2[1][i][0]) + '\t\t' + str(value_list2[1][i][1]) + '\t\t')
            file.write(str(value_list2[2][i][0]) + '\t\t' + str(value_list2[2][i][1]) + '\n')
