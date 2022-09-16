#Autor Marc Corominas
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Definició de classes
class UnitatFormativa:
    nom = None
    qualificacio = None

    def __init__(self, nom):
        self.nom = nom


# Inici del programa
uf1 = UnitatFormativa("UF1. Desenvolupament del programari")
uf2 = UnitatFormativa("UF2. Optimització del programari")
uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes")

uf1.qualificacio = 8
uf2.qualificacio = 10
uf3.qualificacio = 4

print(uf1.nom, ":", uf1.qualificacio)
print(uf2.nom, ":", uf1.qualificacio)
print(uf3.nom, ":", uf1.qualificacio)