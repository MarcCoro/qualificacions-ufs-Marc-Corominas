#Autor Marc Corominas
# This is a sample Python script.
from ModulProfessional import ModulProfessional
from UnitatFormativa import UnitatFormativa


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpointasdfasdfasdfasdfasdfasdfsda.

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Definició de classes
def inicialitzar_modul_professional():
    global uf1, uf2, uf3, uf1, mp5
    uf1 = UnitatFormativa("UF1. Desenvolupament del programari", 20)
    uf2 = UnitatFormativa("UF2. Optimització del programari", 20)
    uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes", 26)
    uf1.qualificacio = 8
    uf2.qualificacio = 10
    uf3.qualificacio = 4
    mp5 = ModulProfessional("MP05. Entorns de desenvolupament")
    mp5.afegir_unitat_formativa(uf1)
    mp5.afegir_unitat_formativa(uf2)
    mp5.afegir_unitat_formativa(uf3)


# Inici del programa
inicialitzar_modul_professional()


def mostrar_dades_modul():
    print(uf1.nom, ":", uf1.qualificacio)
    print(uf2.nom, ":", uf2.qualificacio)
    print(uf3.nom, ":", uf3.qualificacio)
    print(mp5.nom, ":", mp5.get_qualificacio())



mostrar_dades_modul()
