import wersja_graf
import wykres

print "SYMULATOR EPIDEMII\n"
print "Wybor grafu badz wykresu \n"

k = 0
while k == 0:
    wybor = raw_input("Wpisz graf/wykres: ")
    if wybor == 'graf':
        k = k + 1
        wersja_graf.graf()

    if wybor == 'wykres':
        k= k+1
        wykres.wykres()

    else:
        print "Blad"
