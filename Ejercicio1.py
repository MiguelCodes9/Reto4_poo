#Creo esta superclase que es la bse de las otras 
class Shape:
  def __init__(self):
    pass

  def calcular_area(self):
    raise NotImplementedError("Subclases deben implementar area()")
#Estas son las funciones solicitadas 
class Rectangle(Shape):
  def __init__(self, width, height):
    super().__init__()
    self.width = width
    self.height= height 
    #El caso para el area de el rectangulo y el cuadrado es distinto pero muy similar
      #Aqui el area es la base por la altura
  def compute_area(self):
        return self.width * self.height 
       #El doble de cada lado sumados

  def compute_perimeter(self):
        return (self.width*2 )+ (self.height*2)

class Square(Shape):
  def __init__(self, side):
    super().__init__()
    self.side = side
#Para calcular el area basta multiplicar por si mismo el lado 2 veces
  def compute_area(self):
        return self.side **2
  #Como los lados con iguales , el perimetro sera igual a el lado por 4
  def compute_perimeter(self):
        return self.side*4 

#Seccion de impresiones 
rectangulo1 = Rectangle(5,2)
cuadrado1 = Square(5)
#Despues de asignar variables para cada clase , se utilizan en las impresiones 
print(f"El area del rectangulo es: {rectangulo1.compute_area()}")
print(f"El perimetro del rectangulo es: {rectangulo1.compute_perimeter()}")
print(f"El area del cuadrado es: {cuadrado1.compute_area()}")
print(f"El perimetro del cuadrado es: {cuadrado1.compute_perimeter()}") 