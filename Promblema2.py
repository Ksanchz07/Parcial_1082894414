def agregar_producto(inventario):
    nombre = input("Ingresa el nombre del producto: ").strip()
    if nombre in inventario:
        print("El producto ya existe.")
        return
    try:
        cantidad = int(input("Ingresa la cantidad: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
        precio = float(input("Ingresa el precio: "))
        if precio <= 0:
            print("El precio debe ser un número positivo.")
            return
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
        print("Producto agregado exitosamente.")
    except ValueError:
        print("Cantidad y precio deben ser números válidos.")

def ver_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("Inventario:")
    for nombre, datos in inventario.items():
        total = datos['cantidad'] * datos['precio']
        print(f"- {nombre}: Cantidad: {datos['cantidad']}, Precio: {datos['precio']:.2f}, Total: {total:.2f}")

def buscar_producto(inventario):
    nombre = input("Ingresa el nombre del producto a buscar: ").strip()
    if nombre in inventario:
        datos = inventario[nombre]
        total = datos['cantidad'] * datos['precio']
        print(f"Producto encontrado: {nombre}")
        print(f"Cantidad: {datos['cantidad']}, Precio: {datos['precio']:.2f}, Total: {total:.2f}")
    else:
        print("Producto no encontrado.")

def actualizar_cantidad(inventario):
    nombre = input("Ingresa el nombre del producto a actualizar: ").strip()
    if nombre not in inventario:
        print("Producto no encontrado.")
        return
    try:
        nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
        if nueva_cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
        inventario[nombre]['cantidad'] = nueva_cantidad
        print("Cantidad actualizada exitosamente.")
    except ValueError:
        print("La cantidad debe ser un número entero válido.")

def eliminar_producto(inventario):
    nombre = input("Ingresa el nombre del producto a eliminar: ").strip()
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado exitosamente.")
    else:
        print("Producto no encontrado.")

def menu():
    inventario = {}
    while True:
        print("\nMenú de Inventario:")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Buscar producto")
        print("4. Actualizar cantidad")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            ver_inventario(inventario)
        elif opcion == '3':
            buscar_producto(inventario)
        elif opcion == '4':
            actualizar_cantidad(inventario)
        elif opcion == '5':
            eliminar_producto(inventario)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
