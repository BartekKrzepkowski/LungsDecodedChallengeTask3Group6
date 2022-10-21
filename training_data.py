# Format of training prompt
defaultPrompt = {
    'opis_badania': f'''Wyciągnij informacje medyczne z tekstu:

Przykład1:
Okrągły guzek tkankowy w miąższu płucnym w s.4 płuca prawego .Pojedynczy guzek w płucu prawym. Guzki tarczycy. Torbiele w wątrobie o sr. do 8 mm. Zwłóknienia nadprzeponowo w obu płucach. 

Informacje:
Guzek tkankowy: okrągły
Guzek tkankowy: w miąższu płucnym
Guzek tkankowy: w s.4 płuca prawego
Guzek: pojedyńczy
Guzek: w płucu prawym
Guzki tarczycy: Tak
Torbiel: w wątrobie
Torbiel: o sr do 8 mm
Zwłoknienie: nadprzeponowo w obu płuchach

Przykład 2:
Przykład danych wejściowych: "wynik wątpliwy, zmiany dodatkowe W s. 4 płuca prawego, przy szczelinie owalny, nieuwapniony guzek ok. 8x8x4mm. Drugi owalny guzek ok. 6x4,5mm widoczny na poz seg 6 płuca prawego, na przebiegu szczeliny."

Informacje:
Wynik: wątpliwy
Obecność guzków: Tak
Liczba guzków: 2
Lokalizacja guzka - segment: 4
Lokalizacja guzka - segment: 6
Lokalizacja guzka - płuco: prawe
Pierwszy guzek: ok. 8x8x4mm
Drugi guzej: ok. 6x4.5mm

Tekst:
{}

Informacje:''',
}
