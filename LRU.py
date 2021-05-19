from processing import make_list_copy


def least_recently_used(page_list, number_of_frames):
    # tworzymy kopie oryginalnych danych
    page_list_copy = make_list_copy(page_list)
    # zmienne do zliczania trafien i pominiec
    fault = 0
    hit = 0
    # lista do ktorej bedziemy zapisywac wynik
    value = []
    # pusta lista na ramki pamieci
    frames = []
    # pierwsze indeksy oznaczaja, ze strona w ramce jest najrzadziej uzywana, a ostatnie indeksy to strony ktore dopiero
    # przyszly do ramek pamieci
    for element in page_list_copy:
        # uzupelniamy cala ramke numerami stron
        if len(frames) != number_of_frames:
            frames.append(element)
            # sprawdzamy czy przy uzupelnianiu ramki nie ma powtorzonych numerow
            for i in range(len(frames)-1):
                if element.p_number == frames[i].p_number:
                    # zwiekszamy liczbe trafien o 1
                    hit += 1
                    # usuwamy element ktory sie powtarza
                    del frames[i]
                    # zeby nastepnie dac go jako miejsce ostatnio uzytego
                    frames.append(element)
                    break
            # jezeli numery sie nie powtarzaja, to zglaszany jest pominiecie
            else:
                fault += 1
        # sprawdzamy czy numer strony juz wystapil w ramce
        else:
            for i in range(0, number_of_frames):
                # jezeli numer strony pokrywa sie z tymi w ramce zglaszamy trafienie
                if element.p_number == frames[i].p_number:
                    hit += 1
                    # usuwamy indeks ktory sie powtarza i ustawiamy go jako najnowszy, czyli ostatni indeks
                    del frames[i]
                    frames.append(element)
                    break
            else:
                # zglaszamy pominiecie, usuwamy ostatnio uzywany numer strony, czyli pierwszy indeks i uzupelniamy nowym
                fault += 1
                del frames[0]
                frames.append(element)

    # na koniec czyszczenie pamieci z adresow instancji klasy
    page_list_copy.clear()
    # zwracamy wartosc trafien i pominiec stron w liscie
    value.append(fault)
    value.append(hit)
    return value
