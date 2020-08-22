archivo = open("archivo2.xml","r")
def lector(archivo):
    print("Archivo .xml")
    for linea in archivo.readlines():
        print(linea)
    archivo.close()
lector(archivo)