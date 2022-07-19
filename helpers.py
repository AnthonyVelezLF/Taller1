class Helper:
  
  def __init__(self):
    x=10
    pass
  def menu(self,opciones,titulo):
    print(titulo)
    for opcion in opciones:
        print(opcion)
    opc = input("Elija Opcion[1...{}]: ".format(len(opciones)))
    return opc
