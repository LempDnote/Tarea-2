import re;


def Letra(self, letra, opcion):
    x = object
    if(opcion == 0):
        x = re.findall("[a-z]", letra)
    else:
        x = re.findall("[1-9]", letra)
    if x:
        return True
    else:
        return False

class lector():
    def estados(self,cadena):
        estado = 0;
        for i in range(len(cadena)+1):
            if estado == 0:
                if Letra(0, cadena[i], 0):

                    estado = 2
                elif cadena[i] == "_":

                    estado = 1
                else:
                    print("Expresion no valida")
                    break
            elif estado == 1:
                if Letra(0, cadena[i], 0):

                    estado = 3
                elif cadena[i] == "_":

                    estado = 1
                else:
                    print("Expresion no valida")
                    break
            elif estado == 2:
                if Letra(0, cadena[i], 0):

                    estado = 2
                elif Letra(0, cadena[i], 1):

                    estado = 4
                else:
                    print("Expresion no valida")
                    break
            elif estado == 3:
                if Letra(0, cadena[i], 0):

                    estado = 3
                elif Letra(0, cadena[i], 1):

                    estado = 4
                else:
                    print("Expresion no valida")
                    break
            elif estado == 4:
                    print(">>>Expresion Aceptada ty")

cadena1 = "__servidor1";
cadena2 = "3servidor1";

lector.estados(0,cadena1)