# Programa de gestión de inventario simple

# Diccionario para almacenar los productos
# La clave será el nombre del producto y el valor será otro diccionario con cantidad y precio
inventario = {}

# Función para agregar un producto
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    if nombre in inventario:
        print("El producto ya existe en el inventario.")
        return
    
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        
        # Validar que cantidad y precio sean positivos
        if cantidad <= 0 or precio <= 0:
            print("La cantidad y el precio deben ser positivos.")
            return
        
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        print("Producto agregado correctamente.")
    except ValueError:
        print("Error: cantidad debe ser número entero y precio debe ser número decimal.")

# Función para ver el inventario completo
def ver_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        total = 0
        print("\n--- Inventario ---")
        for nombre, datos in inventario.items():
            subtotal = datos["cantidad"] * datos["precio"]
            total += subtotal
            print(f"{nombre} - Cantidad: {datos['cantidad']} - Precio: {datos['precio']} - Subtotal: {subtotal}")
        print(f"Total en pesos: {total}\n")

# Función para buscar un producto por nombre
def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ")
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"{nombre} - Cantidad: {datos['cantidad']} - Precio: {datos['precio']}")
    else:
        print("Producto no encontrado.")

# Función para actualizar la cantidad de un producto
def actualizar_cantidad():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre in inventario:
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            if nueva_cantidad <= 0:
                print("La cantidad debe ser positiva.")
                return
            inventario[nombre]["cantidad"] = nueva_cantidad
            print("Cantidad actualizada correctamente.")
        except ValueError:
            print("Error: la cantidad debe ser un número entero.")
    else:
        print("Producto no encontrado.")

# Función para eliminar un producto
def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")

# Función principal para mostrar el menú
def menu():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
menu()