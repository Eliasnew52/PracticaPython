class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Persona():
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def Saludo(self):
        return f"Hola {self.nombre}"





p = Point(2,4)
Sujeto = Persona("Elias","Castillo",18)

print(p)
print(Sujeto)

print(p.x)
print(Sujeto.Saludo())