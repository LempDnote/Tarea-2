archivo = open("archivo1.json","r")
def lector(archivo):
    print("Archivo .json")
    for linea in archivo.readlines():
        print(linea)
    archivo.close()
lector(archivo)