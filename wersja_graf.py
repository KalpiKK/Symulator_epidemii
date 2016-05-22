import networkx as nx
import random
import matplotlib.pyplot as plot
import imageio

# GRAF
# Funkcja rysujaca graf, na podstawie wprowadzonych danych -  beta, gamma, ilosc populacji, czas.
# Zalozenia:
# - liczebnosc populacji jest stala
# - beta > gamma, w innym przypadku nie jest to przypadek epidemii,
# - kazdy typ osobnika ma rowne szanse spotkania osobnika innego typu,
# - pojawia sie 1 zainfekowanywy


def graf():

    q = 0;

    while q == 0:
        beta = float(raw_input("Podaj wartosc bety (predkosc rozprzestrzenania sie epidemii, beta > gamma): "))
        gamma = float(raw_input("Podaj wartosc gamma (predkosc zdrowienia populacji, beta > gamma): "))
        if beta > gamma:
            q = 1
        else:
            print 'Nieprawidlowe dane! (beta > gamma; liczby zmiennoprzecinkowe)'
            q = 0

    N = int(raw_input("Podaj liczebnosc populacji: "))
    czas = int(raw_input("Podaj czas trwania obserwacji epidemii: "))

    options_2 = {
        'with_labels': False,
        'node_color': 'grey',
        'node_size': 100,
        'edge_color': 'grey',
        'linewidths': 0,
        'width': 0.3,
        }
    options_i = {
        'with_labels': False,
        'node_color': 'red',
        'node_size': 100,
        'edge_color': 'grey',
        'linewidths': 0,
        'width': 0.3,
    }
    options_r = {
        'with_labels': False,
        'node_color': 'blue',
        'node_size': 100,
        'edge_color': 'grey',
        'linewidths': 0,
        'width': 0.3,
    }

    nazwy=[]

    i=[]
    r=[]

    graf = nx.barabasi_albert_graph(N,4) # graf w ksztalcie kuli, 4 oznacza kreski odchodzace od kulek ich zasieg
    pos = nx.spring_layout(graf)

    # pierwszy chory losowo
    pierwszy = random.choice(graf.nodes())
    graf.node[pierwszy] = 'I'
    i.append(pierwszy)

    for x in range(czas):
        liczba = 0
        while liczba < N:
            liczba = liczba + 1
            los = random.choice(graf.nodes())  # wybiera losowo kulke
            if graf.node[los] == 'I':  # chory -   losowanie czy wyzdrowieje, czy zarazi (0.0,1.0)
                if len(i) == 1:
                    sasiad = random.choice(graf.neighbors(los))  # los na sasiada
                    if graf.node[sasiad] != 'R' and graf.node[sasiad] != 'I':
                        # gdy sasiad jest zdrowy porownanie do szybkosci rozprzestrzeniania i zarazenie lub nie
                        if random.random() < beta:
                            graf.node[sasiad] = 'I'
                else:
                    a = random.random()
                    if a < gamma:
                        graf.node[los] = 'R'
                    if a > gamma:
                        sasiad = random.choice(graf.neighbors(los))  # los na sasiada
                        if graf.node[sasiad] != 'R' and graf.node[sasiad] != 'I':
                        # gdy sasiad jest zdrowy porownanie do szybkosci rozprzestrzeniania i zarazenie lub nie
                            if random.random() < beta:
                                graf.node[sasiad] = 'I'

        for no in graf.nodes():
            if graf.node[no] == 'I':
                i.append(no)
            if graf.node[no] == 'R':
                r.append(no)
            else:
                continue

        nx.draw_networkx_edges(graf,pos,edge_color='k')
        nx.draw_networkx_nodes(graf, pos, **options_2)
        nx.draw_networkx_nodes(graf, pos, nodelist=i,label=len(i), **options_i)
        nx.draw_networkx_nodes(graf, pos, nodelist=r, **options_r)

        p = str(len(i))
        plot.title(x)
        plot.annotate(p, xy=(2, 1), xytext=(3, 1.5))

        filenames = str(x) +  ".png"
        plot.savefig(filenames)
        plot.savefig(filenames)
        nazwy.append(filenames)


    images=[]
    for nazwa in nazwy:
        images.append(imageio.imread(nazwa))
    imageio.mimsave('test.gif', images, duration=4, fps=10)



