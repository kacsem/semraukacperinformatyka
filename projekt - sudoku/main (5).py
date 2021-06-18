class Sudoku:
    # poczatkowe dane
    def __init__(self):
        # litery i cyfry będą podawane jako współrzędne
        self.litery = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.cyfry = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        # tworzy plansze
        self.plansza = self.stworz_plansze()
        # jeszcze raz tworzy tą samą planszę, żeby sprawdzać później czy można zmienić wartość w którymś miejscu
        self.poczatkowa_plansza = self.stworz_plansze()
        # indeksy pól w kwadracie 3x3, raz zapisane żeby później nie powtarzać
        self.indeksy = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]

    def stworz_plansze(self):
        # plansza = [[2, 9, 5, 4, 8, 1, 7, 3, 6],
        #            [1, 4, 7, 6, 3, 9, 2, 8, 5],
        #            [8, 3, 6, 7, 5, 2, 9, 4, 1],
        #            [6, 8, 4, 5, 1, 7, 3, 9, 2],
        #            [7, 5, 3, 9, 2, 8, 1, 6, 4],
        #            [9, 1, 2, 3, 6, 4, 8, 5, 7],
        #            [5, 6, 1, 2, 9, 3, 4, 7, 8],
        #            [3, 7, 8, 1, 4, 6, 5, 2, 9],
        #            [4, 2, 9, 8, 7, 5, 6, 1, 0]]
        plansza = [[2, 0, 0, 6, 0, 7, 5, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 9, 6],
                   [6, 0, 7, 0, 0, 1, 3, 0, 0],
                   [0, 5, 0, 7, 3, 2, 0, 0, 0],
                   [0, 7, 0, 0, 0, 0, 0, 2, 0],
                   [0, 0, 0, 1, 8, 9, 0, 7, 0],
                   [0, 0, 3, 5, 0, 0, 6, 0, 4],
                   [8, 4, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 5, 2, 0, 6, 0, 0, 8]]
        # 0 zmieniają się w spacje, żeby ładniej się wyświetlało
        # for przechodzący po rzędach
        for i in range(0, len(plansza)):
            # for przechodzący po kolumnach rzędu z poprzedniego fora
            for j in range(0, len(plansza)):
                # jeśli liczba na danej pozycji to 0, zmień na spację
                if plansza[i][j] == 0:
                    plansza[i][j] = ' '
        # zwraca planszę
        return plansza

    def print_plansza(self):
        # tworzy grida, współrzędne dla kolumn są literami a dla rzędów cyframi

        pierwsza_linia = "     |  " + "     ".join(self.litery[:3]) + "  |  " + "     ".join(self.litery[3:6]) +\
                         "  |  " + "     ".join(self.litery[6::]) + "  |"
        # można to rozbić na
        # "     |  "
        # to bierze wszystkie wartości z listy self.litery i tworzy z nich stringa, czyli napis
        # w którym są wartości z listy, a między nimi wstawione "  |  "
        # "  |  ".join(self.litery)
        # "  |"
        print(pierwsza_linia)

        # linijka przerwy
        print("")

        # odstępy pomiędzy rzędami
        # wstawia -, po nim 4 spacje i dalej do końca -, sprawdzając ile linii powinno być i odejmując 5, bo wcześniej
        # jest już wstawione 5 znaków
        odstep = '-' + 4 * ' ' + '-' * (len(pierwsza_linia) - 5)
        print(odstep)
        # for przechodzący po rzędach
        for i in range(len(self.plansza)):
            # wyświetla rząd, tak samo jak wcześniej tylko tutaj wstawia już cyfry z planszy
            # i po lewej dodaje współrzędne, czyli i+1
            # [str(l) for l in self.plansza[i]] to lista wartości z rzędu, tylko przerobionych na stringi zamiast intów,
            # bo nie da się dodać stringa i inta, czyli trzeba przerobić inta na stringa i dopiero dodać
            print(str(i+1) + "    |  " + "     ".join([str(l) for l in self.plansza[i][:3]]) + '  |  ' +
                  "     ".join([str(l) for l in self.plansza[i][3:6]]) + '  |  ' +
                  "     ".join([str(l) for l in self.plansza[i][6::]]) + '  |  ')
            if i % 3 == 2:
                print(odstep)
            else:
                print("")

    def odczytaj_pozycje(self, pozycja):
        # przerabia wszystkie litery na duże, żeby można
        pozycja = pozycja.upper()
        # jeśli kolejność jest zła, czyli cyfra litera, to tworzy listę w odwrotnej kolejności
        if pozycja[1] in self.litery:
            pozycja = [pozycja[1], pozycja[0]]
        # jeśli kolejność jest dobra, to tworzy listę w takiej samej kolejności
        else:
            pozycja = [pozycja[0], pozycja[1]]
        # zmienia literę na cyfrę, np A na 1, C na 3
        pozycja[0] = self.litery.index(str(pozycja[0]))
        # zmniejsza drugą cyfrę pozycji o 1, bo przy wyświetlaniu są liczby 1-9, a indeksowanie listy
        # w pythonie zaczyna się od 0
        pozycja[1] = int(pozycja[1]) - 1
        return pozycja

    # sprawdza czy plansza jest poprawnie rozwiązana
    def sprawdz_plansze(self):
        # for przechodzący po rzędach planszy
        # sprawdza czy cała plansza jest wypełniona
        for linia in self.plansza:
            # if sprawdzający czy w rzędzie są jakieś spacje, jeśli są to nie jest poprawnie rozwiązana
            if " " in linia:
                return False
        # set() to taka lista, w której taka sama wartość występuje tylko raz, np lista [2, 2, 3] to set {2, 3}
        cyfry = set()
        # for przechodzący po rzędach
        # sprawdza czy rzędy są poprawnie rozwiązane
        for i in range(0, len(self.plansza)):
            # dla każdego rzędu tworzy set
            cyfry = set()
            # for przechodzący po każdej kolumnie danego rzędu
            for j in range(0, len(self.plansza)):
                # dodaje wartość z aktualnej pozycji do setu cyfry
                cyfry.add(self.plansza[i][j])
            # żeby plansza była poprawnie rozwiązana to w każdym rzędzie muszą być wszystkie cyfry od 1 do 9
            # czyli jak set, w którym wartości nie mogą się powtarzać nie ma 9 cyfr to jest źle rozwiązana
            if len(cyfry) != 9:
                return False
        # for przechodzący przez rzędy
        # sprawdza czy kolumny są poprawnie rozwiązane
        for i in range(0, len(self.plansza)):
            # dla każdego rzędu tworzy set
            cyfry = set()
            # for przechodzący po każdej kolumnie danego rzędu
            for j in range(0, len(self.plansza)):
                # dodaje wartość z aktualnej pozycji do setu cyfry
                # to samo co wyżej, tylko tu jest [j][i], czyli sprawdza kolumny
                cyfry.add(self.plansza[j][i])
            # jeśli set nie ma 9 cyfr to jest źle rozwiązana
            if len(cyfry) != 9:
                return False
        # for przechodzący przez rzędy kwadratów 3x3
        # sprawdza czy poszczególne kwadraty są poprawnie rozwiązane
        for i in range(0, 3):
            # for przechodzący przez kolumny kwadratów 3x3
            for j in range(0, 3):
                # dla każdego kwadratu tworzy set
                cyfry = set()
                # po to były nam indeksy, żeby teraz w każdym kwadracie dało się odczytać wartości
                for indeks in self.indeksy:
                    # indeksy wyglądają tak
                    #  00  10  20  30  40  50  60  70  80
                    #  01  11  21  31  41  51  61  71  81
                    #  02  12  22  32  42  52  62  72  82
                    #  03  13  23  33  43  53  63  73  83
                    #  04  14  24  34  44  54  64  74  84
                    #  05  15  25  35  45  55  65  75  85
                    #  06  16  26  36  46  56  66  76  86
                    #  07  17  27  37  47  57  67  77  87
                    #  08  18  28  38  48  58  68  78  88
                    # czyli na przykład kwadrat w prawym dolnym rogu to
                    #  66  76  86
                    #  67  77  87
                    #  68  78  88
                    # indeksy to
                    #  00 10 20
                    #  01 11 21
                    #  02 12 22
                    # a to dzięki forom można zapisać jako
                    # 3 * i + indeks-lewy, 3 * j + indeks-prawy
                    cyfry.add(self.plansza[3 * i + indeks[0]][3 * j + indeks[1]])
                # jeśli set nie ma 9 cyfr to jest źle rozwiązana
                if len(cyfry) != 9:
                    return False
        # jak wszystkie poprzednie warunki przeszły to znaczy że jest rozwiązane poprawnie
        return True

    def dostepne_cyfry(self, pozycja):
        # tworzy set dostepne
        # na początku wszystkie cyfry są dostępne, później będą odchodzić te których się nie da wpisać
        dostepne = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        # sprawdza co można wpisać poziomo
        cyfry = set()
        # for przechodzący po danym wierszu
        for i in range(0, len(self.plansza)):
            # wybiera cyfrę z danego wiersza
            cyfra = self.plansza[pozycja[1]][i]
            # jeśli na danej pozycji jest jakaś cyfra
            if cyfra != ' ':
                # to dodaje ją do setu cyrfy
                cyfry.add(cyfra)
        # usuwa z setu dostępnych cyfr te, których nie da się wpisać, bo sa już w danym rzędzie
        dostepne = dostepne - cyfry
        # sprawdza co można wpisać pionowo
        cyfry = set()
        # for przechodzący po danej kolumnie
        for i in range(0, len(self.plansza)):
            # wybiera cyfrę z danej kolumny
            cyfra = self.plansza[i][pozycja[0]]
            # jeśli na danej pozycji jest jakaś cyfra
            if cyfra != ' ':
                # to dodaje ją do setu cyfry
                cyfry.add(cyfra)
        # usuwa z setu dostępnych cyfr te, których nie da się wpisać, bo sa już w danej kolumnie
        dostepne = dostepne - cyfry

        # sprawdza co można wpisać w kwadracie
        cyfry = set()
        # for przechodzący przez dany kwadrat
        for indeks in self.indeksy:
            # pobiera cyfrę z danej pozycji w danym kwadracie
            cyfra = self.plansza[3 * int(pozycja[1] / 3) + indeks[1]][3 * int(pozycja[0] / 3) + indeks[0]]
            # jeśli na danej pozycji jest jakaś cyfra
            if cyfra != ' ':
                # to dodaje ją do setu cyfry
                cyfry.add(self.plansza[3 * int(pozycja[1] / 3) + indeks[1]][3 * int(pozycja[0] / 3) + indeks[0]])
        # usuwa z setu dostępnych cyfr te, których nie da się wpisać, bo sa już w danym kwadracie
        dostepne = dostepne - cyfry
        return dostepne

    def wpisz_cyfre(self, pozycja, cyfra):
        if cyfra == 0:
            self.plansza[pozycja[1]][pozycja[0]] = ' '
        else:
            self.plansza[pozycja[1]][pozycja[0]] = int(cyfra)

    def walidacja_pozycji(self, pozycja):
        # jeśli pozycja nie istnieje, czyli nic nie jest wpisane, to jest zła
        if not pozycja:
            return "Podaj pozycję w którą chcesz wpisać cyfrę (np E3)"
        # jeśli pozycja nie składa się z 2 znaków to jest zła
        if len(pozycja) != 2:
            return "Pozycja musi składać się z dwóch znaków (np E3)"
        # jeśli pozycja nie składa się z litery i cyfry lub z cyfry i litery to jest zła
        if not (((pozycja[0] in self.litery) and (pozycja[1] in self.cyfry)) or
                ((pozycja[0] in self.cyfry) and (pozycja[1] in self.litery))):
            return "Pozycja musi składać się z litery i cyfry (np E3)"
        # przerabia pozycję z np E3 na [3, 3]
        pozycja = self.odczytaj_pozycje(pozycja)
        # jeśli na początkowej planszy ta pozycja już była wypełniona, to nie można jej zmienić
        if self.poczatkowa_plansza[pozycja[1]][pozycja[0]] != ' ':
            return "Nie możesz zmienić tej pozycji. Wybierz inną"
        # jak wszystkie poprzednie warunki przeszły to znaczy że jest rozwiązane poprawnie
        return False

    def walidacja_cyfry(self, cyfra, dostepne_cyfry):
        # jeśli podana jest cyfra 0 to jest w porządku
        if cyfra == '0':
            return False
        # jeśli nie jest podana żadna cyfra to jest źle
        if not cyfra:
            return "Podaj jedną cyfrę. Dostępne cyfry: " + " ".join(dostepne_cyfry)
        # jeśli podana jest litera to nie da się z niej zrobić inta, czyli
        # próbuje zrobić z niej inta
        try:
            int(cyfra)
        # jeśli wyskakuje error to jest źle
        except ValueError:
            return "Podaj cyfrę. Dostępne cyfry: " + " ".join(dostepne_cyfry)
        # jeśli cyfra nie zawiera się w przedziale 1-9 to jest źle
        if 0 > int(cyfra) > 10:
            return "Podaj dokładnie jedną cyfrę. Dostępne cyfry: " + " ".join(dostepne_cyfry)
        # jeśli cyfra nie może zostać wybrana to jest źle
        if cyfra not in dostepne_cyfry:
            return "Niepoprawna cyfra! Dostępne cyfry: " + " ".join(dostepne_cyfry)
        # jeśli poprzednie warunki przeszły, to jest w porządku
        return False

    def graj(self):
        # pobiera od użytkownika pozycję, .upper() przerabia wszystkie litery na duże, żeby można
        # było podać a3 zamiast A3
        pozycja = input("Podaj pozycję w którą chcesz wpisać cyfrę (np E3)").upper()
        # sprawdza czy pozycja jest poprawnie podana
        walidacja = self.walidacja_pozycji(pozycja)
        # wykonuj dopóki walidacja zwraca jakiś błąd
        while walidacja:
            # pobiera od użytkownika pozycję, przerabia wszystkie litery na duże
            pozycja = input(walidacja).upper()
            # sprawdza czy pozycja jest poprawnie podana
            walidacja = self.walidacja_pozycji(pozycja)
        # jeśli pozycja jest poprawna, to przerabia ją z np E3 na [3, 3]
        pozycja = self.odczytaj_pozycje(pozycja)
        # sprawdza jakie cyfry można wpisać i przerabia je na stringi, żeby można je było później dodać w
        # jednego stringa
        dostepne_cyfry = [str(cyfra) for cyfra in list(self.dostepne_cyfry(pozycja))]
        # pobiera od użytkownika cyfrę którą chce wpisać w podane wcześniej miejsce
        cyfra_input = "Podaj cyfrę. Dostępne cyfry: " + " ".join(dostepne_cyfry) + ". Wpisz 0 żeby usunąć cyfrę"
        cyfra = input(cyfra_input)
        # sprawdza czy pozycja jest poprawnie podana
        walidacja = self.walidacja_cyfry(cyfra, dostepne_cyfry)
        # wykonuj dopóki walidacja zwraca jakiś błąd
        while walidacja:
            # pobiera od użytkownika cyfrę którą chce wpisać w podane wcześniej miejsce
            cyfra = input(walidacja)
            # sprawdza czy pozycja jest poprawnie podana
            walidacja = self.walidacja_cyfry(cyfra, dostepne_cyfry)
        # jeśli  cyfra jest poprawna, to przerabia ją na inta
        cyfra = int(cyfra)
        # i wstawia w podane wcześniej miejsce
        self.wpisz_cyfre(pozycja, cyfra)


if __name__ == '__main__':
    # tworzy obiekt sudoku na podstawie klasy Sudoku
    sudoku = Sudoku()
    # wykonuj dopóki plansza nie jest poprawnie rozwiązana
    while not sudoku.sprawdz_plansze():
        # wyświetla planszę
        sudoku.print_plansza()
        # wykonuje kolejny ruch na planszy
        sudoku.graj()
    # jak jest rozwiązane poprawnie to przestaje się wykonywać i pokazuje że się udało
    print("Wygrałeś!")
