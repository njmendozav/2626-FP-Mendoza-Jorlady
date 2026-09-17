def calcular_total(precio_producto, cantidad_producto):
    total = precio_producto * cantidad_producto
    return total


# Datos de la compra
precio = 2.50
cantidad = 4

# Llamada a la función
resultado = calcular_total(precio, cantidad)

# Mostrar el resultado
print("Precio del producto: $", precio)
print("Cantidad comprada:", cantidad)
print("Precio total de la compra: $", resultado)