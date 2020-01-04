import sys
import time
import re
import os


class Kalendarz():

    def wczytaj_dane_z_plikow_tekstowych(self):
        for file in os.listdir("E:\Studia\pc_projekty\Kalendarzyk_release"):
            if file.endswith(".txt"):
                print(os.path.join("E:\Studia\pc_projekty\Kalendarzyk_release", file))
        print("załaduj plik z rozszerzeniem .txt")
        self.y = input()
        f = open(self.y).read()
        print(f)




    def dodaj_i_zapisz_do_pliku(self):

        self.data1 = (input("wprowadz date \nnp. 12/12/2019\n"))
        sciezka = r'^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$'
        dopasowanie = re.search(sciezka, self.data1)
        if dopasowanie:  # Sprawdzamy czy udalo sie cos znalezc
            numer = dopasowanie.group()
            print(numer)
            print("poprawnie wprowadzono numer ")

        else:
            print("bledne dospasowanie")
            return Kalendarz12.dodaj_i_zapisz_do_pliku()



        self.godzina1 = float(input("wprowadz godzine rozpoczecia"))
        self.godzina2 = float(input("wprowadz godzine zakonczenia pracy "))

        print("data :", self.data1)
        print("godzina rozpoczecia pracy", self.godzina1)
        print("godzina zakonczenia pracy", self.godzina2)

        szer = 80
        print("-" * szer)
        print("|  Data  |     godzina rozpoczecia      |    godzina zakonczenia     |      ")
        print("*" * szer)
        print("|    {} |             {}                |           {}               |    ".format(self.data1,
                                                                                                  self.godzina1,
                                                                                                  self.godzina2))
        print("*" * szer)
        print("załaduj plik z rozszerzeniem .txt")
        for file in os.listdir("E:\Studia\pc_projekty\Kalendarzyk_release"):
            if file.endswith(".txt"):
                print(os.path.join("E:\Studia\pc_projekty\Kalendarzyk_release", file))
        self.y = input()
        with open(self.y, 'a+') as f:
            f.write(str("\n"))
            f.write("Data {}".format(self.data1))
            f.write(str("\n"))
            f.write("Godzina rozpoczecia pracy : {}".format(self.godzina1))
            f.write(str("\n"))
            f.write("Godzina zakonczenia pracy : {}".format(self.godzina2))
            f.write(str("\n"))


            self.z = self.godzina2 - self.godzina1

        print("łaczny czas pracy w dniu : {}".format(self.z) + (" godziny"))
        with open(self.y, 'a+') as f:
            #f.write(str("\n"))
            #f.write(str("przepracowane godziny"))
            #f.write(str("\n"))
            #f.write(str(self.z ))

            f.write("przepracowane godziny: {}".format(self.z)+ "  w dniu : {}".format(self.data1))


    def czyszczenie_zawartosci(self):
        for file in os.listdir("E:\Studia\pc_projekty\Kalendarzyk_release"):
            if file.endswith(".txt"):
                print(os.path.join("E:\Studia\pc_projekty\Kalendarzyk_release", file))
        print("wybierz plik z rozszerzeniem txt z ktorego chcesz skasowac dane ")
        self.y = input()
        with open(self.y, "w+") as f:  # resetuje wartosci do pierwszej lini
            d = f.readlines()
            #f.seek(0)  # ustawia na pierwsza pozycje w offsecie element
            for i in d:
                if i != " aaaaaaaaaaaa":
                    f.write(i)
                    f.truncate()  # wyrzuca elementy (size)
            print("**********zawartosc pomyslnie skasowana*****************")
                    #Kalendarz12.main()



    def skoncz_program(self):
        sys.exit()

    def zliczanie_wierszy(self):
        for file in os.listdir("E:\Studia\pc_projekty\Kalendarzyk_release"):
            if file.endswith(".txt"):
                print(os.path.join("E:\Studia\pc_projekty\Kalendarzyk_release", file))
        print("wybierz plik z rozszerzeniem txt z ktorego chcesz odczytac dane ")
        self.y = input()
        count = 0
        with open(self.y) as x:
            for line in x:
                count += 1
                print(count)
            if count >= 100:
                print("przekroczyłeś 100 wierszy") ## 

    def sumuj_godziny(self):
            try:
                for file in os.listdir("E:\Studia\pc_projekty\Kalendarzyk_release"):
                    if file.endswith(".txt"):
                        print(os.path.join("E:\Studia\pc_projekty\Kalendarzyk_release", file))
                print("wybierz plik z rozszerzeniem txt z ktorego chcesz odczytac dane ")
                self.y = input()
                with open(self.y) as x:
                    for line in x:
                        # print(line)
                        sciezka = r'^przepracowane'
                        dopasowanie = re.search(sciezka, line)
                        if dopasowanie:
                            godziny = dopasowanie.group()
                            print(line)


            except IOError:
                print("problem z plikiem")

    def wyszukaj_plikow(self):
        for file in os.listdir("E:\Studia\pc_projekty\Kalendarzyk_release"):
            if file.endswith(".txt"):
                print(os.path.join("E:\Studia\pc_projekty\Kalendarzyk_release", file))



    def stworz_plik (self):
        print("Podaj nazwe pliku .txt")
        self.u=input()
        f=open(self.u,"w")
        print("Plik konfiguracyjny został utworzony pod nazwa :{}".format(self.u))

    def wroc_do_menu(self):
        return Kalendarz12.main()

    def main(self):

        while True:

            self.wybierz = int(input(
                "Nr 0 -wyszukaj pliki konfiguracyjne \nNr 1 -stworz swoj_osobisty plik konfiguracyjny\nNr 2 -Wypelnij dzien \nNr 3-Wczytaj zwartości \nNr-4 Sumuj wszystkie godziny pracy\nNr-5 Zlicz ilość wierszy w pliku\nNr-6 Skasuj zawartosc\nNr-7 Wyjscie \nNr-8 Wroc do Menu \n**Podaj cyfre** \n  "))
            if self.wybierz ==0 :
                Kalendarz12.wyszukaj_plikow() #wyszukaj pliki konfiguracyjne
            if self.wybierz ==1:
                Kalendarz12.stworz_plik() #Nr 1 -stworz swoj_osobisty plik konfiguracyjny
            if self.wybierz == 2:
                Kalendarz12.dodaj_i_zapisz_do_pliku() #wypelnij dzien

            if self.wybierz == 6: #OK
                Kalendarz12.czyszczenie_zawartosci()

            if self.wybierz == 7: #OK
                Kalendarz12.skoncz_program()

            if self.wybierz == 5: #OK
                Kalendarz12.zliczanie_wierszy()

            if self.wybierz == 4: #OK
                Kalendarz12.sumuj_godziny()
            if self.wybierz ==3 :
                Kalendarz12.wczytaj_dane_z_plikow_tekstowych() ## OK
            if self.wybierz ==8 :
                Kalendarz12.wroc_do_menu()



Kalendarz12 = Kalendarz()
Kalendarz12.main()
