import os

class Producto:
    def __init__(self, id_producto, nombre_producto, cantidad_producto, precio_producto):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.cantidad_producto = cantidad_producto
        self.precio_producto = precio_producto

    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre_producto

    def obtener_cantidad(self):
        return self.cantidad_producto

    def obtener_precio(self):
        return self.precio_producto

    def establecer_cantidad(self, cantidad_producto):
        self.cantidad_producto = cantidad_producto

    def establecer_precio(self, precio_producto):
        self.precio_producto = precio_producto

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre_producto}, Cantidad: {self.cantidad_producto}, Precio: ${self.precio_producto:.2f}"


class Inventario:
    ARCHIVO_INVENTARIO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_inventario()

    def guardar_inventario(self):
        try:
            with open(self.ARCHIVO_INVENTARIO, "w") as archivo:
                for producto in self.productos:
                    archivo.write(f"{producto.obtener_id()},{producto.obtener_nombre()},{producto.obtener_cantidad()},{producto.obtener_precio()}\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def cargar_inventario(self):
        if not os.path.exists(self.ARCHIVO_INVENTARIO):
            return
        try:
            with open(self.ARCHIVO_INVENTARIO, "r") as archivo:
                for linea in archivo:
                    id_producto, nombre_producto, cantidad_producto, precio_producto = linea.strip().split(",")
                    producto = Producto(id_producto, nombre_producto, int(cantidad_producto), float(precio_producto))
                    self.productos.append(producto)
        except (FileNotFoundError, ValueError):
            print("Error al cargar el inventario. Verifica el formato del archivo.")

    def agregar_producto(self, producto):
        if any(p.obtener_id() == producto.obtener_id() for p in self.productos):
            print("Error: Ya existe un producto con este ID.")
            return
        self.productos.append(producto)
        self.guardar_inventario()
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.obtener_id() == id_producto:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad_producto=None, precio_producto=None):
        for producto in self.productos:
            if producto.obtener_id() == id_producto:
                if cantidad_producto is not None:
                    producto.establecer_cantidad(cantidad_producto)
                if precio_producto is not None:
                    producto.establecer_precio(precio_producto)
                self.guardar_inventario()
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre_producto):
        productos_encontrados = [p for p in self.productos if nombre_producto.lower() in p.obtener_nombre().lower()]
        if productos_encontrados:
            for p in productos_encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(f"Producto: {producto}")


def menu():
    inventario = Inventario()
    while True:
        print("\nMenú de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad_producto = int(input("Ingrese la cantidad: "))
            precio_producto = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre_producto, cantidad_producto, precio_producto)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad_producto = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio_producto = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            cantidad_producto = int(cantidad_producto) if cantidad_producto else None
            precio_producto = float(precio_producto) if precio_producto else None
            inventario.actualizar_producto(id_producto, cantidad_producto, precio_producto)

        elif opcion == "4":
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre_producto)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventario...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    menu()
