import csv


def citeste_fisierul_si_identifica_cuvintele(fisier):
    numar_incercari = 0
    rezultate = []

    with open(fisier, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            cod_joc = row[0]
            cuvant_partial = row[1]
            cuvant_final = row[2]

            numar_incercari += identifica_cuvant(cuvant_partial, cuvant_final)
            rezultate.append((cod_joc, cuvant_partial, cuvant_final))

    return numar_incercari, rezultate


def identifica_cuvant(cuvant_partial, cuvant_final):
    incercari = 0
    # Parcurgem fiecare caracter și verificăm dacă este cunoscut sau necunoscut ('*')
    for i in range(len(cuvant_partial)):
        if cuvant_partial[i] == '*':
            # Înlocuim doar caracterele necunoscute
            incercari += 1
    return incercari


# Exemplu de rulare
fisier_csv = 'cuvinte_joc.csv'  # Numele fișierului CSV
numar_total_incercari, rezultate = citeste_fisierul_si_identifica_cuvintele(fisier_csv)

print(f'Numărul total de încercări: {numar_total_incercari}')
