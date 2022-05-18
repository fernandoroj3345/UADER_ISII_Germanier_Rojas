def decorador(func): # Damos como argumento del decorador a func
    def nueva_funcion(self, mensaje): #Aquí debemos colocar los parámetros con los que trabaja func
        print ("Cajero dice:")#Código decorador
        func(self, mensaje) #En func agregamos los parámetros con los que trabaja
    return nueva_funcion #Retornamos la nueva función
class cajero(object): #Creamos la clase heredando de object
    def __init__(self, nombre):  #Constructor con el atributo nombre
        self.nombre = nombre #Nombre es igual al argumento nombre etc.
#Aca antes del método se coloca el decorador!!!
    def saluda(self, mensaje): #Metodo saludar cajero, como siempre
        self.mensaje = mensaje #El parámetro de saluda mensaje es igual a mensaje argumento.
        print(mensaje) #Imprimir el mensaje ATENCIÓN.
        print("Adelante") #Resto del código
pepito = cajero('Pepito') #Instanciamos
pepito.saluda('Soy el mejor cajero!') #Cuando llamamos al metodo saluda buscara añadirle el decorador
#Osea que se ira hasta arriba. Por ende allí también debimos incluir la instanciacion (self) y el
#Argumento mensaje para ambas (nueva_funcion) y func.