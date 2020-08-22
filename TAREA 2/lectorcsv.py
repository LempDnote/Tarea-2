import csv
print("Archivo.csv")
with open('archivo3.csv',newline='') as File:
    leer = csv.reader(File)
    for row in leer:
        print(row)

