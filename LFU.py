def least_frequently_used(page_list, number_of_frames):
    # zmienne do zliczania trafien i pominiec
    fault = 0
    hit = 0
    minimum = 0
    # pusta lista na ramki pamieci
    frames = []
    # dodajemy licznik frekwencji
    frequency = [1] * number_of_frames
    # pusta tablica na wyniki
    value = []

    line = []
    hit_fault_list = []

    for i in range(number_of_frames):
        line.append([])
        line[i] = i * ['0']
    
    
    for element in page_list:
        # uzupelniamy cala ramke numerami stron
        if len(frames) != number_of_frames:
            # dodajemy strone do ramki pamieci
            frames.append(element)
            # sprawdzamy czy przy uzupelnianiu ramki nie ma powtorzonych numerow
            for i in range(len(frames)-1):
                # jezeli numery strony sie powtarzaja to zwiekszamy liczbe trafien
                if element.p_number == frames[i].p_number:
                    hit += 1
                    frequency[i] += 1
                    break
            else:
                # jezeli numer strony jeszcze nie wystepuje to zglaszamy pominiecie
                fault += 1
        # sprawdzamy czy numer juz wystapil w ramce
        else:
            # jezeli numer strony sie powtarza z tym ktory juz istnieje w ramce,
            # to zwiekszamy ilosc powtorzen(frequency)
            # o 1 i zostawiamy w ramce
            for i in range(0, number_of_frames):
                if element.p_number == frames[i].p_number:
                    hit += 1
                    frequency[i] += 1
                    break
            else:
                # jezeli sie nie powtarzaja to zglaszamy pominiecie
                fault += 1
                # zeby dodac nowy element musimy stwierdzic ktory element ma najmniejsza ilosc pominiec
                for i in range(0, number_of_frames):
                    if i == 0:
                        minimum = 1
                    # w pierwszej kolejnosci ustalamy jaka jest najmniejsza ilosc powtorzen
                    if minimum < frequency[i]:
                        minimum = frequency[i]
                # gdy juz ustalimy najmniejsza ilosc powtorzen, mozna na tej podstawie znalezc w frequency minimalna
                # ilosc powtorzen, indeksy frequency i ramki sie nakladaja, wiec jezeli znajdziemy indeks w
                # frequency, to znajdujemy tez najmniejszy indeks, dla ramki pamieci
                for item in frequency:
                    # jezeli znajdziemy pierwszy numer strony z najmniejsza iloscia powotrzen
                    if item == minimum:
                        # to usuwamy numer strony z ramki pamieci i usuwamy odpowiadajacy mu index w frequency
                        del frames[frequency.index(item)]
                        del item
                        # nastepnie dodajemy numer strony do ramki i uzupelniamy odpowiadajacy dla niego indeks
                        # w liscie powtorzen
                        frames.append(element)
                        frequency.append(1)
                        # break jest konieczny, poniewaz musimy wyrzucic tylko jeden numer strony z ramki
                        break       
    # zwracamy wartosc trafien i pominiec stron w liscie
    value.append(fault)
    value.append(hit)
    return value
