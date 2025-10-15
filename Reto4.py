##reto 3
#Es el mismo codigo del reto anterior del restaurante solamente que ahora usa encapsulamiento
class MenuItem():
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    # Getters y Setters
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price
    
    def total_price(self):
        return self._price
    
    def __str__(self):
        return f"{self._name} - ${self._price}"
    
class StartDish(MenuItem):
    def __init__(self, name, price, type):
        super().__init__(name,price)
        self._type=type
    def get_type(self):
        return self._type
    def set_type(self,type):
        self._type=type
    def __str__(self):
        return f"{self.get_name()}, tipo {self._type} - ${self.get_price()}"

class MainDish(MenuItem):
    def __init__(self, name, price):
        super().__init__(name,price)
    def __str__(self):
        return f"{self.get_name()} - ${self.get_price()}"
    #clase para la bebida


class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name,price)
        self._size=size
    def get_size(self):
        return self._size 
    def set_size(self,size):
        self._size=size
    def __str__(self):
        return f"{self.get_name()}, tamaño {self._size} - ${self.get_price()}"



class Dessert(MenuItem):
    def __init__(self, name, price, flavor):
        super().__init__(name,price)
        self._flavor=flavor
    def get_flavor(self):
        return self._flavor 
    def set_(self,flavor):
        self._flavor=flavor
    def __str__(self):
        return f"{self.get_name()}, textura {self._flavor} - ${self.get_price()}"

class order():#Esta clase recibe los cuatro objetos que componen la orden
  
    def __init__(self, startdish, maindish, beverage, dessert):
        self._startdish = startdish
        self._maindish = maindish
        self._beverage = beverage
        self._dessert = dessert
    
    # Getters y Setters
    def get_startdish(self):
        return self._startdish
    
    def set_startdish(self, startdish):
        self._startdish = startdish
    
    def get_maindish(self):
        return self._maindish
    
    def set_maindish(self, maindish):
        self._maindish = maindish
    
    def get_beverage(self):
        return self._beverage
    
    def set_beverage(self, beverage):
        self._beverage = beverage
    
    def get_dessert(self):
        return self._dessert
    
    def set_dessert(self, dessert):
        self._dessert = dessert  


    def total_order(self):
        price=(
            self._startdish.get_price()+
            self._maindish.get_price()+
            self._beverage.get_price()+
            self._dessert.get_price()
        )
         #Aqui se aplican los descuentos
        discount_applied = 0
        discount_reasons = []
        if self._maindish.get_price() > 0:
            beverage_discount = self._beverage.get_price() * 0.15
            discount_applied += beverage_discount
            discount_reasons.append("15% de descuento en bebida por incluir plato principal")
        
      
        if self._maindish.get_price() > 20000:
            dessert_discount = self._dessert.get_price() * 0.04
            discount_applied += dessert_discount
            discount_reasons.append("4% de descuento en postre por plato principal premium")

        
        final_price = price - discount_applied
        return final_price, discount_applied, discount_reasons
    



    def show_order(self):
        print("Tu orden es la siguiente:")
        #se le asigan a variables los precios y nombres de cada objeto para facilitar la impresion
        p_entrada=self._startdish.get_price() 
        p_fuerte=self._maindish.get_price() 
        p_bebidas=self._beverage.get_price() 
        p_postres=self._dessert.get_price() 
        entrada=self._startdish.get_name()
        plato_fuerte=self._maindish.get_name()
        bebida=self._beverage.get_name()
        postre=self._dessert.get_name()
        #se imprimen los resultados
        print("Plato de entrada:       ", entrada,   "--$", p_entrada)
        print("Plato fuerte:           ", plato_fuerte, "--$",p_fuerte)
        print("Bebida:                 ", bebida,  "--$",p_bebidas)
        print("Postre:                 ", postre, "--$",p_postres)
        print("El total a pagar es:   $", self.total_order())
        return self.total_order()[0]
#Se guia del ejemplo de clase 
class MedioPago:
  def __init__(self):
    pass

  def pagar(self, monto):
    raise NotImplementedError("Subclases deben implementar pagar()")

class Tarjeta(MedioPago):
  def __init__(self, numero, cvv):
    super().__init__()
    self._numero = numero
    self._cvv = cvv
  def get_numero(self):
      return self._numero
  def set_numero(self,numero):
      self._numero= numero
  def get_cvv(self):
      return self._cvv
  def set_cvv(self,cvv):
      self._cvv=cvv

  def pagar(self, monto):
    print(f"Pagando {monto} con tarjeta {self._numero[-4:]}")

class Efectivo(MedioPago):
  def __init__(self, monto_entregado):
    super().__init__()
    self._monto_entregado = monto_entregado

  def get_monto_entregado(self):
      return self._monto_entregado
  def set_monto_entregado(self, monto_entregado):
      self._monto_entregado=monto_entregado

  def pagar(self, monto):
    if self._monto_entregado >= monto:
      print("Pago realizado en efectivo. Cambio:",self._monto_entregado - monto)
    else:
      print("Fondos insuficientes. Faltan",monto - self._monto_entregado," para completar el pago.")

