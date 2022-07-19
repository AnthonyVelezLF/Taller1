from abc import ABC,abstractclassmethod,abstractmethod
from helpers import Helper
import os
      
class Usuario():
  def __init__(self,cedula, nombre, direccion, telefono, correo):
    self.nombre = nombre
    self.direccion = direccion
    self.cedula = cedula
    self.correo = correo
    self.telefono = telefono
    
  @abstractmethod
  def mostrar(self):
    print(self.nombre,self.cedula,self.direccion,self.correo,self.telefono)
        
    
class CrearUsuario(Usuario):
  secuencia=2             
  usuarios = [ {"cedula":"0987654322","nombre":"Hugo","direccion":"Milagro","telefono":"0959696735","correo":"lf@gmail.com"},{"cedula":"0912345678","nombre":"Maria","direccion":"Guayakill","telefono":"0959396735","correo":"lfdddd@gmail.com"}]
  
  def __init__(self):
    CrearUsuario.secuencia +=1
    self.codigo=CrearUsuario.secuencia
  
  def __init__(self, cedula, nombre, direccion, telefono, correo):
    super().__init__(cedula, nombre, direccion, telefono, correo)

  def registro(self):
    return {"cedula":self.cedula,"nombre":self.nombre,"direccion":self.direccion,"telefono":self.telefono,"correo":self.correo}
      
    
class VerificarDatos(Usuario):
  def __init__(self, cedula, nombre, direccion, telefono, correo):
    super().__init__(cedula, nombre, direccion, telefono, correo)
      
  def validarDatos(self):
    #vacio
    if len(cedula) == 0 and len(nombre) == 0 and len(direccion) == 0 and len(telefono) == 0 and len(correo) == 0:
      print ("Datos no ingresados")
    #cedula  
    if len(cedula)!= 10:
      print ("Cedula: '{}' INCORRECTO(debe tener 10 digitos)".format(cedula))
    else:
      print("Cedula: '{}' CORRECTO".format(cedula))
    #nombre
    if len(nombre)==0 and nombre == int(nombre):
      print ("Nombre: '{}' INCORRECTO(campo vacio o incorrecto)".format(nombre))
    else:
      print("Nombre: '{}' CORRECTO".format(nombre))
    #direccion
    if len(direccion)==0:
      print ("Direccion: '{}' INCORRECTO(campo vacio)".format(direccion))
    else:
      print("Direccion: '{}' CORRECTO".format(direccion))
    #telefono
    if len(telefono) < 8:
      print ("Telefono: '{}' INCORRECTO(campo vacio o incorrecto)".format(telefono))
    else:
      print("Telefono: '{}' CORRECTO".format(telefono))
    #correo
    if len(correo)==0:
      print ("Correo: '{}' INCORRECTO(campo vacio)".format(correo))
    else:
      print("Correo: '{}' CORRECTO".format(correo))
    
      
      
class EditarDatos(Usuario):
  def __init__(self, nombre, direccion, cedula, correo, telefono):
    super().__init__(nombre, direccion, cedula, correo, telefono)
      
  def editar(self): 
    if len(nombre)!= 10:
      cedula= input("Cedula: ")
    else:
      print("Cedula: '{}' CORRECTO".format(cedula))
    #nombre
    if len(nombre)==0 and nombre == int(nombre):
      nombre= input("Nombre: ")
    else:
      print("Nombre: '{}' CORRECTO".format(nombre))
    #direccion
    if len(direccion)==0:
      direccion= input("Direccion: ")
    else:
      print("Direccion: '{}' CORRECTO".format(direccion))
    #telefono
    if len(telefono) < 8:
      telefono= input("Telefono: ")
    else:
      print("Telefono: '{}' CORRECTO".format(telefono))
    #correo
    if len(correo)==0:
      print ("Correo: '{}' INCORRECTO(campo vacio)".format(correo))
    else:
      correo= input("Correo: ")
    
      
helper = Helper()
lista=["1) Mantenimiento de Usuarios","2) Salir"]
opcion=""
while opcion != "3":
  os.system("cls")
  opcion = helper.menu(lista,"*"*20+" MÓDULO DE SEGURDAD DEL SISTEMA ADMINISTRATIVO "+"*"*20)
  if opcion == "1":
    opc1=""
    while opc1 != "5":
      os.system("cls")
      print("*"*20,"OPCIONES DE USUARIOS","*"*20)
      opc1 = helper.menu(["1) Crear Usuario","2) Validar Usuario","3) Editar Usuario","4) Lista de Usuarios","5) Salir"],"")
      os.system("cls")
      if opc1 == "1":
        print("*"*20,"CREAR USUARIO","*"*20)
        cedula=input("Cedula:")
        nombre=input("Nombre:")
        direccion=input("Dirección:") 
        correo=input("Correo:")
        telefono=input("Telefono:")
        art= CrearUsuario(cedula,nombre,direccion,telefono,correo)
        articulo = art.registro()
        CrearUsuario.usuarios.append(articulo)

        input("USUARIO CREADO presiona ENTER para regresar")
      
      if opc1 == "2":
        print("*"*20,"VALIDAR USUARIO","*"*20)
        usu=VerificarDatos(cedula,nombre,direccion,telefono,correo)
        usu3=VerificarDatos(cedula,nombre,direccion,telefono,correo)
        usu.validarDatos()
        input("presiona ENTER para regresar")
        
      if opc1 == "3":
        print("*"*20,"EDITAR USUARIO","*"*20)
        cedula=input("Cedula(10 digitos): ")
        nombre=input("Nombre: ")
        direccion=input("Dirección: ") 
        correo=input("Correo: ")
        telefono=input("Telefono(minimo 8 digitos):")
        art= CrearUsuario(cedula,nombre,direccion,telefono,correo)
        articulo = art.registro()
        CrearUsuario.usuarios.append(articulo)

        input("USUARIO EDITADO ENTER para regresar")
    
      elif opc1 == "4":
        print("*"*20,"LISTADO DE USUARIOS","*"*20)
        print("Cedula"," "*8,"Nombre"," "*5,"Direccion"," "*5,"Telefono"," "*5,"Correo"," "*5)
        for art in  CrearUsuario.usuarios:
          cedula = art["cedula"]
          nombre= art["nombre"]
          direccion= art["direccion"]
          telefono= art["telefono"]
          correo= art["correo"]
          
          print(" "*0,cedula," "*5,nombre," "*(9-len(nombre)),direccion," "*(12-len(nombre)),telefono,
                " "*(12-len(str(direccion))),correo," "*(17-len(str(direccion))))
        print("")
        print("*"*59)
        input("Presione una tecla para continuar...")
        
