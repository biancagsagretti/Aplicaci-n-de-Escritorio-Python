import tkinter as tk 


def verificar(dato):
    if dato == "":
        dato == "error"
    return dato
def convertir(valor): 
    if valor.isdecimal():
        valor = int(valor)
    else:
        valor = "error"
    return valor 

ventana = tk.Tk()
ventana.title()

ventana.config(width=400, height=300)
ventana.title("Inventario Python")
class Producto:
    def __init__(self, producto, precio, cantidad):
        self.producto= producto
        self.precio= precio
        self.cantidad=cantidad

    def getProducto(self):
        return self.producto 

    def getPrecio(self):
        return self.precio

    def getCantidad(self):
        return self.cantidad

    def mostrarProducto(self):
        print("Nombre:"+self.getProducto() + "Precio:" + str(self.getPrecio()) + "Cantidad:"+ str(self.getCantidad()))
       
    boton1 = tk.Button (text= "Ver Productos", command= mostrarProducto )
    boton1.place (x=300, y =80, width=200, height=50)

    def agregarProducto(self):

        producto = caja3.get()
        producto=verificar(producto)
        precio= caja4.get()
        precio=verificar(precio)
        cantidad= caja5.get()
        cantidad=verificar(cantidad)

        if producto == "error":
            print("No ingresó un valor correcto")
        elif precio=="error":
            print("Ingresó mal el precio")
        elif cantidad =="error":
            print("Ingresó mal la cantidad")
        else:
            productos= {"producto":"", "precio":"", "cantidad":""}
            print("Ingresaste los datos correctamente")

    boton6 = tk.Button (text= "Agregar", command= agregarProducto)
    boton6.place (x=360, y =420, width=200, height=50)

    

caja3 = tk.Entry()
caja3.place(x=20, y=180, width=200, height=25)

caja4 = tk.Entry()
caja4.place(x=20, y=240, width=200, height=25)

caja5 = tk.Entry()
caja5.place(x=20, y=360, width=200, height=25)
  

producto = caja3.get()
producto=verificar(producto)
precio= caja4.get()
precio=verificar(precio)
cantidad= caja5.get()
cantidad=verificar(cantidad)    
 





e = Producto(producto,precio, cantidad)
e.mostrarProducto()
e.agregarProducto()


class Venta(Producto):
    def __init__(self, producto, cantidad):
        super().__init__(producto,precio, cantidad)
        self.producto = producto
        self.cantidad = cantidad

    def getProducto(self):
        return super().getProducto()

    def getCantidad(self):
        return super().getCantidad()

    def mostrarVenta(self):
        print("Nombre:"+ self.getProducto()+"Cantidad:"+ str(self.getCantidad()))
    
    boton2 = tk.Button (text= "Ver ventas", command= mostrarVenta )
    boton2.place (x=600, y =80, width=200, height=50)

 

producto = caja3.get()
producto=verificar(producto)

cantidad= caja5.get()
cantidad=verificar(cantidad)

e=Venta(producto, cantidad)
e.mostrarVenta()


class Compra(Producto):
    def __init__(self, producto, cantidad):
        super().__init__(producto,precio, cantidad)
        self.producto = producto
        self.cantidad = cantidad

    def getProducto(self):
        return super().getProducto()

    def getCantidad(self):
        return super().getCantidad()

    def mostrarCompra(self):
        print("Nombre:"+ self.getProducto()+"Cantidad:"+ str(self.getCantidad()))

    boton3 = tk.Button (text= "Ver Compras", command= mostrarCompra )
    boton3.place (x=900, y =80, width=200, height=50)

producto = caja3.get()
producto=verificar(producto)

cantidad= caja5.get()
cantidad=verificar(cantidad)
e=Compra(producto, cantidad)
e.mostrarCompra()


#CAJAS
caja1 = tk.Entry()
caja1.place(x=20, y=180, width=200, height=25)

caja2 = tk.Entry()
caja2.place(x=20, y=240, width=200, height=25)

caja3 = tk.Entry()
caja3.place(x=20, y=360, width=200, height=25)


caja4 = tk.Entry()
caja4.place(x=20, y=420, width=200, height=25)

caja5 = tk.Entry()
caja5.place(x=20, y=480, width=200, height=25)



# #ETIQUETAS
etiqueta1 = tk.Label(text="Acciones:")
etiqueta1.place(x=20, y=20)

etiqueta2 = tk.Label(text="Producto:")
etiqueta2.place(x=20, y=150)

etiqueta3 = tk.Label(text="Cantidad:")
etiqueta3.place(x=20, y=210)

etiqueta4 = tk.Label(text="Producto:")
etiqueta4.place(x=20, y= 330)

etiqueta5 = tk.Label(text="Precio:")
etiqueta5.place(x=20, y=390)

etiqueta6 = tk.Label(text="Cantidad:")
etiqueta6.place(x=20, y=450)

# #BOTONES
boton1 = tk.Button (text= "Ver Productos", )
boton1.place (x=300, y =80, width=200, height=50)

boton2 = tk.Button (text= "Ver ventas", )
boton2.place (x=600, y =80, width=200, height=50)

boton3 = tk.Button (text= "Ver Compras", )
boton3.place (x=900, y =80, width=200, height=50)

boton4 = tk.Button (text= "Ventas")
boton4.place (x=360, y =200, width=200, height=50)


boton5 = tk.Button (text= "Compras")
boton5.place (x=720, y =200, width=200, height=50)

boton6 = tk.Button (text= "Agregar",)
boton6.place (x=360, y =420, width=200, height=50)

ventana.mainloop()







ventana.mainloop()

