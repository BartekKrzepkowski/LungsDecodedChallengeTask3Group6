# Format of training prompt
defaultPrompt = {
    'opis_badania': '''Wyciągnij informacje medyczne z tekstu:

Przykład 1:
Opis badania:
Duża masa w śródpiersiu przednim o wymiarze 32x20 mm o niejednorodnej densyjności, naciekająca płat górny płuca prawego z towarzyszącymi powiększonymi węzłami chłonnymi wnęki prawej i podostrogowymi o wymiarach 15x12 mm oraz 11x7 mm, niewielkim wysiękiem opłucnowym oraz płynem w worku osierdziowym.

Wyekstrahowane informacje:
{
"zagęszczenia miąższowe": "[nie]",
"płyn": "[jamy opłucnowe, worek osierdziowy]",
"węzły chłonne": "[powiększone]",
"przerzuty": "[brak]",
"rozedma": "[brak]",
"zmiany":
    {
    "1":{
        "typ": "[masa]",
        "ilość": "[1]",
        "narząd": "[śródpiersie, płuco]",
        "strona": "[prawa]",
        "lokalizacja": "[górny płat]",
        "segment": "[brak]",
        "kształt": "[brak]",
        "rozmiar": "[32x20 mm]",
        "zwapnienia": "[brak]",
        }
    }
}


Przykład 2:
Opis badania:
W płaszczyźnie czołowej po podaniu środka kontrastującego na poziomie rozwidlenia tchawicy uwidoczniono masę miękkotkankową o wymiarach 68x54 mm o policyklicznych zarysach po stronie prawej przytchawiczo i we wnęce płuc z towarzyszącym powiększeniem węzłów chłonnych podostrogowych 18x11 mm oraz 13x9 mm.

Wyekstrahowane informacje:
{
"zagęszczenia miąższowe": "brak",
"płyn": "brak",
"wezły chłonne": "powiększone",
"przerzuty": "brak",
"rozedma": "brak",
"zmiany":
    {
    "1":{
        "typ": "masa mięsnotkankowa",
        "narząd": "płuco",
    "strona" : "prawa"
        "lokalizacja": "wnęka",
        "rozmiar": "68x54",
        "zwapnienia": "",
        "cecha": "policykliczne zarysy"
        },
    "2":{
        "typ": "powiększony węzeł chłonny",
        "narząd": "płuco",
        "strona": "prawa",
        "lokalizacja": "wnęka",
        "rozmiar": "18x11",
        "cecha": "podostrogowy"
        },
    "3":{
        "typ": "powiększony węzeł chłonny",
        "narząd": "płuco",
        "strona": "prawa",
        "lokalizacja": "wnęka",
        "rozmiar": "13x9",
        "cecha": "podostrogowy"
        }
    }
}


Przykład 3:
Opis badania:
W płaszczyźnie poprzecznej niejednorodny guz o wymiarze 28x25 mm z elementami utkania tłuszczowego i miękkotkankowego naciekająca śródpiersie. Bez cech meta.

Wyekstrahowane informacje:
{
"jakość wyniku": "brak",
"badanie kontrolne": "nie",
"zagęszczenia miąższowe": "nie",
"płyn": "brak",
"węzły chłonne": "w normie",
"przerzuty": "brak",
"rozedma": "brak",
"zmiany":
    {
    "1":{
        "typ": "guz",
        "ilość": "1",
        "narząd": "śródpiersie",
        "rozmiar": "28x25",
        "zwapnienia": "brak",
        "cecha": "niejednorodny, elementy utkania tłuszczowego i miękkotkankowego"
        }
    }
}


Przykład 4:
Opis badania:
W płaszczyźnie czołowej po podaniu środka kontrastującego na poziomie rozwidlenia tchawicy uwidoczniono masę miękkotkankową o wymiarach 68x54 mm o policyklicznych zarysach po stronie prawej przytchawiczo i we wnęce płuc z towarzyszącym powiększeniem węzłów chłonnych podostrogowych 18x11 mm oraz 13x9 mm.

Wyekstrahowane informacje:
{
"zagęszczenia miąższowe": "brak",
"płyn": "brak",
"wezły chłonne": "powiększone",
"przerzuty": "brak",
"rozedma": "brak",
"zmiany":
    {
    "1":{
        "typ": "masa mięsnotkankowa",
        "narząd": "płuco",
    "strona" : "prawa"
        "lokalizacja": "wnęka",
        "rozmiar": "68x54",
        "zwapnienia": "",
        "cecha": "policykliczne zarysy"
        },
    "2":{
        "typ": "powiększony węzeł chłonny",
        "narząd": "płuco",
        "strona": "prawa",
        "lokalizacja": "wnęka",
        "rozmiar": "18x11",
        "cecha": "podostrogowy"
        },
    "3":{
        "typ": "powiększony węzeł chłonny",
        "narząd": "płuco",
        "strona": "prawa",
        "lokalizacja": "wnęka",
        "rozmiar": "13x9",
        "cecha": "podostrogowy"
        }
    }
}


''',
'opis_badania2': '''Opis badania:
{}

Wyekstrahowane informacje:
'''
}
