import string

def szyfrowanie(tekst: str, klucz: int):
    szyfr = ""
    alfabet = string.ascii_lowercase

    for litera in tekst:
        if litera not in alfabet:
            szyfr += litera
            continue

        index = alfabet.index(litera)
        nowy_index = (index + klucz) % 26
        szyfr += alfabet[nowy_index]

    return szyfr

# tekst_input = input("Wpisz tekst: ")
# klucz_input = int(input("Wpisz klucz: "))
#
# print(szyfrowanie(tekst_input, klucz_input))