class Payment():
    def __init__(self, order, medio_pago):
        self._order = order
        self._medio_pago = medio_pago
        self._amount = order.total_order()[0] #Obtiene el precio final que es el primer valor de la tupla
        self._payment_status = "pendiente" 
    
    def get_order(self):
        return self._order
    
    def set_order(self, order):
        self._order = order
        self._amount = order.total_order()[0]
    
    def get_medio_pago(self):
        return self._medio_pago
    
    def set_medio_pago(self, medio_pago):
        self._medio_pago = medio_pago
    
    def get_amount(self):
        return self._amount
    
    def get_payment_status(self):
        return self._payment_status

    def process_payment(self):
        print("--- PROCESANDO PAGO ---")
        print("Monto a pagar: $",self._amount)
        
        resultado = self._medio_pago.pagar(self._amount)
        #Actualiza el estado de pago
        if resultado is None or resultado == True:
            self._payment_status = "completado"
            print(" Estado del pago" ,self._payment_status)
        else:
            self._payment_status = "fallido"
            print(" Estado del pago" ,self._payment_status)
        
        return self._payment_status

## Aqui estan conteniadas las opciones que el usuario puede escoger
entradas=[
    StartDish("Empanada de carne", 3000, "frito"),
    StartDish("Empanada campesina", 3200, "frito"),
    StartDish("Sopa de tomate", 6000, "caliente"),
    StartDish("Patacon con ahogao", 3000, "frito"),
]
PlatosFuertes=[
    MainDish("Bandeja Paisa", 37000),
    MainDish("Cocido boyacense", 30200),
    MainDish("Ajiaco", 26000 ),
    MainDish("Tamal", 12000),
    MainDish("Chuleta de cerdo", 21000),
    MainDish("Costillas BBQ", 25000),
    MainDish("Baby Beef", 32000),
    MainDish("Arroz con pollo", 10000),
    MainDish("Lechona", 12000),
    MainDish("Frijolada", 17000),
    MainDish("Sancocho", 14000),
    MainDish("Sudado de pollo", 11000)  
   
] 

bebidas = [
    Beverage("Jugo de mango", 3000 , "grande"),
    Beverage("Jugo de mora", 2500 , "mediana"),
    Beverage("Jugo de maracuya", 3000, "grande"),
    Beverage("Cocacola", 5500 , "1.5 L"),
    Beverage("Cocacola personal", 3000, "grande"),
    Beverage("Pepsi personal", 2500 , "Pequeña"),
    Beverage("Te", 2000, "Pequeño"),
    Beverage("Cerveza", 2800, "mediana"),
]

postres = [
    Dessert("Helado de brownie", 2500, "esponjosa"),
    Dessert("Helado de vainilla", 2500, "cremoso"),
    Dessert("Flan de caramelo", 3000, "gelatinoso"),
    Dessert("Cheesecake de mora", 4500, "gelatinoso"),
    Dessert("Arroz con leche", 3000, "espeso")
]
#esta funcion muestra las opciones de cada categoria
def mostrar_opciones(list, title):
     print(f"  --- {title} ---")
     for i, item in enumerate(list, 1): #  enumerate permite obtener el indice y el item en cada iteracion 
        print(i, item)
     print("---------------------------")
#Esta funcion es importante ya que permite al usuario seleccionar una opcion y valida que la opcion sea correcta
def seleccionar_opciones(list, title):
    while True: #se repite hasta que el usuario ingrese una opcion valida
        mostrar_opciones(list,title) # Se llana otra funcion para mostrar las opciones
        NumIngresado=(input("Por favor seleccione una opcion: "))
         #validacion para asegurar que el usuario ingrese un numero
        if not NumIngresado.isdigit():
            print("Por favor ingresa un número válido.")
            continue
        NumIngresado=int(NumIngresado)
        if 1 <= NumIngresado<= len(list):
            return list[NumIngresado - 1] #Retorna el elemnto seleccionado
        else:
            print("Número fuera de rango, intenta de nuevo.")    
def seleccionar_metodo_pago():
    print("--- MÉTODO DE PAGO ---")
    print("1. Tarjeta")
    print("2. Efectivo")
    
    while True:
        opcion = input("Seleccione método de pago (1-2): ")
        
        if opcion == "1":
            while True:
                numero = input("Ingrese número de tarjeta (16 dígitos): ")
                cvv = input("Ingrese CVV (3 dígitos): ")

                if len(numero) == 16 and numero.isdigit() and len(cvv) == 3 and cvv.isdigit():
                    return Tarjeta(numero, cvv)
                else:
                    print("Datos inválidos. Asegurese de que la tarjeta tenga 16 dígitos y el CVV 3.")

        elif opcion == "2":
            monto = None
            while monto is None:
                entrada = input("Ingrese monto entregado: $")
                if not entrada.replace('.', '', 1).isdigit(): 
                    print(" Por favor ingrese un número válido.")
                    continue

                monto = float(entrada)
                if monto <= 0:
                    print(" El monto debe ser mayor a 0.")
                    monto = None
                    continue

            return Efectivo(monto)
if __name__ == "__main__":
    #Aqui hay varias cosas importates 
    print("Bienvenido a nuestro restaurante, por favor realice su orden")
    #Estas variables reciben lo que la funcion seleccionar_opciones retorna, esta a su vez es la que 
    #pide todas las cosas al usuario , la funcion pide una lista y un titulo para mostrar,
    #lo que hace es acceder a la lista previamente creada que contiene los menus 
    entrada=seleccionar_opciones(entradas, "entradas")
    Platofuerte=seleccionar_opciones(PlatosFuertes, "platos fuertes")
    bebida=seleccionar_opciones(bebidas, "bebidas")
    postre=seleccionar_opciones(postres, "postres")
    
    orden = order(entrada, Platofuerte, bebida, postre)
    total = orden.show_order()
    medio_pago = seleccionar_metodo_pago()
    pago = Payment(orden, medio_pago)
    estado_pago = pago.process_payment()
    
    if estado_pago == "completado":
        print("¡Gracias por su compra, vuelva pronto!")
    else:
        print("El pago no pudo ser procesado. Por favor intente nuevamente.")